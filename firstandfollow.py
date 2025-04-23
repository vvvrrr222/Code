from collections import defaultdict

# Helper to split productions
def get_symbols(production):
    return production.split()

# Compute FIRST set
def compute_first(grammar):
    first = defaultdict(set)

    def first_of(symbol):
        if symbol not in grammar:
            return {symbol}
        if symbol in first and first[symbol]:
            return first[symbol]
        for prod in grammar[symbol]:
            for sym in get_symbols(prod):
                sym_first = first_of(sym)
                first[symbol].update(sym_first - {"ε"})
                if "ε" not in sym_first:
                    break
            else:
                first[symbol].add("ε")
        return first[symbol]

    for non_terminal in grammar:
        first_of(non_terminal)

    return first

# Compute FOLLOW set
def compute_follow(grammar, first, start_symbol):
    follow = defaultdict(set)
    follow[start_symbol].add('$')

    changed = True
    while changed:
        changed = False
        for head in grammar:
            for prod in grammar[head]:
                symbols = get_symbols(prod)
                for i in range(len(symbols)):
                    if symbols[i] in grammar:  # non-terminal
                        next_syms = symbols[i+1:]
                        temp = set()
                        for sym in next_syms:
                            temp |= first[sym] - {'ε'}
                            if 'ε' in first[sym]:
                                continue
                            break
                        else:
                            temp |= follow[head]
                        if not temp.issubset(follow[symbols[i]]):
                            follow[symbols[i]] |= temp
                            changed = True
    return follow

# Main Function
def main():
    grammar = {
        "E": ["T E'"],
        "E'": ["+ T E'", "ε"],
        "T": ["F T'"],
        "T'": ["* F T'", "ε"],
        "F": ["( E )", "id"]
    }
    start_symbol = "E"

    first = compute_first(grammar)
    follow = compute_follow(grammar, first, start_symbol)

    print("FIRST sets:")
    for nt in first:
        print(f"FIRST({nt}) = {first[nt]}")
    
    print("\nFOLLOW sets:")
    for nt in follow:
        print(f"FOLLOW({nt}) = {follow[nt]}")

if __name__ == "__main__":
    main()
