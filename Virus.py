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

                        
def simulationWithoutDrug(numVirus, maxPop, maxBirthProb, clearProb, numTrial):

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
    plt.xlabel("time steps")
    plt.ylabel("number viruses")
    plt.show()


def initial(numVirus, maxPop, maxBirthProb, clearProb, timeStep):
    
    virList = []
    for i in range(0, numVirus):
        virList.append(SimpleVirus(maxBirthProb, clearProb))

    patient = SimplePatient(virList, maxPop)

    updateVirNum = []
    for i in range(0, timeStep):
        updateVirNum.append(patient.update())

    return updateVirNum

simulationWithoutDrug(10, 1000, 0.9, 0.1, 30)

