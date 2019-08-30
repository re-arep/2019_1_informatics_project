from vpython import* #vpython 을 import
import DNA_def_1 as dna1 #위의 코드에서 dna 함수 불러오기
import RNAP_def_3 as rnap3 # 위의 코드에서 rna 함수 불러오기
import random as rd 

print("rna transciption start y or n :", end='')
inp = input() # 여기서 Y 입력 시 전사 시작
if inp == 'y':
    while True:
        dna_length = 50 #DNA 길이 50
        mode = rd.randint(0, 1) 
        tgcode = "ATG" #전사 시작 인식부분
        ficode = "GTC" #전사 종결 인식부분
        dna = dna1.DNA(dna_length) #실행
        rna = rnap3.RNAP(dna, mode, tgcode, ficode) #실행
        rrna = rna.transcription() #실행

        if rrna != False:
            rrnaf = rrna[3]

            #A is red, G is blue, C is yellow, T is green, U is purple, DNA is Box
            A = box(pos=vector(0, 0, 0), length = 1, height = 1, width = 1, color = color.red) #A 모양 지정
            A.visible = False # 복사해서 붙이기 위하여 원본을 안보이게 해놓음
            G = box(pos=vector(1, 0, 0), length = 1, height = 1, width = 1, color = color.blue) #G 모양 지정
            G.visible = False # 복사해서 붙이기 위하여 원본을 안보이게 해놓음
            C = box(pos=vector(2, 0, 0), length = 1, height = 1, width = 1, color = vec(1,1,0)) #C 모양 지정
            C.visible = False # 복사해서 붙이기 위하여 원본을 안보이게 해놓음
            T = box(pos=vector(3, 0, 0), length = 1, height = 1, width = 1, color = color.green) #T 모양 지정
            T.visible = False # 복사해서 붙이기 위하여 원본을 안보이게 해놓음


            #RNA is sphere 
            Ar = sphere(pos=vector(0, 0, 0), radius = 0.5, color = color.red) # RNA 중 A의 모양 지정
            Ar.visible = False
            Gr = sphere(pos=vector(1, 0, 0), radius = 0.5, color = color.blue) # RNA 중 G의 모양 지정
            Gr.visible = False
            Cr = sphere(pos=vector(2, 0, 0), radius = 0.5, color = vec(1,1,0)) # RNA 중 C의 모양 지정
            Cr.visible = False
            Ur = sphere(pos=vector(3, 0, 0), radius = 0.5, color = vec(0.4, 0.2, 0.6)) # RNA 중 U의 모양 지정
            Ur.visible = False

            #DNA set
            p1 = vec(0, 0, 0)  # 시작지점
            p2 = vec(0, -6, 0) # 시작지점
            dnau = dna[0] # 염기서열
            dnad = dna[1] # 염기서열

            #DNA generator
            for i in dnau: #서열을 인식함
                if i == 'A': #인식한 서열이 A일때 복제한 후 가시화함
                    Acopy = A.clone(pos = p1)
                    Acopy.visible = True
                if i == 'G': #인식한 서열이 G일때 복제한 후 가시화함
                    Gcopy = G.clone(pos = p1)
                    Gcopy.visible = True
                if i == 'C': #인식한 서열이 C일때 복제한 후 가시화함
                    Ccopy = C.clone(pos = p1)
                    Ccopy.visible = True
                if i == 'T': #인식한 서열이 T일때 복제한 후 가시화함
                    Tcopy = T.clone(pos = p1)
                    Tcopy.visible = True
                p1.x += 1 # 위치 배치

            for i in dnad:
                if i == 'A': #인식한 서열이 A일때 복제한 후 가시화함
                    Acopy = A.clone(pos = p2)
                    Acopy.visible = True
                if i == 'G': #인식한 서열이 G일때 복제한 후 가시화함
                    Gcopy = G.clone(pos = p2)
                    Gcopy.visible = True
                if i == 'C': #인식한 서열이 C일때 복제한 후 가시화함
                    Ccopy = C.clone(pos = p2)
                    Ccopy.visible = True
                if i == 'T': #인식한 서열이 T일때 복제한 후 가시화함
                    Tcopy = T.clone(pos = p2)
                    Tcopy.visible = True
                p2.x += 1 #위치 배치

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
