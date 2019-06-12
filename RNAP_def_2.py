import random as rd


class RNAP:

    def __init__(self, dna, dna_mode, in_code, fi_code, rna=str()):
        self.in_code = str(in_code)
        self.fi_code = str(fi_code)
        self.dna_mode = dna_mode
        self.dna = dna[self.dna_mode]
        if self.dna_mode == 1:
            reversed(self.dna)
        self.dna_len = len(self.dna)
        self.rna = rna
        self.pos = rd.randrange(self.dna_len)

    def find_in_code(self):
        if self.in_code in self.dna[self.pos:]:
            return self.dna[self.pos:].index(self.in_code)+self.pos
        else:
            return False

    def find_fi_code(self):
        if self.fi_code in self.dna[self.find_in_code():]:
            return self.dna.index(self.fi_code)
        else:
            return False

    def transcription(self):
        fic = self.find_in_code()
        ffc = self.find_fi_code()
        direct = ["3'", "5'"]
        if fic != False and ffc != False:
            for i in range(fic, ffc+len(self.fi_code)):
                if self.dna[i] == "A":
                    self.rna += "U"
                elif self.dna[i] == "T":
                    self.rna += "A"
                elif self.dna[i] == "G":
                    self.rna += "C"
                else:
                    self.rna += "G"
            if self.dna_mode == 1:
                reversed(self.rna)
            else:
                reversed(direct)
            return "DNA mode :"+str(self.dna_mode)+"\n"+"접합 지점 :"+str(self.pos)+"\n"+ \
                   "전사된 RNA :\n"+direct[0]+"->"+self.rna+"->"+direct[1]
        else:
            return "RNA가 합성될 수 없습니다\n"+"DNA mode :"+str(self.dna_mode)+"\n"+"접합 지점 :"+str(self.pos)+ \
                   "\n"+"개시코드존재 :"+str(fic)+"번째,"+"종결코드존재 :"+str(ffc)+"번째"
