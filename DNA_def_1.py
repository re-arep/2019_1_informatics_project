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


'''
dna = DNA()
print("3'-> " + dna[0] + " ->5'")
print("5'<- " + dna[1] + " <-3'")
'''