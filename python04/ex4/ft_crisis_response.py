def main():
    print('=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n')
    try:
        print("CRISIS ALERT: Attempting access to 'lost_archive.txt'...")
        with open('lost_archive.txt', 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print('RESPONSE: Archive not found in storage matrix')
    finally:
        print('STATUS: Crisis handled, security maintained\n')
    
    try:
        # Cria um arquivo sem permisao nenhma
        print("CRISIS ALERT: Attempting access to 'classified_vault.txt'...")
        with open('classified_vault.txt', 'r') as file:
            print(file.read())
    except PermissionError:
        print('RESPONSE: Security protocols deny access')
    finally:
        print('STATUS: Crisis handled, security maintained\n')

    try:
        print("ROUTINE ACCESS: Attempting access to 'standard_archive.txt'...")
        with open('standard_archive.txt', 'w+') as file:
            file.write('SUCCESS: Archive recovered - "Knowledge preserved for humanity"')
            file.seek(0)
            print(file.read())
    except FileExistsError:
        print('File already exists')
    finally:
        print('STATUS: Normal operations resumed')


if __name__ == '__main__':
    main()