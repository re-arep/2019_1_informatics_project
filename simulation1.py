from vpython import*
import DNA_def_1 as dna1
import RNAP_def_3 as rnap3
import random as rd

print("rna transciption start y or n :", end='')
inp = input()
if inp == 'y':
    while True:
        dna_length = 50
        mode = rd.randint(0, 1)
        tgcode = "ATG"
        ficode = "GTC"
        dna = dna1.DNA(dna_length)
        rna = rnap3.RNAP(dna, mode, tgcode, ficode)
        rrna = rna.transcription()

        if rrna != False:
            rrnaf = rrna[3]

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
            p2 = vec(0, -6, 0)
            dnau = dna[0]
            dnad = dna[1]

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

            ds = 4
            num = ds #starting point
            ps = int(rna.find_in_code())
            if mode == 0:
                p3 = vec(ps, -2, 0)
            else:
                p3 = vec(ps, -4, 0)

            #RNA generator
            for k in rrnaf:
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
                p3.x += 1

            break


