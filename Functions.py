import numpy as np

# evaluates fitness of population
def eval_fit(pop):
    fit_vals = []
    for i in range(len(pop)):
        fit_vals.append(np.sum(pop[i]))
        
    return np.array(fit_vals)

# ranks population
def rank_pop(pop):
    ranked =  [ pop[i] for i in np.argsort(-eval_fit(pop))]
    return ranked

# crossovers
def cross_pop(pop,size, n):
    new_pop = []
    for i in range(n):
        for j in range(i,n):
            x = np.random.randint(low=int(size/4),high=3*int(size/4)) # crossover point between 1/4 and 3/4
            new_pop.append(np.concatenate([pop[i][:x],pop[j][x:]]))
    return new_pop

# mutations
def mut_pop(pop,size, k):       # 1/k is prob of mutating an individual
    for i in range(len(pop)):
        x = np.random.randint(0,k)
        if(x==0):
            y = np.random.randint(0,size)
            pop[i][y] = (pop[i][y]+1) %2
    return pop