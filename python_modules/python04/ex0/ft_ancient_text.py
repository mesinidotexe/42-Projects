def main():
    print('=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===')
    print('Accessing Storage Vault: ancient_fragment.txt')
    try:
        with open('ancient_fragment.txt', 'r') as file:
            print('Connection established...')
            print(f'{file.read()}')
        print('Data recovery complete. Storage unit disconnected.')
    except FileNotFoundError:
        print('ERROR: Storage vault not found. Run'
              '"python3 data_generator.py" first.')


if __name__ == '__main__':
    main()
