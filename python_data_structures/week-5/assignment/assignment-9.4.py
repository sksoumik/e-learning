"""
9.4 Write a program to read through the mbox-short.txt and 
figure out who has sent the greatest number of mail messages. 
The program looks for 'From ' lines and takes the second word 
of those lines as the person who sent the mail. The program creates
 a Python dictionary that maps the sender's mail address to a count 
 of the number of times they appear in the file. After the dictionary 
 is produced, the program reads through the dictionary 
using a maximum loop to find the most prolific committer.
"""

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

words = list() 

for line in handle:
    line.rstrip()
    if not line.startswith("From "): continue
    word = line.split()
    words.append(word[1])
    
max_author = dict()


# frequency count
for w in words:
    max_author[w] = max_author.get(w, 0) + 1

max_value = 0  # frequency 
max_key = 0  # emails

for key, val in max_author.items():
    if val > max_value: 
        max_value = val
        max_key = key

print(max_key, max_value)

