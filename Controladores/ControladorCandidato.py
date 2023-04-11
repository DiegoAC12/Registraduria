from Modelos.Candidato import Candidato
from Modelos.Partido import Partido
from Repositorios.RepositorioCandidato import RepositorioCandidato
from Repositorios.RepositorioPartido import RepositorioPartido


class ControladorCandidato():
    """
   constructor que permite llevar a cabo la creacion de instancias del controlador.
   """

    def __init__(self):
        self.repositorioCandidato = RepositorioCandidato()
        self.repositorioPartido = RepositorioPartido()
        print("Creando ControladorCandidato")

    def index(self):
        print("Listar todos los Candidatos")
        return self.repositorioCandidato.findAll()

    def create(self, elCandidato):
        print("Crear un Candidato")
        nuevoCandidato = Candidato(elCandidato)
        return self.repositorioCandidato.save(nuevoCandidato)

    def show(self, id):
        print("Mostrando un Candidato con id ", id)
        elCandidato = Candidato(self.repositorioCandidato.findById(id))
        return elCandidato.__dict__

    def update(self, id, elCandidato):
        print("Actualizando Candidato con id ", id)
        CandidatoActual = Candidato(self.repositorioCandidato.findById(id))
        CandidatoActual.cedula = elCandidato["cedula"]
        CandidatoActual.no_resolucion = elCandidato["no_resolucion"]
        CandidatoActual.nombre = elCandidato["nombre"]
        CandidatoActual.apellido = elCandidato["apellido"]
        return self.repositorioCandidato.save(CandidatoActual)

    def delete(self, id):
        print("Elimiando Candidato con id ", id)
        return self.repositorioCandidato.delete(id)

    def asignarPartidos(self, id, id_partido):
        candidatoActual = Candidato(self.repositorioCandidato.findById(id))
        partidoActual = Partido(self.repositorioPartido.findById(id_partido))
        candidatoActual.partido = partidoActual
        return self.repositorioCandidato.save(candidatoActual)
