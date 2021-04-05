# coding in class from Monday, April 5

# calculate the factorial of some number

#iteratively
"""
number = int(input("Enter a positive integer and we will calculate the factorial"))
fact = 1
for i in range(2,number+1):
    fact *= i
print (number, "Factorial is ", fact)
"""
# this calculates 1 * 2 * 3 * 4 * 5

def recursive_fact(number):
    if number <= 1:  #base case
        return 1  #do not necessarily return to the main program
    else:
        print("number is ", number)
        return(number*recursive_fact(number-1)) # recursive case

if __name__ == "__main__":
    num = int(input("Enter a positive integer and we will calculate its factorial recursively"))
    ans = recursive_fact(num)
    print("The recursive answer is ", ans)