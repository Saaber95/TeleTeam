from aiogram import Bot
from aiogram.types import Message
from aiogram.types import FSInputFile
import json
import openai
from core.settings import settings
import string
SPREADSHEET_URL = "https://docs.google.com/spreadsheets/d/1S4Xzkcy2DDVnb6WlzkaOQwxob0vAZgKTx-MuZIPDYpo/edit#gid=0"


import gspread
from gspread import Cell, Client, Spreadsheet, Worksheet

from  work_with_googl import  show_available_worksheets,show_main_ws,create_ws_fill_and_del, \
    insert_some_data, append_rows,update_table_by_cells, show_all_values_in_ws, create_and_fill_comments_ws, show_worksheet

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
    await message.answer(f'           Добро пожаловать в HR-бот Teleteam v.3.0       . \n ')



    photo = FSInputFile(r'TeleTeam.png')
    await bot.send_photo(message.chat.id, photo)
    await message.answer(f'.                ГЛАВНОЕ  МЕНЮ                     .\n ',
                reply_markup=get_inline_keyboard())





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


#-----------------------------------------

async def get_vasja(message: Message, bot: Bot):
    if message.chat.id != settings.oficial and \
       message.chat.id != settings.profile and \
       message.chat.id != settings.projects:
        ask = message.text
        ask.replace('/R2D2','')
        await message.answer(f'@R2D2> готовлю ответ.')
        json_str = json.dumps(message.dict(), default=str)
        print(json_str)

        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
#            model="gpt-4",
            messages=[
                {"role": "user", "content": ask}
            ]
        )
        await message.answer(completion.choices[0].message.content)
#-----------------------------------------


def  init_google_sheets():
    gc: Client = gspread.service_account("./service_account.json")
    sh: Spreadsheet = gc.open_by_url(SPREADSHEET_URL)
    print(sh)
    global ws
    ws = sh.sheet1
    show_available_worksheets(sh)
    show_main_ws(sh)
    show_all_values_in_ws(ws)
    print ('WS==', ws)

async def set_task(message: Message, bot: Bot ):


    if message.chat.id != settings.oficial and \
       message.chat.id != settings.profile and \
       message.chat.id != settings.projects:
        ask = message.text
        print (ask)
        ask.replace('Task', ';')
        ask.replace('task', ';')
        ask.replace('TASK', ' ;')
        print (ask)


        words = ask.split(";",6)
        print(words)
        print(ws)
        ws.append_rows([
                        words,
                    ])

#    await message.answer(f'Добавлено:',words)


#-----------------------------------------



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
    await message.answer(f' Повторите вопрос.')
#    photo = FSInputFile(r'Vall.jpg')
#    await bot.send_photo(message.chat.id, photo)


#    await set_commands(Bot)



async def make_profile(message: Message, bot: Bot):
    # --------------Чистим--------------------------------#

    chatID = -1001828541503  # ID канала, из которого нужно удалить сообщения
#    chatID = 1928470387
    # message_count = 0 # Счетчик удаленных сообщений
    #
    # async for message in bot.iter_history(chatID, message_thread_id=6 ):
    #     try:
    #         await bot.delete_message(chatID, message.message_id, message_thread_id=6 )
    #         message_count += 1
    #     except exceptions.MessageCantBeDeleted:
    #         pass
    #

    # --------------Отправляем в канал профили--------------------------------#

    codecs = ["utf-8", "cp1252", "cp437", "utf-16be", "utf-16"]
    path_pic = r'BASE\PIC\\'
    path_txt = r'BASE\TXT\\'
    for i in range(0, 4):
        name_pic = path_pic + str(i + 1) + '.png'
        name_txt = path_txt + str(i + 1) + '.txt'
        photo = FSInputFile(name_pic)
        text = open(name_txt, encoding=codecs[0]).read()

#        await bot.send_photo(message.chat.id, photo,  caption=text, disable_notification=True)

#        message_thread_id = 1
        await bot.send_photo(chatID, photo,  caption=text, disable_notification=True)
