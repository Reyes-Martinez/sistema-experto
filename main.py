from experta import *

class Reglas(KnowledgeEngine):
    #funcion inicial donde daremos la bienvenida y las instrucciones del uso del sistema experto
    @DefFacts()
    def _initial_action(self):
        print("Hola amigo bienvenido, este orientador vocaconal te puede ayudar a elegir una carrera univercitari a partir de tus gustos")
        print("Responde las siguientes preguntas con un 'si' o un 'no' dependiendo si te gusta relaizar las cosas")
        yield Fact(accion="buscar-pregunta")

        #Definicmos las preguntas
    @Rule(Fact(accion='buscar-pregunta'), NOT(Fact(pregunta_1=W())), salience=1)
    def pregunta_0(self):
        self.declare(Fact(pregunta_1=input("¿Te gustan los juegos de logica?: ")))

    @Rule(Fact(accion='buscar-pregunta'), NOT(Fact(pregunta_2=W())), salience=1)
    def pregunta_1(self):
        self.declare(Fact(pregunta_2=input("¿Puedo hacer calculos matematicos rapidos?: ")))

    @Rule(Fact(accion='buscar-pregunta'), NOT(Fact(pregunta_3=W())), salience=1)
    def pregunta_2(self):
        self.declare(Fact(pregunta_3=input("¿Se me da bastante bien el leer mapas, graficos y diagramas?: ")))

    @Rule(Fact(accion='buscar-pregunta'), NOT(Fact(pregunta_4=W())), salience=1)
    def pregunta_3(self):
        self.declare(Fact(pregunta_4=input("¿Me gusta realizar construcciones con legos,puzles o similares?: ")))

    @Rule(Fact(accion='buscar-pregunta'), NOT(Fact(pregunta_5=W())), salience=1)
    def pregunta_4(self):
        self.declare(Fact(pregunta_5=input("¿Suelo destacar mucho en los deportes?: ")))

    @Rule(Fact(accion='buscar-pregunta'), NOT(Fact(pregunta_6=W())), salience=1)
    def pregunta_5(self):
        self.declare(Fact(pregunta_6=input("¿De pequeño aprendí rápidamente a montar en bicicleta o a ir en patines?: ")))

    @Rule(Fact(accion='buscar-pregunta'), NOT(Fact(pregunta_7=W())), salience=1)
    def pregunta_6(self):
        self.declare(Fact(pregunta_7=input("¿Me resulta fácil hacer que los demás me escuchen y sigan mis planes, soy un poco líder?: ")))

    @Rule(Fact(accion='buscar-pregunta'), NOT(Fact(pregunta_8=W())), salience=1)
    def pregunta_7(self):
        self.declare(
            Fact(pregunta_8=input("¿Disfruto estando con grupos de personas en reuniones y fiestas para charlar?: ")))

    @Rule(Fact(accion='buscar-pregunta'), NOT(Fact(pregunta_9=W())), salience=1)
    def pregunta_8(self):
        self.declare(Fact(pregunta_9=input("¿Soy una persona muy independiente?: ")))

    @Rule(Fact(accion='buscar-pregunta'), NOT(Fact(pregunta_10=W())), salience=1)
    def pregunta_9(self):
        self.declare(
            Fact(pregunta_10=input("¿Si estoy enfadado o contento, sé perfectamente el motivo?: ")))
        #definimos las diferenites combinaciones en las que se puede responder las preguntas
    @Rule(Fact(accion='buscar-pregunta'), Fact(pregunta_1="si"), Fact(pregunta_2="si"), Fact(pregunta_3="no"),
          Fact(pregunta_4="no"), Fact(pregunta_5="no"), Fact(pregunta_6="no"), Fact(pregunta_7="no"), Fact(pregunta_8="no"),
          Fact(pregunta_9="no"), Fact(pregunta_10="no"))
    def carrera_0(self):
        self.declare(Fact(carrera='\nCiencias economicas \n Ingenierias'))

    @Rule(Fact(accion='buscar-pregunta'), Fact(pregunta_1="no"), Fact(pregunta_2="no"), Fact(pregunta_3="si"),
          Fact(pregunta_4="si"), Fact(pregunta_5="no"), Fact(pregunta_6="no"), Fact(pregunta_7="no"),
          Fact(pregunta_8="no"),Fact(pregunta_9="no"), Fact(pregunta_10="no"))
    def carrera_1(self):
        self.declare(Fact(carrera='\nArquitectura \nArtes graficas'))

    @Rule(Fact(accion='buscar-pregunta'), Fact(pregunta_1="no"), Fact(pregunta_2="no"), Fact(pregunta_3="no"),
          Fact(pregunta_4="no"), Fact(pregunta_5="si"), Fact(pregunta_6="si"), Fact(pregunta_7="no"),
          Fact(pregunta_8="no"),Fact(pregunta_9="no"), Fact(pregunta_10="no"))
    def carrera_2(self):
        self.declare(Fact(carrera='\nMedicina deportiva \nNutricion'))

    @Rule(Fact(accion='buscar-pregunta'), Fact(pregunta_1="no"), Fact(pregunta_2="no"), Fact(pregunta_3="no"),
          Fact(pregunta_4="no"), Fact(pregunta_5="no"), Fact(pregunta_6="no"), Fact(pregunta_7="si"),
          Fact(pregunta_8="si"),Fact(pregunta_9="no"), Fact(pregunta_10="no"))
    def carrera_3(self):
             self.declare(Fact(carrera='\nCiencias politicas \nPedagogia'))

    @Rule(Fact(accion='buscar-pregunta'), Fact(pregunta_1="no"), Fact(pregunta_2="no"), Fact(pregunta_3="no"),
          Fact(pregunta_4="no"), Fact(pregunta_5="no"), Fact(pregunta_6="no"), Fact(pregunta_7="no"),
          Fact(pregunta_8="no"),Fact(pregunta_9="si"), Fact(pregunta_10="si"))
    def carrera_4(self):
        self.declare(Fact(carrera='\nPsicología \n Psiquiatria'))

        #imprimimos los resultados
    @Rule(Fact(accion='buscar-pregunta'), Fact(carrera=MATCH.carrera))
    def carrera(self, carrera):
        print(f"La areas en las cuales puedes encontrar una carrera son {carrera} ")

def main():
    reglas = Reglas()
    reglas.reset()
    reglas.run()

if __name__ == "__main__":
    main()