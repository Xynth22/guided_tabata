from guizero import App, Text
from random import randint
import time
import winsound

exercises = ["Mountain Climber", 
"Burpee", 
"Plank", "Sumo Squat",
"Wall Sit", "Tricep Raise",
"Lunge", 
"SQUAT", 
"Curtsy Lunge",
"Calf raise",
"Standard push-up",
"Superman",
"Diamond push-up",
"Flutter kick",
"Side plank",
"Russian twist",
"Bicycle",
"Crunch",
"Full Sit up","Jumping Jacks",
"High Knee", "Butt Kicks", "Tick Tocks", "Heel Diggs"];

app = App(title="Tapata", width = 2000, height=300)
text = Text(app, text="Temp", size=200)
#counter = Text(app, text="Temp", size=24, align = "left")
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 50  # Set Duration To 1000 ms == 1 second
for x in range(0,10):
    i = randint(0,len(exercises)-1);
    text.value = exercises[i]
    #counter.value = x
    text = Text(app, text=exercises[i], size=128)
    app.update()
    time.sleep(7);
    winsound.Beep(frequency, duration)
    time.sleep(1);
    winsound.Beep(frequency, duration)
    time.sleep(1);
    winsound.Beep(frequency, duration)
    time.sleep(1);
    winsound.Beep(frequency-500, 150)
    
    time.sleep(17);
    winsound.Beep(frequency, duration)
    time.sleep(1);
    winsound.Beep(frequency, duration)
    time.sleep(1);
    winsound.Beep(frequency, duration)
    time.sleep(1);
    winsound.Beep(frequency-500, 150)
 
    
winsound.Beep(frequency+500, 700)
app.display()
    
