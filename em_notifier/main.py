import requests

from flask import Flask
from flask import request
from flask import jsonify

from config import token, chats     # TODO check usernames from getUpdates, collect chat IDs

app = Flask(__name__)

URL = f'https://api.telegram.org/bot{token}/'


def send_message(chat_id, text='Wait, please...'):
    url = URL + 'sendMessage'

    msg = {'chat_id': chat_id, 'text': text}
    r = requests.post(url, json=msg)
    return r.json()


# @app.route(f'/{token}', methods=['POST', 'GET'])
@app.route('/', methods=['POST', 'GET'])
def index():
    return '<h1>Telebot EM notifier for Smart Analytics</h1>'


# Event monitoring listener
@app.route('/listener/', methods=['POST', 'GET'])
def listener():
    if request.method == 'POST':
        data = request.get_json()
        msg = f"Huston, we have a problem! \n{data['name']}: {data['desc']}"

        for chat in chats:
            send_message(chat, text=msg)        # TODO send trb in file?
        return jsonify({'status': 'success'})
    return "<h1>I'm EM notifier</h1>"


if __name__ == '__main__':
    app.run()
