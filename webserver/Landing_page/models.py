from django.db import models
#from django.contrib.gis.db import models as gis_models
from django.contrib.gis.db import models as geomodels
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from .managers import MyUserManager
from django.db import models
from django.conf import settings

'''
class City(models.Model):
    name = models.CharField(max_length=100, blank=False)
    geometry = geomodels.PointField()

    class Meta:
        # order of drop-down list items
        ordering = ('name')

        # plural form in admin view
        verbose_name_plural = 'cities'
'''   

class User(AbstractBaseUser, PermissionsMixin):
	user_id = models.AutoField(primary_key=True)
	email = models.EmailField(unique=True, null=False)
	first_name = models.CharField(max_length=700)
	last_name = models.CharField(max_length=700)
	phone_number = models.IntegerField(default = 0, null=True)

	# Will be specific to if a person wants to collaborate
	#location = gis_models.PointField()

	# Keeps track of users wanting to collaborate and create ideas
	collaborator = models.BooleanField(default=False)
	ideamaker = models.BooleanField(default=False)

	# If a collaborator want to be matched or not. Say someone found their ideal match.
	want_to_be_matched = models.BooleanField(default=False)

	is_staff = models.BooleanField(
		_('staff status'),
		default=False,
		help_text=_('Designates whether the user can log into this site.'),
	)
	is_active = models.BooleanField(
		_('active'),
		default=True,
		help_text=_(
		    'Designates whether this user should be treated as active. '
		    'Unselect this instead of deleting accounts.'
	),
	)
	USERNAME_FIELD = 'email'
	objects = MyUserManager()
	def __str__(self):
		return self.email
	def get_full_name(self):
		return self.email
	def get_short_name(self):
		return self.email


class Language(models.Model):
	language_id = models.AutoField(primary_key=True)
	language = models.CharField(max_length=200)


class User_Language(models.Model):
	user_language_id = models.AutoField(primary_key=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	language = models.ForeignKey(Language, on_delete=models.CASCADE, default='None')

# The ESCO string skills.
class Skill(models.Model):
	skill_id = models.AutoField(primary_key=True)
	skill = models.CharField(max_length=200)
	group = models.CharField(max_length=200, default='None')


class Passion(models.Model):
	#passion_id = models.AutoField(primary_key=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	passion = models.ForeignKey(Skill, on_delete=models.CASCADE, default='None')
	passion_free_text = models.CharField(max_length=200, default='None')
	
class Assigned_Skill(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	assigned_skill = models.ForeignKey(Skill, on_delete=models.CASCADE, default='None')
	assigned_skill_free_text = models.CharField(max_length=200, default='None')

class Business_Experience(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	experience = models.ForeignKey(Skill, on_delete=models.CASCADE)
	experience_free_text = models.CharField(max_length=200, default='None')

class Up_For(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	interest = models.ForeignKey(Skill, on_delete=models.CASCADE, default='None')
	interest_free_text = models.CharField(max_length=200, default='None')


# Start of collaboration fields (IDEAMAKER)
class Collaboration(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	# Basic no limit
	description = models.TextField()
	#location = gis_models.PointField()

	# If the collaboration want to be matched. Say they found their dream team already and is pausing their matches for now.
	want_to_be_matched = models.BooleanField(default=False)
	
	
class Colab_Language(models.Model):
	colab = models.ForeignKey(Collaboration, on_delete=models.CASCADE)
	language = models.ForeignKey(Language, on_delete=models.CASCADE, default='None')

class Colab_Passion(models.Model):
	colab = models.ForeignKey(Collaboration, on_delete=models.CASCADE)
	passion = models.ForeignKey(Skill, on_delete=models.CASCADE, default='None')
	passion_free_text = models.CharField(max_length=200, default='None')
	
class Colab_Assigned_Skill(models.Model):
	colab = models.ForeignKey(Collaboration, on_delete=models.CASCADE)
	assigned_skill = models.ForeignKey(Skill, on_delete=models.CASCADE, default='None')
	assigned_skill_free_text = models.CharField(max_length=200, default='None')

class Colab_Business_Experience(models.Model):
	colab = models.ForeignKey(Collaboration, on_delete=models.CASCADE)
	experience = models.ForeignKey(Skill, on_delete=models.CASCADE, default='None')
	experience_free_text = models.CharField(max_length=200, default='None')

class Colab_Up_For(models.Model):
	colab = models.ForeignKey(Collaboration, on_delete=models.CASCADE)
	interest = models.ForeignKey(Skill, on_delete=models.CASCADE, default='None')
	interest_free_text = models.CharField(max_length=200, default='None')

class Passion_Matched(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	colab = models.ForeignKey(Collaboration, on_delete=models.CASCADE)
	score = models.IntegerField(default=0)
	weight = models.IntegerField(default=100)

class Assigned_Skill_Matched(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	colab = models.ForeignKey(Collaboration, on_delete=models.CASCADE)
	score = models.IntegerField(default=0)
	weight = models.IntegerField(default=100)

class Business_Experience_Matched(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	colab = models.ForeignKey(Collaboration, on_delete=models.CASCADE)
	score = models.IntegerField(default=0)
	weight = models.IntegerField(default=100)

class Up_For_Matched(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	colab = models.ForeignKey(Collaboration, on_delete=models.CASCADE)
	score = models.IntegerField(default=0)
	weight = models.IntegerField(default=100)

class Matched(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	colab = models.ForeignKey(Collaboration, on_delete=models.CASCADE)
	score = models.IntegerField(default=0)








