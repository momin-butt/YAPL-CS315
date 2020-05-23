
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftORleftANDleftDOUBLEQUALNOTEQUALnonassocLESSERGREATERLESSEQUALGREATEQUALleftPLUSMINUSleftMULTIPLYDIVIDEMODleftPOWERrightNOTnonassocDOUBLEPLUSDOUBLEMINUSnonassocLPARENRPARENAND BOOL CHAR COMMA DIVIDE DOUBLEMINUS DOUBLEPLUS DOUBLEQUAL EQUAL FLOAT FOR GREATEQUAL GREATER INT LCURL LESSEQUAL LESSER LPAREN MINUS MOD MULTIPLY NEWLINE NOT NOTEQUAL OR PLUS POINT POWER PRINT RCURL RPAREN SCOLON STRING STRUCT TYPE VARID\n    parent : lang\n           | lang parent\n           \n    \n    lang : expression SCOLON\n         | variables SCOLON\n         | print_stmt SCOLON\n         | block\n         | for_loop\n         | struct SCOLON\n         | struct_dec SCOLON\n         | struct_assign SCOLON\n         | struct_fetch SCOLON\n         | empty\n    \n    empty : \n    \n    print_stmt : print_multiple_stmt\n    \n    print_multiple_stmt : PRINT LPAREN multiple RPAREN \n    \n    multiple : expression\n             | expression COMMA multiple\n             | struct_fetch\n             | struct_fetch COMMA multiple\n    \n    struct : STRUCT VARID LCURL struct_block RCURL\n    \n    struct_block : variables SCOLON\n                 | variables SCOLON struct_block\n    \n    struct_dec : VARID VARID\n    \n    struct_assign : VARID POINT variableassign\n    \n    struct_fetch : VARID POINT VARID\n    \n    block : LCURL parent RCURL \n    \n    for_loop : FOR LPAREN TYPE VARID EQUAL expression SCOLON expression SCOLON forupdate RPAREN block\n    \n    variables : variableassign\n              | type_declare\n              | type_assign\n    \n    forupdate : expression\n              | variableassign\n    \n    type_declare : TYPE VARID\n    \n    variableassign : VARID EQUAL expression\n    \n    type_assign : TYPE VARID EQUAL expression\n    \n    expression : expression PLUS expression\n               | expression MINUS expression\n               | expression MULTIPLY expression\n               | expression DIVIDE expression\n    \n    expression : MINUS expression\n    \n    expression : expression MOD expression\n               | expression POWER expression\n    \n    expression : expression LESSER expression\n               | expression GREATER expression\n               | expression LESSEQUAL expression\n               | expression GREATEQUAL expression\n               | expression NOTEQUAL expression\n               | expression DOUBLEQUAL expression\n               | expression AND expression\n               | expression OR expression\n    \n    expression : LPAREN expression RPAREN \n    \n    expression : expression DOUBLEPLUS\n               | expression DOUBLEMINUS\n    \n    expression : NOT expression\n    \n    expression : VARID\n    \n    expression : INT\n               | FLOAT\n               | BOOL\n               | CHAR\n               | STRING\n               | empty\n    '
    
_lr_action_items = {'MINUS':([0,2,3,6,7,12,13,14,15,16,17,18,19,20,21,26,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,62,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,85,86,88,91,93,95,100,101,103,109,111,112,113,114,115,119,],[13,13,34,-6,-7,-12,13,13,13,-55,-56,-57,-58,-59,-60,13,-3,13,13,13,13,13,13,13,13,13,13,13,13,13,13,-52,-53,-4,-5,-8,-9,-10,-11,-40,-55,-61,34,-54,13,13,-36,-37,-38,-39,-41,-42,34,34,34,34,34,34,34,34,-51,34,-26,13,34,-55,34,13,13,13,34,13,34,13,-55,34,-27,]),'LPAREN':([0,2,6,7,12,13,14,15,26,27,30,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,49,50,51,52,53,54,62,67,86,88,100,101,103,111,113,119,],[14,14,-6,-7,-12,14,14,14,14,64,67,-3,14,14,14,14,14,14,14,14,14,14,14,14,14,14,-4,-5,-8,-9,-10,-11,14,14,-26,14,14,14,14,14,14,-27,]),'NOT':([0,2,6,7,12,13,14,15,26,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,49,50,51,52,53,54,62,67,86,88,100,101,103,111,113,119,],[15,15,-6,-7,-12,15,15,15,15,-3,15,15,15,15,15,15,15,15,15,15,15,15,15,15,-4,-5,-8,-9,-10,-11,15,15,-26,15,15,15,15,15,15,-27,]),'VARID':([0,2,6,7,12,13,14,15,16,26,28,29,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,49,50,51,52,53,54,61,62,67,86,87,88,89,100,101,102,103,105,111,113,119,],[16,16,-6,-7,-12,56,56,56,60,16,65,66,-3,56,56,56,56,56,56,56,56,56,56,56,56,56,56,-4,-5,-8,-9,-10,-11,83,56,93,-26,94,56,96,93,93,108,56,96,56,114,-27,]),'INT':([0,2,6,7,12,13,14,15,26,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,49,50,51,52,53,54,62,67,86,88,100,101,103,111,113,119,],[17,17,-6,-7,-12,17,17,17,17,-3,17,17,17,17,17,17,17,17,17,17,17,17,17,17,-4,-5,-8,-9,-10,-11,17,17,-26,17,17,17,17,17,17,-27,]),'FLOAT':([0,2,6,7,12,13,14,15,26,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,49,50,51,52,53,54,62,67,86,88,100,101,103,111,113,119,],[18,18,-6,-7,-12,18,18,18,18,-3,18,18,18,18,18,18,18,18,18,18,18,18,18,18,-4,-5,-8,-9,-10,-11,18,18,-26,18,18,18,18,18,18,-27,]),'BOOL':([0,2,6,7,12,13,14,15,26,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,49,50,51,52,53,54,62,67,86,88,100,101,103,111,113,119,],[19,19,-6,-7,-12,19,19,19,19,-3,19,19,19,19,19,19,19,19,19,19,19,19,19,19,-4,-5,-8,-9,-10,-11,19,19,-26,19,19,19,19,19,19,-27,]),'CHAR':([0,2,6,7,12,13,14,15,26,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,49,50,51,52,53,54,62,67,86,88,100,101,103,111,113,119,],[20,20,-6,-7,-12,20,20,20,20,-3,20,20,20,20,20,20,20,20,20,20,20,20,20,20,-4,-5,-8,-9,-10,-11,20,20,-26,20,20,20,20,20,20,-27,]),'STRING':([0,2,6,7,12,13,14,15,26,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,49,50,51,52,53,54,62,67,86,88,100,101,103,111,113,119,],[21,21,-6,-7,-12,21,21,21,21,-3,21,21,21,21,21,21,21,21,21,21,21,21,21,21,-4,-5,-8,-9,-10,-11,21,21,-26,21,21,21,21,21,21,-27,]),'LCURL':([0,2,6,7,12,26,32,49,50,51,52,53,54,66,86,118,119,],[26,26,-6,-7,-12,26,-3,-4,-5,-8,-9,-10,-11,89,-26,26,-27,]),'FOR':([0,2,6,7,12,26,32,49,50,51,52,53,54,86,119,],[27,27,-6,-7,-12,27,-3,-4,-5,-8,-9,-10,-11,-26,-27,]),'STRUCT':([0,2,6,7,12,26,32,49,50,51,52,53,54,86,119,],[29,29,-6,-7,-12,29,-3,-4,-5,-8,-9,-10,-11,-26,-27,]),'TYPE':([0,2,6,7,12,26,32,49,50,51,52,53,54,64,86,89,105,119,],[28,28,-6,-7,-12,28,-3,-4,-5,-8,-9,-10,-11,87,-26,28,28,-27,]),'PRINT':([0,2,6,7,12,26,32,49,50,51,52,53,54,86,119,],[30,30,-6,-7,-12,30,-3,-4,-5,-8,-9,-10,-11,-26,-27,]),'SCOLON':([0,2,3,4,5,6,7,8,9,10,11,12,13,15,16,17,18,19,20,21,22,23,24,25,26,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,59,60,62,65,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,88,95,98,99,103,104,109,111,112,119,],[-13,-13,32,49,50,-6,-7,51,52,53,54,-12,-13,-13,-55,-56,-57,-58,-59,-60,-28,-29,-30,-14,-13,-3,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-52,-53,-4,-5,-8,-9,-10,-11,-40,-55,-61,-54,-23,-13,-33,-36,-37,-38,-39,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-25,-24,-34,-26,-13,-35,105,-15,-13,-20,111,-13,113,-27,]),'PLUS':([0,2,3,6,7,12,13,14,15,16,17,18,19,20,21,26,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,62,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,85,86,88,91,93,95,100,101,103,109,111,112,113,114,115,119,],[-13,-13,33,-6,-7,-12,-13,-13,-13,-55,-56,-57,-58,-59,-60,-13,-3,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-52,-53,-4,-5,-8,-9,-10,-11,-40,-55,-61,33,-54,-13,-13,-36,-37,-38,-39,-41,-42,33,33,33,33,33,33,33,33,-51,33,-26,-13,33,-55,33,-13,-13,-13,33,-13,33,-13,-55,33,-27,]),'MULTIPLY':([0,2,3,6,7,12,13,14,15,16,17,18,19,20,21,26,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,62,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,85,86,88,91,93,95,100,101,103,109,111,112,113,114,115,119,],[-13,-13,35,-6,-7,-12,-13,-13,-13,-55,-56,-57,-58,-59,-60,-13,-3,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-52,-53,-4,-5,-8,-9,-10,-11,35,-55,-61,35,-54,-13,-13,35,35,-38,-39,-41,-42,35,35,35,35,35,35,35,35,-51,35,-26,-13,35,-55,35,-13,-13,-13,35,-13,35,-13,-55,35,-27,]),'DIVIDE':([0,2,3,6,7,12,13,14,15,16,17,18,19,20,21,26,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,62,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,85,86,88,91,93,95,100,101,103,109,111,112,113,114,115,119,],[-13,-13,36,-6,-7,-12,-13,-13,-13,-55,-56,-57,-58,-59,-60,-13,-3,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-52,-53,-4,-5,-8,-9,-10,-11,36,-55,-61,36,-54,-13,-13,36,36,-38,-39,-41,-42,36,36,36,36,36,36,36,36,-51,36,-26,-13,36,-55,36,-13,-13,-13,36,-13,36,-13,-55,36,-27,]),'MOD':([0,2,3,6,7,12,13,14,15,16,17,18,19,20,21,26,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,62,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,85,86,88,91,93,95,100,101,103,109,111,112,113,114,115,119,],[-13,-13,37,-6,-7,-12,-13,-13,-13,-55,-56,-57,-58,-59,-60,-13,-3,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-52,-53,-4,-5,-8,-9,-10,-11,37,-55,-61,37,-54,-13,-13,37,37,-38,-39,-41,-42,37,37,37,37,37,37,37,37,-51,37,-26,-13,37,-55,37,-13,-13,-13,37,-13,37,-13,-55,37,-27,]),'POWER':([0,2,3,6,7,12,13,14,15,16,17,18,19,20,21,26,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,62,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,85,86,88,91,93,95,100,101,103,109,111,112,113,114,115,119,],[-13,-13,38,-6,-7,-12,-13,-13,-13,-55,-56,-57,-58,-59,-60,-13,-3,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-52,-53,-4,-5,-8,-9,-10,-11,38,-55,-61,38,-54,-13,-13,38,38,38,38,38,-42,38,38,38,38,38,38,38,38,-51,38,-26,-13,38,-55,38,-13,-13,-13,38,-13,38,-13,-55,38,-27,]),'LESSER':([0,2,3,6,7,12,13,14,15,16,17,18,19,20,21,26,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,62,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,85,86,88,91,93,95,100,101,103,109,111,112,113,114,115,119,],[-13,-13,39,-6,-7,-12,-13,-13,-13,-55,-56,-57,-58,-59,-60,-13,-3,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-52,-53,-4,-5,-8,-9,-10,-11,-40,-55,-61,39,-54,-13,-13,-36,-37,-38,-39,-41,-42,None,None,None,None,39,39,39,39,-51,39,-26,-13,39,-55,39,-13,-13,-13,39,-13,39,-13,-55,39,-27,]),'GREATER':([0,2,3,6,7,12,13,14,15,16,17,18,19,20,21,26,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,62,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,85,86,88,91,93,95,100,101,103,109,111,112,113,114,115,119,],[-13,-13,40,-6,-7,-12,-13,-13,-13,-55,-56,-57,-58,-59,-60,-13,-3,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-52,-53,-4,-5,-8,-9,-10,-11,-40,-55,-61,40,-54,-13,-13,-36,-37,-38,-39,-41,-42,None,None,None,None,40,40,40,40,-51,40,-26,-13,40,-55,40,-13,-13,-13,40,-13,40,-13,-55,40,-27,]),'LESSEQUAL':([0,2,3,6,7,12,13,14,15,16,17,18,19,20,21,26,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,62,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,85,86,88,91,93,95,100,101,103,109,111,112,113,114,115,119,],[-13,-13,41,-6,-7,-12,-13,-13,-13,-55,-56,-57,-58,-59,-60,-13,-3,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-52,-53,-4,-5,-8,-9,-10,-11,-40,-55,-61,41,-54,-13,-13,-36,-37,-38,-39,-41,-42,None,None,None,None,41,41,41,41,-51,41,-26,-13,41,-55,41,-13,-13,-13,41,-13,41,-13,-55,41,-27,]),'GREATEQUAL':([0,2,3,6,7,12,13,14,15,16,17,18,19,20,21,26,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,62,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,85,86,88,91,93,95,100,101,103,109,111,112,113,114,115,119,],[-13,-13,42,-6,-7,-12,-13,-13,-13,-55,-56,-57,-58,-59,-60,-13,-3,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-52,-53,-4,-5,-8,-9,-10,-11,-40,-55,-61,42,-54,-13,-13,-36,-37,-38,-39,-41,-42,None,None,None,None,42,42,42,42,-51,42,-26,-13,42,-55,42,-13,-13,-13,42,-13,42,-13,-55,42,-27,]),'NOTEQUAL':([0,2,3,6,7,12,13,14,15,16,17,18,19,20,21,26,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,62,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,85,86,88,91,93,95,100,101,103,109,111,112,113,114,115,119,],[-13,-13,43,-6,-7,-12,-13,-13,-13,-55,-56,-57,-58,-59,-60,-13,-3,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-52,-53,-4,-5,-8,-9,-10,-11,-40,-55,-61,43,-54,-13,-13,-36,-37,-38,-39,-41,-42,-43,-44,-45,-46,-47,-48,43,43,-51,43,-26,-13,43,-55,43,-13,-13,-13,43,-13,43,-13,-55,43,-27,]),'DOUBLEQUAL':([0,2,3,6,7,12,13,14,15,16,17,18,19,20,21,26,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,62,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,85,86,88,91,93,95,100,101,103,109,111,112,113,114,115,119,],[-13,-13,44,-6,-7,-12,-13,-13,-13,-55,-56,-57,-58,-59,-60,-13,-3,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-52,-53,-4,-5,-8,-9,-10,-11,-40,-55,-61,44,-54,-13,-13,-36,-37,-38,-39,-41,-42,-43,-44,-45,-46,-47,-48,44,44,-51,44,-26,-13,44,-55,44,-13,-13,-13,44,-13,44,-13,-55,44,-27,]),'AND':([0,2,3,6,7,12,13,14,15,16,17,18,19,20,21,26,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,62,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,85,86,88,91,93,95,100,101,103,109,111,112,113,114,115,119,],[-13,-13,45,-6,-7,-12,-13,-13,-13,-55,-56,-57,-58,-59,-60,-13,-3,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-52,-53,-4,-5,-8,-9,-10,-11,-40,-55,-61,45,-54,-13,-13,-36,-37,-38,-39,-41,-42,-43,-44,-45,-46,-47,-48,-49,45,-51,45,-26,-13,45,-55,45,-13,-13,-13,45,-13,45,-13,-55,45,-27,]),'OR':([0,2,3,6,7,12,13,14,15,16,17,18,19,20,21,26,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,62,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,85,86,88,91,93,95,100,101,103,109,111,112,113,114,115,119,],[-13,-13,46,-6,-7,-12,-13,-13,-13,-55,-56,-57,-58,-59,-60,-13,-3,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-52,-53,-4,-5,-8,-9,-10,-11,-40,-55,-61,46,-54,-13,-13,-36,-37,-38,-39,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,46,-26,-13,46,-55,46,-13,-13,-13,46,-13,46,-13,-55,46,-27,]),'DOUBLEPLUS':([0,2,3,6,7,12,13,14,15,16,17,18,19,20,21,26,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,62,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,85,86,88,91,93,95,100,101,103,109,111,112,113,114,115,119,],[-13,-13,47,-6,-7,-12,-13,-13,-13,-55,-56,-57,-58,-59,-60,-13,-3,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-52,-53,-4,-5,-8,-9,-10,-11,47,-55,-61,47,47,-13,-13,47,47,47,47,47,47,47,47,47,47,47,47,47,47,-51,47,-26,-13,47,-55,47,-13,-13,-13,47,-13,47,-13,-55,47,-27,]),'DOUBLEMINUS':([0,2,3,6,7,12,13,14,15,16,17,18,19,20,21,26,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,62,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,85,86,88,91,93,95,100,101,103,109,111,112,113,114,115,119,],[-13,-13,48,-6,-7,-12,-13,-13,-13,-55,-56,-57,-58,-59,-60,-13,-3,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-52,-53,-4,-5,-8,-9,-10,-11,48,-55,-61,48,48,-13,-13,48,48,48,48,48,48,48,48,48,48,48,48,48,48,-51,48,-26,-13,48,-55,48,-13,-13,-13,48,-13,48,-13,-55,48,-27,]),'$end':([0,1,2,6,7,12,31,32,49,50,51,52,53,54,86,119,],[-13,0,-1,-6,-7,-12,-2,-3,-4,-5,-8,-9,-10,-11,-26,-27,]),'RCURL':([2,6,7,12,26,31,32,49,50,51,52,53,54,63,86,97,105,110,119,],[-1,-6,-7,-12,-13,-2,-3,-4,-5,-8,-9,-10,-11,86,-26,104,-21,-22,-27,]),'RPAREN':([13,14,15,17,18,19,20,21,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,55,56,57,58,59,62,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,85,90,91,92,93,100,101,106,107,108,113,114,115,116,117,],[-13,-13,-13,-56,-57,-58,-59,-60,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-52,-53,-40,-55,-61,82,-54,-13,-13,-36,-37,-38,-39,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,-34,99,-16,-18,-55,-13,-13,-17,-19,-25,-13,-55,-31,118,-32,]),'COMMA':([13,15,17,18,19,20,21,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,55,56,57,59,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,91,92,93,100,101,108,],[-13,-13,-56,-57,-58,-59,-60,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-13,-52,-53,-40,-55,-61,-54,-13,-36,-37,-38,-39,-41,-42,-43,-44,-45,-46,-47,-48,-49,-50,-51,100,101,-55,-13,-13,-25,]),'POINT':([16,93,],[61,102,]),'EQUAL':([16,65,83,94,96,114,],[62,88,62,103,62,62,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'parent':([0,2,26,],[1,31,63,]),'lang':([0,2,26,],[2,2,2,]),'expression':([0,2,13,14,15,26,33,34,35,36,37,38,39,40,41,42,43,44,45,46,62,67,88,100,101,103,111,113,],[3,3,55,58,59,3,68,69,70,71,72,73,74,75,76,77,78,79,80,81,85,91,95,91,91,109,112,115,]),'variables':([0,2,26,89,105,],[4,4,4,98,98,]),'print_stmt':([0,2,26,],[5,5,5,]),'block':([0,2,26,118,],[6,6,6,119,]),'for_loop':([0,2,26,],[7,7,7,]),'struct':([0,2,26,],[8,8,8,]),'struct_dec':([0,2,26,],[9,9,9,]),'struct_assign':([0,2,26,],[10,10,10,]),'struct_fetch':([0,2,26,67,100,101,],[11,11,11,92,92,92,]),'empty':([0,2,13,14,15,26,33,34,35,36,37,38,39,40,41,42,43,44,45,46,62,67,88,100,101,103,111,113,],[12,12,57,57,57,12,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,]),'variableassign':([0,2,26,61,89,105,113,],[22,22,22,84,22,22,117,]),'type_declare':([0,2,26,89,105,],[23,23,23,23,23,]),'type_assign':([0,2,26,89,105,],[24,24,24,24,24,]),'print_multiple_stmt':([0,2,26,],[25,25,25,]),'multiple':([67,100,101,],[90,106,107,]),'struct_block':([89,105,],[97,110,]),'forupdate':([113,],[116,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> parent","S'",1,None,None,None),
  ('parent -> lang','parent',1,'p_parent','parser.py',20),
  ('parent -> lang parent','parent',2,'p_parent','parser.py',21),
  ('lang -> expression SCOLON','lang',2,'p_lang','parser.py',32),
  ('lang -> variables SCOLON','lang',2,'p_lang','parser.py',33),
  ('lang -> print_stmt SCOLON','lang',2,'p_lang','parser.py',34),
  ('lang -> block','lang',1,'p_lang','parser.py',35),
  ('lang -> for_loop','lang',1,'p_lang','parser.py',36),
  ('lang -> struct SCOLON','lang',2,'p_lang','parser.py',37),
  ('lang -> struct_dec SCOLON','lang',2,'p_lang','parser.py',38),
  ('lang -> struct_assign SCOLON','lang',2,'p_lang','parser.py',39),
  ('lang -> struct_fetch SCOLON','lang',2,'p_lang','parser.py',40),
  ('lang -> empty','lang',1,'p_lang','parser.py',41),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',47),
  ('print_stmt -> print_multiple_stmt','print_stmt',1,'p_print_stmt','parser.py',53),
  ('print_multiple_stmt -> PRINT LPAREN multiple RPAREN','print_multiple_stmt',4,'p_print_multiple_stmt','parser.py',59),
  ('multiple -> expression','multiple',1,'p_multiple','parser.py',65),
  ('multiple -> expression COMMA multiple','multiple',3,'p_multiple','parser.py',66),
  ('multiple -> struct_fetch','multiple',1,'p_multiple','parser.py',67),
  ('multiple -> struct_fetch COMMA multiple','multiple',3,'p_multiple','parser.py',68),
  ('struct -> STRUCT VARID LCURL struct_block RCURL','struct',5,'p_struct','parser.py',77),
  ('struct_block -> variables SCOLON','struct_block',2,'p_struct_block','parser.py',83),
  ('struct_block -> variables SCOLON struct_block','struct_block',3,'p_struct_block','parser.py',84),
  ('struct_dec -> VARID VARID','struct_dec',2,'p_struct_dec','parser.py',93),
  ('struct_assign -> VARID POINT variableassign','struct_assign',3,'p_struct_assign','parser.py',99),
  ('struct_fetch -> VARID POINT VARID','struct_fetch',3,'p_struct_getdata','parser.py',105),
  ('block -> LCURL parent RCURL','block',3,'p_block','parser.py',111),
  ('for_loop -> FOR LPAREN TYPE VARID EQUAL expression SCOLON expression SCOLON forupdate RPAREN block','for_loop',12,'p_for_loop','parser.py',117),
  ('variables -> variableassign','variables',1,'p_variables','parser.py',124),
  ('variables -> type_declare','variables',1,'p_variables','parser.py',125),
  ('variables -> type_assign','variables',1,'p_variables','parser.py',126),
  ('forupdate -> expression','forupdate',1,'p_forupdate','parser.py',131),
  ('forupdate -> variableassign','forupdate',1,'p_forupdate','parser.py',132),
  ('type_declare -> TYPE VARID','type_declare',2,'p_type_declare','parser.py',137),
  ('variableassign -> VARID EQUAL expression','variableassign',3,'p_variableassign','parser.py',143),
  ('type_assign -> TYPE VARID EQUAL expression','type_assign',4,'p_type_assign','parser.py',149),
  ('expression -> expression PLUS expression','expression',3,'p_expression_plus_minus_mult_div','parser.py',155),
  ('expression -> expression MINUS expression','expression',3,'p_expression_plus_minus_mult_div','parser.py',156),
  ('expression -> expression MULTIPLY expression','expression',3,'p_expression_plus_minus_mult_div','parser.py',157),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_plus_minus_mult_div','parser.py',158),
  ('expression -> MINUS expression','expression',2,'p_expression_minus','parser.py',164),
  ('expression -> expression MOD expression','expression',3,'p_expression_mod_power','parser.py',170),
  ('expression -> expression POWER expression','expression',3,'p_expression_mod_power','parser.py',171),
  ('expression -> expression LESSER expression','expression',3,'p_expression_logical_operators','parser.py',177),
  ('expression -> expression GREATER expression','expression',3,'p_expression_logical_operators','parser.py',178),
  ('expression -> expression LESSEQUAL expression','expression',3,'p_expression_logical_operators','parser.py',179),
  ('expression -> expression GREATEQUAL expression','expression',3,'p_expression_logical_operators','parser.py',180),
  ('expression -> expression NOTEQUAL expression','expression',3,'p_expression_logical_operators','parser.py',181),
  ('expression -> expression DOUBLEQUAL expression','expression',3,'p_expression_logical_operators','parser.py',182),
  ('expression -> expression AND expression','expression',3,'p_expression_logical_operators','parser.py',183),
  ('expression -> expression OR expression','expression',3,'p_expression_logical_operators','parser.py',184),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_bracs','parser.py',190),
  ('expression -> expression DOUBLEPLUS','expression',2,'p_expression_increase_decrease','parser.py',196),
  ('expression -> expression DOUBLEMINUS','expression',2,'p_expression_increase_decrease','parser.py',197),
  ('expression -> NOT expression','expression',2,'p_expression_logical_not','parser.py',203),
  ('expression -> VARID','expression',1,'p_expression_var','parser.py',209),
  ('expression -> INT','expression',1,'p_expression_types','parser.py',215),
  ('expression -> FLOAT','expression',1,'p_expression_types','parser.py',216),
  ('expression -> BOOL','expression',1,'p_expression_types','parser.py',217),
  ('expression -> CHAR','expression',1,'p_expression_types','parser.py',218),
  ('expression -> STRING','expression',1,'p_expression_types','parser.py',219),
  ('expression -> empty','expression',1,'p_expression_types','parser.py',220),
]