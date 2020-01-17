from guizero import App, Text
from random import randint
import time
import winsound
#app = App()
#text = Text(app, text="Hello World", size=256)
#app.display()

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
#app = App()
#text = Text(app, text="Hello World", size=256)
#app.display()
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 50  # Set Duration To 1000 ms == 1 second
for x in range(0,2):
    i = randint(0,len(exercises)-1);
    
    #text = Text(app, text=exercises[i], size=256)
    #app.display()
    
    print(x, exercises[i]);
    print(x, exercises[i]);
    print(x, exercises[i]);
    print(x, exercises[i]);
    print(x, exercises[i]);
    print(x, exercises[i]);
    print(x, exercises[i]);
    print(x, exercises[i]);
    print(x, exercises[i]);
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
    #app.destroy()
    #app=App();
    
winsound.Beep(frequency+500, 700)

    
