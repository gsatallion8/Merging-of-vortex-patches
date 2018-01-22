
# coding: utf-8

# In[31]:

class vortexParticle:
    def __init__(self, z=0.0+0.0j, gamma=0.0, r=0.1):
        self.z=z
        self.gamma=gamma
        self.v=0.0+0.0j
        self.r=r
    def Set_z(self,z):
        self.z=z
    def Set_gamma(self,gamma):
        self.gamma=gamma
    def vel(self,z):
        if(abs(z-self.z)<self.r):
            return (self.gamma)*(z-self.z)*(1j)/(2*3.14159*(self.r)*(self.r))
        else:
            return (self.gamma)*(1j)/(2*3.14159*(z-self.z).conjugate())


# In[32]:

import numpy as np


# In[33]:

with open('VortexMerging_40.txt') as f:
    Data = []
    for line in f:
        line = line.split()
        if line:
            line = [float(x) for x in line]
            Data.append(line)
n=Data[0][0]
dt=Data[0][1]
nSteps=Data[0][2]
i=1
vp=[]
while i<n+1:
    vp.append(Data[i])
    i+=1


# In[34]:

n=int(n)
nSteps=int(nSteps)


# In[35]:

Patch=np.empty((nSteps,n),dtype=object)


# In[36]:

i=0
a=0.1
while i<n:
    Patch[0,i]=vortexParticle(vp[i][1]+vp[i][2]*1j,vp[i][0],a)
    i+=1


# In[37]:

t=0
while t<nSteps-1:
    i=0
    while i<n:
        j=0
        while j<n:
            Patch[t,i].v+=Patch[t,j].vel(Patch[t,i].z)
            j+=1
        Patch[t+1,i]=vortexParticle(Patch[t,i].z+Patch[t,i].v*dt,Patch[t,i].gamma,Patch[t,i].r)
        i+=1
    t+=1


# In[38]:

import matplotlib.pyplot as plt


# In[ ]:

t=0
while t<nSteps:
    i=0
    fig=plt.figure()
    plt.xlim(-5,5)
    plt.ylim(-5,5)
    while i<n/2:
        plt.scatter(Patch[t,i].z.real,Patch[t,i].z.imag,color='r')
        i+=1
    while i<n:
        plt.scatter(Patch[t,i].z.real,Patch[t,i].z.imag,color='b')
        i+=1
    s="VortexMerge_%d.png"%t 
    fig.savefig(s)
    plt.close(fig)
    t+=nSteps/1000


# In[ ]:



