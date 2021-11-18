import numpy as np
import random 

def DE(fobj, bound, dimensions, mut=0.8, crossp=0.7, popsize=15, its=1000):
    pop = np.random.rand(popsize, dimensions)
    diff = abs(min(bound) - max(bound))
    pop_denorm = min(bound) + pop * diff
    fitness = np.asarray([fobj(ind) for ind in pop_denorm])
    best_idx = np.argmin(fitness)
    best = pop_denorm[best_idx]
    for _i in range(its):
        for j in range(popsize):
            idxs = [idx for idx in range(popsize) if idx != j]
            p, q, r = pop[np.random.choice(idxs, 3, replace = False)]
            mutant = np.clip(p + mut * (q - r), 0, 1)
            cross_points = np.random.rand(dimensions) < crossp
            if not np.any(cross_points):
                cross_points[np.random.randint(0, dimensions)] = True
            trial = np.where(cross_points, mutant, pop[j])
            trial_denorm = min(bound) + trial * diff
            f = fobj(trial_denorm)
            if f < fitness[j]:
                fitness[j] = f
                pop[j] = trial
                if f < fitness[best_idx]:
                    best_idx = j
                    best = trial_denorm
    return best, fitness[best_idx]

def func(x):
    return x[0]**2 + x[1]**2 + x[2]**2

bound = [-5, 5]
dimensions = 3
pop = random.randint(5 * dimensions, 10 * dimensions)
iteration = 300
X, result = DE(func, bound, dimensions, popsize=pop, its=iteration)

print('answer that generated by DE in ' + str(bound))
print('x1 = ' + str(X[0]))
print('x2 = ' + str(X[1]))
print('x3 = ' + str(X[2]))
print('fx = x1^2 + x2^2 + x3^2 = ' + str(result))