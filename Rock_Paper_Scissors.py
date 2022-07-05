from random import randint
from tkinter import *
from tkinter import ttk

root=Tk()
root.title('Rock Paper Scissors')
root.geometry('600x600')
root.config(bg="white")

rock=PhotoImage(file="rock.jpg")
paper=PhotoImage(file="paper.png")
scissors=PhotoImage(file="scissors.png")

moves = [rock, paper, scissors]
pick_number=randint(0,2)
image_label=Label(root,image=moves[pick_number],bd=0)
image_label.pack(pady=20)

def game():
  pick_number=randint(0,2)
  image_label.config(image=moves[pick_number])

  if user_choice.get()=="Rock":
    user_choice_value=0
  elif user_choice.get()=="Paper":
    user_choice_value=1
  elif user_choice.get()=="Scissors":
    user_choice_value=2
  
  if pick_number==user_choice_value:
    win_lose_label.config(text="Draw!")
  elif user_choice_value==0:
    if pick_number==1:
      win_lose_label.config(text="You Lose!")
    else:
      win_lose_label.config(text="You Win!")
  elif user_choice_value==1:
    if pick_number==2:
      win_lose_label.config(text="You Lose!")
    else:
      win_lose_label.config(text="You Win!")
  elif user_choice_value==2:
    if pick_number==0:
      win_lose_label.config(text="You Lose!")
    else:
      win_lose_label.config(text="You Win!")

user_choice=ttk.Combobox(root,value=("Rock","Paper","Scissors"))
user_choice.current(0)
user_choice.pack(pady=20)

start_button=Button(root,text="Confirm",command=game)
start_button.pack(pady=20)

win_lose_label=Label(root,text="",font=("Helvetica",18),bg="white")
win_lose_label.pack(pady=50)

root.mainloop()
