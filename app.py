from flask import Flask,request
import telegram
# Create the application instance
TOKEN ='6440042136:AAGp50G4rRElB42wkDg7DlM91-opDBQwjhc'
bot = telegram.Bot(TOKEN)
# chat_id = '5271463532'
app = Flask(__name__)

@app.route('/',methods=["POST"])
def index():
    data=request.get_json()
    print(data)
    if 'text' in data['message']:
        bot.send_message(chat_id=data['message']['chat']['id'], text=data['message']['text'])

    if 'file_id' in data['message']:
        bot.send_document(chat_id=data['message']['chat']['id'], document=data['message']['file_id'])

    return 'index page'

if __name__=="__main__":
    app.run(debug=True)
