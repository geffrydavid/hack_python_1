"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    result = "fooziman"
    result = result.upper()
    texto_lista = list(result)
    sustituciones = {
        'O': '0',
        'I': '1',
        'A': '@'
    }
    texto_lista = [sustituciones.get(i, i) for i in texto_lista]
    return texto_lista

print(fn_hack_10())