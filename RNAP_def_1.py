import random as rd


def RNAP(st, stmode, tgcode, ficode):
    """
    :param st: dna
    :param stmode: dna 0(0 mean's up and it is 3 -> 5) or 1(1 mean's down and it is 5 -> 3)
    :param stlen: dna length
    :param tgcode: rna initiation code(its length is 3)
    :param ficode: rna termination code(its length is 3)
    :return: rna
    """
    cnt = 0
    dnaline = []
    stmode = stmode

    if stmode == 0:
        dnaline += st
    else:
        dnaline += reversed(st)

    stlen = len(st)
    which = rd.randrange(stlen)
    bpwhich = str()
    in_code = tgcode
    fi_code = ficode
    in_dn_str = ''
    fn_dn_str = ''
    dn_str = ''
    rn_str = ''
    in_code_ext = False
    fi_code_ext = False

    while fn_dn_str != fi_code and (which+1) != stlen:
        while in_dn_str != in_code and which < stlen:
            if (which+1) == stlen:
                bpwhich = "None"
                break
            in_dn_str += dnaline[which]
            if len(in_dn_str) > 3:
                in_dn_str = in_dn_str[-3:]
            if in_dn_str == in_code:
                break
            which += 1

        if len(in_dn_str) > 3:
            in_dn_str = in_dn_str[-3:]

        if in_dn_str == in_code:
            bpwhich = str(which - 2)
            dn_str += in_dn_str
            fn_dn_str += in_dn_str
            for i in range(len(in_code)):
                if dn_str[i] == "A":
                    rn_str += "U"
                elif dn_str[i] == "T":
                    rn_str += "A"
                elif dn_str[i] == "G":
                    rn_str += "C"
                else:
                    rn_str += "G"
            in_dn_str = str()
            in_code_ext = True

        dn_str += dnaline[which]
        fn_dn_str += dnaline[which]
        if len(fn_dn_str) > 3:
            fn_dn_str = fn_dn_str[-3:]

        if dn_str[-1] == "A":
            rn_str += "U"
        elif dn_str[-1] == "T":
            rn_str += "A"
        elif dn_str[-1] == "G":
            rn_str += "C"
        else:
            rn_str += "G"

        which += 1
        cnt +=1

    if fn_dn_str == fi_code:
        fi_code_ext = True
        for j in range(len(fi_code)):
            if fn_dn_str[j] == "A":
                rn_str += "U"
            elif fn_dn_str[j] == "T":
                rn_str += "A"
            elif fn_dn_str[j] == "G":
                rn_str += "C"
            else:
                rn_str += "G"

    if len(rn_str) >= 6 and in_code_ext is True and fi_code_ext is True:
        if stmode == 0:
            bpwhich2 = "nice"
            return bpwhich, bpwhich2, "3'->" + rn_str + "->5'" + in_code + "-" + str(
                in_code_ext) + "-" + fi_code + "-" + str(fi_code_ext), cnt
        else:
            reversed(rn_str)
            bpwhich2 = stlen - int(bpwhich) + 1
            return bpwhich, bpwhich2, "5'->" + rn_str + "->3'" + in_code + "-" + str(
                in_code_ext) + "-" + fi_code + "-" + str(fi_code_ext), cnt
    else:
        bpwhich2 = 24
        if stmode == 1 and bpwhich == int:
            bpwhich2 = stlen - int(bpwhich) + 1
        return bpwhich, bpwhich2, "RNA가 합성될 수 없습니다 "+"개시코드존재 :"+str(in_code_ext)+", 종결코드존재 :"+str(fi_code_ext), cnt
