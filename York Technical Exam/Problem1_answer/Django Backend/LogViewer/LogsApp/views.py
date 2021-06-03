from django.shortcuts import render
import csv, io
import json
import datetime

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from LogsApp.models import Logs
from LogsApp.serializers import LogsSerializer

from django.core.files.storage import default_storage



# Create your views here.

@csrf_exempt
def LogsApi(request):
    if request.method =='GET':
        logs = Logs.objects.all()
        log_serializer = LogsSerializer(logs, many= True)
        return JsonResponse(log_serializer.data, safe=False)
    elif request.method == 'POST':

        #reuest for the file 
        file=request.FILES['myFile']
        file_name = default_storage.save(file.name,file)
        with open('./LogFiles/'+file_name) as csv_file:
            csv_file = csv.reader(csv_file, delimiter=',')
            
            for row in csv_file:
                #convert the timestamp into date time
                time = datetime.datetime.fromtimestamp(int(row[1])).strftime('%Y-%m-%d %H:%M:%S')
                severity= int(row[2])
                # make a dictionary
                x= {
                    "LOG_PRODUCER": row[0],
                    "TIMESTAMP": time,
                    "SEVERITY":severity ,
                    "LOG_MESSAGE": row[3]
       
                }
                #parse it into a Json objject
                y = json.dumps(x)
                print("================================================================")
                print(y)
                print("================================================================")
                #log_data=JSONParser().parse(x)
                log_serializer = LogsSerializer(data=x)
                print("================================================================")
                print(log_serializer)
                print("================================================================")
                if log_serializer.is_valid():
                    log_serializer.save()
                    
               
        return JsonResponse("Added Successfully!!", safe=False)

@csrf_exempt
def LogsSearchByDate(request,startDate,endDate):
    
    #search by date
    if request.method =='GET':
        
        
       
        logs = Logs.objects.filter(TIMESTAMP__range=(startDate,endDate))

        log_serializer = LogsSerializer(logs, many= True)
        return JsonResponse(log_serializer.data, safe=False)
  
@csrf_exempt
def LogsApiSearchBySeverity(request,log_severity):
    
    #search by severity
    if request.method =='GET':
        logs = Logs.objects.filter(SEVERITY__exact=log_severity)
        log_serializer = LogsSerializer(logs, many= True)
        return JsonResponse(log_serializer.data, safe=False)
@csrf_exempt
def LogsApiSearchByProducer(request, producer):
    
    #search by user
    if request.method =='GET':
        logs = Logs.objects.filter(LOG_PRODUCER__exact=producer)
        log_serializer = LogsSerializer(logs, many= True)
        return JsonResponse(log_serializer.data, safe=False)

   

      

        

    

   