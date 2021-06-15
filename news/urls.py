from django.urls import path
from . import views

urlpatterns=[
    path('',views.welcome,name="welcome"),
    path('news_of_day',views.news_of_day,name="news_of_day"),
    path('past_days_news\d{4}-\d{2}-\d{2}',views.past_days_news,name="past_days_news")


]
