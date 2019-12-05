from scipy.stats import binom


#Find learners
found = False
accuracy = 0
learners = 7 + 1
 
while not found:
    i = learners/2
    if( 1 - binom.cdf(i, learners, .55)) >= .9:
        found = True
        accuracy = (1 - binom.cdf(i, learners, .55))
    else:
        learners += 1

