input = open('instructions.txt', 'r')
output = open ('bin-instr.txt', 'w')
test = open('out.o', 'wb')

lines = input.readlines()
input.close()

for line in lines:
    splitted = line.split("\t")
    intval = int(splitted[1], 16)
    binary = "{:032b}".format(intval)
    test.write(intval.to_bytes(4, byteorder = 'little'))
    output.write("{}\t{} {} {} {} {} {}\n".format(splitted[0], binary[0:7], binary[7:12], binary[12:17], binary[17:20], binary[20:25], binary[-7:]))

output.close()
test.close()
