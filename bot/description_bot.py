import asyncio
from typing import List, Union
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from bot.states import States
from descriptor_editor.db import DataBase
from bot_login.bot_api import Token
from descriptor_editor.description_editor import description_creater
from bot.keyboards import create_new_manofacture
from aiogram.utils.exceptions import MessageToDeleteNotFound
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage



logging.basicConfig(level=logging.INFO)
db = DataBase("database.db")
storage = MemoryStorage()
bot = Bot(token=Token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=storage)
ID_CHANEL = "-1001455060853"


class AlbumMiddleware(BaseMiddleware):
    """This middleware is for capturing media groups."""

    album_data: dict = {}

    def __init__(self, latency: Union[int, float] = 0.3):
        """
        You can provide custom latency to make sure
        albums are handled properly in highload.
        """
        self.latency = latency
        super().__init__()

    async def on_process_message(self, message: types.Message, data: dict):
        if not message.media_group_id:
            return

        try:
            self.album_data[message.media_group_id].append(message)
            raise CancelHandler()  # Tell aiogram to cancel handler for this group element
        except KeyError:
            self.album_data[message.media_group_id] = [message]
            await asyncio.sleep(self.latency)

            message.conf["is_last"] = True
            data["album"] = self.album_data[message.media_group_id]

    async def on_post_process_message(self, message: types.Message, result: dict, data: dict):
        """Clean up after handling our album."""
        if message.media_group_id and message.conf.get("is_last"):
            del self.album_data[message.media_group_id]


@dp.message_handler(is_media_group=True, content_types=types.ContentType.ANY, state=None)
async def handle_albums(message: types.Message, album: List[types.Message], state: FSMContext):
    """This handler will receive a complete album of any type."""

    try:
        manofact_id = message.forward_from_chat.id
        manofact_title = message.forward_from_chat.title
    except AttributeError:
        manofact_id = message.forward_sender_name
        manofact_title = message.forward_sender_name
    if message.chat.type == "private":
        if not db.user_exist(manofact_id):
            await bot.send_message(message.chat.id,
                                   "Этого производителя нет в системе, давайте добавим?",
                                   reply_markup=create_new_manofacture())

            await state.update_data(manofact_id=manofact_id, manofact_name=manofact_title)
            return
    if message.from_user.id == "653500570":
        await bot.send_message(message.chat.id,
                               "СЭР, Переходим на ручное управление"
                               )
        await States.manual_state.set()
    media_group = types.MediaGroup()
    for obj in album:
        if obj.photo:
            file_id = obj.photo[-1].file_id
            caption = description_creater(obj.caption, manofact_id)
        else:
            file_id = obj[obj.content_type].file_id
            caption = description_creater(obj.caption, manofact_id)

        try:
            media_group.attach({"media": file_id, "type": obj.content_type, "caption": caption})
        except ValueError:
            return await message.answer("This type of album is not supported")

    await bot.send_media_group(message.chat.id, media_group, disable_notification=True)


@dp.message_handler(content_types=["photo"])
async def handle_photo(message: types.Message):

    try:
        manofact_id = message.forward_from_chat.id
        await bot.send_media_group(message.chat.id,
            [
                types.InputMediaPhoto(
                    media=message.photo[-1].file_id,
                    caption=description_creater(message.caption, manofact_id), parse_mode=types.ParseMode.HTML
                )
            ],
            disable_notification=True
        )
    except AttributeError:
        manofact_id = message.forward_sender_name
        await bot.send_media_group(message.chat.id,
                                   [
                                       types.InputMediaPhoto(
                                           media=message.photo[-1].file_id,
                                           caption=description_creater(message.caption, manofact_id),
                                           parse_mode=types.ParseMode.HTML
                                       )
                                   ],
                                   disable_notification=True
                                   )


@dp.callback_query_handler(text=["add_new_manofactures"])
async def add_new_manofactures(message: types.Message, state: FSMContext):
    data = await state.get_data()
    if 'menu_message_id' in data:
        try:
            await bot.delete_message(message.from_user.id, data['menu_message_id'])
            await message.delete()
        except MessageToDeleteNotFound:
            pass
    db.add_user(data["manofact_id"], name=data["manofact_name"])
    await bot.send_message(message.from_user.id, "Производитель добавлен.\nТепdfdfерь отправьте мне смайл которым мы будем отмечать данного производителя")
    await States.new_chanel.set()


@dp.message_handler(content_types=["text"], state=States.new_chanel)
async def change_smile(message: types.Message, state: FSMContext):
    data = await state.get_data()
    manofact_id = data['manofact_id']
    db.set_smile(smiile=message.text, id_chat=manofact_id)
    await bot.send_message(message.from_user.id, f"Сохранен производитель {data['manofact_name']}\n{message.text}")
    await state.finish()


@dp.message_handler(content_types=["text"], state=States.manual_state)
async def change_smile(message: types.Message, state: FSMContext):
    db.set_smile(smiile=message.text, id_chat=653500570)
    await bot.send_message(message.from_user.id, f"Будет такой смайл\n{message.text}")
    await state.finish()


@dp.message_handler(content_types=["text"], state=None)
async def just_text_editor(message: types.Message, state: FSMContext):
    try:
        manofact_id = message.forward_from_chat.id
    except AttributeError:
        manofact_id = message.forward_sender_name
    await asyncio.sleep(1)
    await bot.send_message(message.from_user.id, description_creater(message.text, manofact_id))


@dp.message_handler(commands=["cancel"], state="*")
async def cancel(message: types.Message, state: FSMContext):
    data = await state.get_data()
    if 'menu_message_id' in data:
        try:
            await bot.delete_message(message.from_user.id, data['menu_message_id'])
            await message.delete()
        except MessageToDeleteNotFound:
            pass
    current_state = await state.get_state()
    if current_state is None:
        return

    await state.finish()

if __name__ == "__main__":
    dp.middleware.setup(AlbumMiddleware())
    executor.start_polling(dp)
