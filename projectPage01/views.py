from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse,HttpResponseRedirect
import sqlite3

#使用MySQL
#pip install pymysql
import pymysql
# 使用django封裝好的connection對象，會自動讀取settings.py中資料庫的配置信息
from django.db import connection
"""
#使用PostgreSQL
#pip install psycopg2
import psycopg2
"""
#資料庫建立由Django的setting.py決定使用的資料庫
#建立資料庫資料表
db_name='db.sqlite3'
#連接Sqlite
conn=sqlite3.connect(db_name)

#連接MySQL
#pymysql.install_as_MySQLdb()#放setting.py
conn_mysql=connection.cursor()

#建立資料表
#conn_MySQL.execute('create database django_demo;')
conn.execute('create table if not exists test_table(\
"id" integer NOT NULL primary key AUTOINCREMENT,\
"name" varChar ,\
"num_area" varChar ,\
"address" varChar ,\
"tel1" varChar ,\
"tel2" varChar ,\
"note" varChar )')
conn.commit()
conn.close()


def defaultHomePage(request):

    #return HttpResponse('<a href="test.html"> 點擊跳頁</a>')
    #return HttpResponse('<script>document.location.href=”test.html”;</script><br> 歡迎使用')
    #return HttpResponse('<meta http-equiv="refresh" content="3;url=test.html" /><br> 3秒後自動跳轉')
    return HttpResponse('<meta http-equiv="refresh" content="3;url=buttonPage" /><br> 3秒後自動跳轉')

def testdefault(request):

    return render(request,'test.html',{'getDjangoBackValue' : '取得python後臺傳送的值'})

#整合頁面(左邊按鈕控制右邊跳頁)
def setui(request):
    #return render(request,['merge.html','test.html','left_button.html'])
    return render(request,'iframe.html')

def welcomePage(request):
    print('welcome')
    return render(request,'welcome.html')

#全部資料頁面(讀取頁面)
def searchPage(request):
    return render(request,'search.html')

#頁面功能--搜尋資料
def functionSearch(request):
    conn=sqlite3.connect(db_name)
    conn_mysql=connection.cursor()
    search_sql='select * from test_table'
    all_data=conn.execute(search_sql).fetchall()
    """
    for data in all_data:
        for i in range(len(data)):
            data[i]
    """
    conn.commit()
    conn.close()

    print(all_data)
    return render(request,'search.html',locals())


#新增資料頁面(讀取頁面)
def addPage(request):
    return render(request,'add.html')

#頁面功能--新增資料
def functionAdd(request):
    name=request.GET['name']
    area_num=request.GET['num_area']
    address=request.GET['address']
    tel1=request.GET['tel1']
    tel2=request.GET['tel2']
    note=request.GET['note']

    insertDataSQL(name,area_num,address,tel1,tel2,note)
    print(name)

    #return HttpResponse('Success<br><meta http-equiv="refresh" content="3;url=buttonPage" /><br> 3秒後自動跳轉')
    #return HttpResponse('Success<br><meta http-equiv="refresh" content="3;url=buttonPage" /><br> 3秒後自動跳轉')
    return HttpResponseRedirect('/buttonPage/search') #重新指向連接的網址
    #return HttpResponseRedirect('buttonPage/')

#建立新增資料庫語法函式
def insertDataSQL(name,num_area,address,tel1,tel2,note):
    insert_sql="""insert into test_table(name,num_area,address,tel1,tel2,note) 
    values(?,?,?,?,?,?) """
    conn=sqlite3.connect('db.sqlite3')
    conn_mysql=connection.cursor()
    conn.execute(insert_sql,(name,num_area,address,tel1,tel2,note))
    conn.commit()
    conn.close()

#更新資料頁面(讀取頁面)
def updatePage(request):
    return render(request,'update.html')

def buttonPage(request):
    return render(request,'left_button.html')

def repage(request,page):
    page=''
    return render(request,'test.html',{'repath':'正則路徑'})








