
import telebot
from telebot import types
from congif import TOKEN
import psycopg2


a = psycopg2.connect(database = 'new',user = 'timka',password = '1234',host = 'localhost',port = '5432')

a.autocommit = True
cur = a.cursor()
# cur.execute("create table pe(id serial primary key,name varchar,age int)")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])

def wel(message):
    menu = types.InlineKeyboardMarkup(row_width=1)
    b1 = types.InlineKeyboardButton("данные",callback_data="full")
    menu.add(b1)
    bot.send_message(message.chat.id,"привет дорогой друг",reply_markup=menu)


@bot.callback_query_handler(func=lambda call:True)
def welcome(call):
       
        if call.data == "full":
              @bot.message_handler(content_types=['text'])
              def new(message):
                    if message.text is not None:
                          cur.execute(f"insert into pe(name,age)values(%s,%s)",tuple(message.text.split()))
                          bot.send_message(message.chat.id,"данные сохранили")
                    else:
                          print("не добвлен")
        else:
              print("не ок")







        






bot.polling(non_stop=True)

a.close()
cur.close()

