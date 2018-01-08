def checkPythogoreanTheorem(a,b,c):
    if(((a**2)==((b**2)+(c**2))) or ((b**2)==((c**2)+(a**2))) or ((c**2)==((a**2)+(b**2)))):
        return "Ohh yeah!"
    else:
        return "Nope."
counter = "y"
while(True):
    if(counter == "n" or counter == "N"):
        break
    elif(counter == "y" or counter == "Y"):
        a,b,c=input("Enter three numbers seperated by a space: ").split()
        a,b,c=int(a),int(b),int(c)
        print("Are these Pythogorean Triplets? "+str(checkPythogoreanTheorem(a,b,c)))
        counter = input("Do you want to continue? (Y/N) ")
    else:
        print("Dude, it was a yes/no question.")
        counter = input("Do you want to continue? (Y/N) ")
