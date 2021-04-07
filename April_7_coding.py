# in-class coding for Wednesday, April 7
def fib(n):
    if n <= 3:
        return n
    else:
        fib = [1, 1]
        for i in range(2, n + 1):
            fib.append(fib[i - 1] + fib[i - 2])
        return (fib[n])

def recursive_fib(n):
    if n <= 3:  # base case
        return n
    else:     # recursive case
        return (recursive_fib(n-1) + recursive_fib(n-2))

# recursive palindrome function

def palindrome(word):
    print ("word is ", word)
    input("hit enter to continue")
    #word is the string that we check
    # we return True if word IS a palindrome
    # we return False if it is not
    if len(word) == 0:   # base case 1
        return True
    elif len(word) == 1:   # base case 2
        return True
    elif word[0] != word[-1]: # base case 3
        return False
    else:                    # recursive case
        new_word = word[1:-1]    # this leaves out the first and last letters
        return (palindrome(new_word))

def efficient_palindrome(word):
    if len(word) <= 1:
        return True
    if word[1] != word[-1]:
        return False
    return(efficient_palindrome(word[1:-1]))


if __name__ == "__main__":
    print (fib(10))
