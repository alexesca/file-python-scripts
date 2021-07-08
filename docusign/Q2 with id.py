import re


ccfile = open("../data/Envelope Report with IDs.csv", "r")
output = open("../data/contracts.txt", "a")
i = 0
list = []
for aline in ccfile:
    regex = re.search("(Invoice|Change Order)", aline)
    if regex == None:
        if i != 0:
            id = aline.split(",")[8]
            id = re.findall("([A-Za-z0-9\-]+)", id)
            list.append(id)

            output.write(aline)
        i += 1;
ccfile.close()
output.close()

print(list)
