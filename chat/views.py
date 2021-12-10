from django.shortcuts import render,redirect
from django.http import HttpResponseBadRequest, HttpResponse, JsonResponse
from django.template import loader
from .models import Message, Room

def chat(request):
	if request.user.is_anonymous or request.user.is_active==False:
		return redirect('/login')
	else:
		if request.method =='POST':
			target = request.POST.get('target')
			user = request.user.username
			if target == user:
				return redirect('chat/')
			if Room.objects.filter(user=user).filter(target=target).exists()==False:
				new_target1 = Room.objects.create(user=user,target=target)
				new_target1.save()
				new_target2 = Room.objects.create(user=target,target=user)
				new_target2.save()
		unsorted_user_chats = Room.objects.all().filter(user=request.user.username)
		user_chats=sorted(list(unsorted_user_chats.values()),key=lambda k:k['date'])[::-1]
		return render(request, 'chat.html',{'user_chats':user_chats})

def room(request,friend):
	if request.user.is_anonymous or request.user.is_active==False:
		return redirect('/login')
	else:
		is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
		if is_ajax:
			template = loader.get_template("message.html")
			return HttpResponse(template.render({'friend':friend}, request))
		else:
			return HttpResponseBadRequest('Invalid request')

def getmessages(request,friend):
    if request.user.is_anonymous or request.user.is_active==False:
        return redirect('/login')
    else:
    	all_messages=Message.objects.all().filter(sender=request.user).filter(receiver=friend)|Message.objects.all().filter(sender=friend).filter(receiver=request.user)
    	all_messages.order_by('-date')
    	if len(all_messages) != 0:
    		Room.objects.filter(user=request.user.username).filter(target=friend).update(date=all_messages.last().date,last_message=all_messages.last().message)
    	return JsonResponse({"messages":list(all_messages.values())})

def send(request):
    if request.user.is_anonymous or request.user.is_active==False:
        return redirect('/login')
    else:
    	if request.method == 'POST':
    		sender=request.POST.get("username")
    		receiver=request.POST.get("friend")
    		message=request.POST.get("message")
    		message=message.strip()
    		if (message == "") or (request.user.username != sender):
    			return redirect('/room/'+receiver)
    		if sender==receiver:
    			return redirect('/')
    		newmessage=Message(sender=sender,receiver=receiver,message=message)
    		newmessage.save()
    		newmessage.rooms.add(Room.objects.filter(user=sender).filter(target=receiver))
    		all_messages=Message.objects.all().filter(sender=sender).filter(receiver=receiver)|Message.objects.all().filter(sender=receiver).filter(receiver=sender)
    		all_messages.order_by('-date')
    		if len(all_messages) != 0:
    			Room.objects.filter(user=request.user.username).filter(target=friend).update(date=all_messages.last().date,last_message=all_messages.last().message)
    		return HttpResponse("message sent")
    	else:
    		return redirect('/')