"""
7.2 Write a program that prompts for a file name, then opens that file and 
reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines
 and compute the average of those values and produce 
an output as shown below. Do not use the sum() function or a variable named 
sum in your solution.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
 when you are testing below enter mbox-short.txt as the file name.
"""

# Use the file name mbox-short.txt as the file name

fname = input("Enter file name: ")
fh = open(fname)

all_values = []
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : 
        continue
    count = count + 1
    data = line.find('0')
    values = line[data:]
    all_values.append(float(values))
        
# print("Average spam confidence: ", mean(all_values))
sum_of_values = 0
for i in all_values:
    sum_of_values = sum_of_values + i 

print("Average spam confidence:", sum_of_values/count)
