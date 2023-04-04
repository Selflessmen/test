from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def create_new_manofacture() -> InlineKeyboardMarkup:
    menu = InlineKeyboardMarkup(row_width=2)
    yes = InlineKeyboardButton(text="✔Да", callback_data="add_new_manofactures")
    no = InlineKeyboardButton(text="👎No", callback_data="cancel")
    return menu.add(yes, no)


