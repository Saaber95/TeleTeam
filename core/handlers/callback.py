from aiogram import Bot
from aiogram.types import CallbackQuery, FSInputFile, InputMediaPhoto
from core.utils.callbackdata import MacInfo
import glob

# async def select_macbook(call: CallbackQuery, bot: Bot):
#     model = call.data.split('_')[1]
#     size = call.data.split('_')[2]
#     chip = call.data.split('_')[3]
#     year = call.data.split('_')[4]
#     answer = f'{call.message.from_user.first_name}, ты выбрал Apple Macbook {model} с диагональю экрана ' \
#              f'{size} дюймов, на чипе {chip} {year} года.'
#     await call.message.answer(answer)
#     await call.answer()


async def select_macbook(call: CallbackQuery, bot: Bot, callback_data: MacInfo ):

    model = callback_data.model
    size = callback_data.size
    chip = callback_data.chip
    year = callback_data.year
    codecs = ["utf-8","cp1252", "cp437", "utf-16be", "utf-16"]
    if size==1 :
        answer = f'--ветка Х-1-'
#  итак нужно последовательно вывести 4 фотки с текстм



    if size==2 :
        answer = f'--ветка Х-2-'
    if size==3 :
        all_media=[]
        images = glob.glob('images/*.jpg')
        answer = f'--ветка Х-3-'
        path_pic = r'BASE/PIC/'
        path_txt = r'BASE/TXT/'
        for i in range (0, 4):
            name_pic = path_pic + str(i+1) + '.png'
            name_txt = path_txt + str(i+1) + '.txt'
            photo = FSInputFile ( name_pic )
           #
           # all_media[i] =

            text = open(name_txt, encoding=codecs[0]).read()
            # media = InputMediaPhoto(type='photo',
            #                             media=FSInputFile(name_pic),
            #                             caption=text)
            # all_media.append(media)
            mymess = call.message

#        await bot.send_media_group(mymess.chat.id, all_media)
            await bot.send_photo(mymess.chat.id, photo, caption=text)
#
    if size == 4 :
        photo = FSInputFile('baraban.gif')
        text = 'кручу-верчу-обмануть хочу'
        mymess = call.message
        await bot.send_photo(mymess.chat.id, photo, caption=text)
        answer = 'Выбран сотрудник ХХХХ ему отправленно приглашение'
    if size == 5:
        answer = 'Сегодня отмечабт день рождения:....\n А также  сегондня правднуется день взятия бастилии парижскими коммунарами'

    if size == 6:
        answer = 'ФОТКИ С КОРПОРАТИВА( Вы УВЕРЕНЫ ЧТО ХОТИТЕ ЭТО УВИДЕТЬ ?)'
    #    https: // t.me / c / 1873667582 / 1
        await call.message.answer(answer)
