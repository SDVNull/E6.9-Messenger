const socket = new WebSocket(`ws://localhost:8000/ws/group_chat/${groupId}/`);

socket.onmessage = (e) => {
    const message = JSON.parse(e.data);
    // Обработка сообщения
};

// Отправка сообщения
function sendMessage(text) {
    socket.send(JSON.stringify({
        'sender': currentUserId,
        'text': text,
        'group_id': groupId
    }));
}