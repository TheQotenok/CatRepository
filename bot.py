#bot.py
import logging, time, random

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text

logging.basicConfig(level=logging.INFO)

bot = Bot(token="1940303458:AAGKZNxaSqvBdR9s6sS6qBfXYt5C0zZJEzc")
dp = Dispatcher(bot)



@dp.message_handler(commands=['unmute'])
async def unmute(message: types.Message):
  await bot.restrict_chat_member(message.chat.id,message.reply_to_message.from_user.id,types.ChatPermissions(can_send_messages=True,can_send_media_messages=True,can_send_polls=True,can_send_other_messages=True,can_add_web_page_previews=True,can_invite_users=True))

@dp.message_handler(commands=['keyboard'])
async def keyboardd(message: types.Message):
  keyboard = types.ReplyKeyboardMarkup()
  keyboard.add(*['Убрать клавиатуру','Рандомное число'])
  await message.answer("Лови клавиатуру!",reply_markup=keyboard)

@dp.message_handler(Text(equals='кусь',ignore_case=True))
async def kus_func(message: types.Message):
  await message.answer("Щас укушу...")
  await bot.restrict_chat_member(message.chat.id,message.reply_to_message.from_user.id,types.ChatPermissions(can_send_messages=False),until_date=time.time()+60)
  await message.answer("Укусил!")

@dp.message_handler(Text(equals='убрать клавиатуру',ignore_case=True))
async def remove_keyboard(message: types.Message):
  await message.reply("Убрал клавиатуру",reply_markup=types.ReplyKeyboardRemove())

@dp.message_handler(Text(equals='рандомное число',ignore_case=True))
async def random_number(message: types.Message):
  await message.answer(f"Рандомное число от 0 до 10: {random.randint(0,10)}")

if __name__ == '__main__':
  executor.start_polling(dp, skip_updates=True)