import re

# Define token patterns
token_specification = [
    ('NUMBER',   r'\d+(\.\d*)?'),    # Integer or decimal number
    ('ASSIGN',   r'='),              # Assignment operator
    ('END',      r';'),              # Statement terminator
    ('ID',       r'[A-Za-z_]\w*'),   # Identifiers
    ('OP',       r'[+\-*/]'),        # Arithmetic operators
    ('LPAREN',   r'\('),             # Left Parenthesis
    ('RPAREN',   r'\)'),             # Right Parenthesis
    ('SKIP',     r'[ \t]+'),         # Skip over spaces and tabs
    ('NEWLINE',  r'\n'),             # Line endings
    ('MISMATCH', r'.'),              # Any other character
]

# Compile regex into a pattern object
tok_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_specification)
get_token = re.compile(tok_regex).match

# Lexer function
def tokenize(code):
    line_num = 1
    pos = line_start = 0
    mo = get_token(code)
    while mo is not None:
        kind = mo.lastgroup
        value = mo.group()
        if kind == 'NEWLINE':
            line_start = pos
            line_num += 1
        elif kind == 'SKIP':
            pass
        elif kind == 'MISMATCH':
            raise RuntimeError(f'{value!r} unexpected on line {line_num}')
        else:
            yield (kind, value)
        pos = mo.end()
        mo = get_token(code, pos)
    if pos != len(code):
        raise RuntimeError('Unexpected character %r on line %d' % (code[pos], line_num))

# Example usage
if __name__ == '__main__':
    code = '''
    x = 10;
    y = x + 25;
    result = x * y;
    '''
    tokens = list(tokenize(code))
    for token in tokens:
        print(token)
