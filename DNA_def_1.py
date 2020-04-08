import random as rd


def DNA(length):

    neclt = ["A", "T", "G", "C"]
    dicneclt = {"A": "T", "T": "A", "G": "C", "C": "G"}
    dnau = str()
    dnad = str()
    length = length

    for i in range(length):
        k = rd.choice(neclt)
        dnau += k
        dnad += dicneclt[k]

    return dnau, dnad


'''
dna = DNA()
print("3'-> " + dna[0] + " ->5'")
print("5'<- " + dna[1] + " <-3'")
'''
