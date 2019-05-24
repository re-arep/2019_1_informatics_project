import random as rd


def DNA():

    neclt = ["A", "T", "G", "C"]
    dnau = str()
    dnad = str()

    for i in range(100):
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


dna = DNA()
print(dna[0])
print(dna[1])