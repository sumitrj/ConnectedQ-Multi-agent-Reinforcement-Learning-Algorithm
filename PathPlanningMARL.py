#!/usr/bin/env python
# coding: utf-8

# # MARL: Path planning for Swarm Robotics
# 
# # lnitializing Field 
# 

# In[ ]:


import torch
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from IPython.display import HTML
from itertools import permutations
import random
print("GPU used: ", torch.cuda.get_device_name(0))


# # Specifications

# In[ ]:


E = 5 # Number of Episodes
R = 5 # Field of View is of radius units
L = 250 # Length of the total Area 
B = 200 # Breadth of the total Area
N = 2 # Number of Bots
M = 4 # Number of points
Di = (L**2 + B**2)**0.5 # Diagonal Length
G = 0.7 # Gamma=Learning Rate


# # Initializing Locations

# In[ ]:


def spawn(N,L,B):
    locs = {'x':torch.randn(N),'y':torch.randn(N)}
    
    for t in locs['x']:
        if(t<0):
            t*=-1
        if(t<1):
            t*=L
        else:
            t*=10

    for t in locs['y']:
        if(t<0):
            t*=-1
        if(t<1):
            t*=B
        else:
            t*=10
    locs = pd.DataFrame(locs)
    return locs


# # Function to Display Map

# In[ ]:


def ShowMap(locBots,locDests,status):
    print("______________________State ",status,"______________________")
    beacons()
    plt.scatter(locBots['x'],locBots['y'],c = 'red')
    plt.scatter(locDests['x'],locDests['y'],c = 'green')
    plt.title('Field Simulation')
    plt.xlabel('Length')
    plt.ylabel('Breadth')
    
def beacons():
    plt.scatter(np.array([0,0,250,250]),np.array([0,200,0,200]),c = 'black')


# In[ ]:


Bots = spawn(N,L,B)
Dests = spawn(M,L,B) 
ShowMap(Bots,Dests,0)


# # Location of Bots

# In[ ]:


Bots.head()


# # Location of Destinations 

# In[ ]:


Dests.head()


# # Function to Limit Field of View

# In[ ]:


def inrange(r,j,s=1):
    e = []
    for i in range(len(Dests.values)):
        if(dist(Dests.values[i][0],Dests.values[i][1],Bots.values[j][0],Bots.values[j][1]))<=r:
            e.append(i)
    
    if(s==1):
        beacons()
        for k in e:
            plt.scatter(Dests.values[k][0],Dests.values[k][1],c = 'blue')

        plt.scatter(Bots.values[j][0],Bots.values[j][1], c = 'red')
        plt.title('Visible Destinations for Bot '+ str(j))
        plt.xlabel('Length')
        plt.ylabel('Breadth')

    return e 

def dist(x1,y1,x2,y2):
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

def distance(a,b):
    return(dist(Dests.iloc[a]['x'],Dests.iloc[a]['y'],Dests.iloc[b]['x'],Dests.iloc[b]['y']))


# # Penalty Function

# In[ ]:


def penalty(a,b,Di):
    s = 0
    for i in range(len(a)):
        s+=distance(a[i],b[i])
    return s/(Di*len(a))


# # Covered Points

# In[ ]:


Covered = set()


# # State Space

# In[ ]:


def StateSpace(M,N):
    return(list(permutations(np.arange(M),N)))    


# In[ ]:


len(StateSpace(M,N))


# # Play Episode

# In[ ]:


def PlayEpi(x):
    ShowMap()
    


# In[ ]:


def ShowMap(Bot,Dest,status):
    print("______________________State ",status,"______________________")
    beacons()
    lbots = [locBots.iloc(i) for i in Bot]
    ldest = [locBots.iloc(i) for i in Bot]
    
    plt.scatter(locBots['x'],locBots['y'],c = 'red')
    plt.scatter(locDests['x'],locDests['y'],c = 'green')
    plt.title('Field Simulation')
    plt.xlabel('Length')
    plt.ylabel('Breadth')


# In[ ]:





# In[ ]:


Q = torch.zeros(len(StateSpace(M,N)),len(StateSpace(M,N)))


# In[ ]:


Q


# # Training

# In[ ]:


scores = []
policies = []


# In[ ]:


AllPoints = set([x for x in range(M)])
AllPoints


# In[ ]:


def NextState(visited):
    
    visited = set(visited)
    x = random.randint(0,len(StateSpace(M,N))-1)
    x = StateSpace(M,N)[x]
    if(set(x).issubset(visited)):
        return NextState(visited)
    else:
        return x


# In[ ]:


for i in range(E):
    
    visited = set()
    initial_state_index = random.randint(0,len(StateSpace(M,N))-1)
    ep_length = 0
    score  = 0
    
    while(AllPoints!=visited):
        
        initial_state = StateSpace(M,N)[initial_state_index]
        visited = visited.union(set(initial_state))
        next_state = NextState(visited)
        initial_state = next_state
        
        ep_length+=1
        
    print('Episode Length = ', ep_length)
    print(score)
    scores.append(score)


# # Policy Making

# In[ ]:


def NextStateByQ(Initial_State):
    s = 0
    for i in range ( length ( Q[Initial_State] ) ):
        if(Q[Initial_State][i]<Q[Initial_State][m]):
            s = i
    return StateSpace[s]


# In[ ]:


Initial_State = < As given in the input >
current_state = Initial_State 
Visited = {} # Set of Visited Points 
Visited = Union( Visited, set( current_state ) ) 
policy = [] # Sequence of States forming the policy for the considered episode
EpisodePenalty = 0 


# In[ ]:


while( AllPoints.issuperset(Visited) ): 
    next_state = NextStatebyQ( Visited ) 
    policy.append(next_state) 
    Visited = Union( Visited , set(next_state) ) 
    EpisodePenalty = EpisodePenalty + Penalty(current_state, next_state)
    Q[current_state][next_state] = Penalty(current_state, next_state) + G*max(Q[next_state]) current_state = next_state scores.append(EpisodePenalty) policies.append(policy)


# In[ ]:


policy


# In[]:
initial_state_index = random.randint(0,len(StateSpace(M,N))-1)
initial_state = StateSpace(M,N)[initial_state_index]
policy = []
visited = []
AllPoints = [x for x in range(M)]

for k in range(2):
    
    for i in initial_state:
        visited.append(i)
    
    policy.append(initial_state)
    next_state = NextState(visited)
    initial_state = next_state   
    
