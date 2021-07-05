import telebot
import yfinance as yf

TOKEN = '1680930811:AAGfWdG7kBwQFRFSnzeck9fr-sGTQLsSz8A'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, '''Olá.
Para ações brasileiras adicione ".SA" no final. Exemplo: MGLU3.SA
Para critomoedas escreva a sigla seguida de "-USD". Exemplo: BTC-USD
Para ações internacionais apenas a sigla. Exemplo: AAPL
Índice Bovespa: ^BVSP
S&P 500: ^GSPC
Se alguma sigla não funcionar, pesquise o nome da ação em https://finance.yahoo.com/ e veja qual é a sigla correta.
Caso o erro persista, @kayoricardo no telegram.


    ''')


@bot.message_handler(commands=["help"])
def comandos(message):
    bot.send_message(message.chat.id, '''Para ações brasileiras adicione ".SA" no final. Exemplo: MGLU3.SA
Para critomoedas escreva a sigla seguida de "-USD". Exemplo: BTC-USD
Para ações internacionais apenas a sigla. Exemplo: AAPL
Índice Bovespa: ^BVSP
S&P 500: ^GSPC
Se alguma sigla não funcionar, pesquise o nome da ação em https://finance.yahoo.com/ e veja qual é a sigla correta.
Caso o erro persista, @kayoricardo no telegram. ''')


@bot.message_handler(commands=["pause"])
def pause(message):
    bot.send_message(message.chat.id, 'Parado')


@bot.message_handler(func=lambda m: True)
def text(message):
    try:
        fechamento = yf.Ticker(message.text)
        fechamento_dia = fechamento.history(period='1d', interval='1m')
        final = fechamento_dia.Close[-1].round(2)
        bot.reply_to(message, f'O último preço da ação {(message.text).upper()} é {final}')

    except:
        bot.reply_to(message, 'Não encontrei essa ação. Digite /help para ver como digitar.')


bot.polling()