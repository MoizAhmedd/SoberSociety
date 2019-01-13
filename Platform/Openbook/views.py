from django.shortcuts import render,redirect
from Openbook.forms import SignUpForm
from django.contrib.auth import authenticate,login
from django.views.generic import ListView,DetailView
from django.contrib.auth.models import User
from .models import Challenge,Blog,Comment
from django.views.generic.edit import CreateView

# Create your views here.
def HomePageView(request,*args,**kwargs):
    context = {
        'items': Challenge.objects.all()
    }

    return render(request,'index.html',context)


class SuccessView(ListView):
    model = User
    template_name = 'success.html'

class RedirectView(ListView):
    model = User
    template_name = 'redirect.html'

class ProfileView(DetailView):
    model = User
    template_name = 'profile.html'
    context_object_name = 'details'

class ChallengeView(ListView):
    model = Challenge
    template_name = 'challenges.html'
    context_object_name = 'habits'

class ChallengeDetailView(DetailView):
    model = Challenge
    template_name = 'challenge_details.html'
    context_object_name = 'cdetails'

class NewChallengeView(CreateView):
    model = Challenge
    template_name = 'newchallenge.html'
    fields = '__all__'

class BlogView(ListView):
    model = Blog
    template_name = 'blog.html'
    context_object_name = 'blogs'

class BlogTextView(DetailView):
    model = Blog
    template_name = 'blogdetails.html'
    context_object_name = 'myblog'

class CommentsView(ListView):
    model = Comment
    template_name = 'blogdetails.html'
    context_object_name = 'comments'

class WriteCommentsView(CreateView):
    model = Comment
    template_name = 'newcomment.html'
    context_object_name = 'newcomment'
    fields = '__all__'

class ChatView(ListView):
    model = User
    template_name = 'chat.html'

class WriteBlogView(CreateView):
    model = Blog
    template_name = 'newblog.html'
    fields = '__all__'



def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username = username,password=raw_password)
            login(request,user)
            return redirect('/')

    else:
        form = SignUpForm()

    return render(request,'registration/signup.html',{'form':form})
