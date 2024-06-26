# 2 ESTRUCTURA DE ÁRBOL HTML
class Tag:
    def __init__(self, nodo, identacion):
        self.tag = nodo
        self.id = identacion
        self.childs = []

html = Tag("html", None)
html.childs.append(Tag("head", None))
html.childs.append(Tag("body", None))
html.childs[1].childs.append(Tag("header", None))
html.childs[1].childs.append(Tag("article", None))
html.childs[1].childs.append(Tag("footer", None))
html.childs[1].childs[1].childs.append(Tag("div", "content"))
html.childs[1].childs[1].childs[0].childs.append(Tag("p", "text"))

def print_html(tag, indent=''):
    arbol_html = []
    if tag.id:
        arbol_html.append(f"{indent}<{tag.tag} id='{tag.id}'>")
    else:
        arbol_html.append(f"{indent}<{tag.tag}>")
    for child in tag.childs:
        arbol_html.append(print_html(child, indent + '    '))
    arbol_html.append(f"{indent}</{tag.tag}>")
    return '\n'.join(arbol_html)

# Generar la estructura HTML como una cadena
html_estructura = print_html(html)

# Imprimir la estructura HTML
print(html_estructura)

# Guardar la estructura HTML en un archivo
with open(r'A:\Documents SSD\UAP\2° AÑO\algoritmo-estructura-datos\parciales\estructura_html.html', "w", encoding='utf8', newline="\n") as file:
    file.write(html_estructura)
