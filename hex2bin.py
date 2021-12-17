input = open('instructions.txt', 'r')
output = open ('bin-instr.txt', 'w')

lines = input.readlines()
input.close()

for line in lines:
    splitted = line.split("\t")
    intval = int(splitted[1], 16)
    funct7 = (intval & (0b1111111 << 25)) >> 25
    rs2 = (intval & (0b11111 << 20)) >> 20
    rs1 = (intval & (0b11111 << 15)) >> 15
    funct3 = (intval & (0b111 << 12)) >> 12
    rd = (intval & (0b11111 << 7)) >> 7
    opcode = intval & (0b1111111)
    output.write("{}\t{:07b} {:05b} {:05b} {:03b} {:05b} {:07b}\n".format(splitted[0], funct7, rs2, rs1, funct3, rd, opcode))

output.close()
