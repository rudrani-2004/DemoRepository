##Write a python function which will take user input as a number and 
### Will print the table of that number.

def table(num):
    for i in range(1,11):
        print(f"{num}*{i}={num*i}")
        i=i+1
no=int(input("Enter the number: "))
table()
