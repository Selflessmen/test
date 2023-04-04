from aiogram.dispatcher.filters.state import StatesGroup, State


class States(StatesGroup):
    new_chanel = State()
    manual_state = State()
