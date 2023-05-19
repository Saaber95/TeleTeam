from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from core.utils.callbackdata import MacInfo
from core.settings import settings


#TT_oficial = 'https://t.me/c/1959648126'
#TT_profile = 'https://t.me/c/1828541503'
#TT_projects = 'https://t.me/c/1925274052'
#TT_flood = 'https://t.me/c/1928470387'
# ProfilChanal = 'https://t.me/c/1857429309/6'

FAQurl='https://docs.google.com/document/d/1Rxbrr5mqoa-UlLR-RqmnhF6p8n3S3H8hwuzo0PJezWU/edit'
MyQuiz = 'https://docs.google.com/forms/d/1LbLF_vE_0RRRr9tgZPDMmRrAJU33VImCrEMp3DidUUc/edit'

def get_inline_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(text='FAQ', url=FAQurl)
    keyboard_builder.button(text='ОФИЦИАЛЬНЫЙ', url=settings.TT_oficial )
    keyboard_builder.button(text='ПРОФИЛИ', url=settings.TT_profile )
    keyboard_builder.button(text='ПРОЕКТЫ', url=settings.TT_projects)
    keyboard_builder.button(text='БОЛТАЛКА',  url=settings.TT_flood)
    keyboard_builder.button(text='ФОТОСКЛАД',  callback_data=MacInfo(model='1', size=6, chip='1', year=1))

 #    keyboard_builder.button(text='Общий канал', callback_data=MacInfo(model='1', size=1, chip='1', year=1))

    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()


def get_inline_keyboard1():
    keyboard_builder = InlineKeyboardBuilder()

    keyboard_builder.button(text='FAQ1', callback_data=MacInfo(model='air', size=13, chip='m1', year=2020))
    keyboard_builder.button(text='FAQ2', callback_data=MacInfo(model='pro', size=14, chip='m1', year=2021))
    keyboard_builder.button(text='FAQ3', callback_data=MacInfo(model='pro', size=16, chip='i7', year=2019))

    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()

def get_inline_keyboard2():
    keyboard_builder = InlineKeyboardBuilder()

    keyboard_builder.button(text='Общий Канал1', callback_data=MacInfo(model='air', size=13, chip='m1', year=2020))
    keyboard_builder.button(text='Общий Канал2', callback_data=MacInfo(model='pro', size=14, chip='m1', year=2021))
    keyboard_builder.button(text='Общий Канал3', callback_data=MacInfo(model='pro', size=16, chip='i7', year=2019))

    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()


def get_inline_keyboard3():
    keyboard_builder = InlineKeyboardBuilder()

    keyboard_builder.button(text='FAQ1', callback_data=MacInfo(model='air', size=13, chip='m1', year=2020))
    keyboard_builder.button(text='FAQ2', callback_data=MacInfo(model='pro', size=14, chip='m1', year=2021))
    keyboard_builder.button(text='FAQ3', callback_data=MacInfo(model='pro', size=16, chip='i7', year=2019))

    keyboard_builder.adjust(1)
    return keyboard_builder.as_markup()




