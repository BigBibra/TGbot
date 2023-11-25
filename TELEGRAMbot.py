from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token='5878973937:AAHxfRaN0jj_6MA99ugmlOdyRh_UnpHAr0s')
dp = Dispatcher(bot)

@dp.message_handler()
async def handle_message(message: types.Message):
    if message.text == 'привет':
        await message.answer('иди в кроватку пупсик')
    else:
        #await message.answer(message.text)
        #await message.reply(message.text)
        await bot.send_message(message.from_user.id, message.text)


executor.start_polling(dp, skip_updates=True)