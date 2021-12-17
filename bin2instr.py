input = open('bin-instr.txt', 'r')
stats = open('stats.txt', 'w')
output = open('code.txt', 'w')

lines = input.readlines()
input.close()

opcodes = {}

opcodes_str = {
    0b0010011 : {0b000 : 'addi', 0b001 : 'slli'},
    0b1100011 : {0b000 : 'beq', 0b001 : 'bne', 0b101 : 'bge'},
    0b0110011 : {0b000 : 'add/sub'},
    0b0100011 : {0b010 : 'xor'},
    0b1100111 : {0b000 : 'jalr'},
    0b0000011 : {0b010 : 'lw'}
}

opcodes_fun7 = {
    0b0110011 : {0b000 : {0b0000000 : 'add', 0b0100000 : 'sub'}}
}

types = {
    0b0010011 : 'I',
    0b1100011 : 'SB',
    0b0110011 : 'R',
    0b0100011 : 'R',
    0b1100111 : 'UJ',
    0b0000011 : 'I'
}

regnames = {
    0 : 'zero',
    1 : 'ra',
    2 : 'sp',
    3 : 'gp',
    4 : 'tp',
    8 : 's0',
    9 : 's1'
}

def reg_name(n):
    if n in regnames:
        return regnames[n]
    
    if n > 4 and n < 8:
        return 't{}'.format(n - 5)

    if n > 9 and n < 18:
        return 'a{}'.format(n - 10)
    
    if n > 17 and n < 28: 
        return 's{}'.format(n - 17)
    
    if n > 27 and n < 32:
        return 't{}'.format(n - 24)

linecount = 0
for line in lines:
    splitted = line.split()
    funct7 = int(splitted[1], 2)
    rs2 = int(splitted[2], 2)
    rs1 = int(splitted[3], 2)
    funct3 = int(splitted[4], 2)
    rd = int(splitted[5], 2)
    opcode = int(splitted[6], 2)
    if not opcode in opcodes.keys():
        opcodes[opcode] = []
    
    fun_spec = '[{:07b} {:03b}]'.format(funct7, funct3)

    if not fun_spec in opcodes[opcode]:
        opcodes[opcode].append(fun_spec)


    command = opcodes_str[opcode][funct3]

    if opcode in opcodes_fun7.keys():
        command = opcodes_fun7[opcode][funct3][funct7]

    fmt_string = ''

    if types[opcode] == 'I':
        immediat = funct7 << 5 | rs2
        fmt_string = '{} {}, {}, #{}'.format(command, reg_name(rd), reg_name(rs1), immediat)
    elif types[opcode] == 'S':
        immediat = (funct7 << 5 | rs2) << 5 | rd
        fmt_string = '{} {}, #{}'.format(command, reg_name(rs1), immediat)
    elif types[opcode] == 'R':
        fmt_string = '{} {}, {}, {}'.format(command, reg_name(rd), reg_name(rs1), reg_name(rs2))
    elif types[opcode] == 'UJ':
        temp = ((funct7 << 5 | rs2) << 5 | rs1) << 3 | funct3
        immediat = temp & (1 << 20) | (temp & 255) << 12 | (temp & 0b11111111111 << 9) >> 8 | (temp & (1 << 7)) << 3 

        fmt_string = '{} {}, #{}'.format(command, reg_name(rd), immediat)
    elif types[opcode] == 'SB':
        temp = funct7 << 5 | rd
        immediat = temp
        fmt_string = '{}, {}, {}, #{}'.format(command, reg_name(rs1), reg_name(rs2), immediat)
    
    linecount += 4
    output.write("{:02x}: {}\t[{}]\n".format(linecount, fmt_string, types[opcode]))

for opcode in opcodes.keys():

    stats.write('{:07b} : {}\n'.format(opcode, ' '.join(opcodes[opcode])))

stats.close()
output.close()
