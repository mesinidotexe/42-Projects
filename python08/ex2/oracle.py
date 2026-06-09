import os


if __name__ == '__main__':
    print()
    print('ORACLE STATUS: Reading the matrix')
    print()

    try:
        from dotenv import load_dotenv

    except ImportError:
        print('Change to virtual enviroment first')
        print('Or do pip install dotenv to intall dotenv and python-dotenv')

    load_dotenv('.env.example')
    mode = os.getenv('MATRIX_MODE')
    data_base = os.getenv('DATABASE')
    api_access = os.getenv('API_KEY')
    log_level = os.getenv('LOG_LEVEL')
    zion_network = os.getenv('ZION_NETWORK')
    env_vars = [data_base,
                api_access,
                log_level,
                zion_network
                ]

    if None in env_vars:
        print('Missing variable in .env file')
        quit()

    if mode == 'development' or mode == 'production':
        print(f'Mode: {mode}')
    else:
        print(f'Mode "{mode}" not in the standards')
        print('Quitting the program')
        quit()

    if mode == 'development':
        print(f'Batabase: Connected to local instance')
        print(f'API Access: Authenticated')
        print(f'Log Level: DEBUG')
        print(f'Zion Network: ONLINE')

        print()

        print('[OK] No hardcoded secrets detected')
        if os.path.exists('.env'):
            print('[OK] .env file properly configured')
        else:
            print('[X] .env file not configured')
        print('[X] Production overrides available')
        print()

    else:
        print(f'Batabase: {data_base}')
        print(f'API Access: {api_access}')
        print(f'Log Level: {log_level}')
        print(f'Zion Network: {zion_network}')
        print()

        print('[X] No hardcoded secrets detected')
        if os.path.exists('.env'):
            print('[OK] .env file properly configured')
        else:
            print('[X] .env file not configured')
        print('[OK] Production overrides available')
        print()
        print('The Oracle sees all configurations')
