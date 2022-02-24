text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

alph_en = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"

def ceaser(msg, off, alph):
    itog = ''
    for i in msg:
        mesto = alph.find(i)
        new_mesto = mesto + off
        if i in alph:
            itog += alph[new_mesto]
        else:
            itog += i
    print(itog)

ceaser(text.upper(), 2, alph_en)
