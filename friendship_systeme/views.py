from django.shortcuts import render

from django.contrib.auth.models import User
from friendship.models import Friend, Follow, Block ,FriendshipRequest
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from django.db.models import FilteredRelation, Q



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
    print(FriendshipRequest._meta.fields)
    _requests_= {
        'MY_requests':my_requests,
    }

    return render(request,'friendship_systeme/sent_requesets.html',_requests_)


def unread_requests_view(request):
    all_unread_requests = Friend.objects.unread_requests(user=request.user)
    print(Friend._meta.fields)
    response = {
        'all_unread_requests':all_unread_requests
    }

    return render(request , 'friendship_systeme/all_unread_requests.html' , response)



    

    