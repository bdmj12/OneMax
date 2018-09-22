from Functions import *
import numpy as np


#size of an individual, i.e. length of the vector
size = 2000

# this is the size of breeding pool and used to generate the population
n=5

# in making this is a triangle number we can breed 
# the top n individuals and get the same size population back
pop_size= sum(range(n+1))

if __name__ == '__main__':

    # creates a population
    pop = []

    for i in range(pop_size):    
        pop.append(np.random.randint(low=0,high=2, size=(size)))

    
    # runs the algorithm and finds an optimum
    m = 0
    mut_prob = 5   # probability of a mutation in a given individual (i.e. 1/mut_prob)
    best_fitn = np.amax(eval_fit(pop))

    while(best_fitn < size and m<1000):
        
        pop = rank_pop(pop)
        pop = cross_pop(pop,size,n)
        pop = mut_pop(pop,size,mut_prob)
    
        print("Generation: " + str(m))
        print(str(best_fitn) + " : " + str(100*best_fitn/size) + "%")
        #print(pop[0])
    
    
        best_fitn = np.amax(eval_fit(pop))
        m=m+1
  
    print("\n")
    print("Completed at generation: " + str(m))
    print("Best fitness is: " + str(100*best_fitn/size) + "%")
    pop = rank_pop(pop)
    print("Best individual is: ")
    print(pop[0])
