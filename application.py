# -*- coding: UTF-8 -*-

"""
Este programa pide el ingreso de dos páginas y una palabra.
Compara que página tiene mayor cantidad de la palabra elegida.
"""
import urllib2 #Ayuda en la apertura de URL.
import re #Cuenta las letras dentro de las palabras en la pagina.
import time # Controla el tiempo de una variable.
import os # Proporciona una manera facil de utilizar el sistema.

class Union(object): # Es el Objeto principal.

    def __init__(self): # Funcion Global.
        self.pag1 = "" # Para hacer referencia a Pagina 1.
        self.req2 = "" # Para hacer referencia a Pagina 2.
        self.palabra = "" # Para hacer referencia a 'Palabra'.
        self.cont1 = "" # Para hacer referencia al Conteo 1.
        self.cont2 = "" # Para hacer referencia al Conteo 2.
        print """
        \r+++++++++++++++++++++++++++
        \r++++    Bienvenidos    ++++
        \r+++++++++++++++++++++++++++
        """
        time.sleep(2)

    def verify(self): # Funcion que verifica la respuesta.
        try:
            respuesta = urllib2.urlopen(self.pag1) # Abre el URL no. 1.
            pagina = respuesta.read() # Lee lo que se encuentra en el URL 1.
            self.cont1 = len(re.findall(self.palabra, pagina)) # Cuenta la cantidad de palabras.
            print "\nEl primer URL contiene %d \"%s\"" % (self.cont1, self.palabra)
            # Muestra la cantidad de palabras.
        except ValueError:
            os.system('clear')
            print """
            \r////////////////////////////////
            \r/////    Faltal Error!    //////
            \r////////////////////////////////
            """
            print "El primer URL que ingreso no es valido!!!" # Aviso de ingreso incorrecto.
            raw_input("\nPresione enter para cotinuar...") # Con un enter para continuar.
            self.ingresos() # Regresa a la función Ingresos.

        try:
            respuesta2 = urllib2.urlopen(self.req2) # Abre el URL no. 2.
            pagina2 = respuesta2.read() # Lee lo que se encuentra en el URL 2.
            self.cont2 = len(re.findall(self.palabra, pagina2)) # Cuenta la cantidad de palabras.
            print "El segundo URL contiene %d \"%s\"" % (self.cont2, self.palabra)
            # Muestra la cantidad de palabras.
        except ValueError:
            os.system('clear')
            print """
            \r////////////////////////////////
            \r/////    Faltal Error!    //////
            \r////////////////////////////////
            """
            print "El segundo URL que ingreso no es valido!!!" # Avido de ingreso incorrecot.
            raw_input("\nPresione enter para cotinuar...") # Con untere para continuar.
            self.ingresos()

        if self.cont1 == self.cont2: # Compara los dos URL.

            print """
            \r############################
            \r#####    Resualtado    #####
            \r############################
            """
            print "\nLos URL contienen la misma cantidad de palabras que usted busca."
            # Muestra la cantidad de palabras.
            print "Le recomendamos que ingrese al URL que usted guste:" # Recomendación.
            print str(self.pag1) + "\n"
            print str(self.req2) + "\n"
            raw_input("\nPresione enter para cotinuar...") # Con un enter para continuar.
            self.ingresos() # Regresa a la función Ingresos.

        elif self.cont1 < self.cont2:
        # Compara si la pag. 2 tiene mayor cantidad de palabra elegida.

            print """
            \r############################
            \r#####    Resualtado    #####
            \r############################
            """
            print "\nEl URL2 contienen mas palabras de las que usted busca que la URL1"
            print "Le recomendamos que ingrese a él:"
            print str(self.req2) + "\n\n"
            raw_input("\nPresione enter para cotinuar...") # Con un enter para continuar.
            self.ingresos()
        else: # Compara si la pagina 2 tiene mayor cantidad de palabra elegida.

            print """
            \r############################
            \r#####    Resualtado    #####
            \r############################
            """
            print "\nEl URL1 contienen mas palabras de las que usted busca que la URL2"
            print "Le recomendamos que ingrese a él:"
            print str(self.pag1) + "\n\n"
            raw_input("\nPresione enter para cotinuar...") # Con un enter para continuar.
            self.ingresos() # Regresa a la función Ingresos.

    def ingresos(self): # Función que registra los ingresos del usuario.
        os.system('reset')
        print """
        \r##########################
        \r#####    Ingresos    #####
        \r##########################"""
                                        # INSTRUCCIONES GENERALES.
        print """
        \r\tInstrucciones:
        \r\tPara que puedas buscar correctamente recuerda poner al principio
        \r\tDe tu URL \"http:// o https://\" esto de pente de que pagina elijas
        \r\tcomo por ejemplo: http://www.google.com o http://google.com
        """
        self.pag1 = (raw_input('Ingrese primer url: ')) # Variable que guarda el URL 1.
        self.req2 = (raw_input('Ingrese segunda url: ')) # Variable que guarda el URL 2.
        self.palabra = raw_input("Ingrese palabra: ")
        # Variable que guarda la palabra que desea buscar.
        os.system('clear') # Limpia la pantalla.
        self.verify() # Regresa a la función Verify.

RUN = Union() # Objeto Principal.
RUN.ingresos() # Abre la función Ingresos.
