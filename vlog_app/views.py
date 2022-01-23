from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Article, Social_medial
from .forms import *
from django.core.paginator import Paginator
from .serializers import *
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Get all social media
socials = Social_medial.objects.all()


# Django Templates
def index(request):
    articles_ = Article.objects.all().order_by('-updated_date')
    articles = Paginator(articles_, 3)
    page_number = request.GET.get('page')
    articles = articles.get_page(page_number)
    context = {'articles': articles,
               'socials': socials}
    return render(request=request, template_name='vlog_app/index.html', context=context)


def post_detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {'article': article,
               'socials': socials}
    return render(request=request, template_name='vlog_app/post.html', context=context)


def about(request):
    about_text = AboutMe.objects.latest('pk')
    context = {'socials': socials,
               'text': about_text}
    return render(request=request, template_name='vlog_app/about.html', context=context)

def contact(request):
    context = {'socials': socials}
    return render(request=request, template_name='vlog_app/contact.html', context=context)


def profile(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            cd['user_id'] = request.user
            Article.objects.create(**cd)
            return redirect('/')
        else:
            return HttpResponse('In valid!')
    else:
        form = ArticleForm()
        context = {'form': form,
                   'socials': socials}
        return render(request=request, template_name='vlog_app/profile.html', context=context)
    
def logins(request):
    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request=request, username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')
                else:
                    return HttpResponse('Your account disable')
            else:
                return HttpResponse('Your username or passwor   d inncorrect please try agan')
        else:
            return HttpResponse('Please input coorect data')
    else:
        form = LogInForm()
        context = {'form': form,
                   'socials': socials}
        return render(request=request, template_name='vlog_app//login.html', context=context)


def register(request):
    if request.method == 'POST':
        form = RegisterUser(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return HttpResponse(form.error_messages)
    else:
        form = RegisterUser()
        context = {'form': form,
                   'socials': socials}
        return render(request=request, template_name='vlog_app/sign-up.html', context=context)


def logouts(request):
    logout(request)
    return redirect('index')



# Django Rest Api

# Funcsion Based Api views
# @api_view(['GET'])
# def index_api(request):
#     data = Article.objects.filter(status=True)
#     serializer = ArticleSerializer(data, many=True)
#     return Response(data=serializer.data, status=status.HTTP_200_OK)

# @api_view(['GET', 'DELETE'])
# def detail_api(request, pk):
#     if request.method == 'GET':
#         data = Article.objects.get(pk=pk)
#         serializer = ArticleSerializer(data)
#         return Response(serializer.data, status.HTTP_200_OK)
#     elif request.method == 'DELETE':
#         data = Article.objects.filter(pk=pk).update(status=False)
#         # data = Article.objects.get(pk=pk)
#         # data.status = False
#         # data.save()
#         return Response(status.HTTP_204_NO_CONTENT)
        

# Classed Based Api Views
class IndexListApiView(ListAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.filter(status=False)
    
class ArticleCreateApiView(CreateAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    
class ArticleRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    
# class DestroyArticleApiView(DestroyAPIView):
#     serializer_class = ArticleSerializer
#     queryset = Article.objects.all()
    

# class ArticleRetrieveApiView(RetrieveAPIView):
#     serializer_class = ArticleSerializer
#     queryset = Article.objects.all()
    
# class ArticleUpdateApiView(UpdateAPIView):
#     serializer_class = ArticleSerializer
#     queryset = Article.objects.all()