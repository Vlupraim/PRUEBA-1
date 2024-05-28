class Fraccion:
    """
    Representa una fracción matemática.

    Atributos:
        numerador (int): El numerador de la fracción.
        denominador (int): El denominador de la fracción.

    Métodos:
        __init__(self, numerador, denominador=1): Constructor.
        get_numerador(self): Obtiene el numerador.
        set_numerador(self, nuevo_numerador): Establece el numerador.
        get_denominador(self): Obtiene el denominador.
        set_denominador(self, nuevo_denominador): Establece el denominador.
        __str__(self): Representación en cadena de la fracción.
        simplificar(self): Simplifica la fracción.
        sumar(self, otra_fraccion): Suma dos fracciones.
        restar(self, otra_fraccion): Resta dos fracciones.
        multiplicar(self, otra_fraccion): Multiplica dos fracciones.
        dividir(self, otra_fraccion): Divide dos fracciones.
        calcular_mcm(self, otra_fraccion): Calcula el MCM de los denominadores.
    """
    
    def __init__(self, numerador, denominador=1):
        """
        Constructor de la clase Fracción.

        Args:
            numerador (int): El numerador de la fracción.
            denominador (int, opcional): El denominador de la fracción (por defecto 1).

        Raises:
            ZeroDivisionError: Si el denominador es 0.
        """

        if denominador == 0:
            raise ZeroDivisionError("El denominador no puede ser 0")

        self.numerador = numerador
        self.denominador = denominador

        # Ajustar signo si numerador y denominador tienen diferente signo
        if self.numerador * self.denominador < 0:
            self.numerador = abs(self.numerador)
            self.denominador = abs(self.denominador)
    
    def get_numerador(self):
        """Obtiene el numerador de la fracción."""
        return self.numerador

    def set_numerador(self, nuevo_numerador):
        """Establece el numerador de la fracción."""
        self.numerador = nuevo_numerador

    def get_denominador(self):
        """Obtiene el denominador de la fracción."""
        return self.denominador

    def set_denominador(self, nuevo_denominador):
        """Establece el denominador de la fracción."""
        if nuevo_denominador == 0:
            raise ZeroDivisionError("El denominador no puede ser 0")

        self.denominador = nuevo_denominador

    def __str__(self):
        """Representación en cadena de la fracción."""
        if self.denominador == 1:
            return str(self.numerador)
        else:
            return f"{self.numerador}/{self.denominador}"

    def simplificar(self):
        """Simplifica la fracción."""
        mcd = self.mcd(self.numerador, self.denominador)
        if mcd != 1:
            self.numerador //= mcd
            self.denominador //= mcd

        return self

    def mcd(self, a, b):
        """Calcula el máximo común divisor (MCD) de dos números."""
        while b != 0:
            a, b = b, a % b
        return a

    def sumar(self, otra_fraccion):
        """Suma dos fracciones."""
        # Simplificar ambas fracciones
        self.simplificar()
        otra_fraccion.simplificar()

        # Calcular el mínimo común múltiplo (MCM) de los denominadores
        mcm = self.calcular_mcm(otra_fraccion)

        # Calcular la suma de las fracciones con el MCM como denominador
        nuevo_numerador = self.numerador * (mcm // self.denominador) + otra_fraccion.numerador * (mcm // otra_fraccion.denominador)
        nueva_fraccion = Fraccion(nuevo_numerador, mcm)

        return nueva_fraccion
    def restar(self, otra_fraccion):
        """Resta dos fracciones."""
        # Simplificar ambas fracciones
        self.simplificar()
        otra_fraccion.simplificar

    def multiplicar(self, otra_fraccion):
        """Multiplica dos fracciones."""
        # Simplificar ambas fracciones
        self.simplificar()
        otra_fraccion.simplificar()

        # Multiplicar numeradores y denominadores
        nuevo_numerador = self.numerador * otra_fraccion.numerador
        nuevo_denominador = self.denominador * otra_fraccion.denominador

        # Simplificar la fracción resultante
        nueva_fraccion = Fraccion(nuevo_numerador, nuevo_denominador)
        nueva_fraccion.simplificar()

        return nueva_fraccion
    def dividir(self, otra_fraccion):
        """Divide dos fracciones."""
        # Simplificar ambas fracciones
        self.simplificar()
        otra_fraccion.simplificar()

        # Si la fracción divisora es cero, levantar una excepción
        if otra_fraccion.numerador == 0:
            raise ZeroDivisionError("No se puede dividir por una fracción con numerador 0")

        # Invertir la fracción divisora
        inversa_fraccion = Fraccion(otra_fraccion.denominador, otra_fraccion.numerador)

        # Multiplicar la fracción dividendo por la inversa de la fracción divisora
        nueva_fraccion = self.multiplicar(inversa_fraccion)

        return nueva_fraccion
    def calcular_mcm(self, otra_fraccion):
        """Calcula el mínimo común múltiplo (MCM) de los denominadores."""
        # Simplificar ambas fracciones
        self.simplificar()
        otra_fraccion.simplificar()

        # Calcular el máximo común divisor (MCD) de los denominadores
        mcd = self.mcd(self.denominador, otra_fraccion.denominador)

        # Calcular el MCM utilizando la fórmula: MCM = (denominador1 * denominador2) / MCD
        mcm = (self.denominador * otra_fraccion.denominador) // mcd

        return mcm
    def seleccionar_fraccion(self, fracciones):
        """Permite al usuario seleccionar una fracción de una lista."""
        if not fracciones:
            print("No hay fracciones disponibles.")
            return None

        # Mostrar la lista de fracciones con índices
        for i, fraccion in enumerate(fracciones):
            print(f"{i + 1}. {fraccion}")

        while True:
            # Solicitar índice de la fracción
            indice_str = input("Ingrese el índice de la fracción (1-{}): ".format(len(fracciones)))
            try:
                indice = int(indice_str) - 1
                if 0 <= indice < len(fracciones):
                    return fracciones[indice]
                else:
                    print("Índice inválido. Intente nuevamente.")
            except ValueError:
                print("Error: El índice debe ser un número entero.")

def main():
    # Inicializar lista de fracciones
    fracciones = []
    # Bucle para crear fracciones
    while True:
    # Solicitar al usuario si desea continuar
        continuar = input("¿Desea crear otra fracción? (s/n): ")
        if continuar.lower() != "s":
            break

    # Solicitar datos de la fracción
        numerador_str = input("Ingrese el numerador: ")
        try:
            numerador = int(numerador_str)
        except ValueError:
            print("Error: El numerador debe ser un número entero.")
            continue

        denominador_str = input("Ingrese el denominador: ")
        try:
            denominador = int(denominador_str)
            if denominador == 0:
                raise ZeroDivisionError
        except ValueError:
            print("Error: El denominador debe ser un número entero.")
            continue
        except ZeroDivisionError:
            print("Error: El denominador no puede ser 0.")
            continue

        # Crear la fracción y agregarla a la lista
        fraccion = Fraccion(numerador, denominador)
        fracciones.append(fraccion)

    # Mostrar la lista de fracciones
    print("\nFracciones creadas:")
    for fraccion in fracciones:
        print(f"  - {fraccion}")

    # Menú de operaciones
    while True:
        print("\nSeleccione una operación:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Calcular MCM")
        print("6. Salir")

        opcion = input("Ingrese su opción (1-6): ")

        if opcion == "1":
            # Sumar fracciones
            fraccion1 = fraccion.seleccionar_fraccion(fracciones)
            fraccion2 = fraccion.seleccionar_fraccion(fracciones)
            fraccion_suma = fraccion1.sumar(fraccion2)
            print(f"Suma: {fraccion_suma}")

        elif opcion == "2":
            # Restar fracciones
            fraccion1 = fraccion.seleccionar_fraccion(fracciones)
            fraccion2 = fraccion.seleccionar_fraccion(fracciones)
            fraccion_resta = fraccion1.restar(fraccion2)
            print(f"Resta: {fraccion_resta}")

        elif opcion == "3":
            # Multiplicar fracciones
            fraccion1 = fraccion.seleccionar_fraccion(fracciones)
            fraccion2 = fraccion.seleccionar_fraccion(fracciones)
            fraccion_multiplicacion = fraccion1.multiplicar(fraccion2)
            print(f"Multiplicación: {fraccion_multiplicacion}")

        elif opcion == "4":
            # Dividir fracciones
            fraccion1 = fraccion.seleccionar_fraccion(fracciones)
            fraccion2 = fraccion.seleccionar_fraccion(fracciones)
            try:
                fraccion_division = fraccion1.dividir(fraccion2)
                print(f"División: {fraccion_division}")
            except ZeroDivisionError:
                print("Error: No se puede dividir por una fracción con numerador 0.")

        elif opcion == "5":
            # Calcular MCM de denominadores
            fraccion1 = fraccion.seleccionar_fraccion(fracciones)
            fraccion2 = fraccion.seleccionar_fraccion(fracciones)
            mcm = fraccion1.calcular_mcm(fraccion2)
            print(f"MCM: {mcm}")

        elif opcion == "6":
            # Salir del bucle
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Intente nuevamente.")

    # Verificar si el denominador es 0
    if denominador == 0:
        print("Error: El denominador no puede ser 0.")
        return

    # Crear una instancia de Fracción con los valores ingresados
    fraccion = Fraccion(numerador, denominador)

    # Mostrar la fracción
    print(f"Fracción: {fraccion}")

if __name__ == "__main__":
    main()



