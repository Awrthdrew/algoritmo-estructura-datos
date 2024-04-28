# se crea la clase Tag
class Tag:
    def __init__(self, n, i):
        self.tag = n
        self.id = i
        self.childs = []

# se crea una función recursiva para imprimir la estructura del árbol en un formato HTML
def print_html(tag, indent=''):
    print(f"{indent}<{tag.tag}{' id=' + str(tag.id) if tag.id else ''}>")
    for child in tag.childs:
        print_html(child, indent + '    ')
    print(f"{indent}</{tag.tag}>")

# se crea estructura del árbol DOM de HTML
html = Tag("html", None)
html.childs.append(Tag("head", None))
html.childs.append(Tag("body", None))
html.childs[1].childs.append(Tag("header", None))
html.childs[1].childs.append(Tag("article", None))
html.childs[1].childs.append(Tag("footer", None))
html.childs[1].childs[1].childs.append(Tag("div", "content"))
html.childs[1].childs[1].childs[0].childs.append(Tag("p", "text"))

# se imprime estructura del árbol llamando a la función recursiva
print_html(html)
