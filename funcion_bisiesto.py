#presentamos la funcion con el titulo centrado 
print("Funcion año bisiesto".center(50,"*"))
#iniciamos un bloque try para atrapar el error si no se digita un entero
try:   
    año = int(input("ingresa el año a verificar: "))
except Exception as e:
    print(f"ocurrio un error debes digitar un entero!!!, error tipo {type(e)}")
#agregamos un bloque else para que se ejecute la operacion si no existe el error
else:
    def calculo_año(año):
        if año % 4 != 0:
           return(f"el año {año},no es año bisiesto")
        elif año % 4 == 0 and año % 100 != 0:
           return(f"el año {año}, es bisiesto")
        elif año % 4 == 0 and año % 100 == 0 and año % 400 != 0:
           return(f"el año {año}, no es bisiesto")
        elif año % 4 == 0 and año % 100 == 0 and año % 400 == 0:
           return(f"el año {año},no es año bisiesto")
    print(calculo_año(año))
    #opcionalmente agregamos el bloque fynally pata cerrar con un 
    # mensaje independientemente de si hay o no error
finally:
    print("termino la operacion!!!")

