from algorithm import FCFSParameter


class SSTFOptimization:
    def __init__(self):
        self.dp = FCFSParameter.FCFSParameter("disk.ini")
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

    def arrangeSSTF(self, curr, seq):
        # putting seq in temp
        temp = seq[:]
        # create a list called sstf
        sstf = []
        # putting temp in temp 2
        temp2 = temp[:]
        # the value in curr is assigned to a new variable named num.
        num = curr
        for i in temp:
            # setting the highest value in the seq list into the minimum variable
            minimum = max(seq)
            # the value of num is placed in num2
            num2 = num
            for ii in temp2:
                # calculating num2 - ii to find out distance between
                dist = abs(num2 - ii)
                # print("DIST:" + str(dist))
                # if distance between num2 and ii is less than minimum
                if dist < minimum:
                    # ii is assigned to the variable num
                    num = ii
                    # the value of minimum is then updated to dist
                    minimum = dist
                    # print("*here")
            # print("--------------STOP " + str(num) + "---------------")

            # after finding the va;ue that gives the smallest distance(assigned to num), num is then removed from temp2
            temp2.remove(num)

            # and is appended into list sstf , repeat till the for loop ends
            sstf.append(num)
        # after appending the fully sorted sequence into sstf list, return the list
        return sstf

    def generateSSTF(self):
        # assign the sequence stated in disk.ini to seq
        seq = self.dp.getSequence()
        #assign the current number stated in the disk.ini to curr
        curr = self.dp.getCurrent()
        # calling the method to arrange the sequence for sstf and then passing the return value to print sequence method
        self.printSequence("SSTF", self.arrangeSSTF(curr, seq)) #a list called sstf was returned from arrangeSSTF


    def generateAnalysis(self):
        # calls generate sstf
        self.generateSSTF()
