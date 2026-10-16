import sys
from lexer_md import lexer
from parser_md import parser, html

entrada = open(sys.argv[1], 'r').read()
parser.parse(entrada)
if 'Error sintáctico' in html:
    html.clear()
    html.append('Error sintáctico')
else:
    html.append('</body>')
    html.append('</html>')

archivo = open(f'{sys.argv[1]}.html', 'w')
for linea in html:
    print(linea)
    archivo.write(linea + '\n')
archivo.close()
