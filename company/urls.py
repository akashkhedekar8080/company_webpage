"""
URL configuration for company project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from app.views import aboutus, blog_detail, contactform, index, blogs

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="home"),
    path("contact/", contactform, name="contactform"),
    path("aboutus/", aboutus, name="aboutus"),
    path("blog-detail/<int:blog_id>/", blog_detail, name="blog_detail"),
    path("blogs/",blogs,name="blogs")
]
