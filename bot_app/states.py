from aiogram.dispatcher.filters.state import State, StatesGroup


class AnswerStatus(StatesGroup):
    start = State()
    answer = State()