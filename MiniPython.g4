grammar MiniPython;

//
// ------------- PARSER RULES -------------
//

file_input
    : stmt* EOF
    ;

// Statement / Blank Line
stmt
    : simple_stmt
    | compound_stmt
    | NEWLINE
    ;

small_stmt
    : assignment
    | expr
    ;

// Simple Statement: small_stmt with Optional NEWLINE
simple_stmt
    : small_stmt NEWLINE?
    ;

compound_stmt
    : if_stmt
    ;

// if / elif / else with Multi-Line Blocks, Separated by NEWLINE
if_stmt
    : IF test ':' block
      (ELIF test ':' block)*
      (ELSE ':' block)?
    ;

block
    : NEWLINE stmt+
    ;

// Conditionals
test
    : expr
    ;


// ---------- Expressions ----------

expr
    : or_test
    ;

or_test
    : and_test (OR and_test)*
    ;

and_test
    : not_test (AND not_test)*
    ;

not_test
    : NOT not_test
    | comparison
    ;

comparison
    : arith_expr (comp_op arith_expr)*
    ;

comp_op
    : LT
    | GT
    | EQEQ
    | GTE
    | LTE
    | NOTEQ
    ;


// ---------- Arithmetic ----------

arith_expr
    : term ((PLUS | MINUS) term)*
    ;

term
    : factor ((STAR | SLASH | PERCENT) factor)*
    ;

factor
    : (PLUS | MINUS) factor
    | atom
    ;

// Atoms: Names, Numbers, Strings, List Literals, Parenthesized Expressions
atom
    : NAME
    | NUMBER
    | STRING
    | list_literal
    | LPAREN expr RPAREN
    ;

list_literal
    : LBRACK (expr (COMMA expr)*)? RBRACK
    ;

// ---------- Assignments ----------

assignment
    : NAME assignment_op expr
    ;

assignment_op
    : EQ
    | PLUSEQ
    | MINUSEQ
    | STAREQ
    | SLASHEQ
    ;


//
// ------------- LEXER RULES -------------
//

NEWLINE
    : '\r'? '\n'
    ;

// Keywords
IF      : 'if';
ELIF    : 'elif';
ELSE    : 'else';
AND     : 'and';
OR      : 'or';
NOT     : 'not';

// Identifiers & Literals
NAME
    : [a-zA-Z_][a-zA-Z_0-9]*
    ;

// Ints & Floats (e.g. 123, 1.23)
NUMBER
    : [0-9]+ ('.' [0-9]+)?
    ;

// Strings
STRING
    : '"' ~["\r\n]* '"'
    | '\'' ~['\r\n]* '\''
    ;

// Arithmetic
PLUS        : '+' ;
MINUS       : '-' ;
STAR        : '*' ;
SLASH       : '/' ;
PERCENT     : '%' ;

// Assignment
EQ          : '=' ;
PLUSEQ      : '+=' ;
MINUSEQ     : '-=' ;
STAREQ      : '*=' ;
SLASHEQ     : '/=' ;

// Comparison
LT          : '<' ;
GT          : '>' ;
LTE         : '<=' ;
GTE         : '>=' ;
EQEQ        : '==' ;
NOTEQ       : '!=' ;

// List Punctuation
LBRACK      : '[' ;
RBRACK      : ']' ;
COMMA       : ',' ;

// Parenthesis & Colon
LPAREN      : '(' ;
RPAREN      : ')' ;
COLON       : ':' ;

// Ignore Spaces/Tabs inside lines
WS
    : [ \t\f]+ -> skip
    ;

// Comments
COMMENT
    : '#' ~[\r\n]* -> skip
    ;
