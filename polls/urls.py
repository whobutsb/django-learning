from django.urls import path

from .views import *
# from . import views

app_name = 'polls'

urlpatterns = [
    path('', all.index, name='index'),
    path('<int:pk>/', all.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', all.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', all.vote, name='vote'),
    path('login/', login.login_view, name='login'),
    path('logout/', login.logout_view, name='logout'),
    path('login/auth/', login.auth, name='login.auth'),
]

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('<int:question_id>/', views.detail, name='detail'),
#     path('<int:question_id>/results/', views.results, name='results'),
#     path('<int:question_id>/vote/', views.vote, name='vote'),
# ]
