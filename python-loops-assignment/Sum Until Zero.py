#Create a program that keeps asking the user to enter numbers and adds them to a total. When the user enters 0, stop taking input and print the final sum.

sum = 0

while True:
    num = int(input())
    if num == 0:
        break
    sum += num
    
print(sum)    


