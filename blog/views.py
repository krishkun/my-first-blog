from django.shortcuts import render
from django.utils import timezone
from .models import Post
from datetime import datetime

def post_list(request):
	posts = Post.objects.filter(publised_date__lte=timezone.now()).order_by('publised_date')
	return render(request, 'blog/post_list.html',{'posts':posts})


