from django.urls import path
from .views import ViewAllPost,ViewDetails

urlpatterns = [
    path('', ViewAllPost.as_view(), name='home'),
    path('/post/<int:pk>',ViewDetails.as_view(),name='details')
]