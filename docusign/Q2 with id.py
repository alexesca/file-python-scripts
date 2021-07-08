import re


ccfile = open("../data/Envelope Report with IDs.csv", "r")
output = open("../data/sold-contracts-ids.txt", "a")
i = 0
list = []
output.write("[")
for aline in ccfile:
    regex = re.search("(Invoice|Change Order)", aline)
    if regex == None:
        if i != 0:
            id = aline.split(",")[8]
            id = re.findall("([A-Za-z0-9\-]+)", id)
            list.append(id[0])
            output.write('\'' + id[0] + '\'')
            output.write(',\n')
        i += 1;
output.write("]")
ccfile.close()
output.close()

print(list)
