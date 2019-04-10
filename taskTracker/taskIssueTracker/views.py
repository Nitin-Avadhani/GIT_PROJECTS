from django.http import HttpResponse
from django.shortcuts import render, redirect
from taskIssueTracker.models import User, Project, TaskList, IssueList

def userregistration(request):
	return render(request, "userRegistration.html")

def userlogin(request):
	return render(request, "userLogin.html")

def userpush(request):
	userdetails = User.objects.all()
	flag=0

	username = request.POST['username']
	password = request.POST['password']
	confrmpassword = request.POST['confrmpassword']
	for item in userdetails:
		if item.username == username:
			flag=1
			break
   
	if password==confrmpassword and flag==0:
   		logindetails = User.objects.create(username = username, password = password)
   		nameidgenerator()
   		return render(request, 'userLogin.html')
	else:
   		return render(request, 'userRegistration.html',{"flag" : flag})

def nameidgenerator():
	userdetails = User.objects.all()

	for item in userdetails:
 		singleuserdetails = User.objects.get(username = item.username)
 		singleuserdetails.usernameid=singleuserdetails.username+str(singleuserdetails.id)
 		singleuserdetails.save()

def userhome(request):
	username = request.POST['username']
	password = request.POST['password']
	flag = 0

	singleuserdetails = User.objects.get(username = username)

	if singleuserdetails.password == password:
 		porjectobject = Project.objects.all()
 		return render(request,'home.html',{"name":singleuserdetails.username,"user":singleuserdetails.usernameid,"objects":porjectobject})
	else:
 		flag = 1
 		return render(request,'userLogin.html',{"flag":flag,})
 	# return render(request,'home.html')

def addproject (request):
	usernameid = request.POST['usernameid']
	return render(request,'addProject.html',{"user" : usernameid})

def userrehome(request):
	usernameid = request.POST['usernameid']
	projectname = request.POST['projectname']

	projectdetails = Project.objects.create(projectname = projectname,usernameid = usernameid)
	projectidgenerator()

	userdetails = User.objects.get(usernameid = usernameid)

	porjectobject = Project.objects.filter(usernameid = usernameid)
	return render(request,'home.html',{"name" : userdetails.username,"user":usernameid,"objects":porjectobject})

def projectidgenerator():
	projectdetails = Project.objects.all()

	for item in projectdetails:
 		singleprojdetails = Project.objects.filter(usernameid = item.usernameid)
 		# if singleprojdetails.count() > 1:
	 	for inner_item in singleprojdetails:
	 		inner_item.projectid=inner_item.projectname+str(inner_item.id)
	 		inner_item.save()
	 	# else:
	 		# singleprojdetails.projectid=singleprojdetails.projectname+str(singleprojdetails.id)
	 		# singleprojdetails.save()

def tasklist(request):
	username = request.POST['usernameid']
	project = request.POST['projectid']

	singleuserdetails = User.objects.get(usernameid = username)
	taskobject = TaskList.objects.filter(usernameid = username, projectid = project)
	return render(request,'tasks.html',{"name":singleuserdetails.username,"user":singleuserdetails.usernameid,"objects":taskobject,"projectid" : project})

def addtask(request):
	username = request.POST['usernameid']
	project = request.POST['projectid']

	return render(request,'newtasks.html',{"user":username,"projectid":project})

def taskpush(request):
	username = request.POST['usernameid']
	project = request.POST['projectid']
	task = request.POST['task']
	owner = request.POST['owner']
	for item in request.POST.getlist('status'):
   		status = item
	comments = request.POST['comments']

	projectdetails = TaskList.objects.create(projectid = project,usernameid = username, task = task, owner = owner, status = status, comments = comments)
	taskidgenerator()

	singleuserdetails = User.objects.get(usernameid = username)
	taskobject = TaskList.objects.filter(usernameid = username, projectid = project)
	return render(request,'tasks.html',{"name":singleuserdetails.username,"user":singleuserdetails.usernameid,"objects":taskobject,"projectid" : project})
	# return render(request,'',{"user":username,"projectid":project})

def taskidgenerator():
	taskdetails = TaskList.objects.all()

	for item in taskdetails:
 		singletaskdetails = TaskList.objects.filter(usernameid = item.usernameid, projectid = item.projectid)
 		# if singletaskdetails.count() > 1:
	 	for inner_item in singletaskdetails:
	 		inner_item.taskid=inner_item.usernameid+inner_item.projectid+str(inner_item.id)
	 		inner_item.save()
	 	# else:
	 		# singletaskdetails.taskid=singletaskdetails.usernameid+singletaskdetails.projectid+str(singletaskdetails.id)
	 		# singletaskdetails.save()

def updatetasklist(request):
	username = request.POST['usernameid']
	project = request.POST['projectid']

	singleuserdetails = User.objects.get(usernameid = username)
	taskobject = TaskList.objects.filter(usernameid = username, projectid = project)
	return render(request,'updateTask.html',{"name":singleuserdetails.username,"user":singleuserdetails.usernameid,"objects":taskobject,"projectid" : project})

def updatetask(request):
	username = request.POST['usernameid']
	project = request.POST['projectid']
	taskid = request.POST['taskid']
	owner = request.POST['owner']
	for item in request.POST.getlist('status'):
   		status = item
	comments = request.POST['comments']

	taskobjectupdate = TaskList.objects.get(usernameid = username, projectid = project, taskid = taskid)
	taskobjectupdate.owner = owner
	taskobjectupdate.status = status
	taskobjectupdate.comments = comments
	taskobjectupdate.save()

	singleuserdetails = User.objects.get(usernameid = username)
	taskobject = TaskList.objects.filter(usernameid = username, projectid = project)
	return render(request,'updateTask.html',{"name":singleuserdetails.username,"user":singleuserdetails.usernameid,"objects":taskobject,"projectid" : project})

def userrehome_1(request):
	usernameid = request.POST['usernameid']

	userdetails = User.objects.get(usernameid = usernameid)
	porjectobject = Project.objects.filter(usernameid = usernameid)
	return render(request,'home.html',{"name" : userdetails.username,"user":usernameid,"objects":porjectobject})

def issuelist(request):
	username = request.POST['usernameid']
	project = request.POST['projectid']

	singleuserdetails = User.objects.get(usernameid = username)
	issueobject = IssueList.objects.filter(usernameid = username, projectid = project)
	return render(request,'issues.html',{"name":singleuserdetails.username,"user":singleuserdetails.usernameid,"objects":issueobject,"projectid" : project})

def addissue(request):
	username = request.POST['usernameid']
	project = request.POST['projectid']

	return render(request,'newissue.html',{"user":username,"projectid":project})

def issuepush(request):
	username = request.POST['usernameid']
	project = request.POST['projectid']
	issue = request.POST['issue']
	owner = request.POST['owner']
	for item in request.POST.getlist('status'):
   		status = item
	comments = request.POST['comments']

	projectdetails = IssueList.objects.create(projectid = project,usernameid = username, issue = issue, owner = owner, status = status, comments = comments)
	issueidgenerator()

	singleuserdetails = User.objects.get(usernameid = username)
	issueobject = IssueList.objects.filter(usernameid = username, projectid = project)
	return render(request,'issues.html',{"name":singleuserdetails.username,"user":singleuserdetails.usernameid,"objects":issueobject,"projectid" : project})

def issueidgenerator():
	issuedetails = IssueList.objects.all()

	for item in issuedetails:
 		singleissuedetails = IssueList.objects.filter(usernameid = item.usernameid, projectid = item.projectid)
 		# if singleissuedetails.count() > 1:
	 	for inner_item in singleissuedetails:
	 		inner_item.issueid=inner_item.usernameid+inner_item.projectid+str(inner_item.id)
	 		inner_item.save()
	 	# else:
	 		# singleissuedetails.issueid=singleissuedetails.usernameid+singleissuedetails.projectid+str(singleissuedetails.id)
	 		# singleissuedetails.save()

def updateissuelist(request):
	username = request.POST['usernameid']
	project = request.POST['projectid']

	singleuserdetails = User.objects.get(usernameid = username)
	issueobject = IssueList.objects.filter(usernameid = username, projectid = project)
	return render(request,'updateIssue.html',{"name":singleuserdetails.username,"user":singleuserdetails.usernameid,"objects":issueobject,"projectid" : project})

def updateissue(request):
	username = request.POST['usernameid']
	project = request.POST['projectid']
	issueid = request.POST['issueid']
	owner = request.POST['owner']
	for item in request.POST.getlist('status'):
   		status = item
	comments = request.POST['comments']

	issueobjectupdate = IssueList.objects.get(usernameid = username, projectid = project, issueid = issueid)
	issueobjectupdate.owner = owner
	issueobjectupdate.status = status
	issueobjectupdate.comments = comments
	issueobjectupdate.save()

	singleuserdetails = User.objects.get(usernameid = username)
	issueobject = IssueList.objects.filter(usernameid = username, projectid = project)
	return render(request,'updateIssue.html',{"name":singleuserdetails.username,"user":singleuserdetails.usernameid,"objects":issueobject,"projectid" : project})