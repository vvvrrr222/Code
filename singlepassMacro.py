complete_alp = [
    "DOIT MACRO XX",
    "INC XX",
    "ADD B, XX",
    "MUL C, XX",
    "ENDM",
    "STARTUP",
    "LOAD A",
    "DOIT A",  
    "STORE A",
    "LOAD B",
    "DOIT B",  
    "STORE B",
    "END",
]


macro = []
for line in complete_alp:
    macro.append(line)
    if line == "ENDM":
        break



alp = []
startalp = False

for line in complete_alp:
    if line == "STARTUP":
        startalp = True
    if startalp:
        alp.append(line)


print(macro)
print(alp)



print("\n\n\n")

def create_macronametable(macro):
    macroline = macro[0].split()
    macroname = macroline[0]

    macrostartaddress = 1
    index = 1
    print("Macro Name Table")
    print(f"macroindex: macroname : macrostartaddress")
    print(f"{index:<10}: {macroname:<10}:{macrostartaddress}")

create_macronametable(macro)



print("\n\n\n")

def create_macrodefinitiontable(macro):
    macro = macro[1:]

    line_number = 1
    print("macro definition table")
    print(f"line number : macro line")

    for line in macro:
        print(f"{line_number:<10}  : {line}")
        line_number += 1

create_macrodefinitiontable(macro)




def create_argumentlistarray(macro):

    print("\nmacro argument list array \n")
    print("macro line       : argument")
    for line in macro:
        splitline = line.split()
        if splitline[-1] == "XX":
            print(f"{splitline[:-1]} : {splitline[-1]}")
        else:
            print(f"{line}")

create_argumentlistarray(macro)

    
def expandedalp(alp,macro):
    expanded = []

    macro = macro[1:-1]

    for line in alp:
        splitline = line.split()
        if splitline[0] == "DOIT":
            arg = splitline[-1]

            for macroline in macro:
                expanded.append(macroline.replace("XX",arg))

        else:
            expanded.append(line)

    print("\n\n\n")
    print("original alp")
    for line in alp:
        print(line)
    
    print("\n\n\n")
    print("expanded alp")
    for line in expanded:
        print(line)

expandedalp(alp,macro)