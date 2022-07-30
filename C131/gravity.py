import pandas as pd
import csv
import math
df=pd.read_csv('main.csv')
data=[]
with open('main.csv',encoding='utf-8') as f:
    csvreader = csv.reader(f)
    for a in csvreader:
        data.append(a)
header = data[0]
planetdata = data[1:]
mass = df['Mass'].tolist()
radius = df['Radius'].tolist()
name = df['Star_name'].tolist()
distance = df['Distance'].tolist()
gravity = []
newMass = []
newRadius = []
newDistance = []
newName = []
G = 6.67*pow(10,-11)
for a in range(1,51,2):
    m = float(mass[a])*1.989e+30
    newMass.append(m)
    r = float(radius[a])*6.957e+8
    newRadius.append(r)
    g = G*m/pow(r,2)
    gravity.append(g)
    d = distance[a]
    newDistance.append(d)
    n=name[a]
    newName.append(n)
newdataframe = pd.DataFrame({'Name':newName,'Radius':newRadius,'Mass':newMass,'Gravity':gravity})
newdataframe.to_csv('calculated.csv')