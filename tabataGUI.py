from guizero import App, Text
from random import randint
import time
import winsound

exercises = [line.rstrip('\n') for line in open('exercises.txt')]


app = App(title="Tapata", width = 2000, height=400, bg="blue")

text = Text(app, text="Temp", size=200, align = "bottom")
counter = Text(app, text="Temp", size=24, align = "top")


frequency = 2500  # Set Frequency To 2500 Hertz
duration = 50  # Set Duration To 1000 ms == 1 second

for x in range(0,40):
    
    #pick an exercise
    i = randint(0,len(exercises)-1);
    
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
    
