def leap_year():
    Año = int(input("Ingrese un año: "))
    if Año%100==0:
        if Año%400==0:
            print(f"El año {Año} es bisiesto")
        else:
            print(f"El año {Año} no es bisiesto")
    else:
        if Año%4==0:
            print(f"El año {Año} es bisiesto")
        else:
            print(f"El año {Año} no es bisiesto")
