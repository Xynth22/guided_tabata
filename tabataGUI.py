from guizero import App, Text, PushButton
from random import randint
import time
import winsound

exercises = [line.rstrip('\n') for line in open('exercises.txt')]

repetitions = 3
numExercises = 5

app = App(title="Tapata", width = 2000, height=400)

text = Text(app, text="", size=200, align = "bottom")
counter = Text(app, text="", size=24, align = "top")

def close_app():
    app.destroy()

closeButton = PushButton(app, text =  "End Workout", align = "right", command = close_app)

frequency = 2500  # Set Frequency To 2500 Hertz
duration = 50  # Set Duration To 1000 ms == 1 second

for x in range(0,(repetitions*numExercises) - 1):
    
    if (x / repetitions == round(x / repetitions)):
        #pick an exercise
        i = randint(0,len(exercises)-1)
        #Play sound to notify of new exercise
        winsound.Beep(1500, 150)
        winsound.Beep(1500, 150)
        winsound.Beep(3500, 150)

    
    #update text
    text.value = exercises[i]
    counter.value = x        
    app.update()

    #Rest Timer
    time.sleep(7);
    for y in range(1,3):
        winsound.Beep(frequency, duration)
        time.sleep(1);
    winsound.Beep(frequency-500, 150)
    
    #Excercise timer
    time.sleep(17);
    for y in range(1,3):
        winsound.Beep(frequency, duration)
        time.sleep(1);    
    winsound.Beep(frequency-500, 150)
     
winsound.Beep(frequency+500, 700)
app.display()
    
