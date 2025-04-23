alp = [
    "START 3000",
    "LOAD AX",
    "LOOP  ADD AX",
    "ADD =50",
    "MUL BX",
    "MUL =60",
    "SUB CX",
    "SUB =70",
    "JUMP LOOP",
    "STORE AX",
    "STOP",
    "END",
]


symbol_table = {}

def createsymtable(alp):
    location_counter = 3000
    for line in alp:
        line = line.split()  

        if "START" in line or "END" in line or "STOP" in line:
            continue

        operand = line[-1]
        
        if operand not in symbol_table and not operand.startswith("="):
            symbol_table[operand] = location_counter
            location_counter += 1

    return symbol_table

symbol_table = createsymtable(alp)
print("Symbol Table:")
for sym, add in symbol_table.items():
    print(f"{sym}   :   {add}")



literal_table = {}

def createliteraltable(alp):
    literal_numbers = 5000
    for line in alp:
        line = line.split()  

        if line[-1].startswith("="):
            op = line[-1]
            op = op.replace("=", "")  

            literal_table[op] = literal_numbers
            literal_numbers += 1

    return literal_table

literal_table = createliteraltable(alp)
print("\nLiteral Table:")
for lit, addr in literal_table.items():
    print(f"{lit}   :   {addr}")




base_table = {}

def makebasetable(alp):
    base_lit = 4000
    for line in alp:
        line = line.split()

        op = line[-1]
        op = op.replace("=","")

        if not op.isdigit() and op not in base_table and "LOOP" not in line and "STOP" not in line and "END" not in line:
            base_table[op] = base_lit
            base_lit += 1

    return base_table

base_table = makebasetable(alp)
print("\nBase Table:")
for base, addr in base_table.items():
    print(f"{base}   :   {addr}")




location_count_table = {}

def location_counter(alp):
    lc_num = 5000
    for line in alp:
        location_count_table[line] = lc_num
        lc_num += 1

    return location_count_table

location_count_table = location_counter(alp)
print("\nLocation Table:")
for loc, addr in location_count_table.items():
    print(f"{loc:<20}   :   {addr}")




machine_opcode_things = ["MOVE","ADD","SUB","LOAD","STORE","JUMP","MUL","DIV","JNZ"]
mot_table = {}

def createmot(alp):
    opcode = 10
    for line in alp:
        line = line.split()
        for item in line:
            if item in machine_opcode_things:
                mot_table[item] = opcode
                opcode += 1

    return mot_table
                
mot_table = createmot(alp)
print("\nMOT Table:")
for mot, code in mot_table.items():
    print(f"{mot}       :   {code}")




pseudo_opcode_things = ["START", "STOP", "END", "EQU", "ORIGIN", "LTORG", "DS", "DC"]
pot_table = {}

def createpot(alp):
    opcode = 20
    for line in alp:
        line = line.split()
        for item in line:
            if item in pseudo_opcode_things:
                pot_table[item] = opcode
                opcode += 1
    
    return pot_table

pot_table = createpot(alp)
print("\nPOT Table:")
for pot, code in pot_table.items():
    print(f"{pot:<8}:   {code:<10}")



