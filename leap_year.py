def leap_year():
    Año = int(input("Ingrese un año: "))
    if Año%100==0 and Año%400==0:
        print(f"El año {Año} es bisiesto")
    else:
        if Año%4==0 and not(Año%100==0):
            print(f"El año {Año} es bisiesto")
        else:
            print(f"El año {Año} no es bisiesto")
