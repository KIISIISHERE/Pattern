rows=int(input("   Enter the number of rows:"))
number=1
#outer loop for number of rows
for i in range(1,rows+1):
    for n in range(1,i+1):
        print(number,end='')
        number=number+1
    print()