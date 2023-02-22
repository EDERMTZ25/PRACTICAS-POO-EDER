class Personaje:
    #atributos
    especie = "Humano"
    nombre = "Master Chief"
    altura = "2.70"

    #Metodos del personaje
    def correr(self, status):
        if (status):
            print("El personaje "+self.nombre+" esta corriendo")
        else:
            print("El personaje "+ self.nombre +"se detuvo")

    def lanzarGranadas(self):
        print("El personaje "+ self.nombre +" lanzo una granada")

    def recargarArma(self, municiones):
        cargador = 10
        cargador += municiones
        print("El personaje "+ self.nombre +" recargo su arma y ahora tiene "+ str(cargador) +" municiones")