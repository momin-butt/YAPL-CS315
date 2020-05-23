import ply.lex as lex
import ply.yacc as yacc

tokens = (
    'TYPE',
    'STRUCT',
    'POINT',
    'PRINT',
    'COMMA',
    'SCOLON',
    'FOR',
    'INT', 
    'FLOAT',
    'CHAR', 
    'STRING',
    'BOOL',
    'PLUS',
    'MINUS',
    'DIVIDE',
    'MOD',
    'POWER',
    'MULTIPLY',
    'LPAREN',
    'RPAREN',
    'LCURL',
    'RCURL',
    'EQUAL',
    'DOUBLEPLUS',
    'DOUBLEMINUS',
    'LESSER',
    'GREATER',
    'LESSEQUAL',
    'GREATEQUAL',
    'NOTEQUAL',
    'DOUBLEQUAL',
    'NOT',
    'AND',
    'OR',
    'VARID',
    'NEWLINE',
)

t_PLUS    = r'\+'
t_MINUS   = r'\-'
t_MULTIPLY = r'\*'
t_DIVIDE  = r'/'
t_MOD = r'\%'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LCURL  = r'\{'
t_RCURL  = r'\}'
t_COMMA = r','
t_SCOLON = r';'
t_EQUAL = r'='
t_LESSER = r'<'
t_GREATER = r'>'
t_LESSEQUAL = r'<='
t_GREATEQUAL = r'>='
t_NOTEQUAL = r'!='
t_DOUBLEQUAL = r'=='
t_ignore  = ' \t'

def t_newline(t):
    r'\n'
    t.lexer.lineno += 1
    
def t_STRUCT(t):
    r'struct'
    return t

def t_POINT(t):
    r'\.'
    return t
    
def t_PRINT(t):
    r'print'
    return t

def t_FOR(t):
    r'for'
    return t

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_TYPE(t): 
	r'int|float|string|bool|char'
	return t

def t_STRING(t):
    r'"[^"\n]*"'
    t.value = t.value[1:-1]
    return t

def t_CHAR(t):
    r"'\\?[^']'"
    t.value = t.value[1:-1]
    return t

def t_BOOL(t):
    r'true | false'
    return t

def t_OR(t):
    r'or'
    return t

def t_AND(t):
    r'and'
    return t

def t_POWER(t):
    r'\^'
    return t

def t_NOT(t):
    r'not'
    return t

def t_DOUBLEPLUS(t):
	r'\+\+'
	return t

def t_DOUBLEMINUS(t):
	r'\-\-'
	return t

def t_VARID(t):
    r'[a-zA-z_][a-zA-Z_0-9]*'
    t.type = 'VARID'
    return t

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()


