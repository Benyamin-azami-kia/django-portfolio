from email.errors import MalformedHeaderDefect
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from sqlalchemy import null



class Profile(models.Model):
	user=models.OneToOneField(User, on_delete=models.CASCADE)
	title=models.CharField(max_length=150)
	avatar=models.ImageField(upload_to='avatar', null=True, blank=True)
	bio=models.TextField()
	cv=models.FileField(upload_to='cv', null=True, blank=True)
	twitter=models.CharField(max_length=200, null=True, blank=True)
	linkedin=models.CharField(max_length=200, null=True, blank=True)
	instagram=models.CharField(max_length=200, null=True, blank=True)

	def __str__(self) -> str:
		return self.user.username


class Skill(models.Model):
	owner=models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='skills')
	name=models.CharField(max_length=50)
	score=models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])

	def __str__(self) -> str:
		return self.name


class Contact(models.Model):
	name=models.CharField(max_length=100)
	email=models.EmailField()
	text=models.TextField()
	date=models.DateTimeField(auto_now_add=True)
	
	def __str__(self) -> str:
		return self.name


class Project(models.Model):
	owner=models.ForeignKey(Profile, on_delete=models.CASCADE)
	name=models.CharField(max_length=150)
	description=models.TextField()
	photo=models.ImageField(upload_to='projects')
	tags=models.ManyToManyField('Tag')

	def __str__(self) -> str:
		return self.name


class ProjectImages(models.Model):
	project=models.ForeignKey(Project, on_delete=models.CASCADE)
	image=models.ImageField(upload_to='projects')

	def __str__(self) -> str:
		return self.project


class Certificate(models.Model):
	owner=models.ForeignKey(Profile, on_delete=models.CASCADE)
	name=models.CharField(max_length=100)
	description=models.TextField(null=True, blank=True)
	academy=models.CharField(max_length=100)
	score=models.CharField(max_length=5, null=True, blank=True)
	date=models.DateField(null=True, blank=True)
	created=models.DateTimeField(auto_now_add=True)

	def __str__(self) -> str:
		return self.name


class Tag(models.Model):
	name=models.CharField(max_length=50)

	def __str__(self) -> str:
		return self.name
