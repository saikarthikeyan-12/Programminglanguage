class Node:
    def __init__(self):
        self.parent = None
        #print("init node")

    def parentCount(self):
        count = 0
        current = self.parent
        while current is not None:
            count += 1
            current = current.parent
        return count

class NumberNode(Node):
    def __init__(self,number):
        if type(number)==str:
            if 'e' in number:
                self.value = float(number)
            elif '.' in number:
                self.value = float(number)
            elif'E' in number:
                self.value = float(number)
            else:
                self.value = int(number)
    def eval(self):
        return self.value

class StringNode(Node):
    def __init__(self, value):
        self.value = value
    def eval(self):
        return self.value[1:-1]

class BooleanNode(Node):
    def __init__(self, booleanexp):
        if (booleanexp == 'False'):
            self.value = False
        else:
            self.value = True
    def eval(self):
        return self.value

class VARNODE(Node):
    def __init__(self, value):
        self.value = value

    def retrievename(self):
        return self.value

    def eval(self):
        if self.value in execlist:
            return execlist[self.value]
        else:
            raise ValueError("ERROR")

class PrintNode(Node):
    def __init__(self, printval):
        self.printval = printval

    def eval(self):
        if (self.printval.eval() is not None):
            if (type(self.printval)==StringNode):
                print(self.printval.eval())
            elif (type(self.printval.eval())==str):
                print('\'' + self.printval.eval()+ '\'')
            else:
                print(self.printval.eval())
        else:
            raise ValueError("error")

class Tuplee(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def eval(self):
        return (self.left.eval(), self.right.eval())


class TupleeInsert(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def eval(self):
        return self.left.eval() + (self.right.eval(),)

class TupleCurrIndex(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def eval(self):
        try:
            if type(self.left.eval())==int and type(self.right.eval())== tuple:
                if (self.left.eval() <= len(self.right.eval()) and self.left.eval() > 0):
                    return self.right.eval()[self.left.eval() - 1]
        except:
            raise ValueError("ERROR")

class ListNode(Node):
    def __init__(self, val):
        self.val = val
    def eval(self):
        return [self.val.eval()]
    def retrievename(self):
        try:
            return [self.val.retrievename()]
        except:
            raise ValueError("ERROR")

class ListNodeAPPEND(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self):
        return self.left.eval() + [self.right.eval()]

    def retrievename(self):
        try:
            return self.left.retrievename() + [self.right.retrievename()]
        except:
            raise ValueError("error")

class ListNodeINDEXCHECKER(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def eval(self):
        try:
            if (isinstance(self.left.eval(), (list, str)) and isinstance(self.right.eval(), list)):
                if (len(self.right.eval()) == 1):
                    y = self.right.eval()[0]
                    if (y < len(self.left.eval())):
                        return self.left.eval()[y]
        except:
            raise ValueError("ERROR")

class PLUS(Node):
    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right

    def eval(self):
        left = self.left.eval()
        right = self.right.eval()
        if (check_intFloat(left, right) == True or check_intFloat(right,left) == True or check_sametype(left, right) == int or check_sametype(left, right) == float) or check_sametype(left, right) == str or (check_sametype(left, right) == list):
                return  left + right
        else:
            raise ValueError("ERROR")

class MINUS(Node):
    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right

    def eval(self):
        left = self.left.eval()
        right = self.right.eval()

        if (check_intFloat(left, right) == True or check_intFloat(right,left) == True or check_sametype(left, right) == int or check_sametype(left, right) == float):
                return  left - right
        else:
            raise ValueError("ERROR")


class MULTIPLY(Node):
    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right

    def eval(self):
        left = self.left.eval()
        right = self.right.eval()

        if (check_intFloat(left, right) == True or check_intFloat(right,left) == True or check_sametype(left, right) == int or check_sametype(left, right) == float):
                return  left * right
        else:
            raise ValueError("ERROR")

class DIVIDE(Node):
    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right

    def eval(self):
        left = self.left.eval()
        right = self.right.eval()

        if (check_intFloat(left, right) == True or check_intFloat(right,left) == True or check_sametype(left, right) == int or check_sametype(left, right) == float) and right!=0:
                return left / right
        else:
            raise ValueError("ERROR")

class EXPONENTIAL(Node):
    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right

    def eval(self):
        left = self.left.eval()
        right = self.right.eval()

        if (check_intFloat(left, right) == True or check_intFloat(right,left) == True or check_sametype(left, right) == int or check_sametype(left, right) == float):
                return  left ** right
        else:
            raise ValueError("ERROR")

class INTEGERDIVISION(Node):
    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right

    def eval(self):
        left = self.left.eval()
        right = self.right.eval()

        if (check_sametype(left, right) == int ) and right!=0:
                return  left // right
        else:
            raise ValueError("ERROR")

class MODULUS(Node):
    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right

    def eval(self):
        left = self.left.eval()
        right = self.right.eval()
        if (check_sametype(left, right) == int ) and right!=0:
                return  left % right
        else:
            raise ValueError("ERROR")


class NOTBOOL(Node):
    def __init__(self, child):
        self.child = child

    def eval(self):
        if type(self.child.eval()) == bool:
            return not self.child.eval()
        else:
            raise ValueError("ERROR")

class ANDALSOBOOL(Node):
    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right

    def eval(self):
        left = self.left.eval()
        right = self.right.eval()

        if type(left)==bool and type(right)==bool:
                return  left and right
        else:
            raise ValueError("ERROR")

class ORELSEBOOL(Node):
    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right

    def eval(self):
        left = self.left.eval()
        right = self.right.eval()

        if type(left)==bool and type(right)==bool:
                return  left or right
        else:
            raise ValueError("ERROR")
class LESSTHANOPERTATORCHECK(Node):
    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right

    def eval(self):
        left = self.left.eval()
        right = self.right.eval()

        if (check_intFloat(left, right) == True or check_intFloat(right, left) == True or check_sametype(left,right) == int or check_sametype(left, right) == float) or check_sametype(left, right) == str:
            return  left < right
        else:
            raise ValueError("ERROR")

class LESSTHANEQUALTOOPERTATORCHECK(Node):
    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right

    def eval(self):
        left = self.left.eval()
        right = self.right.eval()

        if (check_intFloat(left, right) == True or check_intFloat(right, left) == True or check_sametype(left,right) == int or check_sametype(left, right) == float) or check_sametype(left, right) == str:
            return  left <= right
        else:
            raise ValueError("ERROR")

class GREATERTHANOPERTATORCHECK(Node):
    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right

    def eval(self):
        left = self.left.eval()
        right = self.right.eval()

        if (check_intFloat(left, right) == True or check_intFloat(right, left) == True or check_sametype(left,right) == int or check_sametype(left, right) == float) or check_sametype(left, right) == str:
            return  left > right
        else:
            raise ValueError("ERROR")

class GREATERTHANEQUALTOOPERTATORCHECK(Node):
    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right

    def eval(self):
        left = self.left.eval()
        right = self.right.eval()

        if (check_intFloat(left, right) == True or check_intFloat(right, left) == True or check_sametype(left,right) == int or check_sametype(left, right) == float) or check_sametype(left, right) == str:
            return  left >= right
        else:
            raise ValueError("ERROR")
class EQUALTOOOPERATOR(Node):
    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right

    def eval(self):
        left = self.left.eval()
        right = self.right.eval()

        if (check_intFloat(left, right) == True or check_intFloat(right, left) == True or check_sametype(left,right) == int or check_sametype(left, right) == float) or check_sametype(left, right) == str:
            return  left == right
        else:
            raise ValueError("ERROR")

class NOTEQUALTOOOPERATOR(Node):
    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right

    def eval(self):
        left = self.left.eval()
        right = self.right.eval()

        if (check_intFloat(left, right) == True or check_intFloat(right, left) == True or check_sametype(left,right) == int or check_sametype(left, right) == float) or check_sametype(left, right) == str:
            return  left != right
        else:
            raise ValueError("ERROR")

class UMinus(Node):
    def __init__(self, v):
        super().__init__()
        self.val = v.eval()

    def eval(self):
        return -1*self.val

class MEMBER(Node):
    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right

    def eval(self):
        if type(self.right.eval()) == str or type(self.right.eval()) == list:
                return self.left.eval() in self.right.eval()
        else:
            raise ValueError("ERROR")

class CONCAT(Node):
    def __init__(self, left, right):
        super().__init__()
        self.left = left
        self.right = right

    def eval(self):
        if type(self.right.eval()) == list:
                return [self.left.eval()] + self.right.eval()
        else:
            raise ValueError("ERROR")

class CurrNode(Node):
    def __init__(self, firststatement, secondstatement):
        self.firststatement = firststatement
        self.secondstatement = secondstatement

    def eval(self):
        if self.firststatement is not 0:
            self.firststatement.eval()
        if self.secondstatement is not 0:
            self.secondstatement.eval()


class SimpleAssignment(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def eval(self):
        execlist[self.left.retrievename()] = self.right.eval()

class ListAssignment(Node):
    def __init__(self, left, right, value):
        self.left = left
        self.right = right
        self.value = value
    def eval(self):
        try:
            execlist[self.left.retrievename()][self.right.eval()[0]] = self.value.eval()
        except:
            raise ValueError("ERROR")

class IfChecker(Node):
    def __init__(self, booleanexpression, statement):
        self.booleanexpression = booleanexpression
        self.statement = statement
    def eval(self):
        if (self.booleanexpression.eval() == True):
            self.statement.eval()
        else:
            return Exception("ERROR")

class IFELSECHECKER(Node):
    def __init__(self, booleanexpression, statement1,statement2):
        self.booleanexpression = booleanexpression
        self.statement1 = statement1
        self.statement2 = statement2

    def eval(self):
        try:
            if (self.booleanexpression.eval() == True):
                self.statement1.eval()
            else:
                self.statement2.eval()
        except:
            raise ValueError("Error")


class WhileChecker(Node):
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

    def eval(self):
        if type(self.v1.eval())== bool:
            recurvar = self.v1.eval()
            while recurvar is True:
                if self.v2 is not 0:
                    self.v2.eval()
                recurvar = self.v1.eval()
                if not isinstance(recurvar, bool):
                    raise ValueError("ERROR")
        else:
            return ValueError

class ProgramExecution(Node):
    def __init__(self, code):
        self.code=code
    def eval(self):
        self.code.eval()


class SupportFunction(Node):
    def __init__(self, functioname, parameters, code, expression):
        self.functioname = functioname.retrievename()
        self.code = code
        self.expression = expression
        if parameters is 0:
            self.parameters = 0
        else:
            self.parameters = parameters.retrievename()

    def retrieveparameters(self):
        return self.parameters

    def retrieveexpression(self):
        return self.expression

    def retrievecode(self):
        return self.code

    def eval(self):
       try:
            procedure[self.functioname] = self
       except:
           raise ValueError("ERROR")

def firstargchecker(function):
    firstargument = function.retrieveparameters()
    if firstargument is 0:
        firstargument = []
    return firstargument

def secondargchecker(secondarg):
    if secondarg is 0:
        secondargument = []
    else:
        secondargument= secondarg.eval()
    return secondargument


class InvokerNode(Node):
    def __init__(self, name, parameters):
        self.name = name.retrievename()
        self.parameters = parameters
    def eval(self):
        try:
            function = procedure[self.name]
            firstargument = firstargchecker(function)
            secondargument = secondargchecker(self.parameters)
            callstack.append(dict(execlist))
            execlist.clear()
            for elem in range(len(firstargument)):
                execlist[firstargument[elem]] = secondargument[elem]
            function.retrievecode().eval()
            returnval = function.retrieveexpression().eval()
            val = callstack.pop()
            execlist.clear()
            for copy_var in val.keys():
                execlist[copy_var] = val[copy_var]
            return returnval
        except:
            raise ValueError("ERROR")


class FunctionListNode(Node):
    def __init__(self, listoffunctions, functions):
        self.listoffunctions = listoffunctions
        self.functions = functions
    def eval(self):
        self.listoffunctions.eval()
        self.functions.eval()

class CompleteNode(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def eval(self):
      self.left.eval()
      self.right.eval()

def check_sametype(x,y):
    if(type(x)==type(y)):
        return type(x)
    else:
        return False


def check_intFloat(x,y):
    if(type(x)==int and type(y)==float):
        return True
    else:
        return False

class ListEmpty(Node):
    def __init__(self ):
        pass
    def eval(self):
        return []

class TupleEmpty(Node):
    def __init__(self ):
        pass
    def eval(self):
        return ()


reserved = {
    'print': 'PRINT',
    'andalso': 'CONJUNCTIONBOOLEAN',
    'orelse': 'DISJUNCTIONBOOLEAN',
    'div': 'INTEGERDIVISION',
    'mod': 'MODULUS',
    'not': 'NOTBOOLEAN',
    'in': 'MEMBER',
    'True': 'TRUE',
    'False': 'FALSE',
    'if': 'IF',
    'while': 'WHILE',
    'else': 'ELSE',
    'fun': 'FUNCTION'
}

tokens = (
'LEFTPARENTHESIS',
'RIGHTPARENTHESIS',
'INDEX',
'NUMBER',
'PLUS',
'MINUS',
'MULTIPLY',
'DIVIDE',
'EXPONENTIAL',
'STRING',
'LESSTHAN',
'LESSTHANEQUALTO',
'GREATERTHAN',
'GREATERTHANOREQUAL',
'EQUALTO',
'NOTEQUALTO',
'LEFTSQUARE',
'RIGHTSQUARE',
'COMMA',
'APPEND',
'SEMICOLON',
'LEFTCURLY',
'RIGHTCURLY',
'VAR',
'EQUAL'
) + tuple(reserved.values())

# Tokens
t_LEFTPARENTHESIS = r'\('
t_RIGHTPARENTHESIS = r'\)'
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'/'
t_EXPONENTIAL = r'\*\*'
t_LESSTHAN = r'<'
t_LESSTHANEQUALTO = r'<='
t_EQUALTO = r'=='
t_NOTEQUALTO = r'<>'
t_GREATERTHAN = r'>'
t_GREATERTHANOREQUAL = r'>='
t_LEFTSQUARE=r'\['
t_RIGHTSQUARE = r']'
t_COMMA = r','
t_APPEND = r'::'
t_INDEX = r'\#'
t_SEMICOLON = r'\;'
t_RIGHTCURLY = r'\}'
t_LEFTCURLY = r'\{'
t_EQUAL = r'\='
procedure = {}
callstack = []
execlist={}

def t_VARIABLE(t):
    r'[A-Za-z][A-Za-z0-9_]*'
    t.type = reserved.get(t.value, 'VAR')
    if t.type is 'VAR':
        t.value = VARNODE(t.value)
    if t.type is 'TRUE' or t.type is 'FALSE':
        t.value = BooleanNode(t.value)
    return t

def t_STRING(t):
    r'\"((\\\")|[^\"])*\"|\'((\\\')|[^\'])*\''
    t.value = StringNode(t.value)
    return t

def t_NUMBER(t):
    r'(\d*(\d\.|\.\d)\d*|\d+)([Ee][+-]?\d+)?'
    t.value = NumberNode(t.value)
    return t

t_ignore = " \t\n"

def t_error(t):
    raise SyntaxError("error")

import ply.lex as lex
lex.lex(debug=0)
precedence = (
    ('left', 'DISJUNCTIONBOOLEAN'),
    ('left', 'CONJUNCTIONBOOLEAN'),
    ('left', 'NOTBOOLEAN'),
    ('left', 'EQUALTO', 'NOTEQUALTO', 'LESSTHAN', 'LESSTHANEQUALTO', 'GREATERTHAN', 'GREATERTHANOREQUAL'),
    ('right', 'APPEND'),
    ('left', 'MEMBER'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTIPLY', 'DIVIDE', 'INTEGERDIVISION', 'MODULUS'),
    ('right', 'EXPONENTIAL'),
    ('left', 'LEFTSQUARE', 'RIGHTSQUARE', 'INDEX'),
    ('left', 'LEFTPARENTHESIS', 'RIGHTPARENTHESIS'),
)

def p_entirecode(p):
    '''entirecode : functionlist code_excution'''
    p[0] = CompleteNode(p[1], p[2])

def p_entirecoderecur(p):
    '''entirecode : code_excution'''
    p[0] = p[1]

def p_function_list(p):
    '''functionlist : functionlist function'''
    p[0] = FunctionListNode(p[1], p[2])

def p_function_list2(p):
    '''functionlist : function '''
    p[0] = p[1]

def p_method(p):
    '''function : FUNCTION VAR LEFTPARENTHESIS list_val RIGHTPARENTHESIS EQUAL block prop SEMICOLON'''
    p[0] = SupportFunction(p[2], p[4], p[7], p[8])

def p_method2(p):
    '''function : FUNCTION VAR LEFTPARENTHESIS RIGHTPARENTHESIS EQUAL block prop SEMICOLON '''
    p[0] = SupportFunction(p[2], 0, p[6], p[7])

def p_invoker(p):
    '''invok : VAR LEFTPARENTHESIS list_val RIGHTPARENTHESIS'''
    p[0] = InvokerNode(p[1], p[3])

def p_invokerwithoutlist(p):
    '''invok : VAR LEFTPARENTHESIS RIGHTPARENTHESIS '''
    p[0] = InvokerNode(p[1], 0)

def p_code_execution(p):
    '''code_excution : block '''
    p[0] = ProgramExecution(p[1])

def p_program(p):
    '''block : LEFTCURLY blockhead RIGHTCURLY'''
    p[0] = p[2]
def p_emptyCurly(p):
    ''' block : LEFTCURLY RIGHTCURLY'''
    p[0] = CurrNode(0, 0)
def p_block(p):
    '''blockhead : blockhead statement'''
    p[0] = CurrNode(p[1], p[2])
def p_block2(p):
    '''blockhead : statement'''
    p[0] = p[1]
def p_valcheck(p):
    '''equate : VAR EQUAL prop SEMICOLON'''
    p[0] = SimpleAssignment(p[1], p[3])
def p_assignment2(p):
    '''equate : VAR list EQUAL prop SEMICOLON'''
    p[0] = ListAssignment(p[1],p[2],p[4])

def p_if_statement(p):
    '''ifstatement : IF LEFTPARENTHESIS prop RIGHTPARENTHESIS block'''
    p[0] = IfChecker(p[3], p[5])

def p_if_else(p):
    '''ifelsestatement : IF LEFTPARENTHESIS prop RIGHTPARENTHESIS block ELSE block'''
    p[0] = IFELSECHECKER(p[3], p[5], p[7])

def p_while_statement(p):
    '''whilestatement : WHILE LEFTPARENTHESIS prop RIGHTPARENTHESIS block'''
    p[0] = WhileChecker(p[3], p[5])

def p_statement(p):
    '''statement : invok SEMICOLON
                 | printstatement
                 | ifstatement
                 | equate
                 | ifelsestatement
                 | whilestatement
                 | block   '''

    p[0] = p[1]
def p_printstatement(p):
    """printstatement : PRINT LEFTPARENTHESIS prop RIGHTPARENTHESIS SEMICOLON"""
    p[0] = PrintNode(p[3])

def p_pound(p):
    '''poundexp : INDEX prop'''
    #print(p[2])
    p[0] = p[2]

def p_indexuple(p):
    '''prop : poundexp tuple'''
    p[0] = TupleCurrIndex(p[1],p[2])

def p_indexuplerend(p):
    '''prop : poundexp LEFTPARENTHESIS prop RIGHTPARENTHESIS'''
    p[0] = TupleCurrIndex(p[1], p[3])

def p_wholetuple(p):
    '''tuple : LEFTPARENTHESIS tuple RIGHTPARENTHESIS'''
    p[0] = p[2]

def p_tupleempty(p):
    '''tuple : LEFTPARENTHESIS RIGHTPARENTHESIS'''
    p[0] = TupleEmpty()

def p_tuple(p):
    '''tuple : LEFTPARENTHESIS tuple_val RIGHTPARENTHESIS'''
    p[0] = p[2]

def p_brackets(p):
    '''prop : prop list '''
    p[0] = ListNodeINDEXCHECKER(p[1], p[2])

def p_list(p):
    '''list : LEFTSQUARE  list_val RIGHTSQUARE'''
    #print("this",p[2].eval())
    p[0] = p[2]

def p_Listempty(p):
    '''list : LEFTSQUARE RIGHTSQUARE'''
    p[0] = ListEmpty()

def p_list_val(p):
    '''list_val : prop'''
    p[0] = ListNode(p[1])
    #print(p[0].eval())

def p_parenthesis(p):
    '''prop : LEFTPARENTHESIS prop RIGHTPARENTHESIS'''
    p[0] = p[2]

def p_lists2(p):
    '''list_val : list_val COMMA prop'''
    p[0] = ListNodeAPPEND(p[1], p[3])

def p_expression_add(p):
    '''prop : prop PLUS prop'''
    p[0] = PLUS(p[1],p[3])

def p_expression_sub(p):
    '''prop : prop MINUS prop'''
    p[0] = MINUS(p[1],p[3])


# def p_in_tuple(p):
#     """tuple_val : tuple_val COMMA prop
#                     | prop """
    # if len(p) > 2:
        # p[1].append(p[3])
        # p[0] = p[1]
        # print(p[1].eval())

    # else:
    #     print("HIww",p[1].eval())
    #     p[0] = TupleValueNode(p[1])
#
#
# def p_tuple(p):
#     '''tuple : LEFTPARENTHESIS RIGHTPARENTHESIS
#              | LEFTPARENTHESIS  tuple_val RIGHTPARENTHESIS'''
#     print(p[2].eval())
    # if len(p) > 3:
    #     p[0] = p[2]
    # else:
    #     p[0] = ()
#
# def p_ListRecur(t):
#     """listval : listval COMMA prop
#                  | prop """
#     if len(t)>2:
#         t[1].append(t[3])
#         t[0] = t[1]
#     else:
#         t[0] = ListValueNode(t[1])
#
# def p_list(p):
#     '''list : LEFTSQUARE listval RIGHTSQUARE
#               | LEFTSQUARE RIGHTSQUARE'''
#     if len(p)>3:
#         p[0]=p[2]
#     else:
#        p[0] = []
#
# def p_index(p):
#     '''prop : prop LEFTSQUARE prop RIGHTSQUARE'''
#     if type(p[1].eval())==str or type(p[1].eval())==list:
#         p[0] = CheckIndex(p[1],p[3])

def p_tuple_val(p):
    '''tuple_val : prop COMMA prop'''
    p[0] = Tuplee(p[1], p[3])

def p_tuple_valzz(p):
    '''tuple_val : tuple_val COMMA prop'''
    p[0] = TupleeInsert(p[1], p[3])

def p_expression_mult(p):
    '''prop : prop MULTIPLY prop'''
    p[0] = MULTIPLY(p[1],p[3])

def p_expression_div(p):
    '''prop : prop DIVIDE prop'''
    p[0] = DIVIDE(p[1],p[3])

def p_prop_INTEGERDIVISION(p):
    '''prop : prop INTEGERDIVISION prop'''
    p[0] = INTEGERDIVISION(p[1],p[3])

def p_prop_MODULUS(p):
    '''prop : prop MODULUS prop'''
    p[0] = MODULUS(p[1],p[3])

def p_expression_exponential(p):
    '''prop : prop EXPONENTIAL prop'''
    p[0] = EXPONENTIAL(p[1],p[3])

def p_prop_NOT(p):
    '''prop : NOTBOOLEAN prop'''
    p[0] = NOTBOOL(p[2])

def p_prop_ANDALSO(p):
    '''prop : prop CONJUNCTIONBOOLEAN prop'''
    p[0] = ANDALSOBOOL(p[1],p[3])

def p_prop_ORELSE(p):
    'prop : prop DISJUNCTIONBOOLEAN prop'
    #print("hi")
    p[0] = ORELSEBOOL(p[1],p[3])

def p_prop_LESSTHANOPERTATORCHECK(p):
    '''prop : prop LESSTHAN prop'''
    p[0] = LESSTHANOPERTATORCHECK(p[1],p[3])

def p_prop_LESSTHANEQUALTOOPERTATORCHECK(p):
    '''prop : prop LESSTHANEQUALTO prop'''
    p[0] = LESSTHANEQUALTOOPERTATORCHECK(p[1],p[3])

def p_prop_GREATERTHANOPERTATORCHECK(p):
    '''prop : prop GREATERTHAN prop'''
    p[0] = GREATERTHANOPERTATORCHECK(p[1],p[3])

def p_prop_GREATERTHANEQUALTOOPERTATORCHECK(p):
    '''prop : prop GREATERTHANOREQUAL prop'''
    p[0] = GREATERTHANEQUALTOOPERTATORCHECK(p[1],p[3])

def p_prop_EQUALTOOOPERATOR(p):
    '''prop : prop EQUALTO prop'''
    p[0] = EQUALTOOOPERATOR(p[1],p[3])

def p_prop_NOTEQUALTOOOPERATOR(p):
    '''prop : prop NOTEQUALTO prop'''
    p[0] = NOTEQUALTOOOPERATOR(p[1],p[3])

def p_p_prop_MEMBER(p):
    '''prop : prop MEMBER prop '''
    if(p[2]=='in'):
        p[0] = MEMBER(p[1],p[3])

def p_prop_CONCAT(p):
    'prop : prop APPEND prop'
    if (p[2] == '::'):
        p[0] = CONCAT(p[1], p[3])

def p_unary(p):
    '''prop : MINUS prop'''
    p[0] = UMinus(p[2])

def p_prop_datatype(p):
    '''prop : VAR
              | STRING
              | list
              | tuple
              | invok
              | NUMBER
              | TRUE
              | FALSE
    '''
    p[0] = p[1]

def p_error(t):
    raise SyntaxError("error")
import sys
import ply.yacc as yacc
parser=yacc.yacc(debug=1)

if (len(sys.argv) == 2):
    fd = open(sys.argv[1], 'r')
    linefromcode = fd.read();
    try:
        lex.input(linefromcode)
        while True:
            token = lex.token()
            if not token: break
        result = parser.parse(linefromcode).eval()
    except ValueError:
        print("Semantic ERROR")
    except SyntaxError:
        print("Syntax Error")
