from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.mixins import UserPassesTestMixin,LoginRequiredMixin





class bloghome(ListView):
    model=Post
    context_object_name='post'
    ordering=['-date_posted']
    paginate_by=5


class userposts(ListView):
    model=Post
    context_object_name='post'
    template_name='myblog/user_post.html'
    ordering=['-date_posted']
    paginate_by=5

    def get_queryset(self):
        user=get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user)
        return super().get_queryset().order_by('-date_posted')


class detailpost(LoginRequiredMixin,DetailView):
    model=Post
    context_object_name='post'


class createpost(LoginRequiredMixin,CreateView):
    model=Post
    context_object_name='post'
   
    fields=['title','content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class updatepost(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model=Post
    context_object_name='post'
    fields=['title','content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
         post=self.get_object()
         if self.request.user == post.author:
             return True
         return False

class deletepost(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
     model=Post
     success_url='/'


     def test_func(self):
        post=self.get_object()
        if self.request.user == post.author:
             return True
        return False
        
