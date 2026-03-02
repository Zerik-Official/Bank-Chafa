import os
from colorama import Style, Fore

from utils import show_info_and_tos, generic_input, generic_animation_load

from services import create_account, add_deposit, make_transfer, make_withdrawal


# Diccionario para almacenar los usuarios y sus datos
users:dict[str, dict[str, int]] = {}

# Opciones del menú
options:list[tuple[int, str]] = [
    (1, "Realizar un depósito."),
    (2, "Realizar una transferencia."),
    (3, "Consultar datos de tus cuentas."),
    (4, "Realizar un retiro."),
    (5, "Cerrar sesión y salir.")
]

def inicialite_bank() -> str:
    """Función para inicializar el banco, creando dos cuentas para el usuario y seleccionando una de ellas para iniciar sesión."""

    print(f"{Fore.MAGENTA}[INFO]{Style.RESET_ALL} Antes de continuar, necesitamos que crees sus dos cuentas.")

    while len(users) < 2:

        tag = "primera" if len(users) == 0 else "segunda"

        name = generic_input(f"{Fore.YELLOW}[INFO]{Style.RESET_ALL} Porfavor ingrese el nombre de su {tag} cuenta: ", str)
        initial_deposit = generic_input(f"{Fore.YELLOW}[INFO]{Style.RESET_ALL} Porfavor ingrese el monto del depósito inicial (mínimo $500,000): {Fore.GREEN}$", int)
        try:
            create_account(users, name, initial_deposit)
            print(f"{Fore.GREEN}[SUCCESS]{Style.RESET_ALL} Cuenta creada exitosamente para {name} con un depósito inicial de ${initial_deposit:,}.")
            
            print("=" * 50)

        except ValueError as e:
            print(f"{Fore.RED}[INTERNAL_ERROR] ->{Style.RESET_ALL} {e}")    
    
    print(f"{Fore.GREEN}[SUCCESS]{Style.RESET_ALL} Cuentas creadas exitosamente.")

    clean_accounts = ", ".join(users.keys())

    print(f"{Fore.CYAN}[INFO]{Style.RESET_ALL} Con que cuentas deseas iniciar sesión?, cuentas disponibles: {clean_accounts}")

    select_account = ""

    while select_account not in users:
        select_account = generic_input(f"{Fore.YELLOW}[INFO]{Style.RESET_ALL} Ingresa el nombre de la cuenta con la que deseas iniciar sesión: ", str).title()
        if select_account not in users:
            print(f"{Fore.YELLOW}[WARNING]{Style.RESET_ALL} Cuenta no encontrada. Por favor, ingresa un nombre válido.")
            continue
    
    return select_account

def init_menu(current_account: str) -> None:
    """
    Función para mostrar el menú principal y manejar las opciones seleccionadas por el usuario.
    
    Args:
        current_account (str): El nombre de la cuenta actualmente seleccionada para realizar operaciones.
    Returns:
        None
    """

    generic_animation_load(f"{Fore.YELLOW}[INFO]{Style.RESET_ALL} Limpiando la terminal", 3)
    
    os.system("cls" if os.name == "nt" else "clear")

    print(f"Cuenta seleccionada: {current_account} | Saldo: ${users[current_account]['balance']:,}")

    print("=" * 50)

    print(f"{Fore.CYAN}[INFO]{Style.RESET_ALL} Por favor a continuación, seleccione una opción.")

    init_exit = False

    while (not init_exit):

        result, message = None, None

        print(f"\nCuenta actual: {Fore.CYAN}{current_account}{Style.RESET_ALL} | Saldo: {Fore.GREEN}${users[current_account]['balance']:,}{Style.RESET_ALL}")

        print("=" * 50)

        for num, text in options:
            print(f"{num}. {text}")

        print("=" * 50)

        valid_numbers = [opt[0] for opt in options]

        entry_operation = generic_input("Seleccione su operación: ", int)


        match entry_operation:
            case 1:
                deposit = generic_input(f"{Fore.CYAN}[INFO]{Style.RESET_ALL} Por favor, introduzca su monto a depositar: {Fore.GREEN}$", int)
                result, message = add_deposit(current_account, users, deposit)
            case 2:
                target_account = generic_input(f"{Fore.CYAN}[INFO]{Style.RESET_ALL} Por favor, introduzca el nombre de la cuenta de destino (o 'salir' para cancelar): ", str).title()

                if target_account == "Salir":
                    continue

                if target_account == current_account:
                    print(f"{Fore.YELLOW}[WARNING]{Style.RESET_ALL} No puedes transferir a la misma cuenta activa.")
                    continue

                amount_transfer = generic_input(f"{Fore.CYAN}[INFO]{Style.RESET_ALL} Por favor, introduzca el monto a transferir, (minimo $5.000): {Fore.GREEN}$", int)
                result, message = make_transfer(current_account, target_account, users, amount_transfer)

            case 3:
                generic_animation_load(f"{Fore.BLUE}[INFO]{Style.RESET_ALL} Consultando la base de datos", 3)
                print(f"\n{Fore.CYAN}--- ESTADO GENERAL DE CUENTAS ---{Style.RESET_ALL}")
                
                for holder, data in users.items():
                    print(f"Cuenta: {Fore.YELLOW}{holder:<15}{Style.RESET_ALL} | Saldo: {Fore.GREEN}${data['balance']:,}{Style.RESET_ALL}")

                print("=" * 50)

            case 4:
                amount_withdraw = generic_input(f"{Fore.CYAN}[INFO]{Style.RESET_ALL} Por favor, introduzca el monto a retirar (minimo $5.000): {Fore.RED}$", int)
                result, message = make_withdrawal(current_account, users, amount_withdraw)
            case 5:
                generic_animation_load(f"{Fore.YELLOW}[INFO]{Style.RESET_ALL} Cerrando sesión", 3)
                init_exit = True
            case _:
                print(f"{Fore.RED}[ERROR_OPTION]{Style.RESET_ALL} Opción no válida.")

        if result is not None:
            print(f"{message}")


def main() -> None:
    # Inicializar el banner, TOS y demás datos
    show_info_and_tos()

    # Inicializar el banco, creando las cuentas y seleccionando una para iniciar sesión
    select_account = inicialite_bank()

    init_menu(select_account)

if __name__ == "__main__":
    main()