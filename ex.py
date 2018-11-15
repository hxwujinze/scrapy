from tkinter import *
import warnings
warnings.filterwarnings("ignore")
from urllib.parse import quote
from urllib import request
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import time
import re


def change_schedule(now_schedule,all_schedule):  
    canvas.coords(fill_rec, (5, 5, 6 + (now_schedule/all_schedule)*100, 25))  
    top.update()  
    x.set(str(round(now_schedule/all_schedule*100,2)) + '%')  
    if round(now_schedule/all_schedule*100,2) == 100.00:  
        x.set("完成")
def reg0():

    f = open("all.txt","a",encoding='utf-8')
    f2 = open("select.txt","a",encoding='utf-8')
    title=e1.get().strip()
    word=e2.get().strip()
    itemnum = 0
    page = 1
    logic = False
    print("查询条件:",title,word,file = f)
    print(time.strftime("%Y-%m-%d",time.localtime(time.time())),file = f)
    print("查询条件:",title,word,file = f2)
    print(time.strftime("%Y-%m-%d",time.localtime(time.time())),file = f2)
    title = title.encode('gbk')
    title = quote(title)
    pattern= re.compile(word,re.IGNORECASE)
    try:
        url = 'http://www.taiguo.com/plugin.php?id=aljzp&act=list&search='+title+'&rid=&subrid=&pid=&subpid=&sex=&view=&wanted=&pay=&page='+('%d'%page)
        req = request.Request(url, headers = {
            'Connection': 'keep-alive',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'})
        resp =request.urlopen(req)
        html_data  = resp.read().decode('gbk')
        soup = bs(html_data,'html.parser')
        alltitle = soup.find_all('div', class_='media-body')
        itemnum = soup.find('font').text
        href = []
        text = []

        itemnum = int(itemnum)
        allitem = itemnum
        while itemnum > 0:
            for item in alltitle:
                href.append("http://www.taiguo.com/"+item.find('a').get('href'))
                text.append(item.find('div',class_= 'typo-small').get('title'))
                url = href[len(href)-1]
                req = request.Request(url, headers = {
                 'Connection': 'keep-alive',
                 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                 'Accept-Language': 'zh-CN,zh;q=0.8',
                 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'})
                resp =request.urlopen(req)
                html_data  = resp.read().decode('gbk')
                soup = bs(html_data,'html.parser')
                detail = soup.find_all('span' ,class_="normal")
                dr = re.compile(r'(<[^>]+>)|({[^}]+})|.qqkf|.qqkf|img|.vm', re.S)
                dd = dr.sub('', str(detail))
                text[len(text)-1] = text[len(text)-1] + dd
            itemnum = itemnum - int(len(alltitle))
            change_schedule(allitem-itemnum,allitem) 
            if itemnum > 0:
                page = page + 1
                url = 'http://www.taiguo.com/plugin.php?id=aljzp&act=list&search='+title+'&rid=&subrid=&pid=&subpid=&sex=&view=&wanted=&pay=&page='+('%d'%page)
                req = request.Request(url, headers = {
                'Connection': 'keep-alive',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Language': 'zh-CN,zh;q=0.8',
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'})
                resp =request.urlopen(req)
                html_data  = resp.read().decode('gbk')
                soup = bs(html_data,'html.parser')
                alltitle = soup.find_all('div', class_='media-body')
        dic=dict(zip(href,text))

        for key,value in dic.items():
            print(key,file = f) 
            print(value,file = f)
            print(" ",file = f)
            if pattern.findall(value):
                print(key,file = f2)
                print(value,file = f2)
                print(" ",file = f2)    
                                     
        
    except:
        c["text"]="网络错误"   
def reg():
    f = open("all.txt","a",encoding='utf-8')
    f2 = open("select.txt","a",encoding='utf-8')
    title=e1.get().strip()
    word=e2.get().strip()
    itemnum = 0
    page = 1
    logic = False
    print("查询条件:",title,word,file = f)
    print(time.strftime("%Y-%m-%d",time.localtime(time.time())),file = f)
    print("查询条件:",title,word,file = f2)
    print(time.strftime("%Y-%m-%d",time.localtime(time.time())),file = f2)
    title = title.encode('gbk')
    title = quote(title)
    pattern= re.compile(word,re.IGNORECASE)
    try:
        url = 'http://www.taiguo.com/plugin.php?id=aljzp&act=list&search='+title+'&rid=&subrid=&pid=&subpid=&sex=&view=&wanted=&pay=&page='+('%d'%page)
        req = request.Request(url, headers = {
            'Connection': 'keep-alive',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'})
        resp =request.urlopen(req)
        html_data  = resp.read().decode('gbk')
        soup = bs(html_data,'html.parser')
        alltitle = soup.find_all('div', class_='media-body')
        itemnum = soup.find('font').text

        itemnum = int(itemnum)
        allitem = itemnum
        while itemnum > 0:
            href = []
            text = []
            for item in alltitle:
                href.append("http://www.taiguo.com/"+item.find('a').get('href'))
                text.append(item.find('div',class_= 'typo-small').get('title'))
            itemnum = itemnum - int(len(alltitle))
            print(itemnum)
            change_schedule(allitem-itemnum,allitem) 
            if itemnum > 0:
                page = page + 1
                print(page)
                url = 'http://www.taiguo.com/plugin.php?id=aljzp&act=list&search='+title+'&rid=&subrid=&pid=&subpid=&sex=&view=&wanted=&pay=&page='+('%d'%page)
                req = request.Request(url, headers = {
                'Connection': 'keep-alive',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Language': 'zh-CN,zh;q=0.8',
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'})
                resp =request.urlopen(req)
                html_data  = resp.read().decode('gbk')
                soup = bs(html_data,'html.parser')
                alltitle = soup.find_all('div', class_='media-body')
            dic=dict(zip(href,text))

            for key,value in dic.items():
                print(key,file = f) 
                print(value,file = f)
                print(" ",file = f)
                if pattern.findall(value):
                    print(key,file = f2)
                    print(value,file = f2)
                    print(" ",file = f2)    
                                     
        
    except:
        c["text"]="网络错误"   


top=Tk()
top.wm_title("www.taiguo.com")
top.geometry("400x300+100+50")

s1=Label(top,text="标题：")
s1.grid(row=0,column=0,sticky=W)
e1=Entry(top)
e1.grid(row=0,column=1,sticky=E)

s2=Label(top,text="内容：")
s2.grid(row=1,column=0,sticky=W)
e2=Entry(top)

e2.grid(row=1,column=1,sticky=E)

b=Button(top,text="常规搜索",command=reg)
b.grid(row=2,column=0,sticky=E)

c=Label(top,text="")
c.grid(row=3)

d=Button(top,text="深度搜索",command=reg0)
d.grid(row=2,column=3,sticky=E)

frame = Frame(top).grid(row = 3,column = 0)#使用时将框架根据情况选择新的位置  
canvas = Canvas(frame,width = 120,height = 30,bg = "white")  
canvas.grid(row = 3,column = 0)  
x = StringVar()  
#进度条以及完成程度  
out_rec = canvas.create_rectangle(5,5,105,25,outline = "blue",width = 1)  
fill_rec = canvas.create_rectangle(5,5,5,25,outline = "",width = 0,fill = "blue")  
  
Label(frame,textvariable = x).grid(row = 3,column = 1)  
top.mainloop()
