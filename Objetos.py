import Personaje 

#1. Crear un objeto de la clase Personaje
heroe = Personaje()

#2. Usar atributos del objeto

print("El personaje se llama: "+ heroe.nombre)
print("El personaje es de la especie: "+ heroe.especie)
print("El personaje mide: "+ heroe.altura+" metros")

#3. Usar metodos del objeto
heroe.correr(True)
heroe.lanzarGranadas()
heroe.recargarArma(87)

#Fin del programa