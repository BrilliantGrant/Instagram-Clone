from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
# from . forms import CommentForm,PicForm,ProfileUpdateForm,UpdatePicCaption 
from django.http  import HttpResponse
from . models import Pic ,Profile, Likes, Follow, Comment,Unfollow
from django.conf import settings


# Create your views here.
@login_required(login_url='/accounts/login/')
def comment(request):
	username = current_user.username
	comments = Comment.objects.filter(image_id=image_id)
	current_user = request.user

	if request.method == 'POST':
		form = CommentForm(request.POST)

		if form.is_valid():
			comment = form.save(commit = False)
			comment.user_id = current_user
			comment.save()
			return redirect(timeline)
		else:
			form = CommentForm()

			return render(request,'my-inst/comment.html',{"form":form})  


@login_required(login_url='/accounts/login/')
def profile(request):
	 current_user = request.user
	 profile = Profile.objects.all()
	 follower = Follow.objects.filter(user = profile)

	 return render(request, 'profile.html',{"current_user":current_user,"profile":profile,"follower":follower})

@login_required(login_url='/accounts/login/')
def timeline(request):
	current_user = request.user 
	Myprofile = Profile.objects.order_by('-time_uploaded')
	comment = Comment.objects.order_by('-time_comment')
	

	return render(request, 'my-inst/timeline.html',{"Myprofile":Myprofile,"comment":comment})

@login_required(login_url='/accounts/login/')
def single_pic(request,pic_id):
	pic = pic.objects.get(id= pic_id)

	return render(request, 'my-inst/single_pic.html',{"pic":pic})

@login_required(login_url='/accounts/login/')
def like(request,pic_id):
	Pic = Pic.objects.get(id=pic_id)
	like +=1
	save_like()
	return redirect(timeline)

@login_required(login_url='/accounts/login/')
def search_pic(request):

	if 'pic' in request.GET and request.GET["pic"]:
		search_pic = request.GET.get("pic")
		got_users = Profile.find_profile(search_pic)
		message =f"{search_pic}"

		return render(request,'my-inst/search_pic.html',{"got_users":got_users,"message":message})
	else:
		message = "Invalid username"
		return render(request,'my-inst/search_pic.html',{"message":message})

def search_results(request):

    if 'pic' in request.GET and request.GET["pic"]:
        search_term = request.GET.get("pic")
        searched_images = Images.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'my-inst/search_pic.html',{"message":message,"pics": searched_pics})

    else:
        message = "You haven't searched for any term"
        return render(request, 'my-inst/search_pic.html',{"message":message})
