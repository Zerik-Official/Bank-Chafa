import time
from colorama import Style, Fore, init

init(autoreset=True)

def generic_input(message:str, normalized:type | None = None) -> str | int | float:
    """
    Función para solicitar una entrada al usuario, normalizarla y devolver el valor.

    Args:
        message (str): El mensaje que se mostrará al usuario para solicitar la entrada.
        normalized (type | None): El tipo de normalización que se aplicará a la entrada (e.g., "int" o "float", si no se especifica no se normaliza).
    Returns:
        user_input (str, int or float): La entrada del usuario normalizada como una cadena de texto.
    """
    valid:bool = False # Variable anti hander-noWhileTrue

    while (not valid):
        try:
            user_input = input(message).strip()
            
            if normalized is None:
                return user_input
            
            if normalized in [int, float]:
                clean_input = user_input.replace(".", "").replace(",", "")
                return normalized(clean_input)
            
            return normalized(user_input)
            
        except ValueError:
            print(f"{Fore.YELLOW}[WARNING]{Style.RESET_ALL} Entrada no válida. Por favor, ingresa un valor correcto.")

def generic_animation_load(message:str, points:int, wait_duration: int | float | None = 0.7) -> None:
    """
    Función para mostrar una animación de carga con puntos.
    
    Args:
        message (str): El mensaje que se mostrará antes de la animación de carga.
        points (int): El número de puntos que se mostrarán en la animación de carga.
        wait_duration (int | float): El tiempo de espera entre cada punto en segundos si es int, float si es en milisegundos.
    Returns:
        None
    """

    print(f"\n{message}", end="")
    for i in range(points):
        print(".", end="")
        time.sleep(wait_duration)