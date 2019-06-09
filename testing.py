import DNA_def_1 as dna1
import RNAP_def_1 as rnap1
import random as rd
'''
dna_length = 200
mode = rd.randint(0, 1)
tgcode = "ATT"
ficode = "ACT"

dna = dna.DNA(dna_length)
rna = rnap.RNAP(dna[mode], mode, dna_length, tgcode, ficode)

print("3'-> " + dna[0] + " ->5'")
print("5'<- " + dna[1] + " <-3'")
print(mode)
print("결합위치(왼쪽에서부터) :"+rna[0]+"번째"+str(rna[1]))
print(rna[2])
print(rna[3])
'''
dna_length = 200
for i in range(10000):

    mode = rd.randint(0, 1)
    tgcode = "ATG"
    ficode = "GTC"
    dna = dna1.DNA(dna_length)
    rna = rnap1.RNAP(dna[mode], mode, tgcode, ficode)

    if rna[2][0] != "R":

        print("3'-> " + dna[0] + " ->5'")
        print("5'<- " + dna[1] + " <-3'")
        print(mode)
        print("결합위치(왼쪽에서부터) :" + rna[0] + "번째" + str(rna[1]))
        print(rna[2])
        print(rna[3])
