from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Pic(models.Model):
    pic = models.ImageField(upload_to = "pics/",null = True)
    user = models.ForeignKey(User,null=True)
    pic_name = models.CharField(max_length = 30,null = True)
    likes = models.IntegerField(default=0)
    pic_caption = models.TextField(null = True)
    pub_date = models.DateTimeField(auto_now_add=True,null=True)
    # profile = models.ForeignKey(Profile, null=True) 
    comments = models.IntegerField(default=0)


    def __str__(self):
    	return self.pic_name

    def delete_pic(self):
    	self.delete()

    def save_pic(self):
    	self.save()

    def update_caption(self,new_caption):
    	self.pic_caption = new_caption
    	self.save()


    @classmethod
    def get_pics_by_user(cls,id):
        sent_pics = Pic.objects.filter(user_id=id)
        return sent_pics

    @classmethod
    def get_pics_by_id(cls,id):
        fetched_pic = Pic.objects.get(id = id)
        return  fetched_pic

    class Meta:
    	ordering = ['-pub_date']


    def __str__(self):
    	return self.user.username

    def save_profile(self):
    	self.save()

class Profile(models.Model):
	username = models.CharField(default='User',max_length=30)
	profile_pic = models.ImageField(upload_to = "pics/",null=True)
	bio = models.TextField(default='',blank = True)
	first_name = models.CharField(max_length =30)
	last_name = models.CharField(max_length =30)

	def __str__(self):
		return self.username

	def delete_profile(self):
		self.delete()

	def save_profile(self):
		self.save()

	@classmethod
	def search_profile(cls,name):
		got_profiles = cls.objects.filter(username__icontains = name).all()
		return got_profiles


  


class Comment(models.Model):
	pic = models.ForeignKey(Pic, null=True)
	date_posted = models.DateTimeField(auto_now_add=True,null=True)
	comment= models.TextField(max_length ='')
	user = models.ForeignKey(User, null=True)

	def __str__(self):
		return self.comment


	def delete_comment(self):
		self.delete()

	def save_comment(self):
		self.save()

class Follow(models.Model):
	user = models.ForeignKey(Profile,null=True)
	follower = models.ForeignKey(User,null=True)

	def __int__(self):
		return self.name

	def save_follower(self):
		self.save()

	def delete_follower(self):
		self.save()

class Unfollow(models.Model):
	user = models.ForeignKey(Profile,null=True)
	follower = models.ForeignKey(User,null=True)

	def __int__(self):
		return self.name

class Likes(models.Model):
	user = models.ForeignKey(Profile,null=True)
	# pic = models.ForeignKey(Pic,null=True)

	def __int__(self):
		return self.name

	def unlike(self):
		self.delete()

	def save_like(self):
		self.save() 

















