import ollama

def generar_tag_html(tag, texto):
    respuesta = ollama.chat(
        model='llama3.2',
        messages=[
            {
                'role': 'user',
                'content': f''' 
                Devuelve únicamente el HTML. 
                Sin explicaciones. 
                Sin markdown. 
                Sin texto adicional. 
                Genera el tag {tag} para el texto: {texto} 
                '''
            }
        ]
    )

    return respuesta['message']['content']
