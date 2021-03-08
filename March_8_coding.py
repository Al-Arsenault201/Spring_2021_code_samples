# coding in class for Monday, March 8 2021

def edit (str,char,index):
    """
This is a function that edits a string by replacing
the character currently at index with a new character.
    parameter:  value passed to the function by the main
      str: the string we want to edit
      char: the new character to insert in the string
      index: where to put that new character
    return: the edited string
"""
    l = []   # a new empty list
    for c in str:
        l.append(c)
    l[index] = char
    new_str = "".join(l)
    return new_str





if __name__ == "__main__":

    # from here down is the main program

    # edit a string
    # using a list
    s = "Baltimore County Public Schools R3open March 1"
    # change that 3 to an e
    #s[33] = 'e'
    """
    l = []
    #split the string so that each letter is an element
    for char in s:
        l.append(char)
    print(l)
    l[33] = 'e'
    new_s = "".join(l)
    print(new_s)
"""
    #suppose I want to do this with another string
    # I need to put the same code in again

    new_s = edit(s, "e", 33)
    print(new_s)

    # do it again with a new string
    y = "New Orleans  Aints"
    new_y = edit(y,'S', 12)
    print(new_y)
