from flask import Flask, request
import vk_api
import os

app = Flask(__name__)

GROUP_TOKEN = os.getenv("GROUP_TOKEN")
vk_session = vk_api.VkApi(token=GROUP_TOKEN)
vk = vk_session.get_api()

@app.route('/', methods=['POST'])
def main():
    data = request.json

    if data['type'] == 'confirmation':
        return 'ТВОЙ_КОД_ПОДТВЕРЖДЕНИЯ'

    elif data['type'] == 'message_new':
        user_id = data['object']['peer_id']
        message_text = data['object']['text']

        vk.messages.send(peer_id=user_id, message=f"Вы написали: {message_text}", random_id=0)

    return 'ok'
