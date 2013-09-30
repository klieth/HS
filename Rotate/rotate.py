#if you want to use sys.stdout.write, you have to import sys
import sys
#I would also suggest using print("string",end='') if you're using python3

#grab the number of lines out of stdin and make it an int so the computer doesn't get angry
lines = int(input())
words = list() #create a new list that will contain the words to write



#get all the words from stdin and force them onto the list
for i in range(lines):
    words.append(input())



#  Figure out which word is the longest. This is important because
#  we can't stop the program until the longest word has been
#  completely written
max = 0
for i in range(0,lines):
    if len(words[i]) > max:
        max = len(words[i])

# A cooler way to do this is:
# max = len(max(words,key=len))

# An even cooler way to do this:
# g = lambda x: len(max(x,key=len))
# max = g(words)
# Or, instead of using the variable max at all, use g(words)



#  reverse the list so that the words show up in the correct order
words.reverse()




#  This does the actual writing of the words.
for i in range(max): #Make sure you write all the letters...
    for j in words:  #Make sure you write one letter from each word per line
        if i >= len(j):  #If there are no more letters to write,
            sys.stdout.write(' ')  #write a space instead
        else:
            sys.stdout.write(j[i]) #otherwise, write the current letter
    print()   #Include a newline after each row
