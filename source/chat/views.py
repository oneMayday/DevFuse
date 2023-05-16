from django.shortcuts import render


def room_choice(request):
    return render(request, "chat/room-choice.html")


def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})
