#!/usr/bin/env python3
from collections.abc import Callable
from functools import wraps
import time as t # Could I do this without it? 

# Should I add type hints to the wraps?

def spell_timer(func: Callable) -> Callable:
	#  Create a decorator that measures function execution time
	#  Use functools.wraps to preserve original function metadata
    
    @wraps(func)
    def wrapper(*args, **kwargs):
	    # Print "Casting function_name..." before execution
        print(f"Casting {func.__name__}...")
        
        start = t.time()
        result = func(*args, **kwargs)
        end = t.time()
	    
        # Print "Spell completed in X.XXX seconds" after execution
        print(f"Spell completed in {(end - start):.3f} seconds")
        
	    # Return the original function’s result 
        return result
    
    return wrapper

def power_validator(min_power: int) -> Callable:
	#  Create a decorator factory that validates power levels
	#  Applied on a standalone function
	
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            power = kwargs.get("power", args[-1])
            if power >= min_power:
            # If power is valid, execute the function normally
                return func(*args, **kwargs)
            else:
	        # If invalid, return "Insufficient power for this spell"
                return "Insufficient power for this spell"
        return wrapper
        
    return decorator


def retry_spell(max_attempts: int) -> Callable:
	#  Create a decorator that retries failed spells
	#  If function raises an exception, retry up to max_attempts times
    def decorator(func: Callable) -> Callable:
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts+1):
                try:
	                # If one attempt succeeds, return its result normally
                    return func(*args, **kwargs)
                except Exception:
	            # Print "Spell failed, retrying... (attempt n/max_attempts)"
                    print(
                            "Spell failed, retrying... "
                            f"(attempt {attemp}/{max_attempts})"
                    )
             # If all attempts fail, return: 
             return f"Spell casting failed after {max_attempts} attempts"
         
         return wrapper

     return decorator

class MageGuild:
    
    @staticmethod
    def validate_mage_name(name: str) -> bool:
    
    # Static method that checks if name is valid
    # (at least 3 characters and contains only letters/spaces)
        if len(name) < 3:
            return False
        for char in name:
            if not char.isalpha() and not char.isspace():
                return False
        return True

    def cast_spell(self, spell_name: str, power: int) -> str:
        
        if power < 10:
            return "Insufficient power for this spell"
        
        return f"Successfully cast {spell_name} with {power} power"

def main() -> None:
    #TODO: this


if __name__ == '__main__':
    main()
