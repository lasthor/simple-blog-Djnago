'''from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import Post,Follower
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q

# Create your views here.

def home(request):
    try:
        user_who_is_following = Follower.objects.filter(follower=request.user.id)
        #we used flat=True to get list of followed user id instead of tuples of followed user id
        following_postes = Post.objects.filter(author__in=user_who_is_following.values_list('followed',flat=True))

    except:
        return HttpResponse('No posts found')
    return render(request,'blog_app/poste.html',{'postes':following_postes})

#this view is for showing the about page
#we used safe=False to return a dictionary instead of a string

def about(request):
    return JsonResponse({'about':'This is the about page'},safe=False)


#this view is for showing the current user profile
#the current user profile contains the number of followers and the number of users that the current user is following

def profile(request):
    try:
        user_followers_count = Follower.objects.filter(followed=request.user.id)
        user_who_is_following_count = Follower.objects.filter(follower=request.user.id)
        my_post = Post.objects.raw('SELECT * FROM blog_app_post WHERE author_id = %s ORDER BY  date_created',[request.user.id])

    except:
        return HttpResponse('no profile found')
      
    context = {
        'user_followers_count':user_followers_count.count(),
        'user_who_is_following_count':user_who_is_following_count.count(),
        'my_post':my_post,
    }
    return render(request,'blog_app/profile.html',context)



#this view is for showing the list of users that the current user is not following
#and the current user can follow them

def friends_suggestions(request):
    try:
       user_who_is_following = Follower.objects.filter(follower_id=request.user.id)
       #n Django, 'Q' is a class that is used to create complex database queries by combining different filters with logical operators. 
       # It allows you to create more advanced queries than just using the 'filter()' method alone.
       # 'Q' objects are particularly useful when you need to use OR conditions between filters. 
       # By default, when you use 'filter()' method on a queryset, 
       # all filters are combined using the AND operator. However, 
       # sometimes you may want to use OR conditions, which is where 'Q' comes in handy.
       users = User.objects.all().exclude(Q(pk__in=user_who_is_following.values_list('followed',flat=True)) | Q (pk=request.user.id))
        
    except:
        return HttpResponse('no users found problem of query')
    
    return render(request,'blog_app/friends_suggestions.html',{'users':users})



#there may be cases where you want to exempt a view from CSRF protection. 
# For example, if you're building an API and want to allow requests from external sources,
#  you may need to disable CSRF protection for that view.
@csrf_exempt
def follow(request):
    if request.method =='POST':
        user_following = request.POST.get('user_id_for_following')
        relation = Follower.objects.create(followed_id=user_following,follower_id=request.user.id)
        relation.save()
        user_name_of_following = User.objects.get(pk=user_following)

        return JsonResponse ({'success': 'request is success','user_name_of_following':user_name_of_following.username})
    
    else:
         return JsonResponse ({'success': False, 'error': 'Invalid request method'})
    
    return redirect('friends_suggestions')
    
#function to unfollow a user# code from whisperer aws
def unfollow(request):
    if request.method =='POST':
        user_following = request.POST.get('user_id_for_following')
        relation = Follower.objects.filter(followed_id=user_following,follower_id=request.user.id).delete()
        return JsonResponse ({'success': 'request is success'})
    
    else:
         return JsonResponse ({'success': False, 'error': 'Invalid request method'})
    
    return redirect('friends_suggestions')

#funtion to unfollow a user #code from copilot
def unfollow(request):
    if request.method =='POST':
        user_following = request.POST.get('user_id_for_following')
        relation = Follower.objects.filter(followed_id=user_following,follower_id=request.user.id).delete()
        return JsonResponse ({'success': 'request is success'})
    
    else:
         return JsonResponse ({'success': False, 'error': 'Invalid request method'})
    
    return redirect('friends_suggestions')'''