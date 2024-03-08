from django.shortcuts import render
from rest_framework.response import Response 
from rest_framework.views import APIView 
from reminderApi.models import *
from reminderApi.serializer import *

# Create your views here.
class  Reminders(APIView):

    def get(self,request):
        
        reminders = ReminderInfo.objects.all()
        Iserializer = ReminderSerializer(reminders, many=True)
        return Response(Iserializer.data)


    def post(self,request):
        data = request.data

        Iserializer =  ReminderSerializer(data=data)

        if Iserializer.is_valid():
            Iserializer.save()
            return Response({"Status":"Success", "Message":"Data is saved to the database"}, status=200)
        
        else:
            return Response({"Status":"Failed","Error":str(Iserializer.errors)}, status=400)