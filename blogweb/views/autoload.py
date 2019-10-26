from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django import template
from adminpanel.models import *
from blogweb.models import *
from adminpanel.configuration import *
from django.core.paginator import Paginator
import json 
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
 