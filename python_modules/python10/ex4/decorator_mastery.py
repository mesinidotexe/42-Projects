from collections.abc import Callable
from functools import wraps
from time import time, sleep


def spell_timer(func: Callable) -> Callable:

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'Casting {func.__name__}...')
        start: float = time()
        sleep(0.5)
        result: Callable = func(*args, **kwargs)
        total: float = time() - start
        print(f'Spell completed in {total:.3f} seconds ')
        return result

    return wrapper


def power_validator(min_power: int) -> Callable:
    
    def decorator(func: Callable) -> Callable:
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            power: int = args[2]
            if power >= min_power:
                return func(*args, **kwargs)
            return f'Insuficient power ({args[2]}) for this spell ({args[1]})'
        
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    
    def decorator(func: Callable):
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            trial: int = 1
            msg: str = f'Spell casting failed after {max_attempts} attempt'
            while trial <= max_attempts:
                try:
                    result: Callable = func(*args, **kwargs)
                    break
                except Exception:
                    print(f'Spell failed, retrying... ({trial}/{max_attempts})')    
                trial += 1
            if trial >= max_attempts:
                return msg
            return result
        return wrapper
    return decorator


@spell_timer
def fireball() -> str:
    return 'Result: Fireball cast!'


@retry_spell(max_attempts=3)
def retries() -> None:
    raise RuntimeError("FAAAAAHHH")


class MageGuild:
    
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) >= 3:
            for char in name:
                if not char.isalpha() and not char == ' ':
                    return False
            return True
        return False
    
    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f'Successfully cast {spell_name} with {power} power'


def main() -> None:
    print('Testing spell timer...')
    print(fireball())
    
    print()

    print('Testing retrying spell...')
    sleep(1)
    print(retries())
    
    print()
    
    print('Testing MageGuild...')
    sleep(1)
    guild: MageGuild = MageGuild()
    print(MageGuild.validate_mage_name("Sage"))
    print(MageGuild.validate_mage_name("R3yna"))
    print(MageGuild.validate_mage_name("Manuel Gomes"))

    print(guild.cast_spell("lightning", 15))
    print(guild.cast_spell("Fireball", 5))
    

if __name__ == '__main__':
    main()