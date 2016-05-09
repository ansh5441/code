import pylab
def possible_mean(L):
    return sum(L)/len(L)

def possible_variance(L):
    mu = possible_mean(L)
    temp = 0
    for e in L:
        temp += (e-mu)**2
    return temp / len(L)

x =[6,7,11,12,13,15]
print sum(x)/len(x)
print possible_mean(x)
print pylab.var(x)
print possible_variance(x)