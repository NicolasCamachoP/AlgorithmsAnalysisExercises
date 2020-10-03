class Activity:
    def __init__(self, start, end, **kwargs):
        if 'name' in kwargs:
            self.name = kwargs['name']
        #End if
        self.start = start
        self.end = end
    #End def

    def __repr__(self):
        return f"Name: {self.name} Start: {self.start} End {self.end}"
    #End def

    def setName(self, name):
        self.name = name
    #End def

#End class

class ActivityManager:
    def __init__(self, activities):
        self.activities = activities
        self.nActivities = len(activities)
        self.activities.sort(key = lambda x: x.end)
        self.__updateActNames()
    #End def

    def __repr__(self):
        return f"Registered activities: {self.nActivities}"
    #End def

    def __updateActNames(self):
        for i in range( 0, self.nActivities):
            if i < 10:
                self.activities[i].setName("a" + "0" + str(i))
            else:
                self.activities[i].setName("a" + str(i))
            #End if
        #End for
    #End def

    def removeActivity(self, index):
        self.activities.pop(index)
        self.nActivities -= 1
    #End def

    def printActivities(self, *args):
        if len(args) == 0:
            for i in range(0, self.nActivities):
                print(self.activities[i])
            #End for
        else:
            for i in range (0, len(args)):
                print(self.activities[args[i]])
            #End for
        #End if
    #End def

    def ActivitySelectorDP(self):
        M = [[0 for j in range (self.nActivities )] for i in range (self.nActivities ) ]
        BT = [[0 for j in range (self.nActivities )] for i in range (self.nActivities )]
        for i in range(0, self.nActivities ):
            for j in range(0, self.nActivities ):
                if i != j:
                    for k in range (i + 1, j + 1):
                        if M[i][j] < M[i][k] + M[k][j] + 1:
                            #Si a_i es antes que a_k
                            if self.activities[i].end <= self.activities[k].start: 
                                #Si a_j es después que a_k
                                if self.activities[k].end <= self.activities[j].start:
                                    M[i][j] = M[i][k] + M[k][j] + 1
                                    BT[i][j] = k
                                #End if
                            #End if
                        #End if
                    #End for
                #End if
            #End for
        #End for
        index = []
        self.__dpBT(M, BT, 0, self.nActivities - 1 , index)
        return index
    #End def

    def __dpBT(self, M, BT, i, j, indexList):
        if M[i][j] > 0:
            k = BT[i][j]
            indexList.append(k)
            self.__dpBT(M, BT, i, k, indexList)
            self.__dpBT(M, BT, k, j, indexList)
        #End if
    #End def
    

    def ActivitySelectorGreedy(self):
        R = [0]
        k = 0
        for m in range(1, self.nActivities):
            if self.activities[m].start >= self.activities[k].end:
                R.append(m)
                k = m
            #End if
        #End for
        return R
    #End def

#Activities 
"""activities = [Activity( 0, 0, name = "a0"), Activity( 12, 16, name = "a1"), Activity( 2, 14, name = "a2"), Activity( 8, 12, name = "a3"), Activity(8, 11, name = "a4"), Activity( 6, 10, name = "a5"), 
Activity( 5, 9, name = "a6"), Activity( 3, 9, name = "a7"), Activity( 5, 7, name = "a8"), Activity( 0, 6, name = "a9"), Activity( 3, 5, name = "a10"), 
Activity( 1, 4, name = "a11"), Activity(25, 26, name = "a1000000000")]
actMan = ActivityManager(activities)
print("DP")
actMan.printActivities(*actMan.ActivitySelectorDP())
actMan.removeActivity(0)
actMan.removeActivity(actMan.nActivities - 1)
print("Greedy")
actMan.printActivities(*actMan.ActivitySelectorGreedy())"""




