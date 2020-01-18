from guizero import App, Text, PushButton
from random import randint
import time
import winsound
import webbrowser
from datetime import datetime


exercises = [line.rstrip('\n') for line in open('exercises.txt')]

repetitions = 3
numExercises = 7

app = App(title="Tapata", width = 2000, height=400)

text = Text(app, text="", size=200, align = "bottom")
counter = Text(app, text="0 , 0", size=24, align = "top")

def close_app():
    app.destroy()

closeButton = PushButton(app, text =  "End Workout", align = "right", command = close_app)

frequency = 2500  # Set Frequency To 2500 Hertz
duration = 50  # Set Duration To 1000 ms == 1 second

for exer in range(0,numExercises):
        #pick an exercise
        i = randint(0,len(exercises)-1)
        #Play sound to notify of new exercise
        winsound.Beep(1500, 150)
        winsound.Beep(1500, 150)
        winsound.Beep(3500, 150)
        text.value = exercises[i]
        app.bg = "green"
        app.update()
        time.sleep(10); #extra time to setup next exercise

 
        for rep in range(0,repetitions):
        
            #update text
            counter.value = str(exer+1) + " , " + str(rep+1)
            app.bg = "green"
            app.update()

            #Rest Timer
            time.sleep(7);
            for y in range(1,3):
                winsound.Beep(frequency, duration)
                time.sleep(1);
            winsound.Beep(frequency-500, 150)
            app.bg = "red"
            app.update()
            #Excercise timer
            time.sleep(17);
            for y in range(1,3):
                winsound.Beep(frequency, duration)
                time.sleep(1);    
            winsound.Beep(frequency-500, 150)
        
     
winsound.Beep(frequency+500, 700)
app.bg = "green"
text.value = "Workout Complete"
app.update()

day_of_year = datetime.today().timetuple().tm_yday

f = open("workouts.txt", "a")
f.write("\n%d , %d , %d" % (day_of_year,numExercises,repetitions))
f.close()

app.display()
    
