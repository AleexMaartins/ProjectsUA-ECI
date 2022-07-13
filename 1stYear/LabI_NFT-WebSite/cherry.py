from stringprep import in_table_c21_c22
import cherrypy
import sqlite3 as sql
import sys
import os
import json
import html
import requests
from PIL import Image
from html.parser import HTMLParser
from PIL import ExifTags
cherrypy.config.update({'server.socket_port': 10009,})

PATH = os.path.abspath(os.path.dirname(__file__))
conf = {"/":
        {
            "tools.staticdir.root": PATH
        },
        "/assets/css": {
            "tools.staticdir.on": True,
            "tools.staticdir.dir": os.path.join(PATH, "assets/css")        
        },
        "/assets/js": {
            "tools.staticdir.on": True,
            "tools.staticdir.dir": os.path.join(PATH, "assets/js")        
        },
        "/assets/imgs": {
            "tools.staticdir.on": True,
            "tools.staticdir.dir": os.path.join(PATH, "assets/imgs")        
        },
        "/assets/vendors/themify-icons/css": {
            "tools.staticdir.on": True,
            "tools.staticdir.dir": os.path.join(PATH, "assets/vendors/themify-icons/css")        
        },
        "/assets/vendors/owl-carousel/css": {
            "tools.staticdir.on": True,
            "tools.staticdir.dir": os.path.join(PATH, "assets/vendors/owl-carousel/css")        
        },
        "/assets/vendors/jquery": {
            "tools.staticdir.on": True,
            "tools.staticdir.dir": os.path.join(PATH, "assets/vendors/jquery")        
        },
        "/assets/vendors/bootstrap": {
            "tools.staticdir.on": True,
            "tools.staticdir.dir": os.path.join(PATH, "assets/vendors/bootstrap")        
        },
        "/assets/vendors/owl-carousel/js": {
            "tools.staticdir.on": True,
            "tools.staticdir.dir": os.path.join(PATH, "assets/vendors/owl-carousel/js")        
        },
        "/js": {
            "tools.staticdir.on": True,
            "tools.staticdir.dir": os.path.join(PATH, "js")        
       
		 },
        "/img": {
            "tools.staticdir.on": True,
            "tools.staticdir.dir": os.path.join(PATH, "img")  
            },
        "/ima": {
            "tools.staticdir.on": True,
            "tools.staticdir.dir": os.path.join(PATH, "ima")       
       
		}
}
users = {}
show = {}
add = {}

def databasecreate(db):
    db = sql.connect("database/database.db")
    c = db.cursor()
    c.execute("""CREATE TABLE pic(nome TEXT, pass TEXT, pic TEXT)""")
    db.commit()
    db.close()
    


    
    return None



def  create(user, pas):
    db = sql.connect("database/database.db")
    c = db.cursor()
    rows =  c.execute("SELECT * FROM pic")
    d = 1
    for row in rows:
        if(row[0] == user):
            d = 0
    a = {"id" : user, "pass" : pas}
    users.update(a)
    if(d == 1):
        print(user)
        print(pas)
        c.execute("INSERT INTO pic VALUES (?, ?, ?)", (user, pas, ""))
        db.commit()
    
        db.close()
        
        return json.dumps({"s": "s"})
    else:
    

  
        return json.dumps({"s": "n"})

def  inis(user, pas):
    db = sql.connect("database/database.db")
    c = db.cursor()
    a = c.execute("SELECT nome, pass FROM pic WHERE pass LIKE ? AND nome LIKE ?", (pas, user))
    b = ""
    for row in a:
        a = row[0]
        b = row[1]
                
    print(a)
    print(b)
    db.close()
    if((a != user) or (b != pas)):
            return False
    else:
            a = {"id" : user, "pass" : pas}
            users.update(a)
            return True
            
    
    
    
    

  
    


def upload(i1, i2):
        im1 = Image.open("uploads/" +i1.filename)
        im2 = Image.open("uploads/" +i2.filename)
        x, y = im1.size
        p1 = im1.getpixel( (0+x/4, 0+y/4))
        x, y = im2.size
        size = (50, 50)
        im2.thumbnail(size)
        width, height = im1.size

# Location where we want to paste it on the
# main image
        x = width - 100 - 10
        y = height - 100 - 15

        im1.paste(im2, (x, y))

        cherrypy.response.headers["Content-Type"] = "json"
        im1.save("img/"+i1.filename)
        im1.close()
        im2.close()
        db = sql.connect("database/database.db")
        c = db.cursor()
        print(type(i1.filename))
        print(i1.filename)
        c.execute("INSERT INTO pic VALUES (?, ?, ?)", ( users["id"], users["pass"], str(i1.filename)))
        b = c.execute("SELECT * FROM pic")
        for row in b:
            print(row)
        db.commit()
        db.close()
        return print("10")
    
def upload2(i2):
        i1 = add["pic"]
        im1 = Image.open("img/" +i1)
        im2 = Image.open("uploads/" +i2.filename)
        x, y = im1.size
        p1 = im1.getpixel( (0+x/4, 0+y/4))
        x, y = im2.size
        size = (50, 50)
        im2.thumbnail(size)
        width, height = im1.size

# Location where we want to paste it on the
# main image
        x = width - 100 - 10
        y = height - 100 - 15

        im1.paste(im2, (x, y))

        cherrypy.response.headers["Content-Type"] = "json"
        im1.save("img/"+"1"+i1)
        im1.close()
        im2.close()
        db = sql.connect("database/database.db")
        c = db.cursor()
        c.execute("INSERT INTO pic VALUES (?, ?, ?)", ( users["id"], users["pass"],"1"+i1))
        b = c.execute("SELECT * FROM pic")
        for row in b:
            print(row)
        db.commit()
        db.close()
        return None

def pics():
    p = 0
    a = []
    db = sql.connect("database/database.db")
    c = db.cursor()
    b = c.execute("SELECT * FROM pic")
    for row in b:
        if((row[0] == show["id"])):
            if(row[2] != ''):
                a.append(row[2])
                p = p+1
            
    db.close()


    
    i = -1
    while(i<(p)):
        i = i+1
        
        print(a[i])
        if(i != (p-1)):
            cherrypy.response.headers["Content-Type"] = "application/json"
            return json.dumps({"pics": a[i], "h": i})
        else:
            cherrypy.response.headers["Content-Type"] = "application/json"
            return json.dumps({"pics": a[i], "h" : "-1"})

def pics2(y):
    y = int(y)
    p = 0
    a = []
    db = sql.connect("database/database.db")
    c = db.cursor()
    b = c.execute("SELECT * FROM pic")
    for row in b:
        if((row[0] == show["id"])):
            if(row[2] != ''):
                a.append(row[2])
                p = p+1
            
    db.close()


    
    i = 0
    while(y<(p)):
        y = y+1
        cherrypy.response.headers["Content-Type"] = "application/json"
        print(a[i])
        if(y != (p-1)):
            cherrypy.response.headers["Content-Type"] = "application/json"
            return json.dumps({"pics": a[y], "h": y})
        else:
            cherrypy.response.headers["Content-Type"] = "application/json"
            return json.dumps({"pics": a[y], "h" : "-1"})
        
def pics3():
    p = 0
    a = []
    db = sql.connect("database/database.db")
    c = db.cursor()
    b = c.execute("SELECT * FROM pic")
    for row in b:
        if((row[0] == users["id"])):
            if(row[2] != ''):
                a.append(row[2])
                p = p+1
            
    db.close()


    
    i = -1
    while(i<(p)):
        i = i+1
        
        print(a[i])
        if(i != (p-1)):
            cherrypy.response.headers["Content-Type"] = "application/json"
            return json.dumps({"pics": a[i], "h": i})
        else:
            cherrypy.response.headers["Content-Type"] = "application/json"
            return json.dumps({"pics": a[i], "h" : "-1"})

def pics4(y):
    y = int(y)
    p = 0
    a = []
    db = sql.connect("database/database.db")
    c = db.cursor()
    b = c.execute("SELECT * FROM pic")
    for row in b:
        if((row[0] == users["id"])):
            if(row[2] != ''):
                a.append(row[2])
                p = p+1
            
    db.close()


    
    i = 0
    while(y<(p)):
        y = y+1
        cherrypy.response.headers["Content-Type"] = "application/json"
        print(a[i])
        if(y != (p-1)):
            cherrypy.response.headers["Content-Type"] = "application/json"
            return json.dumps({"pics": a[y], "h": y})
        else:
            cherrypy.response.headers["Content-Type"] = "application/json"
            return json.dumps({"pics": a[y], "h" : "-1"})

def sendinfo():
    p = 0
    a = []
    e = []
    db = sql.connect("database/database.db")
    c = db.cursor()
    b = c.execute("SELECT * FROM pic")
    for row in b:
        d = 0;
        if((row[0] != users["id"])):
            if(row[2] != ''):
                if(len(a) == 0):
                            e.append(row[2])
                            d = d+1
                
                            a.append(row[0])
                            p = p+1
                else:
                        i = 0
                        print(len(a))
                    
                        print(i)
                        l = 0
                        c = 0
                        while(l<len(a)):
                            if((row[0] != a[l])):
                                print(a[l])
                                c = 1;
                            
                            l = l+1 
                        print(row[2])
                        print(c)      
                        if(c == 1):
                            e.append(row[2])
                            d = d+1
                
                            a.append(row[0])
                            p = p+1
                            
                        i = i+1
    db.close()
    i = -1
    print(p)
    print(len(a))
    while(i<p):
        print(i)
        i = i+1
        print(a[i])
        print(e[i])
        if(i != (p-1)):
            return json.dumps({"u": a[i], "pic": e[i], "h": i})
        else:
            return json.dumps({"u": a[i], "pic": e[i], "h" : "0"})
            
    
def sendinfo2(y):
    y = int(y)
    p = 0
    a = []
    e = []
    db = sql.connect("database/database.db")
    c = db.cursor()
    b = c.execute("SELECT * FROM pic")
    for row in b:
        d = 0;
        if((row[0] != users["id"])):
            if(row[2] != ''):
                if(len(a) == 0):
                            e.append(row[2])
                            d = d+1
                
                            a.append(row[0])
                            p = p+1
                else:
                        i = 0
                        print(len(a))
                   
                        print(i)
                        l = 0
                        c = 0
                        while(l<len(a)):
                            print(l)
                            if((row[0] != a[l])):
                                c = 1;
                                
                            
                            l = l+1 
                            
                        if(c == 1):
                            e.append(row[2])
                            d = d+1
                
                            a.append(row[0])
                            p = p+1
                            
                        i = i+1
    db.close()
    print(p)
    print(len(a))
    while(y<p):
        print(users)   
        y = y+1
        print(a[d])
        print(e[d])
        print(d)
        if(y != (p-1)):
            return json.dumps({"u": a[y], "pic": e[y], "h": y})
        else:
            return json.dumps({"u": a[y], "pic": e[y], "h" : "-1"})


class us(object):
    @cherrypy.expose
    def index(self):
        return None
    @cherrypy.expose
    def usepic(self):
        return open("html/showpic.html")
    @cherrypy.expose
    def userpic(self):
        return open("html/showpic2.html")
    @cherrypy.expose
    def pictoadd(self, pic):
        j = {"pic" : pic}
        add.update(j)
        return None
    @cherrypy.expose
    def showpic(self):
        print("ola")
        cherrypy.response.headers["Content-Type"] = "application/json"
        return pics().encode("utf-8", "ignore")
    @cherrypy.expose
    def showpic2(self, i):
        print("ola")
        cherrypy.response.headers["Content-Type"] = "application/json"
        return pics2(i).encode("utf-8", "ignore")
    @cherrypy.expose
    def showpic3(self):
        print("ola")
        cherrypy.response.headers["Content-Type"] = "application/json"
        return pics3().encode("utf-8", "ignore")
    @cherrypy.expose
    def showpic4(self, i):
        print("ola")
        cherrypy.response.headers["Content-Type"] = "application/json"
        return pics4(i).encode("utf-8", "ignore")
    @cherrypy.expose
    def show(self, user):
        print("ola")
        a = {"id" : user}
        show.update(a)
        return None
   
    
class log(object):
    @cherrypy.expose
    def index(self):
        return open("html/sign.html")
    @cherrypy.expose
    def inerr(self):
        return open("html/logE.html")
    @cherrypy.expose
    def cre(self, user, pas):
        cherrypy.response.headers["Content-Type"] = "application/json"
        return create(user, pas).encode("utf-8", "ignore")
    @cherrypy.expose
    def log2(self, user, pas):
        d = inis(user, pas)
        if (d == True):
            print("done")
            print(users["id"])
            return None
        else:
            print("1")
            return None
    @cherrypy.expose
    def log3(self):
        print("d")
        d = {}
        print(users)
        s = json.dumps({"r": "nop"})
        for i in users:
            if(i == ''):
                print("d")
                s = json.dumps({"r": "nop"})
            else:
                print("d")
                s = json.dumps({"r": "done"})
        
        cherrypy.response.headers["Content-Type"] = "application/json"
        return s.encode("utf-8", "ignore")
    @cherrypy.expose
    def logoff(self):
        print(1)
        print(users)
        users.pop('id')
        users.pop('pass')
        print(users)
        return None
            
        
        
      
          
    
   
        

class image(object):
    
    @cherrypy.expose
    def index(self):
        return open("html/image.html")
    @cherrypy.expose
    def im2(self):
        return open("html/image2.html")
    @cherrypy.expose
    def done(self, i1, i2):
        print("done")
        fo = open("uploads/" + i1.filename, "wb")
        while True:
            data = i1.file.read(8192)
            if not data: break
            fo.write(data)
        fo.close()

        print("done")
        fo = open("uploads/" + i2.filename, "wb")
        while True:
            data = i2.file.read(8192)
            if not data: break
            fo.write(data)
        fo.close()
        print("done")
        upload(i1, i2)
        print("done")
        return print("done")
    @cherrypy.expose
    def done2(self, i2):
        print("done")

        print("done")
        fo = open("uploads/" + i2.filename, "wb")
        while True:
            data = i2.file.read(8192)
            if not data: break
            fo.write(data)
        fo.close()
        print("done")
        upload2(i2)
        print("done")
        return print("done")

    
    
       

class Root:
    
    def __init__(self):
        self.image = image()
        self.log = log()
        self.us = us()
    
    @cherrypy.expose
    def index(self):
        db = sql.connect("database/database.db")
        c = db.cursor()
        try:
            a = c.execute("SELECT * FROM pic")
            print(9)
            for row in a:
                print(row)
            db.close()
        except(sql.Error):
            databasecreate(db)
            print(0)
            db.close()
          
        
            
        return open("html/logIndex.html")
        
    @cherrypy.expose
    def rot(self):  
        print(users)      
        return open("index.html")
    @cherrypy.expose
    def showim(self):
        cherrypy.response.headers["Content-Type"] = "application/json"       
        return sendinfo().encode("utf-8", "ignore")
    @cherrypy.expose
    def showim2(self, i):
        cherrypy.response.headers["Content-Type"] = "application/json"       
        return sendinfo2(i).encode("utf-8", "ignore")
    
if __name__ == "__main__":
    cherrypy.config.update({'server.socket_port': 10017})
    cherrypy.quickstart(Root(), "/",config = conf)
    
