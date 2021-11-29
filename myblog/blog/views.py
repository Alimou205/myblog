from django.core import paginator
from django.shortcuts import render, get_object_or_404

from .forms import CommentForm
from .models import Category, Comment, Post
from django.core.paginator import(Paginator,EmptyPage,PageNotAnInteger)
from django.views import generic
# Create your views here.

def post_list(request, category=None):

    posts = Post.objects.all()
    categories = Category.objects.all()
    if category:
        category=get_object_or_404(Category, slug=category)
        posts =posts.filter(category=category)
    paginator =Paginator(posts, 2)
    page = request.GET.get('page')
    try:
        posts= paginator.page(page)
    except PageNotAnInteger:
         posts= paginator.page(1)
    except EmptyPage:
         posts= paginator.page(paginator.num_pages)
    #posts =Post.objects.all()
    context = {'posts': posts, 'page':page,'categories':categories,}
    return render(request,'blog/post/list.html', context)
'''
class PostListView(generic.ListView):
    queryset = Post.objects.all()
    paginate_by = 2
    template_name ='blog/post/list.html'
    context_object_name ='posts'
'''
def post_detail(request, slug: str):

    post = get_object_or_404(Post, slug=slug)
    commnets = Comment.objects.filter(post=post.id)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment =comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request,'blog/post/detail.html', {'post': post,'comments':commnets,'new_comment':new_comment,'comment_form':comment_form})