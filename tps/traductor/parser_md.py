import ply.yacc as yacc
from lexer_md import tokens
from ag_generar_tag_html import generar_tag_html

html = ['<html>', '<body>']

def p_documento(p):
    '''
    documento : documento elemento
              | elemento
    '''
    
def p_elemento_h1(p):
    'elemento : H1 TEXT'
    tag = generar_tag_html('h1', p[2])
    html.append(tag)

def p_elemento_h2(p):
    'elemento : H2 TEXT'
    tag = generar_tag_html('h2', p[2])
    html.append(tag)

def p_elemento_item(p):
    'elemento : ITEM TEXT'
    tag = generar_tag_html('li', p[2])
    html.append(tag)

def p_error(p):
    html.append('Error sintáctico')

parser = yacc.yacc()
