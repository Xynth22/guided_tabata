from matplotlib import pyplot as plt
import numpy as np

def plotStats():
    #day,exers,z = np.loadtxt('workouts.txt', unpack = True, delimiter = ',')
    days,mins = calcMinsPerDay()


    streak = np.array(days)
    
    streak[0] = 0

    for x in range (1, streak.size):
        
        if (mins[x] > 0 and mins[x-1] > 0):
            streak[x] = streak[x-1] + 1
        else:
            streak[x] = 0


    plt.scatter(days,mins)
    plt.plot(days,streak, color = 'red')
    plt.title('Workouts over Time')
    plt.ylabel('Duration of Workout(mins)')
    plt.xlabel('Day of Year')
    plt.show()


def calcMinsPerDay():
    day,exers,reps = np.loadtxt('workouts.txt', unpack = True, delimiter = ',')

    firstDay = int(np.min(day))
    lastDay = int(np.max(day))
    dayList=list(range(firstDay,lastDay+1))


    dayTot = np.asarray(dayList)
    minsTot = np.zeros_like(dayTot)
    
    
    
    #dayTot[0] = day[0]
    #minsTot[0] = (exers[0]*reps[0]*30)/60
    for x in range(0,day.size):
        y = np.argwhere(dayTot == day[x])
        if (y.size == 0):
            print("Error in day indexing")
            return 0
            #dayTot=np.append(dayTot, day[x])
            #minsTot=np.append(minsTot,(exers[x]*reps[x]*30)/60)
        else:
            minsTot[y[0][0]] += (exers[x]*reps[x]*30)/60
    return dayTot,minsTot

#plotStats() #For testing