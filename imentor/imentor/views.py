from django.contrib import auth
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.context_processors import csrf

import models
import mock_responses

Message = models.Message()

Mock = mock_responses.MockResponses()

def homepage(request):
  return render_to_response('home.html')

def user_profile(request, user_id):
  if request.method == "GET":
    return HttpResponse(Mock.user_profile(user_id))

def user_messages(request, user_id):
  if request.method == "GET":
    return HttpResponse(Mock.user_messages(user_id))

def send_message(request, user_id):
  if request.method == "POST":
    return HttpResponse(Message.create_message(request, user_id))
  else:
    return HttpResponseNotFound(Mock.failure())

def pc_pairs(request, user_id):
  if request.method == "GET":
    return HttpResponse(Mock.pc_pairs())

def retrieve_by_tags(request, user_id):
  if request.method == "POST":
    return HttpResponse(Message.retrieve_by_tags(request, user_id))

def message_details(request, user_id, message_id):
  if request.method == "GET":
    return HttpResponse(Mock.message_details(user_id, message_id))

