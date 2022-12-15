# In the name of god

# Linear Congruential Generator 
# LCG

# Mohammad Mahdi Shafiqi
# Computer science student 
# Student at Gilan University, Iran
# Computer Simulation course of 1401

def LCG(seed,a,b,Period):
    iteration=0
    u=[]
    while iteration<Period:
        # print('n_' ,iteration,'=', seed)
        n=(a*seed+b)%Period
        seed=n
        u.append(n/Period) 
        iteration+=1
    return u

print(LCG(7,3,5,11))
