"""
with open("/Users/drewwhitting/Documents/VSCodePython//" \
    "WriteTest.txt", "w") as file1:
        file1.write("Line1\n")
        file1.write("line 2\n")
        file1.write("line 3")
"""

Lines = ["This is line 1", "This is line 2", \
         "This is line 3"]

with open("/Users/drewwhitting/Documents/VSCodePython/" \
    "WriteTest2.txt", "a") as file1:
        for line in Lines:
                file1.write(line + "\n")
print("\n")
print(file1.closed)