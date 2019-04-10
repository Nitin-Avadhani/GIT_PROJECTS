"""taskTracker URL Configuration

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
from django.conf.urls import include, url
# from django.conf.urls.defaults import *
from django.views.generic import TemplateView
from . import views as v
# from django.contrib import admin

# urlpatterns = [
#     url(r'^admin/', include(admin.site.urls)),
# ]

# urlpatterns = patterns('taskIssueTracker.views',
# 	url(r'^tasktracker/',TemplateView.as_view(template_name = 'index.html')),
# 	url(r'^registration/','userregistration',name = 'userregistration'),
# 	url(r'^login/','userlogin',name = 'userlogin'),
# 	url(r'^userpush/','userpush',name = 'userpush'),
# 	url(r'^home/','userhome',name = 'userhome'),
# 	url(r'^addproject/','addproject',name = 'addproject'),
# 	url(r'^rehome/','userrehome',name = 'userrehome'),
# 	url(r'^tasks/','tasklist',name = 'tasklist'),
# 	url(r'^addtask/','addtask',name = 'addtask'),
# 	url(r'^taskpush/','taskpush',name = 'taskpush'),
# 	url(r'^updatetasklist/','updatetasklist',name = 'updatetasklist'),
# 	url(r'^updatetask/','updatetask',name = 'updatetask'),
# 	url(r'^userrehome_1/','userrehome_1',name = 'userrehome_1'),
# 	url(r'^issues/','issuelist',name = 'issuelist'),
# 	url(r'^addissue/','addissue',name = 'addissue'),
# 	url(r'^issuepush/','issuepush',name = 'issuepush'),
# 	url(r'^updateissuelist/','updateissuelist',name = 'updateissuelist'),
# 	url(r'^updateissue/','updateissue',name = 'updateissue'),
# )

urlpatterns = [
	url(r'^tasktracker/',TemplateView.as_view(template_name = 'index.html')),
	url(r'^registration/',v.userregistration,name = 'userregistration'),
	url(r'^login/',v.userlogin,name = 'userlogin'),
	url(r'^userpush/',v.userpush,name = 'userpush'),
	url(r'^home/',v.userhome,name = 'userhome'),
	url(r'^addproject/',v.addproject,name = 'addproject'),
	url(r'^rehome/',v.userrehome,name = 'userrehome'),
	url(r'^tasks/',v.tasklist,name = 'tasklist'),
	url(r'^addtask/',v.addtask,name = 'addtask'),
	url(r'^taskpush/',v.taskpush,name = 'taskpush'),
	url(r'^updatetasklist/',v.updatetasklist,name = 'updatetasklist'),
	url(r'^updatetask/',v.updatetask,name = 'updatetask'),
	url(r'^userrehome_1/',v.userrehome_1,name = 'userrehome_1'),
	url(r'^issues/',v.issuelist,name = 'issuelist'),
	url(r'^addissue/',v.addissue,name = 'addissue'),
	url(r'^issuepush/',v.issuepush,name = 'issuepush'),
	url(r'^updateissuelist/',v.updateissuelist,name = 'updateissuelist'),
	url(r'^updateissue/',v.updateissue,name = 'updateissue'),
]