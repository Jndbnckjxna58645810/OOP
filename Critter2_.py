from tkinter import *
import random
import time
class Critter2_:
    """Critter2_0"""
    total = 0

    @staticmethod
    def status():
        print('Общее число зверюшек', Critter2_.total)

    def __init__(self,name,color,x,y,canvas,a):
        self.canvas = canvas
        self.name = name
        self.color = color
        self.x = x
        self.y = y
        self.a = a
        Critter2_.total += 1

    def talk(self):
        print("My name is", self.name)

    def __str__(self):
        ans = 'Объект класса Critter\n' 
        ans += 'name: ' + self.name + '\n'
        return ans      
    
    def draw(self,x,y):
            canvas.create_rectangle(x,y,x+40,y+40,fill=self.color,outline="white")   
            canvas.create_oval(x+5,y+5,x+35,y+35,fill="white") 
            canvas.create_oval(x+15,y+15,x+25,y+25,fill='black')   

    def move(self,canvas,a,x,y):
        while 10 < x < 450 and 10 < y < 450: 
            if a == "R":
                x += 2
                canvas.create_rectangle(x,y,x+40,y+40,fill=self.color,outline="white")   
                canvas.create_oval(x+5,y+5,x+35,y+35,fill="white") 
                canvas.create_oval(x+15,y+15,x+25,y+25,fill='black') 
                root.update()
                time.sleep(0.05)
                canvas.delete("all")  
            elif a == "L":
                x -= 2
                canvas.create_rectangle(x,y,x+40,y+40,fill=self.color,outline="white")   
                canvas.create_oval(x+5,y+5,x+35,y+35,fill="white") 
                canvas.create_oval(x+15,y+15,x+25,y+25,fill='black') 
                root.update()
                time.sleep(0.05)
                canvas.delete("all")  
            elif a == "U":
                y -= 2
                canvas.create_rectangle(x,y,x+40,y+40,fill=self.color,outline="white")   
                canvas.create_oval(x+5,y+5,x+35,y+35,fill="white") 
                canvas.create_oval(x+15,y+15,x+25,y+25,fill='black') 
                root.update()
                time.sleep(0.05)
                canvas.delete("all")  
            elif a == "D": 
                y += 2
                canvas.create_rectangle(x,y,x+40,y+40,fill=self.color,outline="white")   
                canvas.create_oval(x+5,y+5,x+35,y+35,fill="white") 
                canvas.create_oval(x+15,y+15,x+25,y+25,fill='black')
                root.update()
                time.sleep(0.05)
                canvas.delete("all")   
            elif a == "UR":
                x += 2 
                y -= 2
                canvas.create_rectangle(x,y,x+40,y+40,fill=self.color,outline="white")   
                canvas.create_oval(x+5,y+5,x+35,y+35,fill="white") 
                canvas.create_oval(x+15,y+15,x+25,y+25,fill='black') 
                root.update()
                time.sleep(0.05)
                canvas.delete("all")  
            elif a == "UL":
                x -= 2
                y -= 2
                canvas.create_rectangle(x,y,x+40,y+40,fill=self.color,outline="white")   
                canvas.create_oval(x+5,y+5,x+35,y+35,fill="white") 
                canvas.create_oval(x+15,y+15,x+25,y+25,fill='black') 
                root.update()
                time.sleep(0.05)
                canvas.delete("all") 
            elif a == "DR":  
                x += 2
                y += 2
                canvas.create_rectangle(x,y,x+40,y+40,fill=self.color,outline="white")   
                canvas.create_oval(x+5,y+5,x+35,y+35,fill="white") 
                canvas.create_oval(x+15,y+15,x+25,y+25,fill='black') 
                root.update()
                time.sleep(0.05)
                canvas.delete("all")    
            elif a == "DL":
                x -= 2
                y += 2
                canvas.create_rectangle(x,y,x+40,y+40,fill=self.color,outline="white")   
                canvas.create_oval(x+5,y+5,x+35,y+35,fill="white") 
                canvas.create_oval(x+15,y+15,x+25,y+25,fill='black') 
                root.update()
                time.sleep(0.05)
                canvas.delete("all")          

root = Tk()
canvas = Canvas(root,width=500,height=500,bg='black')
canvas.pack() 

def main():
    c = "#" + ('%06x'%random.randint(0,16777215))
    xa = random.randint(10,450)
    ya = random.randint(10,450)
    i = str(input())
    c1 = Critter2_('First',c,xa,ya,canvas,i)
    c1.talk()
    c1.draw(xa,ya)
    c1.move(canvas,i,xa,ya)
    Critter2_.status()
    root.update()
    time.sleep(1)

main()
root.mainloop()

    

