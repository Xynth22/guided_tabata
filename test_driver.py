#from tabataGUI import close_app

from guizero import App, Text, PushButton
import threading
from random import randint

import time


exerciseFile = [line.rstrip('\n') for line in open('exercises.txt')]
exercises = exerciseFile[2:len(exerciseFile)]
categories = exerciseFile[0].split()
catStarts = exerciseFile[1].split()

catEnds = catStarts[1:len(catStarts)] + [len(exercises)]

numCats = len(catStarts)
numExerInCatComplete = [0] * numCats

exerciseList = []

repetitions = 2
numExercises = 5

minExerPerCat = int(numExercises / numCats)

frequency = 2500  # Set Frequency To 2500 Hertz
duration = 50  # Set Duration To 1000 ms == 1 second

app = App(title="Tapata", width = 400, height=400)

text = Text(app, text="", size=24, align = "bottom")
counter = Text(app, text="0 , 0", size=24, align = "top")
debug = Text(app, text="", size=24, align = "left")

def shortPause():
    time.sleep(0.2)

def findNextCat():
    nxtCat = randint(0,numCats-1)
    if (all(x >= minExerPerCat for x in numExerInCatComplete)):
        return nxtCat
    else:
        while (numExerInCatComplete[nxtCat] >= minExerPerCat):
            nxtCat = randint(0,numCats-1)
        return nxtCat
    
def getExercise(): 
    cat = findNextCat()
    numExerInCatComplete[cat] += 1
    i = randint(int(catStarts[cat]),int(catEnds[cat]) - 1)
    while (i in exerciseList):
        i = randint(int(catStarts[cat]),int(catEnds[cat]) - 1)
    exerciseList.append(i)
    return i


def main():

    for exer in range(0,numExercises):
            
            nxt = getExercise()
            debug.value = exerciseList + ["\n"] + numExerInCatComplete
            text.value = exercises[nxt]
            app.bg = "green"
            counter.value = str(exer+1) + " , 1"
            app.update()
            #Play sound to notify of new exercise
            
            for rep in range(0,repetitions):
                counter.value = str(exer+1) + " , " + str(rep+1)
                app.bg = "green"
                app.update()
                
                #Rest Timer
                tRest = threading.Thread(target=shortPause)
                tRest.start()
                tRest.join()

                app.bg = "red"
                app.update()

                #Excercise timer
                tExercise = threading.Thread(target=shortPause)
                tExercise.start()
                tExercise.join()
            
        
    app.bg = "green"
    debug.value = ""
    text.size = 18    
    finalOutput = ["Workout Complete\n"] + [exercises[i] for i in exerciseList] + ["\n"] + [exerciseFile[0]] + ["\n"] + [numExerInCatComplete]
    text.value = finalOutput
    
    app.update()

 
    app.display()
 
    
if __name__ == '__main__':
    main()