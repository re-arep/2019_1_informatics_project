from vpython import*

import random as rd


def DNA(length):

    neclt = ["A", "T", "G", "C"]
    dnau = str()
    dnad = str()
    length = length

    for i in range(length):
        dnau += rd.choice(neclt)

    for j in range(len(dnau)):
        if dnau[j] == "A":
            dnad += "T"
        elif dnau[j] == "T":
            dnad += "A"
        elif dnau[j] == "G":
            dnad += "C"
        else:
            dnad += "G"

    return dnau, dnad


#A is red, G is blue, C is yellow, T is green, U is purple, DNA is Box
A = box(pos=vector(0, 0, 0), length = 1, height = 1, width = 1, color = color.red)
A.visible = False
G = box(pos=vector(1, 0, 0), length = 1, height = 1, width = 1, color = color.blue)
G.visible = False
C = box(pos=vector(2, 0, 0), length = 1, height = 1, width = 1, color = vec(1,1,0))
C.visible = False
T = box(pos=vector(3, 0, 0), length = 1, height = 1, width = 1, color = color.green)
T.visible = False




#RNA is sphere
Ar = sphere(pos=vector(0, 0, 0), radius = 0.5, color = color.red)
Ar.visible = False
Gr = sphere(pos=vector(1, 0, 0), radius = 0.5, color = color.blue)
Gr.visible = False
Cr = sphere(pos=vector(2, 0, 0), radius = 0.5, color = vec(1,1,0))
Cr.visible = False
Ur = sphere(pos=vector(3, 0, 0), radius = 0.5, color = vec(0.4, 0.2, 0.6))
Ur.visible = False



#DNA set
p1 = vec(0, 0, 0)
p2 = vec(0, -2, 0)
dnau = ['A', 'G', 'T', 'C']
dnad = ['T', 'C', 'A', 'G']

#DNA generator
for i in dnau:
    if i == 'A':
        Acopy = A.clone(pos = p1)
        Acopy.visible = True
    if i == 'G':
        Gcopy = G.clone(pos = p1)
        Gcopy.visible = True
    if i == 'C':
        Ccopy = C.clone(pos = p1)
        Ccopy.visible = True
    if i == 'T':
        Tcopy = T.clone(pos = p1)
        Tcopy.visible = True
    p1.x += 1

for i in dnad:
    if i == 'A':
        Acopy = A.clone(pos = p2)
        Acopy.visible = True
    if i == 'G':
        Gcopy = G.clone(pos = p2)
        Gcopy.visible = True
    if i == 'C':
        Ccopy = C.clone(pos = p2)
        Ccopy.visible = True
    if i == 'T':
        Tcopy = T.clone(pos = p2)
        Tcopy.visible = True
    p2.x += 1



#RNA set
rnau = ['G', 'A', 'C', 'U']
rnad = ['A', 'G', 'U', 'C']

ds = 4
num = ds #starting point
ps = len(rnau)-1

p3 = vec(ps, 2, 0)
p4 = vec(0, -4, 0)



#RNA generator
for k in rnau:
    rate(5)
    if k == 'A':
        Arcopy = Ar.clone(pos = p3)
        Arcopy.visible = True
    if k == 'G':
        Grcopy = Gr.clone(pos = p3)
        Grcopy.visible = True
    if k == 'C':
        Crcopy = Cr.clone(pos = p3)
        Crcopy.visible = True
    if k == 'U':
        Urcopy = Ur.clone(pos = p3)
        Urcopy.visible = True
    p3.x -= 1

for k in rnad:
    rate(5)
    if k == 'A':
        Arcopy = Ar.clone(pos = p4)
        Acopy.visible = True
    if k == 'G':
        Grcopy = Gr.clone(pos = p4)
        Grcopy.visible = True
    if k == 'C':
        Crcopy = Cr.clone(pos = p4)
        Crcopy.visible = True
    if k == 'U':
        Urcopy = Ur.clone(pos = p4)
        Urcopy.visible = True
    p4.x += 1
