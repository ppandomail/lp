import ply.lex as lex

tokens = (
    'H1',
    'H2',
    'ITEM',
    'TEXT'
)

def t_H2(t):
    r'\#\#'
    return t

def t_H1(t):
    r'\#'
    return t

def t_ITEM(t):
    r'\*'
    return t

def t_TEXT(t):
    r'[^\n\#\*]+'
    t.value = t.value.strip()
    return t

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Carácter ilegal: {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()
