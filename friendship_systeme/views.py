from django.shortcuts import render

from django.contrib.auth.models import User
from friendship.models import Friend, Follow, Block ,FriendshipRequest
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from django.db.models import FilteredRelation, Q
from django.utils.http import urlsafe_base64_encode



def all_users(request):
    all_users = User.objects.exclude(pk=request.user.id)
    
    list_users ={
        'all_users':all_users,
    }
    return render(request,'friendship_systeme/list_frindes.html',list_users)
    

@csrf_exempt
def add_friend(request):
    if request.method == 'POST':
        other_user=request.POST.get('user_to_add')
        other_user = User.objects.get(pk=other_user)
        Friend.objects.add_friend(
        request.user,                               # The sender
        other_user,                                 # The recipient
       )
    

    return JsonResponse(
        {
            'Friend':'added',
        }
    )

def sent_request(request):
    my_requests = Friend.objects.sent_requests(user=request.user)

    
    ''' print(my_requests[0].from_user)
    print(my_requests[0].to_user)'''
    _requests_= {
        'MY_requests':my_requests,
    }

    return render(request,'friendship_systeme/sent_requesets.html',_requests_)


def unread_requests_view(request):
    #all_unread_requests = Friend.objects.unread_requests(user=request.user)#its not working good
    all_unread_requests = FriendshipRequest.objects.filter(to_user=request.user.id)
    print(all_unread_requests)
    response = {
        'all_unread_requests':all_unread_requests
    }

    return render(request , 'friendship_systeme/all_unread_requests.html' , response)


@csrf_exempt
def accept(request):
    if request.method =='POST':

        other_user = request.POST.get('user_to_accept')
        friend_request = FriendshipRequest.objects.get(from_user=other_user, to_user=request.user.id)
        friend_request.accept()
        print(FriendshipRequest.objects.all())

        return JsonResponse({'messge':f'{request.user.id} and {other_user} are friends now'})


@csrf_exempt
def reject(request):
    if request.method =='POST':

        other_user = request.POST.get('usr_uuid')
        friend_request = FriendshipRequest.objects.get(from_user=other_user, to_user=request.user.id)
        friend_request.delete()

        return JsonResponse({'messge':f'{request.user.id} reject the user {other_user}'})
    

    