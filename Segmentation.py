import turtle
import sys
t = turtle.getturtle()
t2 = t.clone()
t3 =t.clone()
t4 =t.clone()
t5 =t.clone()
t.ht()
t2.ht()
t3.ht()
t4.ht()
t5.ht()
t.speed(0)
t2.speed(0)
t3.speed(0)
t4.speed(0)
t5.speed(0)
t4.pu()
segList=[]
segStart=[]
segEnd=[]
def header():
    t.speed(0)
    t.pu()
    t3.pu()
    t.shape("turtle")
    t.goto(-200,275)
    t.write("Segmentation", move=False, align="center", font=("Times", 40, "bold italic"))
    t2.pu()
    t2.goto(220,0)
    t2.write("Use Python Shell\nto command the turtle", move=False, align="center", font=("Times", 20, "italic"))
    t.goto(-200,-250)
    t.st()
    t.speed(4)
def colormem():
    t4.goto(-100,-250)
    t4.seth(90)
    t4.fillcolor("grey")
    t4.begin_fill()
    t4.pd()
    t4.fd(500)
    t4.seth(0)
    t4.fd(200)
    t4.seth(-90)
    t4.fd(500)
    t4.seth(180)
    t4.fd(200)
    t4.pu()
    t4.end_fill()
    
def mark(address):
    t5.pensize(5)
    t5.pu()
    t5.goto(-100,-250)
    t5.seth(90)
    t5.fd((address/size)*500)
    t5.pencolor("red")
    t5.seth(0)
    t5.pd()
    t5.fd(200)
    t5.pu()
    t5.fd(25)
    t5.write(address, move=False, align="right", font=("Times", 15, "normal"))
   
def colorseg(name,limit,base):
    draw=(base/size)*500 
    draw2=(limit/size)*500 
    t4.goto(-100,-250)
    t4.seth(90)
    t4.fillcolor('#A6EBF9')
    t4.pd()
    t4.fd(draw)
    t4.begin_fill()
    t4.fd(draw2)
    t4.seth(0)
    t4.fd(200)
    t4.seth(-90)
    t4.fd(draw2)
    t4.seth(180)
    t4.fd(200)
    t4.pu()
    t4.end_fill()
    
def drawmem():
    t.pu()
    t.goto(0,-275)
    t.write("Physical Memory", move=True, align="center", font=("Times", 15, "bold italic"))
    t.goto(-100,-250)
    t.seth(180)
    t.fd(25)
    t.write("0", move=False, align="right", font=("Times", 15, "normal"))
    t.bk(25)
    t.seth(90)
    t.pd()
    t.fd(500)
    t.pu()
    t.seth(180)
    t.fd(25)
    t.write(size, move=False, align="right", font=("Times", 15, "normal"))
    t.bk(25)
    t.seth(90)
    t.pd()
    t.rt(90)
    t.fd(200)
    t.rt(90)
    t.fd(500)
    t.rt(90)
    t.fd(200)
    colormem()
    t.pu()
    t.goto(-200,-250)
    t.seth(0)
    
def drawseg(name,limit,base):
    t.st()
    draw=(base/size)*500 
    draw2=(limit/size)*500
    draw=(base/size)*500 
    draw2=(limit/size)*500 
    t.goto(-100,-250)
    t.seth(90)
    t.pd()
    t.fd(draw)
    t.seth(180)
    t2.goto(t.xcor(),t.ycor())
    t2.seth(180)
    t2.fd(25)
    t2.write(base, move=False, align="right", font=("Times", 15, "normal"))
    t.seth(90)
    t.fd(draw2)
    t.seth(180)
    t2.goto(t.xcor(),t.ycor())
    t2.seth(180)
    t2.fd(25)
    t2.write(base+limit, move=False, align="right", font=("Times", 15, "normal"))
    t.seth(0)
    t.fd(200)
    t.seth(-90)
    t3.seth(-90)
    t3.goto(t.xcor(),t.ycor())
    t3.fd(draw2/2+7.5)
    t.fd(draw2)
    t3.seth(180)
    t3.fd(100)
    t.seth(180)
    t.fd(200)
    colorseg(name,limit,base)
    t3.write("Segment %s"%name, move=False, align="center", font=("Times", 15, "normal"))
    t.pu()
    t.goto(-200,-250)
    t.seth(0)
def Add(name,limit,base):
    if(name in segList):
        print("Segment %s is already in physical memory"%name)
        f1()
    else:
        for i in range(len(segList)):
            if((base>=segStart[i] and base<segEnd[i]) or (base+limit>segStart[i] and base+limit<segEnd[i])): 
                print("Error new segment is intersect with another segment")
                f1()   
        segList.append(name)
        segStart.append(base)
        segEnd.append(base+limit)
        drawseg(name,limit,base)
        f()
        
def Remove(name):
    if(not name in segList):
        print("Segment %s is not in physical memory"%name)
        f1()
    else:
        target=segList.index(name)
        targetS=segStart[target]
        targetE=segEnd[target]
        segStart.remove(targetS)
        segEnd.remove(targetE)
        segList.remove(name)
        t.clear()
        t2.clear()
        t3.clear()
        t4.clear()
        drawmem()
        t.speed(0)
        for j in range(len(segList)):
            drawseg(segList[j],segEnd[j]-segStart[j],segStart[j])
        t.speed(4)
        f()
def f():
    print("Select Function\n \t1.Add/Remove Segment\n\t2.Translate Logical Address to Physical Address\n\t3.Exit")
    try:
        c=int(input("function: "))
        t5.clear()
        if(c==1):
            f1()
        elif(c==2):
            f2()
        elif(c==3):
            print("------------------ Goodbye ------------------")
            sys.exit(1)
    except ValueError:
        print("Invalid Function")
        f()
def f1():
    print("Add/Remove Segment\n\t Add: type \"add segment limit base\" -> \"add 1 100 200\"")
    print("\t Remove: type \"remove target 0 0\" -> \"remove 1 0 0\"")
    try:
        com,name,limit,base=input("Command: ").split()
        if(com!="add" and com!="remove"):
            print("Invalid command")
            f1()
        if(not name.isdigit()):
            print("Invalid segment number")
            f1()
        if(not limit.isdigit()):
            print("Invalid limit")
            f1()
        if(not base.isdigit()):
            print("Invalid base")
            f1()
        limit=int(limit)
        base=int(base)
        if(com=="add"):
            if (base<0 or base>=size):
                print("Invalid base")
                f1()
            if (limit<=0 or limit> size):
                print("Invalid limit")
                f1()
            if (limit+base>size):
                print("?Base+Limit exceed size")
                f1()
            #print("Test")
            Add(name,limit,base)
        elif(com=="remove"):
            Remove(name)
    except ValueError:
        print("Invalid command")
        f1()
def f2(): 
    print("Translate Logical Adress to Physical Address")
    print("\tCommand: <segment,offset> -> <1,100>")
    try:
        inp=input("Command: ")
        if(inp[0]!='<' or inp[len(inp)-1] !='>'):
            print("Invalid input")
            f2()
        inpu=inp
        inp= inp[1:]
        inp= inp[:-1]
        name,offset=inp.split(",")
        offset=int(offset)
        if(not name in segList):
            print("Segment %s is not in physical memory"%name)
            f2()
        target=segList.index(name)
        if(segEnd[target]-segStart[target]<offset):
            print("Offset is more than segment limit")
            f()
        else:
            address=segStart[target]+offset
            print("Logical address %s is at %d in Physical Address\n\n"%(inpu,address))
            mark(address)
            f()
    except ValueError:
        print("Invalid command")
        f2()   
################# main ####################
print("------------------ Segmentation ------------------")
header()
size=int(input("Enter physical memory size(in bytes): "))
drawmem()
f();
