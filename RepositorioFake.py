class RepositorioFake:
    def __init__(self):
        self.compras = [];
    
    def guardar(self, usuario, cantidad):
        self.compras.append({
            'usuario': usuario,
            'cantidad': cantidad
        })
        
# repositorio = RepositorioFake();
# repositorio.guardar("Athina", 3);
# repositorio.guardar("Renata", 2);
# print(repositorio.compras);