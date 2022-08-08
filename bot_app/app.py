import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup
from .states import AnswerStatus
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from .bot_request import send_request
import os 


# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
storage = MemoryStorage()

bot = Bot(token= os.environ.get("API_TOKEN "))
dp = Dispatcher(bot, storage=storage)

@dp.message_handler(commands=['register'])
async def my_handler(message: types.Message):
    await AnswerStatus.answer.set()
    await message.reply("Add login and id")
    
@dp.message_handler(state=AnswerStatus.answer)
async def process_answer(message: types.Message, state: FSMContext):
    
    async with state.proxy() as data:
        letter = message.text
        try:
            int(letter.split(' ')[1])
        except ValueError:
            await message.reply("User_id must be integer value")
        try:    
            values_dict = dict()
            values_dict = {
                'username': letter.split(' ')[0],
                'password': letter.split(' ')[1],
            }
            res = await send_request(values_dict) 
            print(res)
        except IndexError:
            await message.reply("No password")
        