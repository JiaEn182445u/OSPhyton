from algorithm import FCFSParameter


class FCFSOptimization:
    def __init__(self):
        self.dp = FCFSParameter.FCFSParameter("disk.ini")
        self.generateAnalysis()

    def printSequence(self, name, location):
        curr = 0 #current starting point
        prev = self.dp.getCurrent() #previous point
        total = 0#To show the final head movement of cylinders
        working1 = "" #To show the long working and find the difference in the brackets
        working2 = "" #To show the addition of the working after finding the difference in the brackets
        order = "" #To show the order of the queue in FCFS
        for i in location:
            curr = i #holds the same value as i in this for loop
            total += abs(prev - curr) #Calculation of the previous point subtracting the current point throughtout the whole working
            working1 += "|" + str(prev) + "-" + str(curr) + "|+" #Shows the working that finds the difference of the previous point subtracting the current point
            working2 += str(abs(prev - curr)) + "+" #Shows the addition working after finding the difference between the previous point and the current point
            prev = i #setting prev as i when for loop goes for the next value
        # removes arithmetical operations
        working1 = working1[0:-1]
        working2 = working2[0:-1]
        #adding curren tpoint into the order of sequence
        order = str(self.dp.getCurrent()) + ", " + str(location)[1:-1]
        #Say FCFS for indication
        print(name + "\n====")
        #Say the order of sequence
        print("Order of Access: " + order)
        #Show long calculation
        print("Total distance: " + "\n" + working1 + "\n")
        #Show shortened calculation after finding the difference
        print("= " + working2 + "\n")
        #Show total disk head movement
        print("= " + str(total) + "\n")




    def generateFCFS(self):
         # assign the sequence stated in disk.ini to seq
        seq = self.dp.getSequence()

        #Print FCFS sequence
        self.printSequence("FCFS", seq)




    def generateAnalysis(self):
        #generate FCFS
        self.generateFCFS()
