import DNA_def_1 as dna1
import RNAP_def_2 as rnap2
import random as rd

dna_length = 200
'''
while True:

    mode = rd.randint(0, 1)
    tgcode = "ATG"
    ficode = "GTC"
    dna = dna1.DNA(dna_length)
    rna = rnap2.RNAP(dna, mode, tgcode, ficode)
    rrna = rna.transcription()

    if rrna[0] != "R":

        print("3'-> " + dna[0] + " ->5'")
        print("5'<- " + dna[1] + " <-3'")
        print(rrna)
        break


'''
#mode = rd.randint(0, 1)
tgcode = "ATG"
ficode = "GTC"
#dna = dna1.DNA(dna_length)
mode = 0
dna = ["ATGGTAATGGTAGTCCTGGTCCTG", "TACCATTACCATCAGGACCAGGAC"]
rna = rnap2.RNAP(dna, mode, tgcode, ficode)
rrna = rna.transcription()


print("3'-> " + dna[0] + " ->5'")
print("5'<- " + dna[1] + " <-3'")
print(rrna)
print(rna.find_fi_code())
