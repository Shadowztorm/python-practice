sum=0
ch=64       # 65 is ASCII value for 'A', Need to use ASCII for alphabets
no_rows=int(input('Enter No. of rows: '))
typ=int(input("Select a type of pattern:\n 1. Triangle \n 2. Inverted triangle\n 3. Mix triangle\n 4. Row numbers in triangle\n 5. Column numbers in triangle\n 6. Alphabets in triangle\n 7. Alphabets in ascending triangle\n 8. sum of no. in triangle\n"))
# triangle
if typ==1:
    for row in range(1,no_rows+1):
        for column in range(1,row+1):
            print("*",  end=" ")
        print()

# inverted triangle
elif typ==2:
    for row in range(no_rows,0,-1):
        for column in range(1,row+1):
            print("*",end=" ")
        print()

# mix triangle
elif typ==3:
    for row in range(1,no_rows+1):
        for column in range(1,row+1):
            print("*",  end=" ")
        print()
    for row in range(no_rows-1,0,-1):
        for column in range(1,row+1):
            print("*",end=" ")
        print()
# row numbers in triangle
elif typ==4:
    for row in range(1,no_rows+1):
        for column in range(1,row+1):
            print(row,  end=" ")
        print()

# column numbers in triangle
elif typ==5:
    for row in range(1,no_rows+1):
        for column in range(1,row+1):
            print(column,  end=" ")
        print()

# Alphabets in triangle
elif typ==6:
    for row in range(1,no_rows+1):
        for column in range(1,row+1):
            print("{0}".format(chr(ch+column)),  end=" ")
        print()
# Alphabets in ascending triangle
elif typ==7:
    for row in range(1,no_rows+1):
        for column in range(1,row+1):
            ch=ch+1
            print("{0}".format(chr(ch)),  end=" ")
        print()

# sum of no. in triangle
elif typ==8:
    for row in range(1,no_rows+1):
        for column in range(1,row+1):
            sum=sum+1
            print("{0}".format(sum),  end=" ")
        print()

else:
    print("invalid type")
