from guizero import App, Text, PushButton
from random import randint
import time
import winsound
from datetime import datetime
import threading
from exercise_stats import plotStats

exercises = [line.rstrip('\n') for line in open('exercises.txt')]
plotStats()

repetitions = 3
numExercises = 10

frequency = 2500  # Set Frequency To 2500 Hertz
duration = 50  # Set Duration To 1000 ms == 1 second

app = App(title="Tapata", width = 2000, height=400)

text = Text(app, text="", size=200, align = "bottom")
counter = Text(app, text="0 , 0", size=24, align = "top")

def close_app():
    app.destroy()
closeButton = PushButton(app, text =  "End Workout", align = "right", command = close_app)

def tabataTimer(exer, reps, work):
    t = 0
    if (work): tEnd=20
    else: tEnd = 10
    while (t < tEnd):
        time.sleep(1)
        t += 1
        if (t > (tEnd - 3) and t < tEnd):
            winsound.Beep(frequency, duration)
        if (t == tEnd):
            winsound.Beep(frequency-500, 150)
     
def startupTimer():
    time.sleep(10)

exerciseList = []

def getExercise(): #ensure no duplicates, TODO add logic to balance leg/core/arms
    i = randint(0,len(exercises)-1)
    while (i in exerciseList):
        i = randint(0,len(exercises)-1)
    exerciseList.append(i)
    return i





#timerThread = threading.Thread(target=startupTimer)
#timerThread.start()
def main():

    for exer in range(0,numExercises):
            
            nxt = getExercise()
            text.value = exercises[nxt]
            app.bg = "green"
            app.update()
            #Play sound to notify of new exercise
            winsound.Beep(1500, 150)
            winsound.Beep(1500, 150)
            winsound.Beep(3500, 150)
            time.sleep(10)
            for rep in range(0,repetitions):
                counter.value = str(exer+1) + " , " + str(rep+1)
                app.bg = "green"
                app.update()
                
                #Rest Timer
                tRest = threading.Thread(target=tabataTimer, args=(exer,rep, False))
                tRest.start()
                tRest.join()

                app.bg = "red"
                app.update()

                #Excercise timer
                tExercise = threading.Thread(target=tabataTimer, args=(exer,rep, True))
                tExercise.start()
                tExercise.join()
            
        
    winsound.Beep(frequency+500, 700)
    app.bg = "green"
    text.value = "Workout Complete"
    app.update()

    day_of_year = datetime.today().timetuple().tm_yday

    f = open("workouts.txt", "a")
    f.write("\n%d , %d , %d" % (day_of_year,numExercises,repetitions))
    f.close()

    app.display()
    plotStats()

    
if __name__ == '__main__':
    main()