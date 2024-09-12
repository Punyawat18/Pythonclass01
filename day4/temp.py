def main():
    userinput = input("unit to convert + temp + unit convert into sep with space(C F K R)")
    idk = userinput.split()
    if(len(idk) != 3 or check1(idk) == False or check2(idk) == False or (idk[0] == idk[2])):
        print("invalid input")
        quit()
    temp = float(idk[1])
    newtemp = 0
    if(idk[0] == "C" and idk[2] == "F"):
        newtemp = CtoF(temp)
    elif(idk[0] == "C" and idk[2] == "K"):
        newtemp = CtoK(temp)
    elif(idk[0] == "C" and idk[2] == "R"):
        newtemp = CtoR(temp)
    elif(idk[0] == "F" and idk[2] == "C"):
        newtemp = FtoC(temp)
    elif(idk[0] == "K" and idk[2] == "C"):
        newtemp = KtoC(temp)
    elif(idk[0] == "R" and idk[2] == "C"):
        newtemp = RtoC(temp)   
    elif(idk[0] == "F" and idk[2] == "K"):
        newtemp = CtoK(FtoC(temp))
    elif(idk[0] == "F" and idk[2] == "R"):
        newtemp = CtoR(FtoC(temp))
    elif(idk[0] == "K" and idk[2] == "F"):
        newtemp = CtoF(KtoC(temp))
    elif(idk[0] == "K" and idk[2] == "R"):
        newtemp = CtoR(KtoC(temp))
    elif(idk[0] == "R" and idk[2] == "F"):
        newtemp = CtoF(RtoC(temp))
    elif(idk[0] == "R" and idk[2] == "K"):
        newtemp = CtoK(RtoC(temp))
    print(newtemp, idk[2])

def check1(old):
    if((old[0] == "C") or (old[0] == "F") or (old[0] == "K") or (old[0] == "R")):
        return(True)
    else:
        return(False)
    
def check2(old):
    if((old[2] == "C") or (old[2] == "F") or (old[2] == "K") or (old[2] == "R")):
        return(True)
    else:
        return(False)
    
    
def CtoF(c):
    f = ((9 / 5) * c) + 32
    return(f)

def CtoK(c):
    k = c + 273.15
    return(k)

def CtoR(c):
    r = (c * 1.8) + 491.67
    return(r)


def FtoC(f):
    c = (f - 32) * (5 / 9)
    return(c)


def KtoC(k):
    c = k - 273.15
    return(c)


def RtoC(r):
    c = (r * (5 / 9)) - 273.15
    return(c)

main()


    
