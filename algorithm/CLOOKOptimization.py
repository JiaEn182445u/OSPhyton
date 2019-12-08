from algorithm import CLOOKParameter


class CLOOKOptimization:
    def __init__(self):
        self.dp = CLOOKParameter.CLOOKParameter("disk.ini")
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


    def arrangeCLOOK(self,curr,seq,pre):
        temp=[]
        direction="" #declare variable direction
        # self.dp.getCurrent()
        # pre=self.dp.getPrevious()
        if curr>pre: #if current is more than previous, set direction as going "up"
            direction="up"
        if curr<pre: #if current is less than previous, set direction as going "down"
            direction="down"
        seq.append(curr) #append/add in the current disk value into the sequence, as it is not in there yet
        seq.sort() #sort the sequence, in ascending order
        currentIndex=seq.index(curr) #get the index of current in the sorted sequence 

        if direction=="up": #if direction is going up
            for i in seq[currentIndex:]: #for loop to get the values in sequence with index from currentIndex to the end of the sequence
            #for i in range(currentIndex+1):
                temp.append(i) #append into temp while the for loop loops

            for i in seq[:currentIndex]: #for loop to get the values in sequence with index from the start of the sequence(index 0) to currentIndex
            #for i in range(currentIndex+1):
                temp.append(i) #append into temp while the for loop loops
        if direction=="down": #if direction is going down
            for i in seq[currentIndex::-1]: #for loop to get the values in sequence with index from the start of the sequence(index 0) to currentIndex in descending order
            #for i in range(currentIndex+1):
                temp.append(i) #append into temp while the for loop loops
            for i in seq[currentIndex+1:]: #for loop to get the values in sequence with index from the value after currentIndex to the end of sequence
            #for i in range(currentIndex+1):
                temp.append(i) #append into temp while the for loop loops

        return temp

    def generateCLOOK(self):
        seq = self.dp.getSequence()
        curr=self.dp.getCurrent()
        pre=self.dp.getPrevious()
        self.printSequence("CLOOK", self.arrangeCLOOK(curr,seq,pre))


    def generateAnalysis(self):
        self.generateCLOOK()
