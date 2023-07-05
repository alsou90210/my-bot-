
import csv
from aiogram.types import ReplyKeyboardMarkup,InlineKeyboardButton,InlineKeyboardMarkup,Message
from parsing import exchager_currency 
from text import text_start 
from database import Database
from aiogram import Bot, Dispatcher 

TOKEN = ''

bot = Bot(TOKEN)
dp = Dispatcher

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add('рассылка','admin pan')
keyboard.add('тех.поддержка','курсы валют')

keyboard_url = InlineKeyboardMarkup()
instagram_url = InlineKeyboardButton(text='instagram',url='[to listen](https://www.youtube.com/watch?v=W05MCT3Ae6k)')
telegram_url = InlineKeyboardButton (text='telegram',url='https://t.me/alsou3010')
keyboard_url.add(instagram_url,telegram_url)


list_1 = [573015206, 1008889358, 5647517221, 5873445472]
@dp.message_handler(commands=['start','help', '123'])
async def hello_bot(message: Message):
    with open('IDs.csv','r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        user_id = [str(message.from_user.id),str(message.from_user.first_name)]
        check_user =  list(reader)
        if  user_id not in check_user:
            with open('IDs.csv','a') as file:
                writer = csv.writer(file)
                writer.writerow([message.from_user.id, message.from_user.first_name])
                bot.send_message(message.from_user.id, text=text_start, reply_markup=keyboard)
        else:
            bot.send_message(message.from_user.id, text='Привет ты есть в базе', reply_markup=keyboard)



@bot.message_handler(commands=['info'])
def info_bot(message):
    if message.from_user.id == 5949761485:
        for item in list_1:
            try:
                bot.send_message(chat_id = item,text='рассылка от Alsou')
            except Exception:
                continue    
        bot.send_message(message.from_user.id,text='рассылка успешна отправлена')   
    
    else:
        bot.reply_to(message,'u are not admin')


@bot.message_handler(commands=['admin'])
def admin_bot(message):
    if message.from_user.id == 5949761485:
        bot.reply_to(message,'hello admin')
        with open('database.txt','r') as file_name:
            user_list= file_name.read()
       
        bot.reply_to(message ,'all users\n'+user_list)
        with open('database.txt','r') as file1:
            user_list = file1.readlines()
            for ids in user_list:
                bot.send_message(chat_id=ids,text='рассылка успешна отправлена') 
    else:
        bot.reply_to(message,'u are not admin')          



@bot.message_handler(content_types=['text'])
def message_text(message):
    first_name = message.from_user.first_name
    msg = message.text
    with open('message.txt','a') as file2:
        file2.write(f'от пользователя:{first_name}Сообщение {msg}\n')
 
    if message.text == 'тех.поддержка':
        bot.send_message(message.from_user.id,text='связаться с тех поддержкой можно по ссылке\@alsou',reply_markup=keyboard_url)

    elif message.text ==  'рассылка':
        info_bot(message) 

    elif message.text ==  'admin pan':
        admin_bot(message)

    elif message.text == 'курсы валют':
        currency = exchager_currency()
        currency_list = []
        for key,value in currency.items():
            result = f'{key}-{value}'
            currency_list.append(result)
        text = '\n'.join(currency_list)    
        bot.send_message(message.from_user.id,text=f'курсы валют\n\n{text}')   


if __name__ =='__main__':
  bot.polling()    