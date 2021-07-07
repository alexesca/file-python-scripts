import re


ccfile = open("count.txt", "r")
output = open("countOutput.txt", "a")
output.write("[")
for aline in ccfile:
    regex = re.search("\/\*\s[0-9]+\s\*\/", aline)
    print(regex)
    if regex == None:
        output.write(aline)
    else:
        output.write(",")
output.write("]")
ccfile.close()
output.close()
