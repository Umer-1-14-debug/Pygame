def worrior():
    worrior1=input("What is the name of the first worrior")
    chi1=int(input("What is the chi level of the worrior."))
    ability1=input("Does he has any special abilities.")
    nabilities1=int(input("How many abilities."))
    worrior2=input("Enter the name of the second worrior")
    chi2=int(input("Enter the level of chi for the second worrior"))
    ability2=input("Does he has any abilities")
    nabilities2=int(input("How many abi;ities does he has"))
    if chi1>chi2:
        if ability1=="Yes" and ability2=="Yes":
            if nabilities1>nabilities2:
                print(worrior1," has won")
            else:
                if chi1*3>nabilities2:
                    print(worrior1," has won")
                else:
                    print(worrior2," has won")
        elif ability1=="No" and ability2=="Yes":
            if chi1*3>nabilities2:
                print(worrior1," has won")
            else:
                    print(worrior2," has won")
        elif ability1=="Yes" and ability2=="No":
            if chi2*3>nabilities2:
                print(worrior2," has won")
            else:
                    print(worrior1," has won")
        else:
            print(worrior1," has won")
    else:
        print(worrior2," has won")
worrior()