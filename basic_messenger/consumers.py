from channels.generic.websocket import AsyncWebsocketConsumer
import json

class GroupChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_id = self.scope['url_route']['kwargs']['group_id']
        await self.channel_layer.group_add(self.group_id, self.channel_name)
        await self.accept()

    async def receive(self, text_data):
        data = json.loads(text_data)
        # Сохранение сообщения в БД и рассылка участникам
        await self.channel_layer.group_send(
            self.group_id,
            {"type": "chat.message", "data": data}
        )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps(event["data"]))