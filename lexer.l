%{
#include <stdio.h>
int yywrap(void) {  return 1;  }
%}

%%
if                       { printf("Keyword: if\n"); }
else                     { printf("Keyword: else\n"); }
[0-9]+                   { printf("Number: %s\n", yytext); }
[a-zA-Z_][a-zA-Z0-9_]*   { printf("Identifier: %s\n", yytext); }
[ \t\n]+        
%%

int main() {
    yylex();  
    return 0;
}