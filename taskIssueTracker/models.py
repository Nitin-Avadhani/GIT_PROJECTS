from django.db import models

class User(models.Model):
	username = models.CharField(max_length = 100)
	password = models.CharField(max_length = 100)
	usernameid = models.CharField(max_length = 200)

	class Meta:
		db_table = "db_user"

class Project(models.Model):
	usernameid = models.CharField(max_length = 200)
	projectname = models.CharField(max_length = 200)
	projectid = models.CharField(max_length = 200)

	class Meta:
		db_table = "db_project"

class TaskList(models.Model):
	usernameid = models.CharField(max_length = 200)
	projectid = models.CharField(max_length = 200)
	task = models.CharField(max_length = 1000)
	owner = models.CharField(max_length = 200)
	status = models.CharField(max_length = 100)
	comments = models.CharField(max_length = 1000)
	taskid = models.CharField(max_length = 1000)

	class Meta:
		db_table = "db_tasklist"

class IssueList(models.Model):
	usernameid = models.CharField(max_length = 200)
	projectid = models.CharField(max_length = 200)
	issue = models.CharField(max_length = 1000)
	owner = models.CharField(max_length = 200)
	status = models.CharField(max_length = 100)
	comments = models.CharField(max_length = 1000)
	issueid = models.CharField(max_length = 1000)

	class Meta:
		db_table = "db_issuelist"