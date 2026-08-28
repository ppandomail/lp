import ply.lex as lex
import ply.yacc as yacc

# definir tokens
tokens = ('comienza', 'este', 'norte', 'oeste', 'sur')

# definir patrones
t_comienza = r'comienza'
t_este     = r'este'
t_norte    = r'norte'
t_oeste    = r'oeste'
t_sur      = r'sur'
t_ignore   = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Carácter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)

# construir scanner
lexer = lex.lex()

robot = {'x': 0, 'y':0}

# definir GIC
def p_sec(t):
    '''sec : sec instr 
           | comienza '''
    print(robot)

def p_instr_este(t):
    'instr : este'
    robot['x'] += 1

def p_instr_norte(t):
    'instr : norte'
    robot['y'] += 1

def p_instr_oeste(t):
    'instr : oeste'
    robot['x'] -= 1

def p_instr_sur(t):
    'instr : sur'
    robot['y'] -= 1

def p_error(t):
    print("Error sintáctico en '%s'" % t.value)

# construir parser
parser = yacc.yacc()
parser.parse('comienza oeste sur este este este norte norte')
