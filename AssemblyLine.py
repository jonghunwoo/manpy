from dream.simulation.Globals import runSimulation
from dream.simulation.imports import Machine, Source, Exit, Part, Repairman,Queue, Frame, Assembly, Failure

#define the objects of the model
Frame.capacity=4
Sp=Source('SP','Parts', interArrivalTime={'Fixed':{'mean':0.5}}, entity='Dream.Part')
Sf=Source('SF','Frames', interArrivalTime={'Fixed':{'mean':2}}, entity='Dream.Frame')
M=Machine('M','Machine', processingTime={'Fixed':{'mean':1}})
A=Assembly('A','Assembly', processingTime={'Fixed':{'mean':2}})
E=Exit('E1','Exit')

F=Failure(victim=M, distribution={'TTF':{'Fixed':{'mean':60.0}},'TTR':{'Fixed':{'mean':5.0}}})

#define predecessors and successors for the objects
Sp.defineRouting([A])
Sf.defineRouting([A])
A.defineRouting([Sp,Sf],[M])
M.defineRouting([A],[E])
E.defineRouting([M])

def main(test=0):
    # add all the objects in a list
    objectList=[Sp,Sf,M,A,E,F]

    # set the length of the experiment
    maxSimTime=1440.0

    # call the runSimulation giving the objects and the length of the experiment
    runSimulation(objectList, maxSimTime)

    # calculate metrics
    working_ratio_A = (A.totalWorkingTime / maxSimTime) * 100
    working_ratio_M = (M.totalWorkingTime / maxSimTime) * 100

    # print the results
    print "the system produced", E.numOfExits, "frames"
    print "the working ratio of", A.objName, "is", working_ratio_A, "%"
    print "the working ratio of", M.objName, "is", working_ratio_M, "%"

if __name__ == '__main__':
    main()