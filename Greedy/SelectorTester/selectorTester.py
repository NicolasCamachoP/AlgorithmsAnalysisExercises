import sys
import random
import time

sys.path.append(".")
from ActivitySelector import Activity
from ActivitySelector import ActivityManager



def activitiesRandomizer(n):
    if n > 0:
        activities = []
        randStart = random.randrange(1, 22)
        randEnd = random.randrange(randStart + 1, 24 )
        for j in range (n):
            #print(f'Start: {randStart} End: {randEnd}')
            randStart = random.randrange(1, 22)
            randEnd = random.randrange(randStart + 1, 24 )
            activities.append(Activity(randStart, randEnd))
        #End for
        return activities
    #End if
#End def

def MeasureTimeDP(actMan):
    sT = time.process_time()
    actMan.ActivitySelectorDP()
    eT = time.process_time()
    return float( eT - sT)
#End def

def MeasureTimeGreedy(actMan):
    sT = time.process_time()
    actMan.ActivitySelectorGreedy()
    eT = time.process_time()
    return float( eT - sT)
#End def

def timeBench(testNum, actNum):
    if testNum > 0 and actNum > 0:
        timeDP = 0 
        timeGreedy = 0
        for i in range (testNum):
            activities = activitiesRandomizer(actNum)
            activities.append(Activity(-1, 0))
            activities.append(Activity(25, 26))
            actMan = ActivityManager(activities)
            timeDP += MeasureTimeDP(actMan)
            actMan.removeActivity(0)
            actMan.removeActivity(actMan.nActivities - 1)
            timeGreedy += MeasureTimeGreedy(actMan)
        #End for
        return [float (timeDP/testNum), float (timeGreedy/testNum)]
    else:
        return [0,0]
    #End if
#End def

def solutionBench(testNum, actNum):
    if testNum > 0 and actNum > 0:
        dpWins = 0
        greedyWins = 0
        nTies = 0
        for i in range (testNum):
            activities = activitiesRandomizer(actNum)
            activities.append(Activity(-1, 0))
            activities.append(Activity(25, 26))
            actMan = ActivityManager(activities)
            solDP = len(actMan.ActivitySelectorDP())
            actMan.removeActivity(0)
            actMan.removeActivity(actMan.nActivities - 1)
            solGreedy = len(actMan.ActivitySelectorGreedy())
            if solDP > solGreedy:
                dpWins += 1
            elif solGreedy > solDP:
                greedyWins += 1
            else:
                nTies += 1
            #End if
        #End for
        return [dpWins, greedyWins, nTies]
    else:
        return [0,0]
    #End if
#End def

def selectorTimeBench():
    print(f"--------- Selector Time Bench ---------")
    numOfTest = 20
    numOfAct = 50
    results = timeBench(numOfTest, numOfAct)
    print(f"For {numOfTest} runs with {numOfAct} activities...")
    print(f"DP average time: {results[0]}")
    print(f"Greedy average time: {results[1]}")

    numOfTest = 20
    numOfAct = 100
    results = timeBench(numOfTest, numOfAct)
    print(f"For {numOfTest} runs with {numOfAct} activities...")
    print(f"DP average time: {results[0]}")
    print(f"Greedy average time: {results[1]}")

    numOfTest = 20
    numOfAct = 150
    results = timeBench(numOfTest, numOfAct)
    print(f"For {numOfTest} runs with {numOfAct} activities...")
    print(f"DP average time: {results[0]}")
    print(f"Greedy average time: {results[1]}")

    numOfTest = 20
    numOfAct = 200
    results = timeBench(numOfTest, numOfAct)
    print(f"For {numOfTest} runs with {numOfAct} activities...")
    print(f"DP average time: {results[0]}")
    print(f"Greedy average time: {results[1]}")

    numOfTest = 20
    numOfAct = 250
    results = timeBench(numOfTest, numOfAct)
    print(f"For {numOfTest} runs with {numOfAct} activities...")
    print(f"DP average time: {results[0]}")
    print(f"Greedy average time: {results[1]}")
#End def

def selectorSolutionTest():
    print(f"--------- Selector Solution Test ---------")
    numOfTest = 20
    numOfAct = 50
    results = solutionBench(numOfTest, numOfAct)
    print(f"For {numOfTest} runs with {numOfAct} activities...")
    print(f"Times when DP offers a better solution: {results[0]}")
    print(f"Times when Greedy offers a better solution: {results[1]}")
    print(f"Ties: {results[2]}")

    numOfTest = 20
    numOfAct = 100
    results = solutionBench(numOfTest, numOfAct)
    print(f"For {numOfTest} runs with {numOfAct} activities...")
    print(f"Times when DP offers a better solution: {results[0]}")
    print(f"Times when Greedy offers a better solution: {results[1]}")
    print(f"Ties: {results[2]}")

    numOfTest = 20
    numOfAct = 150
    results = solutionBench(numOfTest, numOfAct)
    print(f"For {numOfTest} runs with {numOfAct} activities...")
    print(f"Times when DP offers a better solution: {results[0]}")
    print(f"Times when Greedy offers a better solution: {results[1]}")
    print(f"Ties: {results[2]}")

    numOfTest = 20
    numOfAct = 200
    results = solutionBench(numOfTest, numOfAct)
    print(f"For {numOfTest} runs with {numOfAct} activities...")
    print(f"Times when DP offers a better solution: {results[0]}")
    print(f"Times when Greedy offers a better solution: {results[1]}")
    print(f"Ties: {results[2]}")

    numOfTest = 20
    numOfAct = 250
    results = solutionBench(numOfTest, numOfAct)
    print(f"For {numOfTest} runs with {numOfAct} activities...")
    print(f"Times that DP give a better solution: {results[0]}")
    print(f"Times when Greedy offers a better solution: {results[1]}")
    print(f"Ties: {results[2]}")
#End def

#selectorTimeBench()
selectorSolutionTest()
