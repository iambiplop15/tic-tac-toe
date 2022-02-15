import random
from tkinter import *

wincolor = "#2ECC71"
drawcolor = "#F4D03F"

def next_turn(row,column):
    global player
    if buttons[row][column]["text"] == "" and check_winner() is False:
        if player == players[0]:
            buttons[row][column]["text"] = player
            if check_winner() is True:
                label.config(text=f"{player} wins")
            elif check_winner() is False:
                player = players[1]
                label.config(text=f"{player} turn")
            elif check_winner() == "draw":
                label.config(text="Game draw")
        else:
            buttons[row][column]["text"] = player
            if check_winner() is True:
                label.config(text=f"{player} wins")
            elif check_winner() is False:
                player = players[0]
                label.config(text=f"{player} turn")
            elif check_winner() == "draw":
                label.config(text="Game draw")    

def check_winner():
    for row in range(3):
        if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] != "":
            buttons[row][0].config(bg=f"{wincolor}")
            buttons[row][1].config(bg=f"{wincolor}")
            buttons[row][2].config(bg=f"{wincolor}")
            return True
    for column in range(3):
        if buttons[0][column]["text"] == buttons[1][column]["text"] == buttons[2][column]["text"] != "":
            buttons[0][column].config(bg=f"{wincolor}")
            buttons[1][column].config(bg=f"{wincolor}")
            buttons[2][column].config(bg=f"{wincolor}")
            return True
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        buttons[0][0].config(bg=f"{wincolor}")
        buttons[1][1].config(bg=f"{wincolor}")
        buttons[2][2].config(bg=f"{wincolor}")
        return True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        buttons[0][2].config(bg=f"{wincolor}")
        buttons[1][1].config(bg=f"{wincolor}")
        buttons[2][0].config(bg=f"{wincolor}")
        return True
    elif empty_spaces() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="#F4D03F")
        return "draw"
    else:
        return False

def empty_spaces():
    spaces = 9
    for row in range(3):
        for column in range(3):
            if buttons[row][column]["text"] != "":
                spaces -= 1
    if spaces == 0:
        return False
    else:
        return True

def new_game():
    global player
    player = random.choice(players)
    label.config(text=f"{player} turn")
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="",bg="#F0F0F0")

root = Tk()
root.title("Tic Tac Toe")
root.config(background="white")
players = ["X","O"]
player = random.choice(players)
buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]
label = Label(text= f"{player} turn",font=("consolas",40))
label.pack(side="top")
reset_btn = Button(text="Restart",font=("consolas",10),command=new_game,relief="raise",bd=4,bg="#CB4335",fg="white")
reset_btn.pack(side="top",pady=16,ipadx=8,ipady=8)
frame = Frame(root) 
frame.pack()
for row in range(3):
    for column in range(3):
        
        buttons[row][column] = Button(frame,text="",
                                  font=("consolas",40),
                                  width=5,
                                  height=2,
                                  bg="white",
                                  command= lambda row=row,column=column : next_turn(row,column))
        buttons[row][column].grid(row=row,column=column,padx=1,pady=1)
root.mainloop()