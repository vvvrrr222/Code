class IntermediateToTargetCodeGenerator:
    def __init__(self):
        self.target_code = []

    def generate_target_code(self, tac_code):
        self.target_code = []
        reg_count = 1  # Start register count at R1
        reg_map = {'A': 'R1', 'B': 'R2', 'C': 'R3', 'D': 'R4'}  # Variable to register mapping

        for line in tac_code:
            lhs, rhs = line.split('=')
            lhs = lhs.strip()
            rhs = rhs.strip()
            reg_lhs = f"R{reg_count}"

            # Add to target code depending on the operation
            if '+' in rhs:
                var1, var2 = rhs.split('+')
                var1 = var1.strip()
                var2 = var2.strip()
                self.target_code.append(f"MOV {reg_lhs}, {reg_map[var1]}")
                reg_count += 1
                self.target_code.append(f"ADD {reg_lhs}, {reg_map[var2]}")
            elif '-' in rhs:
                var1, var2 = rhs.split('-')
                var1 = var1.strip()
                var2 = var2.strip()
                self.target_code.append(f"MOV {reg_lhs}, {reg_map[var1]}")
                reg_count += 1
                self.target_code.append(f"SUB {reg_lhs}, {reg_map[var2]}")
            elif rhs.isalpha():
                self.target_code.append(f"MOV {reg_lhs}, {reg_map[rhs.strip()]}")
            self.target_code.append(f"MOV {lhs}, {reg_lhs}")
            reg_count += 1
        
        return self.target_code


# Example TAC Code
tac_code = [
    "A = B + C",
    "B = A - D",
    "C = B + C",
    "D = B"
]

# Convert TAC to target code (Assembly-like)
generator = IntermediateToTargetCodeGenerator()
target_code = generator.generate_target_code(tac_code)

for i in tac_code:
    print(i)

print("---------------------------------")
# Print the target code (assembly-like)
print("Target Code (Assembly-like):")
for line in target_code:
    print(line)
