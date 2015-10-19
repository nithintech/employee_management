"""mediaone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from employee.views import (EmployeeListView, EmployeeCreateView, EmployeeDeleteView, EmployeeUpdateView,
                            # QualificationListView, QualificationCreateView, QualificationDeleteView, QualificationUpdateView
                            )


urlpatterns = [
    url(r'^$', EmployeeListView.as_view()),
    url(r'^add/$', EmployeeCreateView.as_view()),
    url(r'^delete/(?P<pk>[\w]+)/$', EmployeeDeleteView.as_view()),
    url(r'^edit/(?P<pk>[\w]+)/$', EmployeeUpdateView.as_view()),
    # url(r'^qualifications/$', QualificationListView.as_view()),
    # url(r'^qualifications/add/$', QualificationCreateView.as_view()),
    # url(r'^qualifications/delete/(?P<pk>[\w]+)/$', QualificationDeleteView.as_view()),
    # url(r'^qualifications/edit/(?P<pk>[\w]+)/$', QualificationUpdateView.as_view()),
]
