from django.urls import path,include
from website.views import index_view,about_view,contact_view

app_name='website'

urlpatterns = [
    path('', index_view , name='index' ),
    path('about', about_view , name='about'),
    path('contact', contact_view , name='contact'),
]