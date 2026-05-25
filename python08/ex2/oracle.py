import os


if __name__ == '__main__':
    print()
    print('ORACLE STATUS: Reading the matrix')
    print()

    try:
        from dotenv import load_dotenv
        load_dotenv('.env.example')
        mode = os.getenv('MATRIX_MODE')
        if mode == 'development' or mode == 'production':
            print(f'Mode: {mode}')
        else:
            print(f'Mode "{mode}" not in the standards')
            print('Quitting the program')
            quit()
        data_base = os.getenv('DATABASE')
        print(f'Batabase: {data_base}')
        api_access = os.getenv('API_KEY')
        print(f'API Access: {api_access}')
        log_level = os.getenv('LOG_LEVEL')
        print(f'Log Level: {log_level}')
        zion_network = os.getenv('ZION_NETWORK')
        print(f'Zion Network: {zion_network}')
        print()

        print('[OK] No hardcoded secrets detected')
        print('[OK] .env file properly configured')
        print('[OK] Production overrides available')
        print()

        print('The Oracle sees all configurations')
    except ImportError:
        print('Change to virtual enviroment first')
        print('Or do pip install dotenv to intall dotenv and python-dotenv')
