import telebot
from requests import get
import json

CHAVE_API = "6753133670:AAFK5DkmBRNTYcTuUELEGVilB9_hv-hV6qw"

bot = telebot.TeleBot(CHAVE_API)

@bot.message_handler(commands=["dados"])
def dados(msg):
    response = get("http://127.0.0.1:80/dados_clientes")
    if response.status_code == 200:
        data = json.loads(response.text)
        bot.send_message(msg.chat.id, json.dumps(data, indent=4))
    else:
        bot.send_message(msg.chat.id, "Erro ao tentar fazer consulta à API :(")

def verificar(msg):
    return True

@bot.message_handler(func=verificar)
def responder(msg):
    response_default = '''Olá para usar o bot e fazer requisições à API
temos as seguintes opções(clique no item):
/dados 
qualquer outra coisa diferente não funciona, clique em uma das opções!!!
'''
    bot.reply_to(msg, response_default)

bot.polling()
