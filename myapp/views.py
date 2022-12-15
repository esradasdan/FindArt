from django.shortcuts import redirect, render  
from django.core.files.storage import FileSystemStorage
import requests
import json
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,'index.html' )

def result(request):

    context={}

    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
     

    Auth_Token_URL = '''https://iam.ap-southeast-3.myhuaweicloud.com/v3/auth/tokens'''

    Body = { 
    "auth" : {  
        "identity": {  
        "methods": [ "password" ] , 
            "password": {  
                "user": {  
                    "name": "username", 
                    "password": "*******", 
                    "domain": {  
                        "name": "username"
                    } } } }, 
                "scope": {  
                    "project": {  
                        "name": "ap-southeast-3" 
                    } } } 
    } 
    response = requests.request( "POST", Auth_Token_URL, json=Body)
    

    X_auth_token = response.headers["X-Subject-Token"] 

    Service_API_Address = "your_modelarts_model_api_address"
    token=X_auth_token
    file_path = "./media/" + (uploaded_file.name)

    Headers= { 
    'X-Auth-Token' : token
    } 

    Files = { 
    'images' : open( file_path, 'rb' ) 
    } 

    resp = requests.post(Service_API_Address, headers = Headers, files = Files) 


    context['text']=resp.text
    text = json.loads(resp.text)

    
    a=text['predicted_label']
    file="./description/" + a + ".txt"

    with open(file, encoding="ISO-8859-1") as f:
        lines = f.readlines()

    context['description']=lines[0]

    a = a.replace("_", " ")
    a = a.replace("-", " ")

    context['artist']=a
    
    accuracy=float(text['scores'][0][1]) * 100
    round(accuracy, 2)
    context['accuracy']= str(accuracy)
    context['background'] = "../media/"+ name

    

    return render(request, 'result.html', context)
