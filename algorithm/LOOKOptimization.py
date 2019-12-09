from algorithm import LOOKParameter


class LOOKOptimization:
    def __init__(self):
        self.dp = LOOKParameter.LOOKParameter("disk.ini")
        self.generateAnalysis()

    def printSequence(self, name, location):
        # current start point
        curr = 0
        # previous point
        prev = self.dp.getCurrent()
        # assigned variable for the answer after calculation
        total = 0
        # assigned variable to place long working
        working1 = ""
        # assigned variable to place shortened working
        working2 = ""
        # assigned variable to show the order for sstf
        order = ""
        # location is the sorted sequence
        for i in location:
            #  curr holds the same value as i
            curr = i
            # calculation where prev no. - curr no. is added tothe total's previous value to obtain its new value
            total += abs(prev - curr)
            # the working of sstf
            working1 += "|" + str(prev) + "-" + str(curr) + "|+"
            # shortened working of sstf
            working2 += str(abs(prev - curr)) + "+"
            # setting i to prev as the for loop starts on the next value
            prev = i

        # removing extra '+' in working1 & working2
        working1 = working1[0:-1]
        working2 = working2[0:-1]
        # adding current into location
        order = str(self.dp.getCurrent()) + ", " + str(location)[1:-1]
        # name "sstf" for indication
        print(name + "\n====")
        # print of order of sstf
        print("Order of Access: " + order)
        # printing of the detailed working, working1
        print("Total distance: " + "\n" + working1 + "\n")
        # printing of the shortened working, working2
        print("= " + working2 + "\n")
        # printing of result after calculation
        print("= " + str(total) + "\n")

    def arrangeLOOK(self,curr,seq,pre):
        temp=[]
        direction="" #declare variable direction
        # self.dp.getCurrent()
        # pre=self.dp.getPrevious()
        if curr>pre: #if current is more than previous, set direction as going "up"
            direction="up"
        if curr<pre: #if current is less than previous, set direction as going "down"
            direction="down"
        seq.append(curr) #append/add in the current disk value into the sequence, as it is not in there yet
        #order = str(self.dp.getCurrent())+","+str(temp)[1:-1]
        seq.sort() #sort the sequence, in ascending order
        currentIndex=seq.index(curr) #get the index of current in the sorted sequence 

        if direction=="up": #if direction is going up
            for i in seq[currentIndex:]: #for loop to get the values in sequence with index from currentIndex to the end of the sequence
            #for i in range(currentIndex+1):
                temp.append(i) #append into temp while the for loop loops
            for i in seq[currentIndex-1::-1]: #for loop to get the values in sequence with index from the start of the sequence to the value before currentIndex in descending order
            #for i in range(currentIndex+1):
                temp.append(i) #append into temp while the for loop loops
        if direction=="down": #if direction is going down
            for i in seq[currentIndex::-1]: #for loop to get the values in sequence with index from the start of the sequence to currentIndex in descending order
            #for i in range(currentIndex+1):
                temp.append(i) #append into temp while the for loop loops
            for i in seq[currentIndex+1:]: #for loop to get the values of the sequence with index from the value after current index to the end of the sequence
            #for i in range(currentIndex+1):
                temp.append(i) #append into temp while the for loop loops
        return temp

    def generateLOOK(self):
        seq = self.dp.getSequence()
        curr=self.dp.getCurrent()
        pre=self.dp.getPrevious()
        self.printSequence("LOOK", self.arrangeLOOK(curr,seq,pre))


    def generateAnalysis(self):
        self.generateLOOK()
