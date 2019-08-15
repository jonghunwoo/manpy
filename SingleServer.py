import dream

from dream.simulation.Globals import runSimulation
from dream.simulation.imports import Machine, Source, Exit, Part, Repairman,Queue, Failure

"""
#define the objects of the model
S=Source('S1','Source',interArrivalTime={'Fixed':{'mean':0.5}}, entity='Dream.Part')
Q=Queue('Q1','Queue', capacity=1)
M=Machine('M1','Machine', processingTime={'Fixed':{'mean':0.25}})
E=Exit('E1','Exit')

#define predecessors and successors for the objects
S.defineRouting(successorList=[Q])
Q.defineRouting(predecessorList=[S],successorList=[M])
M.defineRouting(predecessorList=[Q],successorList=[E])
E.defineRouting(predecessorList=[M])

def main(test=0):
    # add all the objects in a list
    objectList=[S,Q,M,E]
    # set the length of the experiment
    maxSimTime=1440.0
    # call the runSimulation giving the objects and the length of the experiment
    runSimulation(objectList, maxSimTime)
    # calculate metrics
    working_ratio = (M.totalWorkingTime/maxSimTime)*100
    # return results for the test
    if test:
        return {"parts": E.numOfExits,"working_ratio": working_ratio}
    # print the results
    print "the system produced", E.numOfExits, "parts"
    print "the total working ratio of the Machine is", working_ratio, "%"
"""

R=Repairman('R1', 'Bob')
S=Source('S1','Source', interArrivalTime={'Fixed':{'mean':0.5}},
entity='Dream.Part')
M1=Machine('M1','Machine1', processingTime={'Fixed':{'mean':0.25}})
Q=Queue('Q1','Queue')
M2=Machine('M2','Machine2', processingTime={'Fixed':{'mean':1.5}})
E=Exit('E1','Exit')

F1=Failure(victim=M1,
distribution={'TTF':{'Fixed':{'mean':60.0}},'TTR':{'Fixed':{'mean':5.0}}},
repairman=R)
F2=Failure(victim=M2,
distribution={'TTF':{'Fixed':{'mean':40.0}},'TTR':{'Fixed':{'mean':10.0}}},
repairman=R)

S.defineRouting([M1])
M1.defineRouting([S],[Q])
Q.defineRouting([M1],[M2])
M2.defineRouting([Q],[E])
E.defineRouting([M2])


def main(test=0):
    # add all the objects in a list
    objectList = [S, M1, M2, E, Q, R, F1, F2]

    # set the length of the experiment
    maxSimTime = 1440.0

    # call the runSimulation giving the objects and the length of the experiment
    runSimulation(objectList, maxSimTime)

    # calculate metrics
    blockage_ratio = (M1.totalBlockageTime / maxSimTime) * 100
    working_ratio = (R.totalWorkingTime / maxSimTime) * 100

    # return results for the test
    if test:
        return {"parts": E.numOfExits,
                "blockage_ratio": blockage_ratio,
                "working_ratio": working_ratio}

    # print the results
    print "the system produced", E.numOfExits, "parts"
    print "the blockage ratio of", M1.objName, "is", blockage_ratio, "%"
    print "the working ratio of", R.objName, "is", working_ratio, "%"

if __name__ == '__main__':
    main()