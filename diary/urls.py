from urllib.parse import urlparse
from django.urls import path
from . import views

urlpatterns = [
    path('diary/list', views.DiaryListView.as_view(), name='diarylist'),
    path('diary/diarycreate', views.DiaryCreateView.as_view(), name='creatediary'),
    path('diary/diaryupdate/<pk>', views.DiaryUpdateView.as_view(), name='updatediary'),
    path('diary/diarydelete/<pk>', views.DiaryDeleteView.as_view(), name='deletediary'),
]