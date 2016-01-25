import numpy
import random
import matplotlib.pyplot as plt


class SimpleVirus(object):

    def __init__(self, maxBirthProb, clearProb):


        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb

    def doesClear(self):

        patientProb = random.random()
        if patientProb < self.clearProb:
            return True
        else:
            return False

    
    def reproduce(self, popDensity):

        patientProb = random.random()
        if patientProb < self.maxBirthProb * (1 - popDensity):
            offspring = SimpleVirus(self.maxBirthProb, self.clearProb)
            return offspring
        else:
            return None
                
class SimplePatient(object):

    def __init__(self, viruses, maxPop):

        self.viruses = viruses
        self.maxPop = maxPop


    def getTotalPop(self):

        totalPop = len(self.viruses)
        return totalPop


    def update(self):

        survived = []
        for virus in self.viruses:
            if virus.doesClear() == False:
                survived.append(virus)
        numVirus = len(survived)
        popDensity = float(numVirus/self.maxPop)
        self.viruses = survived
        
        offspringVir = []
        for virus in self.viruses:
            offspringVir.append(virus)
            offspring = virus.reproduce(popDensity)
            if offspring != None:
                offspringVir.append(offspring)
        self.viruses = offspringVir
        return self.getTotalPop()

                        
def runSimulation():

    try:
        numVirus = int(input("Enter the number of viruses initially. Please choose a number greater than zero: \n"))
        maxPop = int(input("Enter the max population in a patient's body. Please choose a number greater than the previous value: \n"))
        maxBirthProb = float(input("Enter the probability the virus can reproduce. Please choose a number between 0 and 1: \n"))
        clearProb = float(input("Enter the probability patient is cured: Please choose a number between 0 and 1: \n"))
        numTrial = int(input("Enter the number of trials. More trials yield a more accurate graph. Number of trials: \n"))

        if numVirus <= 0:
            print ("\n Incorrect input for first variable. Please try again. \n")
            runSimulation()
        if maxPop <= numVirus:
            print ("\n Incorrect input for second variable. Please try again. \n")
            runSimulation()
        if maxBirthProb < 0 or maxBirthProb > 1:
            print ("\n Incorrect input for third variable. Please try again. \n")
            runSimulation()
        if clearProb < 0 or clearProb > 1:
            print ("\n Incorrect input for fourth variable. Please try again. \n")
            runSimulation()
        if numTrial <= 0:
            print ("\n Incorrect input for fifth variable. Please try again. \n")
            runSimulation()
        
        final = None
        timeStep = 30

        for i in range(0, numTrial):
            results = initial(numVirus, maxPop, maxBirthProb, clearProb, timeStep)
            if final == None:
                final = results
            else:
                for j in range(0, len(final)):
                    final[j] += results[j]

        avg = []
        for i in range(0, len(final)):
            avg.append(float(final[i]/numTrial))

        xaxis = []
        for i in range(0, timeStep):
            xaxis.append(i)
        
        plt.plot(xaxis, avg)
        plt.title("Simulation Without Drug")
        plt.xlabel("units of time")
        plt.ylabel("number viruses")
        plt.show()
        
    except ValueError:
        print ("\n Invalid input. Please try again. \n")
        runSimulation()
        
        
def initial(numVirus, maxPop, maxBirthProb, clearProb, timeStep):
    
    virList = []
    for i in range(0, numVirus):
        virList.append(SimpleVirus(maxBirthProb, clearProb))

    patient = SimplePatient(virList, maxPop)

    updateVirNum = []
    for i in range(0, timeStep):
        updateVirNum.append(patient.update())

    return updateVirNum

start = input("Press any key to begin or (n) to end: ")

if not start == 'n':
    runSimulation()
else:
    raise SystemExit
