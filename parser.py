# Stores events in events[i][j][k]. i = event #, j = particle #, k = particle attributes 

with open("unweighted_events.lhe", "r") as f:
    search = f.readlines()

global events

events = []

cnt = 0

m = 0

for i, line in enumerate(search):

    if "<event>" in line:
      n = 0
      m += 1      
      events.append([])
      j = i + 2 # Skip 2 lines from "<event>"

      while "<mgrwt>" not in search[j] and "<\event>" not in search[j]:
        n += 1
        events[m-1].append([])
        b = search[j].split()
        for k in range(len(b)):
           events[m-1][n-1].append(float(b[k]))
        j += 1
      cnt = cnt + 1


import numpy as np
import random

#Basic Lorentz invariant variables
def Get4mom(a): return np.array([a[9],a[6],a[7],a[8]])
def Fourdot(P1,P2): return P1[0]*P2[0]-P1[1]*P2[1]-P1[2]*P2[2]-P1[3]*P2[3]
def MomSq(P): return Fourdot(P,P)
def InvMass(P): return np.sqrt(MomSq(P))

N = int(input('Number of final state particles: '))

particles = []

for i in range(N):
    s = str(i + 1)
    particles.append(input('particle %s : '))

phasespace = []
for i in range(len(events)):
  for j in range(len(events[i])):
    if events[i][j][0] == particles[0]:
      temp1 = events[i][j]
    elif events[i][j][0] == 15.0:
      temp2 = events[i][j]
    elif events[i][j][0] == 5000001.0:
      temp3 = events[i][j]
    elif events[i][j][0] == -5000001.0:
      temp4 = events[i][j]
  phasespace.append([temp1, temp2, temp3, temp4])
momenta = []
for i in range(len(phasespace)):
  momenta.append([Get4mom(phasespace[i][0]), Get4mom(phasespace[i][1]), Get4mom(phasespace[i][2]), Get4mom(phasespace[i][3])])
