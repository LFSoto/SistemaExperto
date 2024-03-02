# Práctica 1 - Sistemas Basados en Conocimiento
## Maestría Ing. Software - CENFOTEC
### Estudiantes: 
- Alexander Garro
- Luis Felipe Soto

## Dependencias
Para esta solución es necesario Python 3.9 y LogPy. Deberá instalar un interprete de
[Python 3.9](https://www.python.org/downloads/release/python-3915/).

Después de instalar Python 3.9, utilice `pip` para instalar LogPy:
> pip install logic  
> pip install logpy
 

## Ejecutar el programa
Con su IDE de preferencia, ejecute el archivo `tarea1.py`. Una vez esté corriendo, un menú de consola deberá mostrarse, 
dándole la bienvenida al Sistema Experto y mostrándole 4 opciones: 
- Agregar nuevo hecho
- Agregar nueva regla (TBD)
- Consultar hechos 
- Salir


## Ejemplos
### 1 - Agregar un nuevo hecho
Para agregar un nuevo hecho, elija la primera opción y siga las indicaciones. Primero le preguntarán por el nombre de la
primera, después la relación y por último la segunda persona.  
Ejemplo: 
- Por favor, introduzca el nombre de la primera persona: `Luis`
- Luis es: `hermano`
- Luis es hermano de: `Andrea`

### 2 - Consultar un hecho: una salida
Para consultar un hecho, elija la tercera opción y siga las instrucciones. Primero le preguntarán por el nombre de la
persona y después la relación. El siguiente ejemplo busca la madre de Juan.  
Ejemplo:
- Por favor, introduzca el nombre de la persona: `Juan`
- Por favor, introduzca la relacion que quiere consultar: `madre`
- **Salida**: La madre de Juan es: ('Luisa',)

### 3 - Consultar un hecho: multiples salidas
El siguiente ejemplo busca los hermanos de Juan.  
Ejemplo:
- Por favor, introduzca el nombre de la persona: `Juan`
- Por favor, introduzca la relacion que quiere consultar: `hermano`
- **Salida**: Los hermanos de Juan son: ['Mario', 'Nicole']

### Referencias
- https://github.com/logpy/logpy
- https://python.hotexamples.com/es/examples/logpy/-/conde/python-conde-function-examples.html
- https://matthewrocklin.com/blog/work/2013/01/14/LogPy-Introduction