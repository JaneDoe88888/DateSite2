from django.shortcuts import render, redirect

from chat.models import Chat, User, Message


def chat_page(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("chat:login-user")
    context = {}
    return render(request, "chat/chat.html", context)


def get_chats(request):
    chats = Chat.objects.filter(members__in=[request.user.id])
    print(chats)
    context = {'chats': chats}
    return render(request, 'chat/chat.html', context)


def get_chat(request, chat_id):
    chats = Chat.objects.filter(members__in=[request.user.id])
    chat = Chat.objects.get(id=chat_id)
    print(chat)
    context = {'active_chat': chat, 'chats': chats}
    return render(request, 'chat/chat.html', context)


def get_message(request):
    message = Message.objects.all().order_by('-created_at')
    return render(request, 'chat/chat.html', {'message': message})