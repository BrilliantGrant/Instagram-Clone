from django.test import TestCase
from . models import Comment



class CommentTestClass(TestCase):

    def setUp(self):
        
        self.new_comment = Comment(comment= "comment")
        self.new_comment.save()

  