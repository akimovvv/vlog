from django.urls import path
from .views import *

urlpatterns = [
    # api endpoints
    path('api/v1/article-destroy-retrieve-update/<int:pk>/', ArticleRetrieveUpdateDestroyAPIView.as_view(), name='article-destroy-retriev-update'),
    path('api/v1/articles/', IndexListApiView.as_view(), name='index-api'),
    path('api/v1/article-create/', ArticleCreateApiView.as_view(), name='artucle-create-api'),
    # path('api/v1/retriev/<int:pk>/', ArticleRetrieveApiView.as_view(), name='article-retriev'),
    # path('api/v1/update/<int:pk>/', ArticleUpdateApiView.as_view(), name='article-update'),
    # path('api/v1/article-destroy/<int:pk>/', DestroyArticleApiView.as_view(), name='artucle-destroy-api'),
    # path('api/v1/articles-func/', index_api, name='index-api-func'),
    # path('api/v1/get-delete-func/<int:pk>/', detail_api, name='index-api-get-delete'),
    
    path('post-detail/<int:pk>/', post_detail, name='post-detail'),
    path('contact/', contact, name='contact'), 
    path("sign-up/", register, name="sign-up"),
    path("login/", logins, name="login"),
    path('logout/', logouts, name='logout'),
    path("profile/", profile, name="profile"),
    path('about/', about, name='about'),
    path('', index, name='index')
]