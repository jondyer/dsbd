# optimization.py
# chapter 5 - Programming Collective Intelligence / Toby Segaran
#
# 2015-02-13  Bug fixes  Raja Sooriamurthi

'''
Summary of functions and variables in this module

people
destination
def load_flights(fname='flights.txt'):
def get_minutes(t):
def print_schedule(rpr):
def schedule_cost(rpr):
'''

import time
import random
import math
from pprint import pprint as pp
# use pp( flights ) to see the hash better

people = [('Seymour','BOS'),     # Boston
          ('Franny','DAL'),      # Dallas Love Field
          ('Zooey','CAK'),       # Akron-Canton
          ('Walt','MIA'),        # Miami
          ('Buddy','ORD'),       # Chicago O'hare
          ('Les','OMA')]         # Omaha
# Laguardia
destination='LGA'

flights = {}
# 

def load_flights(fname='flights.txt'):
    '''
    Load the flight schedule from a file.
    Each line of  the file is of the format:

    <departure>, <destination>, <departure time>, <arrival time>, <cost>

    For example: OMA,LGA,6:11,8:31,249
    '''
    for line in open(fname, 'rU'):
        origin, dest, depart, arrive, price = line.strip().split(',')
        flights.setdefault((origin,dest),[])
        # Add details to the list of possible flights
        flights[(origin,dest)].append((depart,arrive,int(price)))
    return flights

# use pp( flights ) to see the hash better

def get_minutes(t):
    '''
    To enable easy time difference calculations
    e.g.,  time between 6:19 and 4:21
    the function get_minutes converts times to number of minutes past midnight 
    e.g. get_minutes( '6:19' ) -> 379
    e.g. get_minutes( '0:00' ) -> 0
    e.g. get_minutes( '23:59' ) -> 1439
    '''
    x = time.strptime(t,'%H:%M')
    return x[3]*60+x[4]

###################################
# print_schedule
###################################

def print_schedule(rpr):
    '''
    Six people in order are: Seymour, Franny, Zooey, Walt, Buddy, and Les 
    A schedule consists of a pair of flights for each person
    origin -> LGA (dest)
    LGA -> origin

    [1,4,3,2,7,3,6,3,2,4,5,3]

    A solution is represented as a list of 6 numbers
    For example Seymour's BOS -> LGA flight is
    the 1st flight in the possible list of flights from BOS -> LGA
    Seymour's flight from LGA -> BOS is the 
    the 4th flight in the possible list of flights from LGA -> BOS

    ** Treat the function as a blackbox
    ** Understand the input/output.
    ** You can omit understanding the details of the implementation
    '''
    for d in range(len(rpr)//2):
        name = people[d][0]
        origin = people[d][1]
        out = flights[(origin,destination)][int(rpr[2*d])]       #raja
        ret = flights[(destination,origin)][int(rpr[2*d+1])]     #raja
        print( '%10s%10s %5s-%5s $%3s %5s-%5s $%3s' % (name,origin,
                                                  out[0],out[1],out[2],
                                                  ret[0],ret[1],ret[2]))

###################################
# schedule_cost
###################################

def schedule_cost(rpr):
    '''
    A 'cost' function only takes -one- argument: a vector of
    numbers that represents the solution.
    Limiting the arity of the cost function to 1 leads to
    some design decisions in dorm.py

    =graybox= helps to understand the details
    '''
    totalprice = 0
    latestarrival = 0
    earliestdep = 24*60
  
    for d in range(len(rpr)//2):
      # Get the inbound and outbound flights
      origin = people[d][1]  
      outbound = flights[(origin,destination)][int(rpr[2*d])]   #raja
      returnf = flights[(destination,origin)][int(rpr[2*d+1])]  #raja
      
      # Total price is the price of all outbound and return flights
      totalprice += outbound[2]
      totalprice += returnf[2]
      
      # Track the latest arrival and earliest departure
      if latestarrival<get_minutes(outbound[1]): latestarrival=get_minutes(outbound[1])
      if earliestdep>get_minutes(returnf[0]): earliestdep=get_minutes(returnf[0])
    
    # Every person must wait at the airport until the latest person arrives.
    # They also must arrive at the same time and wait for their flights.
    totalwait=0  
    for d in range(len(rpr)//2):
        origin = people[d][1]  
        outbound = flights[(origin,destination)][int(rpr[2*d])]    #raja
        returnf = flights[(destination,origin)][int(rpr[2*d+1])]   #raja
        totalwait += latestarrival-get_minutes(outbound[1])
        totalwait += get_minutes(returnf[0])-earliestdep  
  
    # Does this solution require an extra day of car rental? That'll be $50!
    # raja if latestarrival>earliestdep: totalprice+=50
    if earliestdep > latestarrival: totalprice+=50
    
    return totalprice+totalwait

###################################
# domain
###################################

# range of possible values for each person - element of the solution
#  [(0,9), (0,9), (0,9), ... ]

domain = [(0,9)]* len(people)*2   #raja
