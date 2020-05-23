import ply.yacc as yacc
import sys
from lexer import tokens

precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('left','DOUBLEQUAL','NOTEQUAL'),
    ('nonassoc','LESSER','GREATER','LESSEQUAL','GREATEQUAL'),
    ('left','PLUS','MINUS'),
    ('left','MULTIPLY','DIVIDE','MOD'),
    ('left','POWER'),
    ('right','NOT'),
    ('nonassoc','DOUBLEPLUS','DOUBLEMINUS'),
    ('nonassoc','LPAREN','RPAREN'),
)

def p_parent(p):
    '''
    parent : lang
           | lang parent
           
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]]+p[2]
    # print(p[0])

def p_lang(p):
    '''
    lang : expression SCOLON
         | variables SCOLON
         | print_stmt SCOLON
         | block
         | for_loop
         | struct SCOLON
         | struct_dec SCOLON
         | struct_assign SCOLON
         | struct_fetch SCOLON
         | empty
    '''
    p[0] = p[1]

def p_empty(p):
    '''
    empty : 
    '''
    p[0] = None
    
def p_print_stmt(p):
    '''
    print_stmt : print_multiple_stmt
    '''
    p[0] = p[1]

def p_print_multiple_stmt(p):
    '''
    print_multiple_stmt : PRINT LPAREN multiple RPAREN 
    '''
    p[0] = (p[1],p[3])

def p_multiple(p):
    '''
    multiple : expression
             | expression COMMA multiple
             | struct_fetch
             | struct_fetch COMMA multiple
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]
        
def p_struct(p):
    '''
    struct : STRUCT VARID LCURL struct_block RCURL
    '''
    p[0] = ("struct","struct_init",p[2],p[4])

def p_struct_block(p):
    '''
    struct_block : variables SCOLON
                 | variables SCOLON struct_block
    '''
    if len(p) == 3:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]

def p_struct_dec(p):
    '''
    struct_dec : VARID VARID
    '''
    p[0] = ("struct",'struct_d', p[1], p[2])
    
def p_struct_assign(p):
    '''
    struct_assign : VARID POINT variableassign
    '''
    p[0] = ("struct",'struct_assign', p[1], p[3])

def p_struct_getdata(p):
    '''
    struct_fetch : VARID POINT VARID
    '''
    p[0] = ("struct",'struct_getdata', p[1], p[3])

def p_block(p):
    '''
    block : LCURL parent RCURL 
    '''
    p[0] = ("block",p[2])

def p_for_loop(p):
    '''
    for_loop : FOR LPAREN TYPE VARID EQUAL expression SCOLON expression SCOLON forupdate RPAREN block
    '''

    p[0] = ("for",p[3],p[4],p[6],p[8],p[10],p[12])
    
def p_variables(p):
    '''
    variables : variableassign
              | type_declare
              | type_assign
    '''
    p[0] = p[1]
def p_forupdate(p):
    '''
    forupdate : expression
              | variableassign
    '''
    p[0] = p[1]
def p_type_declare(p):
    '''
    type_declare : TYPE VARID
    '''
    p[0] = ("declaring", p[1],p[2])

def p_variableassign(p):
    '''
    variableassign : VARID EQUAL expression
    '''
    p[0] = ("onlyassign",p[1],p[3])

def p_type_assign(p):
    '''
    type_assign : TYPE VARID EQUAL expression
    '''
    p[0] = ("declaringassign", p[1],p[2],p[4])

def p_expression_plus_minus_mult_div(p):
    '''
    expression : expression PLUS expression
               | expression MINUS expression
               | expression MULTIPLY expression
               | expression DIVIDE expression
    '''
    p[0] = (p[2], p[1], p[3])
    
def p_expression_minus(p):
    '''
    expression : MINUS expression
    '''
    p[0] = (p[1],0,p[2])

def p_expression_mod_power(p):
    '''
    expression : expression MOD expression
               | expression POWER expression
    '''
    p[0] = (p[2], p[1], p[3])

def p_expression_logical_operators(p):
    '''
    expression : expression LESSER expression
               | expression GREATER expression
               | expression LESSEQUAL expression
               | expression GREATEQUAL expression
               | expression NOTEQUAL expression
               | expression DOUBLEQUAL expression
               | expression AND expression
               | expression OR expression
    '''
    p[0] = (p[2], p[1], p[3])
    
def p_expression_bracs(p):
    '''
    expression : LPAREN expression RPAREN 
    '''
    p[0] = p[2]

def p_expression_increase_decrease(p):
    '''
    expression : expression DOUBLEPLUS
               | expression DOUBLEMINUS
    '''
    p[0] = (p[1],p[2])

def p_expression_logical_not(p):
    '''
    expression : NOT expression
    '''
    p[0] = (p[1],p[2])

def p_expression_var(p):
    '''
    expression : VARID
    '''
    p[0] = ('getvar',p[1])
    
def p_expression_types(p):
    '''
    expression : INT
               | FLOAT
               | BOOL
               | CHAR
               | STRING
               | empty
    '''
    p[0] = p[1]

def p_error(p):
    print(f'ERROR -> {p}')
    
# parser = yacc.yacc()


# while True:
#     try:
#         s = input('')
#     except EOFError:
#         break
#     parser.parse(s)
