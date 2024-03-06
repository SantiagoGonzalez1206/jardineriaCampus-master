import storage.cliente as cli

def getNombreClientesEspaña():
    NombreClientesEspaña = []
    for val in cli.clientes:
        if val.get('pais') == "Spain" :
            NombreClientesEspaña.append(
                {
                    "nombre_cliente": val.get("nombre_cliente")
                }
            )  
    return NombreClientesEspaña