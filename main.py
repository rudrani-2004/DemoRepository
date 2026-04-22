##Write a python function which will take user input as a number and 
### Will print the table of that number.

def table(no):
    for i in range(1,11):
        print(f"{no}*{i}={no*i}")
num=int(input("Enter the number: "))
table(num)
