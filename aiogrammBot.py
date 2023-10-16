import logging
import asyncio
# from datetime import datatime

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command,CommandObject
from aiogram.types import FSInputFile
from random import randint
TELEGRAM_TOKEN ="6649093733:AAE1GWSpTLH_kEcCLbptqy5DoSKddn8XFBQ"
GROUP_ID= '-1001674247269'
# вывод отладочных сообщений в терминал
logging.basicConfig(level=logging.INFO)

# создали обьект bot
bot = Bot(token=TELEGRAM_TOKEN)

# создаем обьект диспетчер 
dp = Dispatcher()

# обрабатываем команду старт
@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    image_from_pc = FSInputFile('hello.webp')
    await message.answer_photo(image_from_pc, caption='Пообщаемся?)')
    await asyncio.sleep(2)
    await message.answer("Рад тебя видеть!<b> {0.first_name} </b>".format(message.from_user),parse_mode='html')
    #обработчик команд RANDOM
# /rnd 1-30 
@dp.message(Command(commands=['random','rand','rnd']))
async def get_random(message: types.Message, command:CommandObject):
    a,b=[int(n)for n in command.args.split('-')]
    
    rnum= randint (a,b)
    await message.reply(f'Случайное число:\t{rnum}')


@dp.message(Command('image'))
async def upload_photo(message: types.Message):
    image_from_pc = FSInputFile('hello.webp')
    await message.answer_photo(image_from_pc, caption='Пообщаемся?)')

@dp.message(Command('MyGroup'))
async def cmd_to_group(message:types.Message, bot:Bot):
    await bot.send_message(GROUP_ID,'HELLO from Farzin')
# ping pong 
@dp.message()
async def echo(message: types.Message):
    print("messege listened")
    #await message.answer('бот Фарзин услышал: ' + message.text)



# непрерывный режим работы бота в АССИНХРОННОМ режиме 
async def main():
    await dp.start_polling(bot)
    #delete all unhandled message
    await bot.delete_webhook(drop_pending_updates=True)

# основной цикл
if __name__ == '__main__':
    asyncio.run(main())

