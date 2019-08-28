import random as rd


class RNAP:

    def __init__(self, dna, dna_mode, in_code, fi_code, rna=str()):
        self.in_code = str(in_code)
        self.fi_code = str(fi_code)
        self.dna_mode = dna_mode
        self.dna = dna[self.dna_mode]
        if self.dna_mode == 0:
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
        if self.fi_code in self.dna[self.find_in_code()+len(self.in_code):]:
            return self.dna.index(self.fi_code)
        else:
            return False

    def transcription(self):
        fic = self.find_in_code()
        ffc = self.find_fi_code()
        direct = ["3'", "5'"]
        if (fic is not False) and (ffc is not False):
            com = {'A': 'T', 'T': 'A', 'G':'C', 'C':'G'}
            complement = lambda x : com[x]
            self.rna += ''.join(list(map(complement, self.dna[fic: ffc+len(self.fi_code)])))
            if self.dna_mode == 0:
                reversed(self.rna)
            else:
                reversed(direct)
            return str(self.dna_mode), str(self.pos), direct[0], self.rna, direct[1]
        else:
            return False
