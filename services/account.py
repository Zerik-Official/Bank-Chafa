"""Servicio de gestión de cuentas bancarias para Bank Chafa."""
from colorama import Fore, Style


def create_account(users:dict, name:str, initial_deposit:float) -> dict:
    """
    Crea una nueva cuenta bancaria con un nombre y un depósito inicial.

    Args:
        users (dict): El diccionario de usuarios existentes.
        name (str): El nombre del titular de la cuenta.
        initial_deposit (float): El monto del depósito inicial para la cuenta.

    Returns:
        dict: Un diccionario que representa la cuenta bancaria creada, con el nombre del titular y el saldo inicial.
    """
    if name is None:
        raise ValueError(f"{Fore.RED}[USER_ERROR]{Style.RESET_ALL} El nombre no puede ser nulo.")

    name = name.strip().title()

    if name in users:
        raise ValueError(f"{Fore.RED}[USER_ERROR]{Style.RESET_ALL} El nombre de usuario ya existe. Por favor, elige otro nombre.")
    elif name == "":
        raise ValueError(f"{Fore.RED}[USER_ERROR]{Style.RESET_ALL} El nombre de usuario no puede estar vacío. Por favor, ingresa un nombre válido.")
    elif name.isspace():
        raise ValueError(f"{Fore.RED}[USER_ERROR]{Style.RESET_ALL} El nombre de usuario no puede contener solo espacios. Por favor, ingresa un nombre válido.")
    elif not name.replace(" ", "").isalpha():
        raise ValueError(f"{Fore.RED}[USER_ERROR]{Style.RESET_ALL} El nombre de usuario no puede contener números. Por favor, ingresa un nombre válido.")

    if initial_deposit < 500000:
        raise ValueError(f"{Fore.RED}[DEPOSIT_ERROR]{Style.RESET_ALL} El depósito inicial debe ser de al menos $500,000 para crear una cuenta.")
    
    users[name] = {"balance": initial_deposit}

    return users