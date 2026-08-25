import ply.lex as lex

# definir tokens
tokens  = ('ENTERO', 'SUMA', 'PRODUCTO', 'INCREMENTO')

# definir patrones
t_SUMA       = r'\+'
t_PRODUCTO   = r'\*'
t_INCREMENTO = r'\*\*'

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# construir scanner
lexer = lex.lex()
lexer.input('25 + 5')
while 1:
    tok = lexer.token()
    if not tok: break
    print(tok)
