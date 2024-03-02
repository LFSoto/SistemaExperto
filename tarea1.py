import ast

from logpy import Relation, facts, run, conde, var, eq, fact

# Fuente de ejemplos: https://python.hotexamples.com/es/examples/logpy/-/conde/python-conde-function-examples.html

# Definir las relaciones
hermano = Relation()
hermana = Relation()
padre = Relation()
madre = Relation()
familia = Relation()
hijo = Relation()
hija = Relation()
descendencia = Relation()
ascendencia = Relation()
esposo = Relation()
esposa = Relation()
pareja = Relation()


def get_relacion(tipo_relacion):
    relations = {
        'hermano': hermano,
        'hermana': hermana,
        'padre': padre,
        'madre': madre,
        'familia': familia,
        'hijo': hijo,
        'hija': hija,
        'descendencia': descendencia,
        'ascendencia': ascendencia,
        'esposo': esposo,
        'esposa': esposa,
        'pareja': pareja
    }
    return relations.get(tipo_relacion, None)


# Base de conocimientos con hechos
facts(hermano, ('Juan', 'Mario'))
facts(hermana, ('Ana', 'Maria'))
facts(padre, ('Pedro', 'Juan'), ('Pedro', 'Mario'), ('Pedro', 'Nicole'))
facts(madre, ('Luisa', 'Juan'), ('Luisa', 'Mario'))
facts(esposa, ('Luisa', 'Pedro'))

################################################


# Validaciones
def es_hijo(padre_persona, hijo_persona):
    return conde([padre(hijo_persona, padre_persona)],
                 [madre(hijo_persona, padre_persona)])


def es_hermano_o_hermana(persona1, persona2):
    x = var()
    return conde([padre(x, persona1), padre(x, persona2)],
                 [madre(x, persona1), madre(x, persona2)])


def es_padre(padre_persona, hijo_persona):
    return padre(padre_persona, hijo_persona)


def es_madre(madre_persona, hijo_persona):
    return madre(madre_persona, hijo_persona)


def es_conyuge(persona1, persona2):
    return conde([esposo(persona1, persona2)],
                 [esposa(persona1, persona2)],
                 [esposo(persona2, persona1)],
                 [esposa(persona2, persona1)])


################################################


def cargar_archivo():
    with open("datos.txt", "r") as archivo:
        for line in archivo.readlines():
            tupla = ast.literal_eval(line)
            relacion, nombres = tupla
            fact(get_relacion(relacion), str(nombres[0]), str(nombres[1]))


def guardar_archivo(relacion_p, hechos_p):
    with open("datos.txt", "a+") as archivo:
        data = relacion_p, hechos_p
        archivo.write(str(data))
        archivo.write("\n")


################################################


def agregar_hecho(relacion_p, hecho_p):
    relacion = get_relacion(relacion_p)
    facts(relacion, hecho_p)
    guardar_archivo(relacion_p, hecho_p)
    print('Agregado correctamente a la base de conocimiento')
    #consultar(relacion_p, hecho_p[0])


def agregar_regla(nombre, regla):
    globals()[nombre] = regla


def consultar(relacion, persona):
    x = var()
    if relacion == 'hermano' or relacion == 'hermana':
        resultado = run(0, x, es_hermano_o_hermana(x, persona))
        filtro = [r for r in resultado if r != persona]
        print(f'Los hermanos de {persona} son: {filtro}')
    elif relacion == 'padre':
        resultado = run(1, x, es_padre(x, persona))
        print(f'El padre de {persona} es: {resultado}')
    elif relacion == 'madre':  # work
        resultado = run(1, x, es_madre(x, persona))
        print(f'La madre de {persona} es: {resultado}')
    elif relacion == 'esposa' or relacion == 'esposo':  # work
        resultado = run(1, x, es_conyuge(x, persona))
        print(f'El esposo o la esposa de {persona} es: {resultado}')
    elif relacion == 'hijo':
        resultado = run(1, x, es_hijo(x, persona))
        print(f'El hijo de {persona} es: {resultado}')
    else:
        print("Opción no válida, por favor intenta de nuevo")


def salir():
    print("Gracias por usar el sistema")
    exit(0)


def main():
    cargar_archivo()
    while True:
        print("\nBienvenido al Sistema Experto")
        print("1. Agregar nuevo hecho")
        print("2. Agregar nueva regla")
        print("3. Consultar hechos")
        print("4. Salir")
        opcion = input("Por favor, elige una opción: ")

        if opcion == '1':
            primera_persona = input("Por favor, introduzca el nombre de la primera persona: ")
            relacion = input(f"{primera_persona} es: ")
            segunda_persona = input(f"{primera_persona} es {relacion} de: ")
            agregar_hecho(relacion, (primera_persona, segunda_persona))

        elif opcion == '2':
            #agregar_regla()
            print('TBD')

        elif opcion == '3':
            primera_persona = input("Por favor, introduzca el nombre de la persona: ")
            relacion = input("Por favor, introduzca la relacion que quiere consultar: ")
            consultar(relacion, primera_persona)

        elif opcion == '4':
            salir()

        else:
            print("Opción no válida, por favor intenta de nuevo")


if __name__ == '__main__':
    main()
