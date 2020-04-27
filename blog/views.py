from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q
from blog.models import Post, Comment
from django.views.generic import ListView
from .forms import CommentForm
import pdb

def blog_index(request):
	posts = Post.objects.all().order_by('-created_on')
	paginator = Paginator(posts, 5)

	post_number = request.GET.get('page', 1)
	post_obj = paginator.get_page(post_number)

	context = {
		'post_obj' : post_obj
	}
	return render(request, 'blog_index.html', context)

def blog_category(request, category):
	posts = Post.objects.filter(
		categories__name__contains=category
	).order_by(
		'-created_on'
	)
	context = {
		'category' : category,
		'posts' : posts
	}
	return render(request, 'blog_category.html', context)

def blog_detail(request, pk):
	post = Post.objects.get(pk=pk)
	comments = Comment.objects.filter(post=post)

	form = CommentForm()
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = Comment(
				author = form.cleaned_data['author'],
				body = form.cleaned_data['body'],
				post = post
			)
			comment.save()

	context = {
		'post' : post,
		'comments' : comments,
		'form' : form,
	}
	return render(request, 'blog_detail.html', context)


class SearchResultsView(ListView):
    model = Post
    template_name = 'search.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list= Post.objects.filter(
            Q(title__icontains=query) | Q(body__icontains=query)
        )

        return object_list