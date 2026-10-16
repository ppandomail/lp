import subprocess
from pathlib import Path


def test_caso_feliz():
    md_file = Path("traductor/caso_feliz.md")
    
    resultado = subprocess.run(
        ['python', 'traductor/main.py', str(md_file)],
        capture_output=True,
        text=True
    )

    assert resultado.returncode == 0

    html_generado = Path("traductor/caso_feliz.md.html")

    assert html_generado.exists()

    actual = html_generado.read_text(encoding="utf-8")
    esperado = '''
                <html>
                <body>
                <h1>UNO</h1>
                <h2>Tecn Web</h2>
                <li>PW1</li>
                <li>LP</li>
                <li>BD</li>
                </body>
                </html>
                '''
    
    assert actual.replace('\n', '').replace(' ', '') == esperado.replace('\n', '').replace(' ', '')

def test_caso_no_feliz():
    md_file = Path("traductor/caso_error_sintax.md")
    
    resultado = subprocess.run(
        ['python', 'traductor/main.py', str(md_file)],
        capture_output=True,
        text=True
    )

    assert resultado.returncode == 0

    html_generado = Path("traductor/caso_error_sintax.md.html")

    assert html_generado.exists()

    actual = html_generado.read_text(encoding="utf-8")
    esperado = '''
               Error sintáctico
               '''
    
    assert actual.replace('\n', '').replace(' ', '') == esperado.replace('\n', '').replace(' ', '')
