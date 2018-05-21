from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from django.http import HttpResponse
from blog_posts.models import blog_posts

class PostsForm(ModelForm):
    class Meta:
        model = blog_posts
        fields = ['id', 'title', 'text']

def post_list(request, template_name='blog_posts/post_list.html'):
    posts = blog_posts.objects.all()
    data = {}
    data['object_list'] = reversed(posts)
    return render(request, template_name, data)

def post_create(request, template_name='blog_posts/post_form.html'):
    form = PostsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('blog_posts:post_list')
    return render(request, template_name, {'form': form})

def post_update(request, pk, template_name='blog_posts/post_form.html'):
    post = get_object_or_404(blog_posts, pk=pk)
    form = PostsForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('blog_posts:post_list')
    return render(request, template_name, {'form': form})

def post_delete(request, pk, template_name='blog_posts/post_delete.html'):
    post = get_object_or_404(blog_posts, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('blog_posts:post_list')
    return render(request, template_name, {'object': post})

def health(request):
    return HttpResponse("<html><body>I'm healthy</body></html>")
