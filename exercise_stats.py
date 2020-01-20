import csv
from matplotlib import pyplot as plt
import numpy as np

def plotStats():
    day,exers,z = np.loadtxt('workouts.txt', unpack = True, delimiter = ',')


    streak = np.array(day)
    duration = np.array(day)

    streak[0] = 0;
    for x in range (0,duration.size):
        duration[x] = (exers[x]*z[x]*30)/60
    for x in range (1, streak.size):
        
        if (day[x] - day[x-1] == 1):
            streak[x] = streak[x-1] + 1
        else:
            streak[x] = 0


    plt.scatter(day,duration)
    plt.scatter(day,streak, color = 'red')
    plt.title('Workouts over Time')
    plt.ylabel('Duration of Workout(mins)')
    plt.xlabel('Day of Year')
    plt.show()

#plotStats() #For testing