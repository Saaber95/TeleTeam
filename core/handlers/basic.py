from aiogram import Bot
from aiogram.types import Message
from aiogram.types import FSInputFile
import json
from core.keyboards.reply import reply_keyboard, loc_tel_poll_keyboard, get_reply_keyboard
from core.keyboards.inline import  get_inline_keyboard
#from core.keyboards.inline import select_macbook, get_inline_keyboard
from core.utils.commands import set_commands, set_default_commands
from core.utils.dbconnect import Request

async def get_inline(message: Message, bot: Bot):
    await message.answer(f'Привет, {message.from_user.first_name}. ТЫ В ГЛАВНОМ МЕНЮ !',
                          reply_markup=get_inline_keyboard())


#async def get_start(message: Message, bot: Bot, counter: str, request: Request):
async def get_start(message: Message, bot: Bot):

#    await request.add_data(message.from_user.id, message.from_user.first_name)
#    await message.answer(f'Сообщение #{counter}')
    await message.answer(f' Добро пожаловать в HR-бот Teleteam.  \n '
    'Представьте, что вы едете в лифте в ваш любимый виртуальный офис , Двери вот-вот откроются! '
    'Пожалуйста, следуйте советам, которые помогут вам  быстрее адаптироваться в продукте '
#    'и сразу получать пользу',  reply_markup=get_reply_keyboard())
    'и сразу получать пользу')
    photo = FSInputFile(r'TeleTeam.png')
    await bot.send_photo(message.chat.id, photo)
    await message.answer(f'-                ВЫ НАХОДИТЕСЬ В ГЛАВНОМ МЕНЮ                     -\n ',
                reply_markup = get_inline_keyboard())


async def get_location(message: Message, bot: Bot):
    await message.answer(f'Ты отправил локацию!\r\a'
                         f'{message.location.latitude}\r\n{message.location.longitude}')


async def get_photo(message: Message, bot: Bot):
    await message.answer(f'Получено фото. отправленно на обработку ждите.')
    file = await bot.get_file(message.photo[-1].file_id)
    


    await bot.download_file(file.file_path, 'photo.jpg')
    photo1 = open('photo.jpg', 'rb')
    await bot. send_photo(chat_id = message.chat.id, photo=photo1)
#        file) download_file(file.file_path, 'photo.jpg')



async def get_hello(message: Message, bot: Bot):
    await message.answer(f'И тебе привет!')
    json_str = json.dumps(message.dict(), default=str)
    print(json_str)
async def get_FAQ(message: Message, bot: Bot):
    await message.answer(f'Здесь переход в FAQ!')
    json_str = json.dumps(message.dict(), default=str)
    print(json_str)
async def get_COM(message: Message, bot: Bot):
    await message.answer(f'Здесь переход в общий чай!')
    json_str = json.dumps(message.dict(), default=str)
    print(json_str)
async def get_CAN(message: Message, bot: Bot):
    await message.answer(f'Здесь переход в Канал с профилями')
    json_str = json.dumps(message.dict(), default=str)
    print(json_str)
async def get_ASK(message: Message, bot: Bot):
    await message.answer(f' Тут вопросы!')
    json_str = json.dumps(message.dict(), default=str)
    print(json_str)
async def get_menu(message: Message, bot: Bot):
    await message.answer(f'ВКЛ МЕНЮ')
    await set_default_commands(bot)

async def get_NOTHING(message: Message, bot: Bot):
    await message.answer(f'Я СОВСЕМ ЮНЫЙ БОТ. Я ТОЛЬКО УЧУСЬ.')
    photo = FSInputFile(r'Vall.jpg')
    await bot.send_photo(message.chat.id, photo)


#    await set_commands(Bot)



