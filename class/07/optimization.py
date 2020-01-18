import random

###################################
# random_optimize
###################################

def random_optimize(domain, costf, maxiter=1000):
    '''
    Randomly generate a representation of solution.
    Since there are 6 people, a representation is a vector of 6 tuples.
    Each element of a tuple represents the index of the departure and arrival flight
    of the lists in the 'flights' dictionary.
    '''
    best = 999999999
    bestr = None
    for i in range(0, maxiter):
      # Create a random representation
      #raja - remove 'float'
      rpr = [random.randint( domain[i][0], domain[i][1] )
         for i in range(len(domain))]
    
      # Get the cost
      cost = costf(rpr)
    
      # Compare it to the best one so far
      if cost<best:
         best = cost
         bestr = rpr 
    return bestr  #raja

###################################
# hill_climb
###################################

def hill_climb(domain, costf):
  # Create a random representation
  rpr = [random.randint( domain[i][0], domain[i][1] )
         for i in range(len(domain))]
  # Main loop
  while True:
    # Create list of neighboring solutions
    neighbors=[]
    
    for j in range(len(rpr)):  #raja domain -> rpr
      # One away in each direction
      if rpr[j]>domain[j][0]:           #raja - 1
        neighbors.append(rpr[0:j]+[rpr[j]-1]+rpr[j+1:])
      if rpr[j]<domain[j][1]:           #raja + 1
        neighbors.append(rpr[0:j]+[rpr[j]+1]+rpr[j+1:])

    # See what the best solution amongst the neighbors is
    current = costf(rpr)
    best = current
    for j in range(len(neighbors)):
      cost=costf(neighbors[j])
      if cost<best:
        best=cost
        rpr=neighbors[j]

    # If there's no improvement, then we've reached the top
    if best==current:
      break
  return rpr

###################################
# genetic_optimize
###################################

def genetic_optimize(domain, costf, rpr2sol, popsize=1000, step=1,
                    mutprob=0.5, elite=0.5, maxiter=100): #raja
  # Mutation Operation
  def mutate(vec):
    i=random.randint(0,len(domain)-1)
    if random.random()<mutprob and vec[i]>domain[i][0]: #raja
      return vec[0:i]+[vec[i]-step]+vec[i+1:] 
    elif vec[i]<domain[i][1]:
      return vec[0:i]+[vec[i]+step]+vec[i+1:]
    else:  #raja
      return vec
  
  # Crossover Operation
  # at a random index i segments of the two vectors r1 and r2 are swapped
  # e.g., r1 = [0,2,4,6,8,10,12,14]
  #       r2 = [1,3,5,7,9,11,13,15]
  # crossover could return
  #           [0,2,4,6,8,11,13,15]
  def crossover(r1,r2):
    i=random.randint(1,len(domain)-2)
    return r1[0:i]+r2[i:]

  # Build the initial population
  pop=[]
  for i in range(popsize):
    vec=[random.randint(domain[i][0],domain[i][1]) 
         for i in range(len(domain))]
    pop.append(vec)
  
  # How many winners from each generation?
  topelite=int(elite*popsize)
  
  # Main loop 
  for i in range(maxiter):
    #print(pop)
    #print()
    scores=[(costf(v),v) for v in pop]
    scores.sort()
    ranked=[v for (s,v) in scores]
    
    # Start with the pure winners
    pop=ranked[0:topelite]
    
    # Add mutated and crossovered forms of the winners
    while len(pop)<popsize:
      if random.random()<mutprob:
        # Mutation
        c=random.randint(0,topelite)
        pop.append(mutate(ranked[c]))
      else:
        # Crossover
        c1=random.randint(0,topelite)
        c2=random.randint(0,topelite)
        pop.append(crossover(ranked[c1],ranked[c2]))
    
    # Print current best score
    cost, vec = scores[0]
#    if(i%10==0): print()
#    print( "%6d " % cost,end='',flush=True )
    print( "%4d.  %6.2f >%s<" % (i, cost, rpr2sol(vec)),end='\n',flush=True )
  print()
  return( vec )

###########################################################################
