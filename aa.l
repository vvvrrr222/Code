%{
#include <stdio.h>
int yywrap(void) {
    return 1;
}
%}

%%

if           {printf("keyword : if \n");}
else           {printf("keyword : else \n");}
[0-9]+           {printf("keyword : if \n");}
[a-zA-Z_][a-zA-Z0-9_]* {printf("Identifier : %s\n",yytext);}
%%

int main() {
    yylex();
    return 0;
}