# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i = 0          # cabeza de la parte no ordenada
j = 0          # cursor que recorre y busca el mínimo
min_idx = 0    # índice del mínimo de la pasada actual
fase = "buscar"  # "buscar" | "swap"

def init(vals):
    global items, n, i, j, min_idx, fase
    items = list(vals)
    n = len(items)
    i = 0
    j = i + 1
    min_idx = i
    fase = "buscar"

def step():
    global items, n, i, j, min_idx, fase

    if i >= n - 1:
        
        return {"done": False}

    if fase == "buscar":
        if j < n:
            
            if items[j] < items[min_idx]:
                min_idx = j
            
            resultado = { 
                "done": False,
                "swap": False,
                "a": min_idx, 
                "b": j        
            }
            j += 1
            return resultado
        else:
            fase = "swap"  
            pass
  
    if fase == "swap":
       
        swap_hecho = (min_idx != i)
        if swap_hecho:
            items[i], items[min_idx] = items[min_idx], items[i]
        
        resultado = {
            "done": False,
            "swap": swap_hecho,
            "a": i,        
            "b": min_idx    
        }

        i += 1
        min_idx = i
        j = i + 1
        fase = "buscar"
        
        return resultado
    

    
    # TODO:
    # - Fase "buscar": comparar j con min_idx, actualizar min_idx, avanzar j.
    #   Devolver {"a": min_idx, "b": j_actual, "swap": False, "done": False}.
    #   Al terminar el barrido, pasar a fase "swap".
    # - Fase "swap": si min_idx != i, hacer ese único swap y devolverlo.
    #   Luego avanzar i, reiniciar j=i+1 y min_idx=i, volver a "buscar".
    #
    # Cuando i llegue al final, devolvé {"done": True}.
    