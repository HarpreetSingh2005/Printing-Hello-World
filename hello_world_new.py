from time import sleep

a=input("Enter any thing: ")

repeat =len(a)
small_alphabets = ('''abcdefghijklmnopqrstuvwxyz1234567890''')
capital_alphabets = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
len_alphabets = len(capital_alphabets)

old=("")
new=("")
time=0.01
print("\n\n")
for i in range (0,repeat):

    letter =  a[i]
    if letter in small_alphabets:
        for j in range(0,len_alphabets):
            print(new,end=(""))
            print(small_alphabets[j],end="\n");sleep(time)
        x=small_alphabets.rfind(letter)
        for y in range(0,x+1):
            print(new,end=(""))
            print(small_alphabets[y],end="\n");sleep(time)
    elif letter in capital_alphabets:
        for j in range(0,len_alphabets):
            print(new,end=(""))
            print(capital_alphabets[j],end="\n");sleep(time)
        x=capital_alphabets.rfind(letter)
        for y in range(0,x+1):
            print(new,end=(""))
            print(capital_alphabets[y],end="\n");sleep(time)
    else:
        print(new,end=(""))
        print(letter,end="\r");sleep(time)
    
    new = new + letter
    

print(new, end="\n\n")