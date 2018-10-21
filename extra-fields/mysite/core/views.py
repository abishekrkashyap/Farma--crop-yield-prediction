import time
import schedule
import cv2
import os
import numpy as np
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from mysite.core.forms import SignUpForm
from twilio.rest import Client
recognizer = cv2.face_LBPHFaceRecognizer.create()
recognizer.read('/home/atharsh/Desktop/simple-signup-master/extra-fields/mysite/core/trainer/trainer.yml')
cascadePath = "/home/atharsh/Desktop/simple-signup-master/extra-fields/mysite/core/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);
id = 0
l = [0]
flag=0
names = ['None', 'Ajii', 'ABISHEK', 'ATHARSH', 'ANURAG', 'Ajish'] 
def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect('home')
	else:
		form = SignUpForm()
	return render(request, 'signup.html', {'form': form})
def detect_face(img):
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	faces = faceCascade.detectMultiScale(gray,scaleFactor = 1.2, minNeighbors = 5)
	if(len(faces)==0):
		return None,None
	(x, y, w, h) = faces[0]
	return gray[y:y+w, x:x+h], faces[0]   
def predict(test_img1):
	img = test_img1.copy()
	face, rect = detect_face(img)
	label, confidence = recognizer.predict(face)
	label_val= confidence
	label_text = names[label]
	return label_text,label_val
# @login_required
def home(request):
	val=30
	camera = cv2.VideoCapture(0)
	for i in range(val):
 		return_value,temp =camera.read() 
	return_value, image = camera.read()
	cv2.imwrite("/home/atharsh/Desktop/simple-signup-master/extra-fields/mysite/core/test2.jpg", image)
	del(camera)
	test_img1 = cv2.imread("/home/atharsh/Desktop/simple-signup-master/extra-fields/mysite/core/test2.jpg")
	predicted_img1,val = predict(test_img1)
	if(predicted_img1=='ATHARSH' or predicted_img1=='ANURAG' or predicted_img1=='ABISHEK' ):
		return render(request, 'home.html',{'name':predicted_img1})

	
def god(request):
	return render(request,'god.html')
def chennai(request):
	return render(request,'chennai.html')
def salem(request):
	return render(request,'salem.html')
def home3(request):
	def detect_face2(img):
		gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
		faces = faceCascade.detectMultiScale(
		gray,
		scaleFactor = 1.2,
		minNeighbors = 5,
		)
		if(len(faces)==0):
			return l,l

		(x, y, w, h) = faces[0]
		return gray[y:y+w, x:x+h], faces[0]
	def predict2(test_img):
		img=test_img.copy()
		face,rect=detect_face2(img)
		if(all(rect)):
			label,confidence=recognizer.predict(face)
			label_text=names[label]
			label_val=confidence
			return label_text,label_val
		else:
			# print("zero")
			return 0,0
	def home2():

		val=30
		camera = cv2.VideoCapture(0)
		for i in range(val):
 			return_value,temp =camera.read() 
		return_value, image = camera.read()
		cv2.imwrite("/home/atharsh/Desktop/simple-signup-master/extra-fields/mysite/core/test2.jpg", image)
		del(camera)
		test_img1 = cv2.imread("/home/atharsh/Desktop/simple-signup-master/extra-fields/mysite/core/test2.jpg")
		predicted_img1,val = predict2(test_img1)
		if(val>0):


			print("PEST ALERT..!")
		if(predicted_img1==0 or val==0):
			dummy()
		else:
			print("Scanning in process")
			if(val>0):
				message()

		return	

	schedule.every(0.02).minutes.do(home2)
	while 1:
		schedule.run_pending()
		time.sleep(1)
def dummy():
	time.sleep(4)
	# print("Calm down no pests found..!")
	for i in range(1,10):
		print("You are safe!")
	return 0
def message():
	TWILIO_PHONE_NUMBER = "+18084009610"
			# list of one or more phone numbers to dial, in "+19732644210" format
	DIAL_NUMBERS = ["+919884443400",]
			# URL location of TwiML instructions for how to handle the phone call
	TWIML_INSTRUCTIONS_URL = \
	  "http://static.fullstackpython.com/phone-calls-python.xml"
	client = Client("AC13a39e57cd63d1776dba6566b84b360c", "0b0beb107fda04e09e5111b491ed42e1")


	def dial_numbers(numbers_list):
		for number in numbers_list:
			print("PEST ALERT..!! " + number)
			client.calls.create(to=number, from_=TWILIO_PHONE_NUMBER,
								url=TWIML_INSTRUCTIONS_URL, method="GET")


	if True:
		dial_numbers(DIAL_NUMBERS)

	# account_sid ="ACb3497c1566be1a8ca7db1f64c50ec9a8"
	# auth_token = "0213cd231f7c0dc8f25f2d556d1e6d5f"
	# client = Client(account_sid,auth_token)
	# message = client.api.account.messages.create(
	# 	to="+919884443400",
	# 	from_="+17344283989",
	# 	body="PEST ALERT..!!!")
	print("ALERT sent to the OWNER")