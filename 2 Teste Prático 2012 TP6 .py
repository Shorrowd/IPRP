dicio={"XY2002": 10, "AY2011": 30, "ZX2001": 1000, "XY2010": 400, "XY2009": 40}

def quantidade(ref,dicio):
    soma=0
    if len(ref)==6 and ref in dicio.keys():
        for referencia in dicio.keys():
            if referencia[:2]==ref[:2]:
                soma+=dicio[referencia]
    return soma

print(quantidade("XY2002",dicio))