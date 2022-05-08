#presentamos la funcion con el titulo centrado 
print("Funcion año bisiesto".center(50,"*"))


def calculo_año(año):
   
   if año % 4 != 0:
      return(f"el año {año},no es año bisiesto")
   elif año % 4 == 0 and año % 100 != 0:
      return(f"el año {año}, es bisiesto")
   elif año % 4 == 0 and año % 100 == 0 and año % 400 != 0:
      return (f"el año {año}, no es bisiesto")
   elif año % 4 == 0 and año % 100 == 0 and año % 400 == 0:
      return(f"el año {año},no es año bisiesto")

print(calculo_año(1984))
