import lexer
import parser
import ply.lex as lex
import ply.yacc as yacc
import sys
import copy

dict_list = [{}]

def is_in_dict_list(varname):
    for i in range(len(dict_list) -1, -1, -1):
        if varname in dict_list[i]:
            return True, dict_list[i]
    return False, None

struct_var = {}
struct_exit = {}
activestruct = ""
def evaluate_child(child):
    global dict_list
    dict_var = dict_list[-1]
    struct_var
    global activestruct
    global struct_exit
    
    if type(child) is int:
        return child
    
    if type(child) is float:
        return child

    if type(child) is str:
        return child
    
    if child == "true" or child == "false":
        return child
    
    if child[0] == "declaring": # declaration of a variable
        if child[2] in dict_var:
            exit("RedeclarationError")
        else:
            dict_var[child[2]] = {"vartype": child[1], "varvalue": 0}
            return ""

    elif child[0] == "declaringassign": #declaration and assignment of a variable
        if child[2] in dict_var:
            exit("RedeclarationError")
        else:
            dict_var[child[2]] = {"vartype": child[1], "varvalue": evaluate_child(child[3])}
            return ""
        
    elif child[0] == "onlyassign": #assignment of a variable
        
        var_exists, dict_var = is_in_dict_list(child[1])

        if not var_exists:
            return("Variable does not exist.")
        else:
            dict_var[child[1]]["varvalue"] = evaluate_child(child[2])
            return ""
            
    elif child[0] == "getvar": #retrieving a variable
        
        var_exists, dict_var = is_in_dict_list(child[1])

        if not var_exists:
            return("Trying to retrieve an undeclared variable.")
        else:
            varname = child[1]
            return dict_var[varname]["varvalue"]
        
    elif child[0] == "print":
        array = child[1]
        result = ""
        index = 0
        
        while index < len(array):
            result = result + str(evaluate_child(array[index])) + " "
            index = index + 1
        
        return result
        
    elif child[0] == "+":
        # print(child)
        if (isinstance(evaluate_child(child[1]),int) or isinstance(evaluate_child(child[1]),str) or isinstance(evaluate_child(child[1]),float)) and (isinstance(evaluate_child(child[2]),int) or isinstance(evaluate_child(child[2]),str) or isinstance(evaluate_child(child[2]),float)):
            if ((isinstance(evaluate_child(child[2]),str)) and (isinstance(evaluate_child(child[1]),int) or isinstance(evaluate_child(child[1]),float))) or ((isinstance(evaluate_child(child[1]),str)) and (isinstance(evaluate_child(child[2]),int) or isinstance(evaluate_child(child[2]),float))):
                exit("TypeError")
            else:
                return evaluate_child(child[1]) + evaluate_child(child[2])
        else:
            return "This operation cannot be applied on this type."
    
    elif child[0] == "-":
        if (isinstance(evaluate_child(child[1]),int) or isinstance(evaluate_child(child[1]),float)) and (isinstance(evaluate_child(child[2]),int) or isinstance(evaluate_child(child[2]),float)):
            return evaluate_child(child[1]) - evaluate_child(child[2])
        else:
            return "This operation cannot be applied on this type."
        
    elif child[0] == "*":
        if (isinstance(evaluate_child(child[1]),int) or isinstance(evaluate_child(child[1]),float)) and (isinstance(evaluate_child(child[2]),int) or isinstance(evaluate_child(child[2]),float)):
            return evaluate_child(child[1]) * evaluate_child(child[2])
        else:
            return "This operation cannot be applied on this type."
        
    elif child[0] == "/":
        if (isinstance(evaluate_child(child[1]),int) or isinstance(evaluate_child(child[1]),float)) and (isinstance(evaluate_child(child[2]),int) or isinstance(evaluate_child(child[2]),float)):
            return evaluate_child(child[1]) / evaluate_child(child[2])
        else:
            return "This operation cannot be applied on this type."

    elif child[0] == "^":
        if (isinstance(evaluate_child(child[1]),int) or isinstance(evaluate_child(child[1]),float)) and (isinstance(evaluate_child(child[2]),int) or isinstance(evaluate_child(child[2]),float)):
            return evaluate_child(child[1]) ** evaluate_child(child[2])
        else:
            return "This operation cannot be applied on this type."
        
    elif child[0] == "%":
        if (isinstance(evaluate_child(child[1]),int) or isinstance(evaluate_child(child[1]),float)) and (isinstance(evaluate_child(child[2]),int) or isinstance(evaluate_child(child[2]),float)):
            return evaluate_child(child[1]) % evaluate_child(child[2])
        else:
            return "This operation cannot be applied on this type."
        
    elif child[1] == "++":
        if isinstance(evaluate_child(child[0]),int):
            variable_name = child[0][1]
            variable_value = evaluate_child(('getvar', variable_name))
            return evaluate_child(('onlyassign', variable_name,  evaluate_child(('+', variable_value , 1))))  
        else:
            return "This operation cannot be applied on this type."
        
    elif child[1] == "--":
        if isinstance(evaluate_child(child[0]),int):
            variable_name = child[0][1]
            variable_value = evaluate_child(('getvar', variable_name))
            return evaluate_child(('onlyassign', variable_name,  evaluate_child(('-', variable_value , 1))))  
        else:
            return "This operation cannot be applied on this type."
        
    elif child[1] == "--":
        if (isinstance(evaluate_child(child[0]),int)):
            prev_val = dict_var[child[0][1]]["varvalue"]
            dict_var[child[0][1]]["varvalue"] = prev_val-1
            return dict_var[child[0][1]]["varvalue"]
        else:
            return "This operation cannot be applied on this type."
        
    elif child[0] == "or":
        return evaluate_child(child[1]) or evaluate_child(child[2])
    
    elif child[0] == "and":
        return evaluate_child(child[1]) and evaluate_child(child[2])
    
    elif child[0] == "not":
        return not evaluate_child(child[1]) 
    
    elif child[0] == ">":
        if (isinstance(evaluate_child(child[1]),int) or isinstance(evaluate_child(child[1]),float)) and (isinstance(evaluate_child(child[2]),int) or isinstance(evaluate_child(child[2]),float)):
            return evaluate_child(child[1]) > evaluate_child(child[2])
        else:
            return "This operation cannot be applied on this type."
        
    elif child[0] == "<":
        if (isinstance(evaluate_child(child[1]),int) or isinstance(evaluate_child(child[1]),float)) and (isinstance(evaluate_child(child[2]),int) or isinstance(evaluate_child(child[2]),float)):
            return evaluate_child(child[1]) < evaluate_child(child[2])
        else:
            return "This operation cannot be applied on this type."
        
    elif child[0] == ">=":
        if (isinstance(evaluate_child(child[1]),int) or isinstance(evaluate_child(child[1]),float)) and (isinstance(evaluate_child(child[2]),int) or isinstance(evaluate_child(child[2]),float)):
            return evaluate_child(child[1]) >= evaluate_child(child[2])
        else:
            return "This operation cannot be applied on this type."
        
    elif child[0] == "<=":
        if (isinstance(evaluate_child(child[1]),int) or isinstance(evaluate_child(child[1]),float)) and (isinstance(evaluate_child(child[2]),int) or isinstance(evaluate_child(child[2]),float)):
            return evaluate_child(child[1]) <= evaluate_child(child[2])
        else:
            return "This operation cannot be applied on this type."
        
    elif child[0] == "==":
        return evaluate_child(child[1]) == evaluate_child(child[2])
    
    elif child[0] == "!=":
        return evaluate_child(child[1]) != evaluate_child(child[2])
    
    elif child[0] == "for":
        # print(child)
        variablename = child[2]
        initialvalue = child[3]
        condition = child[4]
        update = child[5]
        code = child[6][1]        
        dict_list.append({})
        dict_var = dict_list[-1]
        evaluate_child(('declaringassign', 'int', variablename, initialvalue))
        
        if code == [None]:
            code = []
            
        while(evaluate_child(condition)):
            i = 0
            dict_list.append({})
            while i < len(code):             
                print(evaluate_child(code[i]))
                i += 1

            evaluate_child(update)
            value = evaluate_child(('getvar', variablename))

            dict_list.pop(-1)
            
            dict_var[variablename]["varvalue"] = value
        
        dict_list.pop(-1)
        return ""
    
    elif child[0] == "struct":
        if child[1] == "struct_init":
            structname = child[2]
            block = child[3]
            l = 0
            while l != len(block):
                lineexec = block[l]
                if lineexec[0] == "declaringassign":
                    if lineexec[2] in dict_var:
                            exit("RedeclarationError")
                    else:
                        struct_var[lineexec[2]] = {"vartype": lineexec[1], "varvalue": evaluate_child(lineexec[3]), "sname": structname}
                        activestruct = structname
                elif lineexec[0] == "declaring":
                    if lineexec[2] in dict_var:
                            exit("RedeclarationError")
                    else:
                        struct_var[lineexec[2]] = {"vartype": lineexec[1], "varvalue": 0,  "sname": structname}
                        activestruct = structname
                else:
                    exit("can't perform this function in struct")
                l +=1
            return ""            
        elif child[1] == "struct_d":
            structfamily = child[2]
            structchild = child[3]
            if structfamily == activestruct:
                for key in struct_var:
                    struct_exit[structchild] = copy.deepcopy(struct_var)
            else:
                exit("Error while declaring struct")
            return ""
        elif child[1] == "struct_assign":
            childname = child[2]
            assignment = child[3]
            assvar = assignment[1]
            assvalue = assignment[2]
            if assvar in struct_var:
                for key in struct_exit:
                    if key == childname:
                        struct_exit[childname][assvar]["varvalue"] = assvalue
            return ""
        elif child[1] == "struct_getdata":
            childname = child[2]
            assvar = child[3]
            if assvar in struct_var:
                for key in struct_exit:
                    if key == childname:
                        return struct_exit[key][assvar]["varvalue"]
        return ""
    return ""

def evaluate_tree(tree):
    for child in tree:
        s = evaluate_child(child)
        if s == "":
            pass
        else:
            print(s)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        fname = sys.argv[1]
        with open("./testcases/"+fname, 'r') as f:
            getfile = f.read()

        lexer = lex.lex(module = lexer)
        lexer.input(getfile)
        parser = yacc.yacc(module=parser)
        getree = parser.parse(getfile, lexer=lexer)

        evaluate_tree(getree)
        
    else:
        print('No such file.')