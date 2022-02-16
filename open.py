from inspect import Traceback

def main_V0():
   open("/path/to/mars.jpg")
if __name__ == '__main__':
    main_V0()   
#---------------------------------------------------------------------------------------------------------------------------

try: #FileNotFoundError exception
   open('/path/to/mars.jpg')
except FileNotFoundError:
   print("Couldn't find the config.txt file!")
#---------------------------------------------------------------------------------------------------------------------------
#Lectura de archivo
def main_V1():#Se crea la función
    try:
        configutation = open('config.txt')#Se almacena el archivo en una variable
    except FileNotFoundError: #Se crea la excepcion de archivo no encontrado
        print("Couldn't find the config.txt file")#se imprime el mensaje
    except IsADirectoryError:
        print("Found config.txt but it is a directory, couldn't read it")
if __name__ == '__main__':#en case de cumplir la sentencia se ejecutara la funcion main
    main_V1()
#---------------------------------------------------------------------------------------------------------------------------
def main_V2():
    try: 
        configuration = open('config.txt')
    except FileNotFoundError:
        print("Couldn't find the config.txt")
    except IsADirectoryError:
        print("Found config.txt but is a directory, couldn't read ir") 
    except (BlockingIOError, TimeoutError):
        print("Filesystem under heavy load, can't complete reading configuration file") 
#---------------------------------------------------------------------------------------------------------------------------
try:
    open("mars.jpg")
except FileNotFoundError as err:
    print("Got a problem trying to read the file",err)
#---------------------------------------------------------------------------------------------------------------------------
try:
    open("config.txt")
except OSError as err:
    if err.errno==2:
        print("Couldn't find the config.txt file!")
    elif err.errno == 13:
        print("Found config.txt but couldn't read it")
#---------------------------------------------------------------------------------------------------------------------------
def water_left(astronauts, water_left, days_left):
    daily_usage = astronauts*11
    total_usage = daily_usage*days_left
    total_water_left = water_left - total_usage
    if total_water_left < 0:
        raise RuntimeError(f"There is not enough water for {astronauts} astronauts after {days_left} days!")
    return f"Total water left after {days_left} days is: {total_water_left} liters"
#---------------------------------------------------------------------------------------------------------------------------
try:
    water_left(5,100,2)
except RuntimeError as err:
    alert_navigation_system(err)

#---------------------------------------------------------------------------------------------------------------------------
 #   water_left("3","200",None)
#Traceback (most recent call last):
 #   File "<stdin>", line 1, in <module>
  #  File "<stdin>", line 3, in water_left
#TypeError: can't multiply sequence by non-int of type 'NoneType'
#---------------------------------------------------------------------------------------------------------------------------
def water_left_V2(astronauts, water_left, days_left):
    for argument in [astronauts, water_left, days_left]:
        try:
            aux=argument.str.isdigit()
            if aux==True:
                argument / 10
        except TypeError:
            raise TypeError(f"will be raised only if it isn't the right type ")
            raise TypeError(f"It isn't de rigth type")
            raise TypeError(f"All arguments must be of type int, but received: '{argument}'")
    daily_usage = astronauts * 11
    total_usage = daily_usage * days_left
    total_water_left = water_left - total_usage
    if total_water_left < 0:
        raise RuntimeError(f"There is not enough water for {astronauts} astronauts after {days_left} days!")
    return f"Total water left after {days_left} days is: {total_water_left} liters"