def getMyNumber():
    for i in range(1,1001):
        #First Test: Does the number have 2 more digits?
        if(len(str(i))>2):
            #Second Test: Is it a prime?
            factors=0
            for j in range(1,i+1):
                if(i%j==0):
                    factors+=1
            if(factors==2):
                #Third Test: The number does NOT contain a 1 or 7 in it.
                if(str(i).find("1") == -1 and str(i).find("7") == -1):
                    #Fourth Test: The sum of all of the digits is less than or equal to 10.
                    sum=0
                    num=str(i)
                    for digit in num:
                        sum+=int(digit)
                    if(sum<=10):
                        #Fifth Test: The first two digits add up to be odd.
                        if((int(num[0])+int(num[1]))%2!=0):
                            #Sixth Test: The second to last digit is even and greater than 1
                            if(int(num[-2])%2==0 and int(num[-2])>1):
                                #Seventh Test: The last digit is equal to how many digits are in the number.
                                if((int(num[len(num) - 2]) % 2 == 0 and (int(num[len(num) - 2]) > 1))):
                                    return i


print("I found the number to be",getMyNumber(),"!")