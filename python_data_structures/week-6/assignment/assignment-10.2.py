"""
10.2 Write a program to read through the mbox-short.txt and 
figure out the distribution by 
hour of the day for each of the messages. You can pull the hour 
out from the 'From ' line by finding the time and then splitting 
the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the 
counts, sorted by hour as shown below.
"""

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

hour_count = dict()

for line in handle:
    line.rstrip()
    if not line.startswith("From "): continue
    word = line.split()
    hour = word[5].split(':')
    hour_count[hour[0]] =hour_count.get(hour[0], 0) + 1

# create a list 
hlst = []

for key, val in hour_count.items(): # key is the hour and val is the count
    hlst.append((key, val))

hlst.sort()

for k, v in hlst:
    print(k,v)

