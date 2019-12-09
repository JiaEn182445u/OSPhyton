from algorithm import SCANParameter


class SCANOptimization:
    def __init__(self):
        self.dp = SCANParameter.SCANParameter("disk.ini")
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
             # the working of SCAN
            working1 += "|" + str(prev) + "-" + str(curr) + "|+"
            # shortened working of SCAN
            working2 += str(abs(prev - curr)) + "+"
            # setting i to prev as the for loop starts on the next value
            prev = i
            # removing extra '+' in working1 & working2
        working1 = working1[0:-1]
        working2 = working2[0:-1]
         # adding current into location
        order = str( str(location)[1:-1])
        # name "sstf" for indication
        print(name + "\n====")
        print("Order of Access: " + order)
         # printing of the detailed working, working1
        print("Total distance: " + "\n" + working1 + "\n")
        # printing of the shortened working, working2
        print("= " + working2 + "\n")
        # printing of result after calculation
        print("= " + str(total) + "\n")


    def arrangeSCAN(self,curr,seq,pre,last):
        first=0

        temp=[]
        direction=""
        # if the previous number is lesser than the current number, the direction is to go up.Which is towards the max number
        if curr>pre:
            direction="up"
        # if the previous number is greater than the current number, the direction is to go down. Which is towards 0.
        if curr<pre:
            direction="down"
        # add the current number into the sequence
        seq.append(curr)
        # sort the sequence from lowest to the highest.
        seq.sort()
        # find the index of the current number in the sorted sequence.
        currentIndex=seq.index(curr)

        if direction=="up":
            # a for loop to add in the current number and numbers bigger than the current number into temp which is an empty list
            for i in seq[currentIndex:]:

                temp.append(i)
            # adding in the max number into the temp, when the line have reach to the edge
            temp.append(last)
            # adding in the numbers that is smaller than the current number from the biggest to the smallest
            for i in seq[currentIndex-1::-1]:

                temp.append(i)


        # a for loop to add in the current number and numbers smaller than the current number into temp which is an empty list from the biggest to the smallest
        if direction=="down":
            for i in seq[currentIndex::-1]:
                temp.append(i)
            # adding the 0 to the temp list, when the line have reach to the edge
            temp.append(first)
            # adding in the numbers that is bigger than the current number
            for i in seq[currentIndex+1:]:

                temp.append(i)

        return temp

    def generateSCAN(self):
        # get the sequence stated in disk.ini to seq
        seq = self.dp.getSequence()
        # get the current stated in disk.ini to curr
        curr=self.dp.getCurrent()
        # get the previous stated in disk.ini to pre
        pre=self.dp.getPrevious()
        # get the total number of cylinders stated in disk.ini
        last=self.dp.getCylinders()-1
        # calling the method to arrange the sequence for SCAN and then passing the return value to print sequence method
        self.printSequence("SCAN", self.arrangeSCAN(curr,seq,pre,last))


    def generateAnalysis(self):
        # calls generate SCAN
        self.generateSCAN()



