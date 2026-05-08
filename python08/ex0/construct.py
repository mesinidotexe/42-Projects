import sys
import os
import site


def find_venvs(start_path):
    venvs = []
    
    for root, dirs, files in os.walk(start_path):
        if 'pyvenv.cfg' in files:
            return True
    return False


def associating_venv(start_path):
    venvs = ''
    
    for root, dirs, files in os.walk(start_path):
        if 'pyvenv.cfg' in files:
            venvs += (root)
    return venvs


def in_venv():
    if sys.prefix != sys.base_prefix:
        return True
    else:
        return False


if __name__ == '__main__':

    # print(f'{sys.prefix}\n{sys.base_prefix}')
    # print()
    if in_venv():
        print('MATRIX STATUS: Welcome to the construct')
        print()

        print(f'Current python: {sys.executable}')
        print(f'Virtual enviroment: {associating_venv('.')}')
        print(f'Enviroment path: {sys.prefix}')
        print()

        print("SUCCESS: You're in an isolated environment!")
        print('Safe to install packages without affecting the global system.\n')
        print()

        print('Package installation path:')
        print(site.getsitepackages()[0])

    else:
        print('MATRIX STATUS: youre still plugged in')
        print()

        print(f'Current Python: {sys.executable}')
        found = 'None detected'
        if find_venvs('.'):
            found = associating_venv('.')
        print(f'Virtual enviroment: {found}')
        print()
        
        print('WARNING: Youre still in the global enviroment')
        print('The machines can see everything you install')
        print()
        
        print('To enter the construct, run:')
        print('python3 -m venv matrix_env')
        print('source matrix_env/bin/activate # On Unix')
        print('matrix_env\\Scripts\\activate # On Windows')
        print()
        
        print('Then run this program again')