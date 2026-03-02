
from colorama import Style, Fore
from utils import generic_input, generic_animation_load

def calculate_tax(amount:int) -> int | float:
    """
    Función para calcular el impuesto a los Movimientos Financieros del 4 x 1000.
    
    Args:
        amount (int | float): El monto sobre el cual se calculará el impuesto.
    Returns:
        tax_amount (int | float): El monto del impuesto calculado.
    """
    tax_rate = 0.004
    tax_amount = amount * tax_rate
    return tax_amount

def add_deposit(current_account:str, users:dict, deposit:int | float) -> tuple[bool, str]:
    """
    Función para agregar un depósito a una cuenta específica.

    Args:
        account (str): El nombre de la cuenta a la que se agregará el depósito.
        users (dict): El diccionario de usuarios y sus datos.
        deposit (int | float): El monto del depósito a agregar.
    Returns:
        tuple[bool, str]: Una tupla que contiene un booleano indicando el éxito de la operación y un mensaje descriptivo del resultado.
    """
    if current_account not in users:
        return (False, f"{Fore.RED}[ACCOUNT_ERROR]{Style.RESET_ALL} La cuenta '{current_account}' no existe. Por favor, verifica el nombre de la cuenta e intenta nuevamente.")

    if deposit < 5000:
        return (False, f"{Fore.RED}[DEPOSIT_ERROR]{Style.RESET_ALL} El monto del depósito debe ser de por lo menos $5.000. Por favor, ingresa un monto válido.")

    users[current_account]["balance"] += deposit

    generic_animation_load(f"{Fore.GREEN}Realizando deposito", 3, 0.8)
    print("\n")
    return (True, f"{Fore.GREEN}[SUCCESS]{Style.RESET_ALL} Depósito de ${deposit:,} agregado exitosamente a la cuenta '{current_account}'. Nuevo saldo: ${users[current_account]['balance']:,}.")

def make_transfer(current_account:str, target_account:str, users:dict, amount_transfer:int | float) -> tuple[bool, str]:
    """
    Función para realizar una transferencia desde una cuenta específica a otra cuenta.

    Args:
        current_account (str): El nombre de la cuenta desde la cual se realizará la transferencia.
        target_account (str): El nombre de la cuenta a la cual se realizará la transferencia.
        users (dict): El diccionario de usuarios y sus datos.
        amount_transfer (int | float): El monto de la transferencia a realizar.
    Returns:
        tuple[bool, str]: Una tupla que contiene un booleano indicando el éxito de la operación y un mensaje descriptivo del resultado.
    """
    if target_account not in users:
        return (False, f"{Fore.RED}[ACCOUNT_ERROR]{Style.RESET_ALL} La cuenta '{target_account}' no existe. Por favor, verifica el nombre de la cuenta e intenta nuevamente.")

    if amount_transfer < 5000:
        return (False, f"{Fore.RED}[TRANSFER_ERROR]{Style.RESET_ALL} El monto minimo de la transferencia debe ser de por lo menos $5.000. Por favor, ingresa un monto válido.")

    if users[current_account]["balance"] < amount_transfer:
        return (False, f"{Fore.RED}[TRANSFER_ERROR]{Style.RESET_ALL} Fondos insuficientes en la cuenta '{current_account}' para realizar la transferencia. Saldo actual: ${users[current_account]['balance']:,}.")

    mount_of_tax = int(calculate_tax(amount_transfer))

    result = int(amount_transfer + mount_of_tax)

    if result > users[current_account]["balance"]:
        if mount_of_tax < users[target_account]["balance"]:
            print(f"{Fore.YELLOW}[TRANSFER_WARNING]{Style.RESET_ALL} La transferencia + la comisión del 4 x 1000, supera la cantidad total de sus fondos, desea cobrar la comisión que es de: {calculate_tax(amount_transfer):,} del saldo de su segunda cuenta?, el cual es de: {users[target_account]['balance']:,}")
            has_accept = generic_input(f"{Fore.YELLOW}[WARNING] Desea cobrar la comisión al saldo de su otra cuenta? (s/n): ", str).lower()
            if has_accept == "s":
                users[current_account]["balance"] -= amount_transfer

                users[target_account]["balance"] -= mount_of_tax

                users[target_account]["balance"] += amount_transfer

                generic_animation_load(f"{Fore.GREEN}Realizando transferencia", 3, 0.8)
                print("\n")
                return (True, f"{Fore.GREEN}[SUCCESS]{Style.RESET_ALL} Transferencia realizada. El impuesto (${mount_of_tax:,}) se cobró de la cuenta '{target_account}', su saldo aumentó a {users[target_account]['balance']:,} y el saldo de su cuenta quedó en: {users[current_account]['balance']:,}")

        return (False, f"{Fore.RED}[TRANSFER_ERROR]{Style.RESET_ALL} Fondos insuficientes en la cuenta '{current_account}' para cubrir el monto de la transferencia más el impuesto. Monto total requerido: ${result:,}. Saldo actual: ${users[current_account]['balance']:,}. Si aún desea realizar la transferencia le recomendamos transferir la cantidad de ${users[current_account]['balance'] - calculate_tax(users[current_account]['balance']):,}.")

    users[current_account]["balance"] -= result


    users[target_account]["balance"] += amount_transfer

    generic_animation_load(f"{Fore.GREEN}Realizando transferencia", 3, 0.8)
    print("\n")
    return (True, f"{Fore.GREEN}[SUCCESS]{Style.RESET_ALL} Transferencia de ${amount_transfer:,} realizada exitosamente desde la cuenta '{current_account}' hacia la cuenta '{target_account}'. Nuevo saldo: ${users[current_account]['balance']:,}.")

def make_withdrawal(current_account:str, users:dict, amount_withdraw:int) -> tuple[bool, str]:
    """
    Función para realizar un retiro de la cuenta actual.

    Args:
        current_account (str): El nombre de la cuenta desde la cual se realizará el retiro.
        users (dict): El diccionario de usuarios y sus datos.
        amount_withdraw (int | float): El monto del retiro a realizar.
    Returns:
        tuple[bool, str]: Una tupla que contiene un booleano indicando el éxito de la operación y un mensaje descriptivo del resultado.
    """
    if amount_withdraw < 5000:
        return (False, f"{Fore.RED}[WITHDRAW_ERROR]{Style.RESET_ALL} El monto minimo del retiro debe ser de por lo menos $5.000. Por favor, ingresa un monto válido.")

    if current_account not in users:
        return (False, f"{Fore.RED}[ACCOUNT_ERROR]{Style.RESET_ALL} La cuenta '{current_account}' no existe. Por favor, verifica el nombre de la cuenta e intenta nuevamente.")

    mount_of_tax = int(calculate_tax(amount_withdraw))

    result = amount_withdraw + mount_of_tax

    other_account = [name for name in users.keys() if name != current_account][0]

    if result > users[current_account]["balance"]:
        if mount_of_tax < users[other_account]["balance"]:
            print(f"{Fore.YELLOW}[WITHDRAW_WARNING]{Style.RESET_ALL} El retiro + el impuesto del 4 x 1000, supera la cantidad total de sus fondos, desea cobrar el impuesto que es de: {calculate_tax(amount_withdraw):,} del saldo de su segunda cuenta?, el cual es de: {users[other_account]['balance']:,}")
            has_accept = generic_input(f"{Fore.YELLOW}[WARNING] Desea cobrar la comisión al saldo de su otra cuenta? (s/n): ", str).lower()
            if has_accept == "s":
                users[current_account]["balance"] -= amount_withdraw

                users[other_account]["balance"] -= mount_of_tax

                generic_animation_load(f"{Fore.GREEN}Realizando retiro", 3, 0.8)
                print("\n")
                return (True, f"{Fore.GREEN}[SUCCESS]{Style.RESET_ALL} Retiro realizado correctamente. El impuesto (${mount_of_tax:,}) se cobró de la cuenta '{other_account}', su nuevo saldo es {users[other_account]['balance']:,} y el saldo de su cuenta después del retiro quedó en: {users[current_account]['balance']:,}")

        return (False, f"{Fore.RED}[WITHDRAW_ERROR]{Style.RESET_ALL} Fondos insuficientes en la cuenta '{current_account}' para cubrir el monto del retiro más el impuesto, monto total requerido: ${result:,}. Saldo actual: ${users[current_account]['balance']:,}. Si aún desea realizar el retiro le recomendamos retirar la cantidad de ${users[current_account]['balance'] - calculate_tax(users[current_account]['balance']):,}.")

    users[current_account]["balance"] -= result

    generic_animation_load(f"{Fore.GREEN}Realizando retiro", 3, 0.8)
    print("\n")
    return (True, f"{Fore.GREEN}[SUCCESS]{Style.RESET_ALL} Retiro de ${amount_withdraw:,} realizado exitosamente desde la cuenta '{current_account}'. Nuevo saldo: ${users[current_account]['balance']:,}. El monto del impuesto cobrado por el retiro fue de: ${mount_of_tax:,}.")