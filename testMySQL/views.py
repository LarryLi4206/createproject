from django.shortcuts import render

# Create your views here.

from django.db import connection
from django.http import HttpResponse,HttpResponseRedirect

conn_mysql=connection.cursor()
conn_mysql.execute("""create table if not exists test_table(
id integer NOT NULL primary key AUTO_INCREMENT,
name varChar(30),
num_area varChar(30) ,
address varChar(120) ,
tel1 varChar(20) ,
tel2 varChar(20) ,
note varChar(20) )""")
#conn_mysql.commit()
conn_mysql.close()

def defaultHomePage(request):

    #return HttpResponse('<a href="test.html"> 點擊跳頁</a>')
    #return HttpResponse('<script>document.location.href=”test.html”;</script><br> 歡迎使用')
    #return HttpResponse('<meta http-equiv="refresh" content="3;url=test.html" /><br> 3秒後自動跳轉')
    return HttpResponse('<meta http-equiv="refresh" content="3;url=factory" /><br> 3秒後自動跳轉')

def testdefault(request):

    return render(request,'factory/factory_homepage.html',{'getDjangoBackValue' : 'testMySQL取得python後臺傳送的值'})

#整合頁面(左邊按鈕控制右邊跳頁)
def setui(request):
    #return render(request,['merge.html','test.html','left_button.html'])
    return render(request,'factory/iframe.html')

def welcomePage(request):
    print('welcome')
    return render(request,'factory/welcome.html')

#全部資料頁面(讀取頁面)
def searchPage(request):
    return render(request,'factory/search.html')
#頁面功能--搜尋資料
def functionSearch(request):
    conn_mysql=connection.cursor()
    search_sql='select * from test_table'
    conn_mysql.execute(search_sql)
    all_data =conn_mysql.fetchall()
    name=[]
    for data in all_data:
        name.append(data)

    conn_mysql.close()
    print(all_data)
    print(name[0])
    return render(request,'factory/search.html',locals())

#新增資料頁面(讀取頁面)
def addPage(request):
    return render(request,'factory/add.html')

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
    return HttpResponseRedirect('/factory/search') #重新指向連接的網址
    #return HttpResponseRedirect('buttonPage/')

#建立新增資料庫語法函式
def insertDataSQL(name,num_area,address,tel1,tel2,note):
    insert_sql="insert into test_table(name,num_area,address,tel1,tel2,note)values(%s,%s,%s,%s,%s,%s); "
    conn_mysql=connection.cursor()
    conn_mysql.execute(insert_sql,(name,num_area,address,tel1,tel2,note))
    #conn_mysql.commit()
    conn_mysql.close()

#更新資料頁面(讀取頁面)
def updatePage(request):
    return render(request,'factory/update.html')

def buttonPage(request):
    return render(request,'factory/left_button.html')

def repage(request,page):
    page=''
    return render(request,'factory/test.html',{'repath':'正則路徑'})
#建立下拉式選單及查詢
def search_condition(request):
    conn_mysql = connection.cursor()
    search_sql = 'select name from test_table group by name;'
    conn_mysql.execute(search_sql)
    all_name_data = conn_mysql.fetchall()
    name=[]
    for i in all_name_data:
        for data in i:
            name.append(data)
    conn_mysql.close()
    print(all_name_data)
    print(name)

    if request.method=='POST':
        selectBox_data = request.POST['selectBox']
    else:
        selectBox_data='選擇查詢內容'

    print(selectBox_data)

    c_name=search_coditioin_name(selectBox_data)

    return render(request, 'factory/search_condition.html', locals())

#查尋方法
def search_coditioin_name(name):
    conn_mysql=connection.cursor()
    search_sql="select * from test_table where name='"+ name+"';"
    conn_mysql.execute(search_sql)
    all_name=conn_mysql.fetchall()

    condition_name = []
    for data in all_name:
        condition_name.append(data)

    conn_mysql.close()
    print(all_name)
    #print(name[0])

    return condition_name
