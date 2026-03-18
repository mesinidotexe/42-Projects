def main():
    print('=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n')
    print('Initiating secure vault access...')
    with open('classified_data.txt', 'r') as file:
        print('Vault connection established with failsafe protocols\n')
        print('SECURE EXTRACTION:')
        print(file.read())
        print()
    with open('security_protocols.txt', 'r') as file:
        print('SECURE PRESERVATION:')
        print(file.read())
        print()
    print('All vault operations copleted with maximum security')


if __name__ == '__main__':
    main()
