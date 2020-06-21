import random
import string
import numpy as np

# User is prompted to input the number of letters, numbers and special characters
letters_len = int(input('Select the number of letters you would like in your password: '))
numbers_len = int(input('Select the number of numbers you would like in your password: '))
nonLatinChars_len = int(input('Select the number of special characters you would like in your password: '))
#letters_len = 5
password = []
chars = []

# use random to choose a random set of lower and upper case letters
for i in range(letters_len):
    password.append(random.choice(string.ascii_letters))
    chars.append(random.choice(string.ascii_letters))

# use Numpy to choose a random set of numbers
#numbers_len = 4
numbers = np.random.randint(1,10,size=numbers_len)
number_str = [str(n) for n in numbers]

# Define set of special characters and then randomly select them
nonLatinChars = ['-','_','#','*','&']
#nonLatinChars_len = 5
rand_select = list(np.random.randint(0,5,nonLatinChars_len))
print(rand_select, '\n', len(rand_select))
nonLatinChars_sel = []
for i in range(len(rand_select)):
    nonLatinChars_sel.append(nonLatinChars[rand_select[i]])

# Combine letters, numbers and other characters into one list
combined = password  + number_str + nonLatinChars_sel

# Generate list of random numbers to be used as indices used in shuffling the combined list
rand_indices = []
i=0
while 1!=0:
    n = np.random.randint(0,len(combined))
    #print('n={}'.format(n))
    if i < len(combined):
        if n not in rand_indices:
            rand_indices.append(n)
            i+=1
    else:
        break

# Randomly shuffle combined list. Go through random indices list with counter variable i and append combined[i] to new list.
new=[]
for i in range(len(rand_indices)):
    new.append(combined[rand_indices[i]])

print('Your password is:','\n','{}'.format(''.join(new)))


