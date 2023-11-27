# automate_startup.py

import os
import platform
import shutil

def create_bat_script(script_path):
    bat_content = f'@echo off\npython {script_path}\n'
    bat_file_path = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup', 'run_on_startup.bat')
    
    with open(bat_file_path, 'w') as bat_file:
        bat_file.write(bat_content)
    
    print(f"Arquivo .bat criado em: {bat_file_path}")

def create_cron_entry(script_path):
    cron_file_path = os.path.expanduser('~/.config/cron_startup')
    
    with open(cron_file_path, 'w') as cron_file:
        cron_file.write(f'@reboot /usr/bin/python3 {script_path}\n')
    
    print(f"Comando adicionado ao cron para iniciar em reboot: {cron_file_path}")

def main():
    # Caminho para o script Python***aqui tem que ser o caminho absoluto***
    script_path = input("Digite o caminho completo para o seu script Python: ")
    
    # Verifica o sistema operacional
    system_platform = platform.system()

    if system_platform == "Windows":
        create_bat_script(script_path)
    
    elif system_platform == "Linux":
        create_cron_entry(script_path)

    else:
        print("Sistema operacional não suportado pelo script.")

if __name__ == "__main__":
    main()
