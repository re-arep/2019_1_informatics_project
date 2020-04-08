

while fn_dn_str != fi_code and which != stlen:

    if in_dn_str != in_code:
        while True:
            in_dn_str += dnaline[which]
            if len(in_dn_str) > 3:
                in_dn_str = in_dn_str[-3:]
            if (which + 1) == stlen:
                bpwhich = "None"
                break
            which += 1
    else:
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
    cnt += 1

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


if len(in_dn_str) > 3:
    in_dn_str = in_dn_str[-3:]


