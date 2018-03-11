from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from . forms import ProfileUploadForm,CommentForm
from django.http  import HttpResponse
from . models import Pic ,Profile, Likes, Follow, Comment,Unfollow
from django.conf import settings


# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
      title = 'Instagram'
      pic_posts = Pic.objects.all()
      comments = Comment.objects.all()

      print(pic_posts)
      return render(request, 'index.html', {"title":title,"pic_posts":pic_posts, "comments":comments})


@login_required(login_url='/accounts/login/')
def comment(request,id):
	
	post = get_object_or_404(Pic,id=id)	
	current_user = request.user
	print(post)

	if request.method == 'POST':
		form = CommentForm(request.POST)

		if form.is_valid():
			comment = form.save(commit=False)
			comment.user = current_user
			comment.pic = post
			comment.save()
			return redirect('index')
	else:
		form = CommentForm()

	return render(request,'index.html',{"form":form})  


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


@login_required(login_url='/accounts/login/')
def upload_profile(request):
    current_user = request.user 
    title = 'Upload Profile'
    try:
        requested_profile = Profile.objects.get(user_id = current_user.id)
        if request.method == 'POST':
            form = ProfileUploadForm(request.POST,request.FILES)

            if form.is_valid():
                requested_profile.profile_pic = form.cleaned_data['profile_pic']
                requested_profile.bio = form.cleaned_data['bio']
                requested_profile.username = form.cleaned_data['username']
                requested_profile.save_profile()
                return redirect( profile )
        else:
            form = ProfileUploadForm()
    except:
        if request.method == 'POST':
            form = ProfileUploadForm(request.POST,request.FILES)

            if form.is_valid():
                new_profile = Profile(profile_pic = form.cleaned_data['profile_pic'],bio = form.cleaned_data['bio'],username = form.cleaned_data['username'])
                new_profile.save_profile()
                return redirect( profile )
        else:
            form = ProfileUploadForm()


    return render(request,'upload_profile.html',{"title":title,"current_user":current_user,"form":form})


@login_required(login_url='/accounts/login/')
def send(request):
    '''
    View function that displays a forms that allows users to upload images
    '''
    current_user = request.user

    if request.method == 'POST':

        form = ImageForm(request.POST ,request.FILES)

        if form.is_valid():
            image = form.save(commit = False)
            image.user_key = current_user
            image.likes +=0
            image.save() 

            return redirect( timeline)
    else:
        form = ImageForm() 
    return render(request, 'my-inst/send.html',{"form" : form}) 

