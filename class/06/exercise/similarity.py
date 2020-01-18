import math

###########################################################################
# Euclidean distance
###########################################################################

# Returns a distance-based similarity score for p1 and p2
def euclidean_distance( prefs, p1, p2 ):
    # Get the list of shared_items
    si={}
    for item in prefs[p1]: 
      if item in prefs[p2]: si[item]=1

    # if they have no ratings in common, return 0
    if len(si)==0: return 0

    # Add up the squares of all the differences
    sum_of_squares=sum([pow(prefs[p1][item]-prefs[p2][item],2) 
                        for item in prefs[p1] if item in prefs[p2]])

    return 1/(1+sum_of_squares)
#  return 1/(1+sqrt(sum_of_squares))

###########################################################################
# Pearson correlation
###########################################################################

# Returns the Pearson correlation coefficient for p1 and p2
def pearson( prefs, p1, p2 ):
    # Get the list of mutually rated items
    si={}
    for item in prefs[p1]: 
      if item in prefs[p2]: si[item]=1
  
    # if they are no ratings in common, return 0
    if len(si)==0: return 0
  
    # Sum calculations
    n=len(si)
    
    # Sums of all the preferences
    sumX=sum([prefs[p1][it] for it in si])
    sumY=sum([prefs[p2][it] for it in si])
    
    # Sums of the squares
    sumXSq=sum([pow(prefs[p1][it],2) for it in si])
    sumYSq=sum([pow(prefs[p2][it],2) for it in si]) 
    
    # Sum of the products
    sumXY=sum([prefs[p1][it]*prefs[p2][it] for it in si])
    
    # Calculate r (Pearson score)
    num=sumXY-(sumX*sumY/n)
    den=math.sqrt((sumXSq-pow(sumX,2)/n)*(sumYSq-pow(sumY,2)/n))
    if den==0: return 0
  
    r=num/den
  
    return r

###########################################################################
