items = []
n = 0
i = 0
j = 0
swapped = False
estado = True 

def init(vals):
    global items, n, i, j, swapped, estado
    items = list(vals)
    n = len(items)
    i = 0
    j = 0
    swapped = False
    estado = True

def step():
    global items, n, i, j, swapped, estado

    if i >= n - 1:
        return {"done": True}
    if estado:
        a = j
        b = j + 1

        hubo_swap = False

        if items[a] > items[b]:
            items[a], items[b] = items[b], items[a]
            swapped = True          
            hubo_swap = True

        j += 1

        if j >= (n - 1 - i):
            estado = False 
        return {"a": a, "b": b, "swap": hubo_swap, "done": False}
    else:
        if not swapped:
            return {"done": True}  
        i += 1
        j = 0
        swapped = False
        estado = True
        return {"a": 0, "b": 0, "swap": False, "done": False}
