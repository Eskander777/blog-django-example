from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from .models import BlogPost
from .forms import BlogPostForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    blogs = BlogPost.objects.order_by('-date_added')
    context = {'blogs': blogs}
    return render(request, 'blogs/index.html', context)

@login_required
def new_post(request):
    """Определяет новую тему."""
    if request.method != 'POST':
        # Данные не отправлялись, создается пустая форма.
        form = BlogPostForm
    else:
        # Отправлены данные POST; обработать данные.
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
            return HttpResponseRedirect(reverse('blogs:index'))
            
    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)

@login_required    
def edit_post(request, blog_id):
    """Редактирует существующую запись."""
    blog = BlogPost.objects.get(id=blog_id)
    check_topic_owner(blog.owner, request.user)
    
    if request.method != 'POST':
        # Исходный запрос; форма заполняется данными текущей записи.
        form = BlogPostForm(instance=blog)
    else:
        # Отправка данных POST; обработать данные.
        form = BlogPostForm(instance=blog, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blogs:index'))
                                                    
    context = {'blog': blog, 'form': form}
    return render(request, 'blogs/edit_post.html', context)

def check_topic_owner(post_owner, current_user):
    """
    Проверяет, что пользователь, связанный с темой является 
        текущим пользователем"
    """
    if post_owner != current_user:
        raise Http404
