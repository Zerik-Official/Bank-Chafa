import time
from colorama import init, Fore, Style

init(autoreset=True)


print(f"{Fore.MAGENTA}Bienvenido al Banco Chafa, gracias por elegirnos, a continuación, porfavor introduce un saldo inicial{Style.RESET_ALL}")

options_bank = [[1, "Realizar un retiro\n"], [2, "Realizar un deposito\n"], [3, "salir"]]



def process_operation(operation:int, balance:int | float, new_balance_entry:int | float) -> list[bool | str]:
    """
    Recibe como parametro el balance introducido por el usuario

    Args:
        balance (init or float): Balance introducido por el usuario
    Returns:
        message (str): Mensaje de error o de ingreso correcto
    """
    try:
        print(f"{Fore.YELLOW}Procesando..... Porfavor espere un momento.")
        time.sleep(2)

        if new_balance_entry <= 0:
            return False, f"El monto debe ser mayor a 0"

        if operation == 1:
            if new_balance_entry <= balance:
                return True, f"Operación exitosa, su nuevo saldo es {balance - new_balance_entry}"
            else:
                return False, f"No se pudo realizar la operación por fondos insuficientes"
        elif operation == 2:
            return True, f"Operación exitosa, su nuevo saldo es {balance + new_balance_entry}"
    except (ValueError, TypeError):
        return False, "Internal error"


swl = False
first_entry = False

while (not first_entry):
    try:
        entry_balance = input("Porfavor ingrese su saldo inicial: ").replace(",", ".")
        balance = float(entry_balance)
        first_entry = True
    except ValueError:
        print("Debes introducir números solamente")

while (not swl):

    try:

        print(f"{Fore.GREEN}Su saldo actual es: {Fore.MAGENTA} ${balance}")

        for i in options_bank:
            print(f"{i[0]}. {i[1]}")

        select_option = input("A continuación, porfavor seleccione una opción para continuar: ")

        try:
            opt = int(select_option)
        except ValueError:
            print(f"{Fore.RED}Opción inválida, ingresa el número de la acción.{Style.RESET_ALL}")
            continue


        if opt == 1:
            new_balance_entry = input(f"{Fore.BLUE}Porfavor ingrese su saldo a retirar: ${Fore.RED}").replace(",", ".")
            sucess, message = process_operation(1, balance, float(new_balance_entry))
            if sucess:
                balance -= float(new_balance_entry)
        elif opt == 2:
            new_balance_entry = input(f"{Fore.BLUE}Porfavor ingrese el monto de su deposito: ${Fore.GREEN}").replace(",", ".")
            sucess, message = process_operation(2, balance, float(new_balance_entry))
            if sucess:
                balance += float(new_balance_entry)
        elif opt == 3:
            print(f"{Fore.RED}Cerrando sesión.... Gracias por usar Bank_Chafa :)")
            swl = True
            continue
        else:
            print(f"{Fore.RED}Opción fuera de rango{Style.RESET_ALL}")

        color = Fore.GREEN if sucess else Fore.RED
        print(f"{color}{message}{Style.RESET_ALL}")

    except ValueError:
        print(f"{Fore.RED}Debes introducir números en tu balance solamente {Style.RESET_ALL}")
        continue