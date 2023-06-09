"""Kandidat2023Backend URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/testResponse', create_user, name='data'),
    path('api/fetchJobs', fetch_jobs, name='data'),
    path('api/authenticate',send_back_auth, name='authenticate'),
    path('api/writeCompAndInt',write_comp_and_int, name='writeCompAndInt'),
    path('api/likedJob', liked_job, name='likedJob'),
    path('api/dislikedJob', disliked_job, name='dislikedJob'),
    path('api/fetchLikedJobs', fetch_liked_jobs, name='likedJobs'),
    path('api/fetchDislikedJobs', fetch_disliked_jobs, name='dislikedJobs'),
    path('api/authWithToken', auth_with_token, name='authWithToken'),
    path('api/getComp', get_comp, name='data'),
    path('api/getInterest', get_interest, name='data'),
    path('api/fetchAllComp', fetch_all_comp, name='data'),
    path('api/fetchAllInterests', fetch_all_interests, name='data'),
    path('api/fetchALLJobs', fetch_all_jobs, name='data'),
    path('api/writeJob', write_job, name='writeJob'),
]