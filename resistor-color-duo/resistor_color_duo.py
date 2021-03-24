def value(colors):
    codigo_color = {'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4,
                    'green': 5, 'blue': 6, 'violet': 7, 'grey': 8, 'white': 9}
    codigo = [str(codigo_color[x]) for x in colors[:2]]
    return int(''.join(codigo))
