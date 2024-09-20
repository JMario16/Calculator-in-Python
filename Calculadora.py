from tkinter import *
import math
import re

win=Tk()
win.title("Calculadora")
win.iconbitmap("Logo_Calc.ico")
win.resizable(0,0)
win.geometry("365x530")
win.config(bg="#353539")


#Functions

has_point=False

def number(n):
    txt=number_l.cget("text")
    if txt[-1] not in ["²"]:
        if txt=="0":
            number_l.config(text=str(n))
        else:
            number_l.config(text=txt+str(n))
    else:
        number_l.config(text=txt)

def cler():
    global has_point
    has_point=False
    number_l.config(text="0")

def poin():
    global has_point
    txt=number_l.cget("text")
    if txt!="0" and has_point==False and txt[-1] not in ["+", "-", "×", "÷", "²", "√"]:
        number_l.config(text=txt+".")
        has_point=True
    elif txt!="0":
        number_l.config(text=txt)
    else:
        number_l.config(text="0.")
        has_point=True

def delet():
    global has_point
    txt=number_l.cget("text")
    if txt=="0":
        number_l.config(text="0")
    elif len(txt)==1:
        number_l.config(text="0")
    else:
        if txt[-1]==".":
            has_point=False
        elif txt[-1] in ["+", "-", "×", "÷"]:
            oper=["+", "-", "×", "÷"]
            last_op=len(txt)-1
            previous_op=max(txt.rfind(op, 0, last_op) for op in oper)
            last_number=txt[previous_op+1:last_op]
            if last_number in ["."]:
                has_point=False
            else:
                has_point=True
        number_l.config(text=txt[:-1])

def addit():
    global has_point
    txt=number_l.cget("text")
    if txt!="0" and txt[-1] not in ["+", "-", "×", "÷", ".", "²"] and ncc(txt, ["√"]):
        number_l.config(text=txt+"+")
        has_point=False
    else:
        number_l.config(text=txt)

def sub():
    global has_point
    txt=number_l.cget("text")
    if txt!="0" and txt[-1] not in ["+", "-", "×", "÷", ".", "²"] and ncc(txt, ["√"]):
        number_l.config(text=txt+"-")
        has_point=False
    else:
        number_l.config(text=txt)

def multi():
    global has_point
    txt=number_l.cget("text")
    if txt!="0" and txt[-1] not in ["+", "-", "×", "÷", ".", "²"] and ncc(txt, ["√"]):
        number_l.config(text=txt+"×")
        has_point=False
    else:
        number_l.config(text=txt)

def div():
    global has_point
    txt=number_l.cget("text")
    if txt!="0" and txt[-1] not in ["+", "-", "×", "÷", ".", "²"] and ncc(txt, ["√"]):
        number_l.config(text=txt+"÷")
        has_point=False
    else:
        number_l.config(text=txt)

def rot():
    txt=number_l.cget("text")
    if txt!="0" and ncc(txt, ["+", "-", "×", "÷", "²", "√"]):
        txt="√"+txt
        number_l.config(text=txt)
    elif ncc(txt, ["+", "-", "×", "÷", "²", "√"]):
        number_l.config(text="√")
    else:
        number_l.config(text=txt)

def pote():
    txt=number_l.cget("text")
    if txt!="0" and ncc(txt, ["+", "-", "×", "÷", "²", "√"]) and txt[-1]!=".":
        number_l.config(text=txt+"²")
    else:
        number_l.config(text=txt)

def ncc(string, list_ch):
    return not any(char in string for char in list_ch)

def sum(as_positions, sign_array, number_array):
    result=[]
    if as_positions:
        for i in range(0, len(as_positions)):
            if i==0:
                if sign_array[i]=="+":
                    result.append(float(number_array[i])+float(number_array[i+1]))
                else:
                    result.append(float(number_array[i])-float(number_array[i+1]))
            else:
                if sign_array[i]=="+":
                    result.append(float(result[i-1])+float(number_array[i+1]))
                else:
                    result.append(float(result[i-1])-float(number_array[i+1]))
        number_l.config(text=str(result[-1]))
    else:
        number_l.config(text=number_array[0])

def calculate():
    txt=number_l.cget("text")

    if txt[-1]=="²":
        number=txt[0:-1]
        number=float(number)*float(number)
        number_l.config(text=str(number))
        return
    if txt[0]=="√":
        number=txt[1:len(txt)]
        print(number)
        number=math.sqrt(float(number))
        number_l.config(text=str(number))
        return

    number_array=re.split(r'[-+×÷]', txt)
    number_array=[num for num in number_array if num]

    sign_array=re.split(r'[1234567890.]', txt)
    sign_array=[num for num in sign_array if num]

    if len(sign_array)==len(number_array):
        sign_array=sign_array[:-1]

    md_positions=[]
    as_positions=[]
    
    for i, sign in enumerate(sign_array):
            if sign=="×" or sign=="÷":
                md_positions.append(i)

    for i, sign in enumerate(sign_array):
            if sign=="-" or sign=="+":
                as_positions.append(i)

    while md_positions:
        mdp=md_positions[0]
        
        left=float(number_array[mdp])
        right=float(number_array[mdp+1])
        
        if sign_array[mdp]=="×":
            result=left*right
        else:
            result=left/right

        number_array[mdp]=result
        del number_array[mdp+1]
        sign_array.pop(mdp)
        
        md_positions=[i for i, sign in enumerate(sign_array) if sign=="×" or sign=="÷"]
    
    sum(as_positions, sign_array, number_array)


#Components

type_l=Label(win, bg="#353539", text="Estandar", fg="#efefef", font=("Bahnschrift", 16))
type_l.pack(padx=(10, 0), pady=(5, 0), anchor=NW)

number_l=Label(win, bg="#353539", text="0", fg="#f1f1f1", font=("Bahnschrift", 26))
number_l.pack(padx=(0, 15), pady=(0, 15), anchor=NE)

frame_p=Frame()
frame_p.config(bg="#2a2a2a")
frame_p.pack()


#Buttons

potency=Button(frame_p, bg="#2a2a2a", bd="0", padx="18", text="x²", fg="#efefef", font=("Bahnschrift", 20), command=lambda: pote())
potency.grid(row=0, column=0, sticky="ew")
root=Button(frame_p, bg="#2a2a2a", bd="0", padx="18", text="√x", fg="#efefef", font=("Bahnschrift", 20), command=lambda: rot())
root.grid(row=0, column=1, sticky="ew")
clear=Button(frame_p, bg="#2a2a2a", bd="0", padx="18", text="CE", fg="#efefef", font=("Bahnschrift", 20), command=lambda: cler())
clear.grid(row=0, column=2, sticky="ew")
delete=Button(frame_p, bg="#2a2a2a", bd="0", padx="18", text="<-", fg="#efefef", font=("Bahnschrift", 20), command=lambda: delet())
delete.grid(row=0, column=3, sticky="ew")

one=Button(frame_p, bg="#2a2a2a", bd="0", padx="18", text="1", fg="#efefef", font=("Bahnschrift", 20), command=lambda: number(1))
one.grid(row=1, column=0, sticky="ew")
two=Button(frame_p, bg="#2a2a2a", bd="0", padx="18", text="2", fg="#efefef", font=("Bahnschrift", 20), command=lambda: number(2))
two.grid(row=1, column=1, sticky="ew")
three=Button(frame_p, bg="#2a2a2a", bd="0", padx="18", text="3", fg="#efefef", font=("Bahnschrift", 20), command=lambda: number(3))
three.grid(row=1, column=2, sticky="ew")
addition=Button(frame_p, bg="#2a2a2a", bd="0", padx="18", text="+", fg="#efefef", font=("Bahnschrift", 20), command=lambda: addit())
addition.grid(row=1, column=3, sticky="ew")

four=Button(frame_p, bg="#2a2a2a", bd="0", padx="18", text="4", fg="#efefef", font=("Bahnschrift", 20), command=lambda: number(4))
four.grid(row=2, column=0, sticky="ew")
five=Button(frame_p, bg="#2a2a2a", bd="0", padx="18", text="5", fg="#efefef", font=("Bahnschrift", 20), command=lambda: number(5))
five.grid(row=2, column=1, sticky="ew")
six=Button(frame_p, bg="#2a2a2a", bd="0", padx="18", text="6", fg="#efefef", font=("Bahnschrift", 20), command=lambda: number(6))
six.grid(row=2, column=2, sticky="ew")
substract=Button(frame_p, bg="#2a2a2a", padx="18", bd="0", text="-", fg="#efefef", font=("Bahnschrift", 20), command=lambda: sub())
substract.grid(row=2, column=3, sticky="ew")

seven=Button(frame_p, bg="#2a2a2a", bd="0", padx="18", text="7", fg="#efefef", font=("Bahnschrift", 20), command=lambda: number(7))
seven.grid(row=3, column=0, sticky="ew")
eight=Button(frame_p, bg="#2a2a2a", bd="0", padx="18", text="8", fg="#efefef", font=("Bahnschrift", 20), command=lambda: number(8))
eight.grid(row=3, column=1, sticky="ew")
nine=Button(frame_p, bg="#2a2a2a", bd="0", padx="18", text="9", fg="#efefef", font=("Bahnschrift", 20), command=lambda: number(9))
nine.grid(row=3, column=2, sticky="ew")
multiply=Button(frame_p, bg="#2a2a2a", bd="0", padx="18", text="×", fg="#efefef", font=("Bahnschrift", 20), command=lambda: multi())
multiply.grid(row=3, column=3, sticky="ew")

equal=Button(frame_p, bg="#ff5757", bd="0", padx="18", text="=", fg="#2a2a2a", font=("Bahnschrift", 20), command=lambda: calculate())
equal.grid(row=4, column=0, sticky="ew")
zero=Button(frame_p, bg="#2a2a2a", bd="0", padx="18", text="0", fg="#efefef", font=("Bahnschrift", 20), command=lambda: number(0))
zero.grid(row=4, column=1, sticky="ew")
point=Button(frame_p, bg="#2a2a2a", bd="0", padx="18", text=".", fg="#efefef", font=("Bahnschrift", 20), command=lambda: poin())
point.grid(row=4, column=2, sticky="ew")
division=Button(frame_p, bg="#2a2a2a", bd="0", padx="18", text="÷", fg="#efefef", font=("Bahnschrift", 20), command=lambda: div())
division.grid(row=4, column=3, sticky="ew")

win.mainloop()