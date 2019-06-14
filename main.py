import time    #här importerar vi alla bibliotek som vi behöver
from tkinter import *


master = Tk()       
master.geometry('300x300')   #storleken på fönstret som öppnas

C = Canvas(master)
C.place(x=0, y=0, width=500, height=500)   #storleken på spelplanen

board = [
     [None, None, None, None, None, None, None, None, None, None, None, None],  #None runt om för att sätta gränser
     [None, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, None],
     [None, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, None],
     [None, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, None],
     [None, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, None],
     [None, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, None],
     [None, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, None],           #här gör vi spelbrädan, där vi lägger in 1or och 0or 
     [None, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, None],           #1or är de som är vid liv
     [None, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, None],           #0or är alltså döda
     [None, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, None],
     [None, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, None],
     [None, None, None, None, None, None, None, None, None, None, None, None]
] 


rows = 10     
columns = 10

def main():   # main funktionen som innehåller själva spelet
    global board
    newboard = board   # vi gör 2 boards, newboard blir en kopia av board för att vi ska kunna ändra på tavlan
    for column in range(1, columns + 1):      
        for row in range(1, rows + 1):      #den går igenom alla 1or och 0or på planen
            if (board[row][column] == 1): #om den positionen är en 1a alltså en ruta vid liv, ska den titta hur många grannar den har
                around = [board[row - 1][column - 1], board[row - 1][column], board[row - 1][column + 1], board[row][column - 1], board[row][column + 1], board[row + 1][column - 1], board[row + 1][column], board[row + 1][column + 1]] 
                neighbors = 0    # på raden ovanför hittar vi de 8 närmsta rutorna
                for slot in around:  
                    try:
                        neighbors += slot #nu lägger vi till alla 8 rutor runt rutan, vi använder try då vissa grannar kommer att vara None, och då blir det fel
                    except:
                        neighbors += 0 #om det blir error lägger den bara till 0 på den rutan
                if neighbors < 2:       #om de blir färre än 2 grannar
                    newboard[row][column] = 0   #så görs rutan om till en 0a, den dör alltså
                elif neighbors > 3:  #om den har fler än 3 grannar 
                    newboard[row][column] = 0   #görs den om till en 0a
            if (board[row][column] == 0):  #om rutan är en nolla
                around = [board[row - 1][column - 1], board[row - 1][column], board[row - 1][column + 1], board[row][column - 1], board[row][column + 1], board[row + 1][column - 1], board[row + 1][column], board[row + 1][column + 1]]
                neighbors = 0
                for slot in around: #så gör vi om samma process med grannar
                    try:
                        neighbors += slot
                    except:
                        neighbors += 0
                if (neighbors == 3):   #men om grannarna är lika med 3 så gör vi om den till en etta
                    newboard[row][column] = 1
    board = newboard  #alla ändringar har skett på newboard, för att det ska synas så sätter vi att board är lika med newboard så lägger vi in ändringarna på board

def paintboard(map):   #funktionen för att visualisera
    for column in range(1, columns + 1):
        for row in range(1, rows + 1):      #går igenom alla 1or och 0or på planen
            if (map[row][column] == 1):     #om det är en 1a 
                C.create_rectangle(column*10, row*10, (column + 1)*10, (row + 1)*10, fill = "black") #skapar vi en svart kvadrat där
            else:
                C.create_rectangle(column*10, row*10, (column + 1)*10, (row + 1)*10, fill = "white") #annars gör vi en vit kvadrat
    master.update() #uppdaterar så att förändringarna syns


while True:  # vi kör en while True loop som gör att koden körs hela tiden tills vi stänger ner den
    C.delete('all')    #vi tömmer spelplanen så att vi kan måla en ny plan
    main()  #sedan kör vi koden för spelet
    paintboard(board)  #därefter visualiseringskoden
    time.sleep(0.5)  #en delay på 0.5 sekunder