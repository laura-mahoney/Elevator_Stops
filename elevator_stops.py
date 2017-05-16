""" There is an elevator in a building with M floors. This elevator can 
take a max of X people at a time or max of total weight Y. Given that a 
set of people and their weight and the floor they need to stop, how many 
stops has the elevator taken to serve all the people? Consider the elevator 
serves in "first come first serve" basis and the order for the queue can not 
be changed. 

Let Array A be the weight of each person A = [60, 80, 40]. Let 
Array B be the floors where each person needs to be dropped off B = [2, 3, 5].
The building has 5 floors, maximum of 2 persons are allowed in the elevator at 
a time with max weight capacity being 200. For this example, the elevator would 
take total of 5 stops in floors: 2, 3, G, 5 and finally G. M is total amount of floors. 

    >>> calc_elevator_stops([60, 80, 400], [2, 3, 5], 5, 2, 200)
    5

    >>> calc_elevator_stops([60, 80, 20], [2, 2, 2], 5, 3, 200)
    2

    >>> calc_elevator_stops([60, 80, 20], [2, 4, 2], 5, 2, 200)
    5
"""


def calc_elevator_stops(A, B, M, X, Y):
    # write your code in Python 2.7
    

    #this dictionary will hold floor keys/destinations, and an array of people indexes to get off
    passenger_dest = {}
    #weight, elevator, and waiting start at zero and empty. elevator will hold index values of A, people
    # currently on the elevator, waiting holds those who couldn't make it on this ride
    ride_weight = 0
    elevator = []
    waiting = []
    stops = 1 #there will always be one stop because the elevator will come back to ground floor

    
    # for each index of A, start at 0 and go until the length, adding the weight and 
    # and index of A(person) to the elevator list until the capacity and weight limits
    # have been hit
    for person in range(0, len(A)):
            
        if ride_weight + A[person] <= Y and len(elevator) < X:
            elevator.append(person)
            ride_weight += A[person]
            
            #if floor key exists in passenger destination dictionary, add the passenger value to that floor key
            if B[person] in passenger_dest.keys(): 
                passenger_dest[B[person]].append(person) 

            #if the floor key does not exist, add it to the dictionary and assign person index to it
            else:
                passenger_dest[str(B[person])] = [person]

        #if the ride weight or capacity hit max, append the person index to waiting 
        else:
            waiting.append(person)
     


    #loop over the floors starting with 0, ending with M 
    for level in range(0, M+1):

        #if the level is a value in list of B from 0 to len(elevator) (people in elevator), increment the stop
        #and remove the passengers from the elevator list 

        if passenger_dest.has_key(str(level)):

            #increment stops here 
            stops += 1
            to_remove = passenger_dest[str(level)]


            #remove all the passengers from elevator with this level as destination 
            for person in elevator:
                if person in to_remove:
                    elevator.remove(person)

        #if level is not a destination, continue 
        else:
            continue 

    #if there are more people waiting in line, return stops, and add to value of calling the function on the rest of the people waiting
    if len(waiting)>0:
        return stops + calc_elevator_stops(waiting, B[len(elevator)::], M, X, Y)
    #if the line is empty/waiting is empty, return stops 
    else:
        return stops 

                
                    


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YAY!"
                
            
    