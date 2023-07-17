from django.shortcuts import render, redirect
from django.http import HttpResponse
import mysql.connector as sql
em=''
pwd=''
# Create your views here.
def loginaction(request):
    global em,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="",database='exonwatch')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="email":
                em=value
            if key=="password":
                pwd=value
        
        c="select * from users where email='{}' and password='{}'".format(em,pwd)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request, 'error.html', {'error_message': 'An error occurred.'})
        else:
             return redirect('home')

    return render(request,'login_page.html')
def home_view(request):
    return render(request, 'upload_video.html')
