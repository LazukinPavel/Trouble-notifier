import requests

from bs4 import BeautifulSoup

from flask import Flask
from flask import request
from flask import jsonify
from flask_sslify import SSLify

from config import token, chats
# from utils import write_json, upload_to_s3, get_file_link

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
    # if request.method == 'POST':
    #     r = request.get_json()
    #     chat_id = r['message']['chat']['id']
    #     print('=== CHAT ID', chat_id)
    #     write_json(chat_id, '/tmp/chat_ids')
    #     upload_to_s3('chat_ids')
    #
    #     print('=== XXX')
    #     link = get_file_link('chat_ids')
    #
    #     print('=== LINK', link)
    #
    #     resp_ids = requests.get(link)
    #     print('=== RESPONSE FROM S3', resp_ids.content)
        # with open('telegram_chat_ids'):
        # print('')
        # send_message(chat_id, text=msg)

        # return jsonify(r)
    return '<h1>Telebot EM notifier for Smart Analytics</h1>'


# Event monitoring listener
@app.route('/listener/', methods=['POST', 'GET'])
def listener():
    if request.method == 'POST':
        data = request.get_json()
        msg = f"Huston, we have a problem! \n{data['name']}: {data['desc']} \n{data['trb']}"

        for chat in chats:
            send_message(chat, text=msg)
        return jsonify({'status': 'success'})
    return "<h1>I'm EM notifier</h1>"


if __name__ == '__main__':
    app.run()
