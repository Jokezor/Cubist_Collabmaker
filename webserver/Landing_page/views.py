from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.template import loader
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from subprocess import check_call
from django.conf.urls import url



# Hello world rest Get message
class HelloWorld(APIView):
	
	def get(self, request):
		return Response('Hello world from Django!')


class TokenViewTest(APIView):
	authentication_classes = (TokenAuthentication,)
	permission_classes = (IsAuthenticated,)

	def get(self, request):
		return Response('Token is working')


def get_tables(request):
    """
    Return a tables in the model
    """
    template = loader.get_template('tables.html')
    context = {}
    # return render(request, "tables.html")
    return HttpResponse(template.render(context, request))



def index(request):
	#tests = Test.objects.count()
    # check_call(['dot','-Tpng','output.dot','-o','OutputFile.png'])
	template = loader.get_template('index.html')

	
	users=User.objects.all()
	#passion=Passions.objects.all()
	context = {
		'users': users
	}
	#context = {
	#    'user': user, 
	#    'passion': passion,
	#}
	#print(user[0])
	#for p in user:
	#	print(p.passions_set.all())
	return HttpResponse(template.render(context, request))

def matches(request):

	template = loader.get_template('matches.html')

	colabs = Collaboration.objects.all()
	match_objects = Matched.objects.filter(colab=colab).order_by('-score')
	
	context = {
		'colabs': colabs
	}
	
	return HttpResponse(template.render(context, request))

def test_matches(request):

	template = loader.get_template('index_henrik.html')

	colabs = Collaboration.objects.all()
	user=User.objects.all()


	context = {
		'colabs': colabs,
		'user': user
	}

	return HttpResponse(template.render(context, request))

def test_view(request):
    #tests = Test.objects.count()
    tests = 0
    return HttpResponse("Det finns {} tests.".format(tests))
# Create your views here.
