grammar Mygrammar;


program:(func)* (statement)* EOF;

func: ID '(' (ID (',' ID)*
)? ')' ':' NLINE (INSIDE func_statement)+;

func_statement
    :statement
    |return_statement;


statement
        :(equal
        |use_func
        |show_statement
        |func
        |for_statement
        |if_statement)  NLINE+;


equal: ID (',' ID)* '=' operation (',' operation)*;

operation
        :change_type
        |sum
        |use_func
        |other_op
        |input
        |INT;


change_type: '('TYPE')'ID;



sum: ('(' ID '+' ID ')'|ID) '+'
('(' ID '+' ID ')'|ID)
('+' ('(' ID '+' ID ')'|ID))*;


other_op: (ID|INT) ('+'|'-'|'/'|'*')
(ID|INT);
input: INPUT;
return_statement: RETURN ID ')' NLINE+;
show_statement: SHOW
(ID | STR | INT | use_func )')' ;
use_func: ID '(' (ID (',' ID)*)? ')' ;

for_statement: FOR ID ':' ID ')' ':'
NLINE (INSIDE statement)+;

if_statement: IF if_condition ')' ':'
NLINE (INSIDE statement)+
(ELSE
NLINE (INSIDE statement)+)?;

if_condition: (ID|INT|use_func)
((EQ|NEQ) (ID|INT|use_func))*;


INT: [0-9]+;
TYPE: 'node' | 'arc'| 'graph';
ID: [a-zA-Z_][a-zA-Z0-9_]*;

WHITESPACE: ' ' -> skip;


PLUS: '+';
MINUS: '-';
MULT: '*';
DIVIDER: '/';

ASSIGN : '=';
NEQ : '!=';
EQ : '==';

LPAREN : '(';
RPAREN : ')';
COMMA : ',';
COLON : ':';
SEMI : ';';
DOT : '.';

IF: 'if(' ;
ELSE: 'else:' ;
FOR: 'for(';
IN: 'in';
INSIDE: '****';
NLINE: '\n';
TAB: '\t';
SHOW: 'show(';
RETURN: 'return(';
INPUT: 'input()';

WS : [\r\f]+ -> skip ;
STR: '\'' [a-zA-Z ,_]* '\'' |
'"' [a-zA-Z _]* '"';