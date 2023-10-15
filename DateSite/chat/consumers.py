import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async

from chat.models import Message


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.roomGroupName = "group_chat_gfg"
        await self.channel_layer.group_add(
            self.roomGroupName,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.roomGroupName,
            self.channel_layer
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)

        chat_id = text_data_json['chat_id']
        message = text_data_json["message"]
        author_id = text_data_json["author_id"]

        message = await database_sync_to_async(self.save_message)(author_id, message, chat_id)

        await self.channel_layer.group_send(
            self.roomGroupName, {
                "type": 'chat_message',
                "message": message,
            })

    def save_message(self, author_id, content, chat_id):
        message = Message.objects.create(
            chat_id=chat_id,
            author_id=author_id,
            content=content
        )
        return {
            'message': message.content,
            'pub_date': message.pub_date.strftime("%Y-%m-%d%H:%M:%S"),
            'chat_id': message.chat_id,
            'author_id': message.author_id
        }

    async def chat_message(self, event):
        message = event["message"]
        await self.send(text_data=json.dumps(message))
