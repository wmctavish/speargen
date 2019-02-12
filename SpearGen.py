#SPEARGEN 1.0

#Takes user input of keywords associated with target
kwords = []
def getKwords():
    print('Welcome to SpearGen. Please enter keywords below. To exit, enter blank entry.')
    while True:
        keys = input()
        if keys:
            kwords.append(keys)
        else:
            break
    return kwords

#A list of common passwords for good measure
common_passwords =['password','123456','12345678','1234','qwerty','12345',
                   'baseball','football','letmein','monkey','696969',
                   'abc123','111111','2000','superman','1234567','fuckme',
                   'soccer','fuck','test','pass','hockey',
                   '6969','access','123456789','654321','123123','666666',
                   'hello','computer','1111','121212','secret','asdfgh']

getKwords()

passwords = kwords + common_passwords

# Makes common character swaps ie. 'a' for '@', 'i' for '!', etc.
swapped_all = []
def charSwapAll():
    for k in passwords:
        swap_all = k.replace('a','@').replace('i','!').replace('s','$').replace('o','0').replace('A','@').replace('I','!').replace('S','$').replace('O','0')
        swapped_all.append(swap_all)
    return swapped_all

swapped_a = []
def charSwapA():
    for k in passwords:
        swap_a = k.replace('a','@').replace('A','@')
        swapped_a.append(swap_a)
    return swapped_a

swapped_i = []
def charSwapI():
    for k in passwords:
        swap_i = k.replace('i','!').replace('I','!')
        swapped_i.append(swap_i)
    return swapped_i

swapped_o = []
def charSwapO():
    for k in passwords:
        swap_o = k.replace('o','0').replace('O','0')
        swapped_o.append(swap_o)
    return swapped_o

swapped_s = []
def charSwapS():
    for k in passwords:
        swap_s = k.replace('s','$').replace('S','$')
        swapped_s.append(swap_s)
    return swapped_s

charSwapAll()
charSwapA()
charSwapI()
charSwapO()
charSwapS()
combined_lists = passwords + swapped_all + swapped_a + swapped_i + swapped_o + swapped_s

#Capitalizes every entry
capitalized = []
def capitalize():
    for i in combined_lists:
        cap = i.capitalize()
        capitalized.append(cap)
    return capitalized

capitalize()

lower_and_upper = combined_lists + capitalized

#Appends all numbers up to 9999 to each item
with_nums = []
def num_add():
    for i in lower_and_upper:
        number = 0
        while number <= 9999:
            added = i + str(number)
            with_nums.append(added)
            number = number + 1
    return with_nums

num_add()

grandUnifiedList = with_nums + lower_and_upper
grandUnifiedList = list(set(grandUnifiedList))

def write_dictionary():
    print_option = input('Would you like to output to a .txt file? (Y/N)')
    if print_option[0] in ('Y','y'):
        dictionary = open('myDictionary.txt','w')
        dictionary.write('\n'.join(str(line) for line in grandUnifiedList))
        dictionary.close()
        print('Dictionary has been created')
        return True
    elif print_option[0] in ('N','n'):
        return False
    else:
        return write_dictionary()

write_dictionary()