import time
from colorama import Style, Fore, init
from .commons import generic_input, generic_animation_load

init(autoreset=True)

# Versión del programa
build:str = "2.0.0"

# Fecha de creación de esta versión
reseale_date:str = "2-03-2025"

# Creador del programa
author:str = "Zerik-Official"

# Repositorio del programa
repository:str = "https://github.com/Zerik-Official/Bank-Chafa"

# Información de la aplicación stylizada con colorama
info_application:str = f"{Fore.CYAN}Build: {Style.BRIGHT}{build}{Style.NORMAL} | Release date: {Style.BRIGHT}{reseale_date}"

# Información del creador stylizada con colorama
info_creator:str = f"{Fore.YELLOW}Author: {Style.BRIGHT}{author}{Style.NORMAL} | Repository: {Style.BRIGHT}{repository}"

# Terminos y condiciones del bank chafa
tos:str = f"""
Al usar esta aplicación, aceptas los siguientes términos y condiciones:
1. Para el uso de esta aplicación, se requiere un depósito inicial mínimo de $500,000. Este monto es necesario para garantizar la viabilidad de las operaciones bancarias dentro de la aplicación.
{Fore.YELLOW}================================================================={Style.RESET_ALL}
2. Al solicitar un retiro, se aplicará automáticamente un impuesto/comisión a los Movimientos Financieros de 4 x 1000. Si el monto total (retiro + impuesto) excede el saldo de la cuenta de origen, 
el sistema te preguntará si quieres usar el saldo de tu cuenta secundaria para cubrir el excedente, al aceptar, esta acción {Fore.RED}NO es reversible y NO reembolsable.{Style.RESET_ALL} De no contar con fondos suficientes en ninguna de las dos cuentas, la transacción será declinada automáticamente.
En este caso, recomendamos, bajar el monto del retiro o realizar un depósito adicional para cubrir el monto total.
"""

# Banner del banco
banner:str = rf"""
{Fore.GREEN}    ____              __  {Fore.YELLOW}   ________          ____     
{Fore.GREEN}   / __ )____ _____  / /__{Fore.YELLOW}  / ____/ /_  ____ _/ __/___ _
{Fore.GREEN}  / __  / __ `/ __ \/ //_/{Fore.YELLOW} / /   / __ \/ __ `/ /_/ __ `/
{Fore.GREEN} / /_/ / /_/ / / / / ,<   {Fore.YELLOW}/ /___/ / / / /_/ / __/ /_/ / 
{Fore.GREEN}/_____/\__,_/_/ /_/_/|_|  {Fore.YELLOW}\____/_/ /_/\__,_/_/  \__,_/  

{info_application}
{info_creator}
"""

def show_info_and_tos() -> None:
    print(banner)
    time.sleep(2)
    generic_animation_load(f"{Fore.GREEN}Inicializando servicios{Style.RESET_ALL}", 3, 2 / 3)

    generic_animation_load(f"{Fore.GREEN}Cargando datos{Style.RESET_ALL}", 3, 2/3)

    print(f"\n{Fore.GREEN}¡Bienvenido a Bank Chafa!{Style.RESET_ALL}")

    print("=" * 50)
    print(f"{Fore.YELLOW}[WARNING] Antes de continuar, por favor lee los términos y condiciones de uso:{Style.RESET_ALL}")
    print(tos)

    option = generic_input(f"{Fore.YELLOW}¿Aceptas los términos y condiciones? (s/n): {Style.RESET_ALL}", str).lower().strip()

    if option != 's':
        print(f"{Fore.RED}No puedes usar la aplicación sin aceptar los términos y condiciones. Lamentamos que nuestras politicas no sean de su agrado. Saliendo...{Style.RESET_ALL}")
        exit()