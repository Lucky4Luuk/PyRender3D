try :
    import tkinter as tk
except Exception :
    import Tkinter as tk
import math
import random

WIDTH = 800
HEIGHT = 600
BGCOLOR = "black"

CAMX = 0
CAMY = 0
CAMZ = 0
camspeed = 1

root = tk.Tk()
w = tk.Canvas(root,width=WIDTH,height=HEIGHT)

def toWorldSpace(x,y,z,vx,vy,vz,model):
    rx = x + vx
    ry = y + vy
    rz = z + vz
    return rx,ry,rz

def toCamSpace(vx,vy,vz):
    return vx-CAMX,vy-CAMY,vz-CAMZ

class Model():
    def __init__(self,x,y,z,f):
        self.f = f
        self.x = x
        self.y = y
        self.z = z
        self.vertices = []
        self.vnormals = []
        self.faces = []

    def load(self):
        self.file = open(self.f,"r")
        self.data = []
        self.data = self.file.readlines()
        for i in range(len(self.data)) :
            self.data[i] = str(self.data[i]).split(" \n")[0]
            self.data[i] = str(self.data[i]).split("\n")[0]
            if self.data[i] != "" :
                if self.data[i].startswith("v ") :
                    #self.vertices.append(self.data[i][2:])
                    self.vertices.append([float(self.data[i][2:].split(" ")[0]),float(self.data[i][2:].split(" ")[1]),float(self.data[i][2:].split(" ")[2])])
                elif self.data[i].startswith("vn ") :
                    self.vnormals.append(self.data[i][3:])
                elif self.data[i].startswith("f ") :
                    self.faces.append(self.data[i][2:])
        #print(self.data)
        self.file.close()
        self.vertices.sort(key=lambda tup: tup[2])

    def drawvertices(self):
        #print(self.vertices)
        for v in self.vertices :
            try :
                vx = float(v[0])*50
                vy = float(v[1])*50
                vz = float(v[2])/2

                vx,vy,vz = toWorldSpace(self.x,self.y,self.z,vx,vy,vz,self)
                vx,vy,vz = toCamSpace(vx,vy,vz)

                #print([vx,vy,vz])

                screenx = vx/vz+WIDTH/2
                screeny = vy/vz+HEIGHT/2

                #print([screenx,screeny])

                w.create_oval(screenx-1,screeny-1,screenx+1,screeny+1,fill="blue",outline="blue")
            except Exception as e :
                print(e)

    def drawlines(self) :
        #print(self.faces)
        for f in self.faces :
            try :
                #LINES 1
                v1 = int(f.split(" ")[0].split("//")[0])-1
                v2 = int(f.split(" ")[1].split("//")[1])-1
                #print([v1,v2])

                x1 = self.vertices[v1][0]*50
                y1 = self.vertices[v1][1]*50
                z1 = self.vertices[v1][2]/2

                x1,y1,z1 = toWorldSpace(self.x,self.y,self.z,x1,y1,z1,self)
                x1,y1,z1 = toCamSpace(x1,y1,z1)

                sx1 = x1/z1+WIDTH/2
                sy1 = y1/z1+HEIGHT/2

                x2 = self.vertices[v2][0]*50
                y2 = self.vertices[v2][1]*50
                z2 = self.vertices[v2][2]/2

                x2,y2,z2 = toWorldSpace(self.x,self.y,self.z,x2,y2,z2,self)
                x2,y2,z2 = toCamSpace(x2,y2,z2)

                sx2 = x2/z2+WIDTH/2
                sy2 = y2/z2+HEIGHT/2

                #print([sx1,sy1,sx2,sy2])

                w.create_line(sx1,sy1,sx2,sy2,fill="red",width=1)
            except Exception :
                pass

            try :
                #LINES 2
                v1 = int(f.split(" ")[2].split("//")[0])-1
                v2 = int(f.split(" ")[3].split("//")[1])-1
                #print([v1,v2])

                x1 = self.vertices[v1][0]*50
                y1 = self.vertices[v1][1]*50
                z1 = self.vertices[v1][2]/2

                x1,y1,z1 = toWorldSpace(self.x,self.y,self.z,x1,y1,z1,self)
                x1,y1,z1 = toCamSpace(x1,y1,z1)

                sx1 = x1/z1+WIDTH/2
                sy1 = y1/z1+HEIGHT/2

                x2 = self.vertices[v2][0]*50
                y2 = self.vertices[v2][1]*50
                z2 = self.vertices[v2][2]/2

                x2,y2,z2 = toWorldSpace(self.x,self.y,self.z,x2,y2,z2,self)
                x2,y2,z2 = toCamSpace(x2,y2,z2)

                sx2 = x2/z2+WIDTH/2
                sy2 = y2/z2+HEIGHT/2

                #print([sx1,sy1,sx2,sy2])

                w.create_line(sx1,sy1,sx2,sy2,fill="red",width=1)
            except Exception :
                pass

            try :
                #LINES 3
                v1 = int(f.split(" ")[3].split("//")[0])-1
                v2 = int(f.split(" ")[0].split("//")[1])-1
                #print([v1,v2])

                x1 = self.vertices[v1][0]*50
                y1 = self.vertices[v1][1]*50
                z1 = self.vertices[v1][2]/2

                x1,y1,z1 = toWorldSpace(self.x,self.y,self.z,x1,y1,z1,self)
                x1,y1,z1 = toCamSpace(x1,y1,z1)

                sx1 = x1/z1+WIDTH/2
                sy1 = y1/z1+HEIGHT/2

                x2 = self.vertices[v2][0]*50
                y2 = self.vertices[v2][1]*50
                z2 = self.vertices[v2][2]/2

                x2,y2,z2 = toWorldSpace(self.x,self.y,self.z,x2,y2,z2,self)
                x2,y2,z2 = toCamSpace(x2,y2,z2)

                sx2 = x2/z2+WIDTH/2
                sy2 = y2/z2+HEIGHT/2

                #print([sx1,sy1,sx2,sy2])

                w.create_line(sx1,sy1,sx2,sy2,fill="red",width=1)
            except Exception :
                pass

            try :
                #LINES 4
                v1 = int(f.split(" ")[3].split("//")[0])-1
                v2 = int(f.split(" ")[1].split("//")[1])-1
                #print([v1,v2])

                x1 = self.vertices[v1][0]*50
                y1 = self.vertices[v1][1]*50
                z1 = self.vertices[v1][2]/2

                x1,y1,z1 = toWorldSpace(self.x,self.y,self.z,x1,y1,z1,self)
                x1,y1,z1 = toCamSpace(x1,y1,z1)

                sx1 = x1/z1+WIDTH/2
                sy1 = y1/z1+HEIGHT/2

                x2 = self.vertices[v2][0]*50
                y2 = self.vertices[v2][1]*50
                z2 = self.vertices[v2][2]/2

                x2,y2,z2 = toWorldSpace(self.x,self.y,self.z,x2,y2,z2,self)
                x2,y2,z2 = toCamSpace(x2,y2,z2)

                sx2 = x2/z2+WIDTH/2
                sy2 = y2/z2+HEIGHT/2

                #print([sx1,sy1,sx2,sy2])

                w.create_line(sx1,sy1,sx2,sy2,fill="red",width=1)
            except Exception :
                pass

            try :
                #LINES 4
                v1 = int(f.split(" ")[2].split("//")[0])-1
                v2 = int(f.split(" ")[0].split("//")[1])-1
                #print([v1,v2])

                x1 = self.vertices[v1][0]*50
                y1 = self.vertices[v1][1]*50
                z1 = self.vertices[v1][2]/2

                x1,y1,z1 = toWorldSpace(self.x,self.y,self.z,x1,y1,z1,self)
                x1,y1,z1 = toCamSpace(x1,y1,z1)

                sx1 = x1/z1+WIDTH/2
                sy1 = y1/z1+HEIGHT/2

                x2 = self.vertices[v2][0]*50
                y2 = self.vertices[v2][1]*50
                z2 = self.vertices[v2][2]/2

                x2,y2,z2 = toWorldSpace(self.x,self.y,self.z,x2,y2,z2,self)
                x2,y2,z2 = toCamSpace(x2,y2,z2)

                sx2 = x2/z2+WIDTH/2
                sy2 = y2/z2+HEIGHT/2

                #print([sx1,sy1,sx2,sy2])

                w.create_line(sx1,sy1,sx2,sy2,fill="red",width=1)
            except Exception :
                pass

    def setScale(self,scale) :
        for v in self.vertices :
            vx = float(v[0])
            vy = float(v[1])
            vz = float(v[2])

            vx = vx * scale
            vy = vy * scale
            vz = vz * scale
            v = str(vx)+" "+str(vy)+" "+str(vz)

    def setRotation(self,rotx,roty,rotz):
        self.rotx = rotx
        self.roty = roty
        self.rotz = rotz

    def drawfaces(self):
        for f in self.faces :
            try :
                #FACES 1
                v1 = int(f.split(" ")[0].split("//")[0])-1
                v2 = int(f.split(" ")[1].split("//")[0])-1
                v3 = int(f.split(" ")[2].split("//")[0])-1
                #print([v1,v2,v3])

                x1 = self.vertices[v1][0]*50
                y1 = self.vertices[v1][1]*50
                z1 = self.vertices[v1][2]/2

                x1,y1,z1 = toWorldSpace(self.x,self.y,self.z,x1,y1,z1,self)
                x1,y1,z1 = toCamSpace(x1,y1,z1)

                sx1 = x1/z1+WIDTH/2
                sy1 = y1/z1+HEIGHT/2

                x2 = self.vertices[v2][0]*50
                y2 = self.vertices[v2][1]*50
                z2 = self.vertices[v2][2]/2

                x2,y2,z2 = toWorldSpace(self.x,self.y,self.z,x2,y2,z2,self)
                x2,y2,z2 = toCamSpace(x2,y2,z2)

                sx2 = x2/z2+WIDTH/2
                sy2 = y2/z2+HEIGHT/2

                x3 = self.vertices[v3][0]*50
                y3 = self.vertices[v3][1]*50
                z3 = self.vertices[v3][2]/2

                x3,y3,z3 = toWorldSpace(self.x,self.y,self.z,x3,y3,z3,self)
                x3,y3,z3 = toCamSpace(x3,y3,z3)

                sx3 = x3/z3+WIDTH/2
                sy3 = y3/z3+HEIGHT/2

                #print([sx1,sy1,sx2,sy2])

                w.create_polygon([sx1,sy1],[sx2,sy2],[sx3,sy3],fill="white",width=1,outline="white")
            except Exception :
                pass

            try :
                #FACES 2
                v1 = int(f.split(" ")[1].split("//")[0])-1
                v2 = int(f.split(" ")[2].split("//")[0])-1
                v3 = int(f.split(" ")[3].split("//")[0])-1
                #print([v1,v2,v3])

                x1 = self.vertices[v1][0]*50
                y1 = self.vertices[v1][1]*50
                z1 = self.vertices[v1][2]/2

                x1,y1,z1 = toWorldSpace(self.x,self.y,self.z,x1,y1,z1,self)
                x1,y1,z1 = toCamSpace(x1,y1,z1)

                sx1 = x1/z1+WIDTH/2
                sy1 = y1/z1+HEIGHT/2

                x2 = self.vertices[v2][0]*50
                y2 = self.vertices[v2][1]*50
                z2 = self.vertices[v2][2]/2

                x2,y2,z2 = toWorldSpace(self.x,self.y,self.z,x2,y2,z2,self)
                x2,y2,z2 = toCamSpace(x2,y2,z2)

                sx2 = x2/z2+WIDTH/2
                sy2 = y2/z2+HEIGHT/2

                x3 = self.vertices[v3][0]*50
                y3 = self.vertices[v3][1]*50
                z3 = self.vertices[v3][2]/2

                x3,y3,z3 = toWorldSpace(self.x,self.y,self.z,x3,y3,z3,self)
                x3,y3,z3 = toCamSpace(x3,y3,z3)

                sx3 = x3/z3+WIDTH/2
                sy3 = y3/z3+HEIGHT/2

                #print([sx1,sy1,sx2,sy2])

                w.create_polygon([sx1,sy1],[sx2,sy2],[sx3,sy3],fill="white",width=1,outline="white")
            except Exception :
                pass

            try :
                #FACES 3
                v1 = int(f.split(" ")[2].split("//")[0])-1
                v2 = int(f.split(" ")[3].split("//")[0])-1
                v3 = int(f.split(" ")[0].split("//")[0])-1
                #print([v1,v2,v3])

                x1 = self.vertices[v1][0]*50
                y1 = self.vertices[v1][1]*50
                z1 = self.vertices[v1][2]/2

                x1,y1,z1 = toWorldSpace(self.x,self.y,self.z,x1,y1,z1,self)
                x1,y1,z1 = toCamSpace(x1,y1,z1)

                sx1 = x1/z1+WIDTH/2
                sy1 = y1/z1+HEIGHT/2

                x2 = self.vertices[v2][0]*50
                y2 = self.vertices[v2][1]*50
                z2 = self.vertices[v2][2]/2

                x2,y2,z2 = toWorldSpace(self.x,self.y,self.z,x2,y2,z2,self)
                x2,y2,z2 = toCamSpace(x2,y2,z2)

                sx2 = x2/z2+WIDTH/2
                sy2 = y2/z2+HEIGHT/2

                x3 = self.vertices[v3][0]*50
                y3 = self.vertices[v3][1]*50
                z3 = self.vertices[v3][2]/2

                x3,y3,z3 = toWorldSpace(self.x,self.y,self.z,x3,y3,z3,self)
                x3,y3,z3 = toCamSpace(x3,y3,z3)

                sx3 = x3/z3+WIDTH/2
                sy3 = y3/z3+HEIGHT/2

                #print([sx1,sy1,sx2,sy2])

                w.create_polygon([sx1,sy1],[sx2,sy2],[sx3,sy3],fill="white",width=1,outline="white")
            except Exception :
                pass

m = Model(0,0,2,"model.obj")
m.load()
m.setScale(5)

def gameloop() :
    w.delete("all")
    w.create_rectangle(0,0,WIDTH,HEIGHT,fill=BGCOLOR,outline=BGCOLOR)
    m.drawvertices()
    m.drawlines()
    m.drawfaces()
    w.after(1,gameloop)

def moveleft(key):
    global CAMX, camspeed
    CAMX += camspeed

def moveright(key):
    global CAMX, camspeed
    CAMX -= camspeed

def moveup(key):
    global CAMY, camspeed
    CAMY -= camspeed

def movedown(key):
    global CAMY, camspeed
    CAMY += camspeed

root.bind("a",moveleft)
root.bind("d",moveright)
root.bind("q",moveup)
root.bind("e",movedown)

gameloop()

w.pack()
root.mainloop()