from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'polls'

urlpatterns = [
    path('detail/<int:question_id>/', views.detailView, name="detail"),
    #dieu huong tuie  ket cua menu
    path('viewvotelist/', views.viewlist, name='viewvotelist'),

    #path('', views.viewlist, name='view_list'),

    path('polls/', views.viewlist, name='view_list'),

    path('votedetail/<int:question_id>', views.vote, name='vote'),
    #path('<int:question_id>', views.vote, name='vote'),
]
