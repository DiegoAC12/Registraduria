from Modelos.Partido import Partido
from Repositorios.RepositorioPartido import RepositorioPartido


class ControladorPartido():
    def __init__(self):
        self.repositorioPartido = RepositorioPartido()
        print("Creando ControladorPartido")

    def index(self):
        return self.repositorioPartido.findAll()

    def create(self, elPartido):
        nuevoPartido = Partido(elPartido)
        return self.repositorioPartido.save(nuevoPartido)

    def show(self, id):
        elPartido = Partido(self.repositorioPartido.findById(id))
        return elPartido.__dict__

    def update(self, id, elPartido):
        partidoActual = Partido(self.repositorioPartido.findById(id))
        partidoActual.nombre = elPartido["nombre"]
        partidoActual.lema = elPartido["lema"]
        return self.repositorioPartido.save(partidoActual)

    def delete(self, id):
        return self.repositorioPartido.delete(id)