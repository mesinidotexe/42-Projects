from collections.abc import Callable
from functools import wraps
from time import time



def spell_timer(func: Callable) -> Callable:
    @wraps
    def wrap():
        print(f'Casting {func.__name__}...')
        t1 = time()
        func()
        t2 = time() - t1
        print(f'pell completed {t2:.3f} in  seconds" ')

    return wrap


def main() -> None:
    
    @spell_timer
    def fireball():
        return 'fireball him'


if __name__ == '__main__':
    main()