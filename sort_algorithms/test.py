def rec_Met(n, attemp=0):
    attemp +=1
    print("at: " ,attemp)
    if n<1:
        print("n less than 1")
    else:
        print(n)
        return rec_Met(n-1, attemp)

rec_Met(5)