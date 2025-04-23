# ------------------- 1) Algebraic simplification 2) Common sub expression elimination.----------------


def optimize(code):
    expr_map, result = {}, []
    for line in code:
        lhs, rhs = map(str.strip, line.split('='))
        # Algebraic Simplification
        rhs = rhs.replace('+ 0', '').replace('0 +', '').replace('* 1', '').replace('1 *', '')
        if rhs in expr_map:
            result.append(f"{lhs} = {expr_map[rhs]}")  # Common Subexpression Elimination
        else:
            expr_map[rhs] = lhs
            result.append(f"{lhs} = {rhs}")
    return result

code = [
    "t1 = a + 0", "t2 = b * 1", "t3 = t1 + t2",
    "t4 = a + 0", "t5 = c + d", "t6 = 5 + 3"
]

print("Optimized Code:")
print('\n'.join(optimize(code)))

# ------------------------ 1)Dead Code Elimination 2) Constant Propagation ------------------------------

import re

def optimize_code(lines):
    consts, used, out, ret = {}, set(), [], False
    for l in lines:
        if '=' in l and not any(op in l for op in "+-*/"):
            v, val = map(str.strip, l.split('='))
            if val.isdigit(): consts[v] = val
    for l in lines:
        for v, val in consts.items():
            l = re.sub(rf'\b{v}\b', val, l)
        if ret or (re.match(r'\w+\s*=', l) and l.split('=')[0].strip() not in used): continue
        out.append(l)
        if 'return' in l: ret = True
        used |= set(re.findall(r'\b\w+\b', l))
    return out

code = [
    "a = 5", "b = a", "c = b", "d = 10", "e = d",
    "print(e)", "return", "x = 999", "y = 888"
]

print("\n--- Optimized Code ---")
for l in optimize_code(code): print(l)