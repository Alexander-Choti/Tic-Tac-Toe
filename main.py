from tkinter import *
import random 

def  next_Turn (row , column):
    
    global player

    if buttons[row] [column] ['text'] == "" and win_Condition() is False:

        if player == players[0]:

            buttons[row][column] ['text'] = player

            if win_Condition() is False:
                player = players[1]
                label.config(text=(players[1]+ "'s" + " " + "turn"))
            elif win_Condition() is True:
                label.config(text=(players[0]+ " " + "Wins"))

            elif win_Condition() == "Tie":
                label.config(text=("Tie!"))
        
        else:

            buttons[row][column] ['text'] = player

            if win_Condition() is False:
                player = players[0]
                label.config(text=(players[0]+ "'s" + " " + "turn"))
            elif win_Condition() is True:
                label.config(text=(players[1]+ " " + "Wins"))

            elif win_Condition() == "Tie":
                label.config(text=("Tie!"))

def win_Condition ():
    
    for row in range(3):
        if buttons [row] [0] ['text'] == buttons [row] [1] ['text'] == buttons [row] [2] ['text'] != "":
           
            buttons[row] [0].config(bg='green')
            buttons[row] [1].config(bg='green')
            buttons[row] [2].config(bg='green')
            return True

    for column in range(3):
        if buttons [0] [column] ['text'] == buttons [1] [column] ['text'] == buttons [2] [column] ['text'] != "":
           
            buttons[0] [column].config(bg='green')
            buttons[1] [column].config(bg='green')
            buttons[2] [column].config(bg='green')
            return True
    
    if buttons [0] [0] ['text'] == buttons [1] [1] ['text'] == buttons [2] [2] ['text'] != "":
           
            buttons[0] [0].config(bg='green')
            buttons[1] [1].config(bg='green')
            buttons[2] [2].config(bg='green')
            return True

    elif buttons [0] [2] ['text'] == buttons [1] [1] ['text'] == buttons [2] [0] ['text'] != "":
           
            buttons[0] [2].config(bg='green')
            buttons[1] [1].config(bg='green')
            buttons[2] [0].config(bg='green')
            return True
    
    elif empty_Spaces() is False:
        for row in range (3):
            for column in range (3):
                buttons[row] [column].config(bg='yellow')   
        return "Tie"

    else:
        return False

def empty_Spaces ():
    
    spaces = 9

    for row in range (3):
        for column in range (3):
            if buttons [row] [column] ['text'] != "":
                spaces-=1
   
    if spaces == 0:
        return False
    else:
        return True 

def new_Game ():
    
    global player 

    player = random.choice(players)

    label.config(text=player + "'s" + " " + "Turn")

    for row in range(3):
        for column in range(3):
            buttons[row] [column].config(text = "", bg = "#F0F0F0")


window = Tk()
window.title("Tic Tac Toe")
players = ["x" , "o"]
player = random.choice (players)
buttons = [[0,0,0], [0,0,0], [0,0,0]]

label = Label(text = player + "'s" + " " +"Turn", font=('times', 40))
label.pack(side = "top")

reset_Button = Button(text = "restart", font=("times" , 20), command=new_Game)
reset_Button.pack(side = "top")

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row] [column] = Button (frame, text = "" , font=('times', 40) , width = 5, height = 2, command = lambda row=row , column=column: next_Turn(row,column))

        buttons[row] [column].grid(row=row, column=column)


window.mainloop()