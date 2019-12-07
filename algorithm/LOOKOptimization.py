from algorithm import LOOKParameter


class LOOKOptimization:
    def __init__(self):
        self.dp = LOOKParameter.LOOKParameter("disk.ini")
        self.generateAnalysis()

    def printSequence(self, name, location):
        curr = 0
        prev = self.dp.getCurrent()
        total = 0
        working1 = ""
        working2 = ""
        order = ""
        for i in location:
            curr = i
            total += abs(prev - curr)
            working1 += "|" + str(prev) + "-" + str(curr) + "|+"
            working2 += str(abs(prev - curr)) + "+"
            prev = i
        working1 = working1[0:-1]
        working2 = working2[0:-1]
        order = str( str(location)[1:-1])
        print(name + "\n====")
        print("Order of Access: " + order)
        print("Total distance: " + "\n" + working1 + "\n")
        print("= " + working2 + "\n")
        print("= " + str(total) + "\n")

    def arrangeLOOK(self,curr,seq,pre):
        temp=[]
        direction="" #declare variable direction
        # self.dp.getCurrent()
        # pre=self.dp.getPrevious()
        if curr>pre: #if current 
            direction="up"
        if curr<pre:
            direction="down"
        seq.append(curr)
        #order = str(self.dp.getCurrent())+","+str(temp)[1:-1]
        seq.sort()
        currentIndex=seq.index(curr)

        if direction=="up":
            for i in seq[currentIndex:]:
            #for i in range(currentIndex+1):
                temp.append(i)
            for i in seq[currentIndex-1::-1]:
            #for i in range(currentIndex+1):
                temp.append(i)
        if direction=="down":
            for i in seq[currentIndex::-1]:
            #for i in range(currentIndex+1):
                temp.append(i)
            for i in seq[currentIndex+1:]:
            #for i in range(currentIndex+1):
                temp.append(i)
        return temp

    def generateLOOK(self):
        seq = self.dp.getSequence()
        curr=self.dp.getCurrent()
        pre=self.dp.getPrevious()
        self.printSequence("LOOK", self.arrangeLOOK(curr,seq,pre))


    def generateAnalysis(self):
        self.generateLOOK()
