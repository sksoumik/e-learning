"""
Read files and coun the number of lines in a file.  
"""

fh = open("sample_file.txt", "r")

count = 0
for line in fh:
    print(line.strip())
    count = count + 1

print(count, "Lines")
