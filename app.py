from flask import Flask
import telegram

TOKEN='6440042136:AAGp50G4rRElB42wkDg7DlM91-opDBQwjhc'
bot = telegram.Bot(TOKEN)
chat_id='5271463532'
app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    bot.send_message(chat_id,text='Hello world')
    return "Hello"

if __name__=='__main__':
    app.run(debug=True)