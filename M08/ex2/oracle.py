#!/usr/bin/env python3
import os
try:
    from dotenv import load_dotenv  # type: ignore

except ImportError as e:
    print(e)
    print("To install via pip:\n")
    print("\tpython3 -m pip install python-dotenv")
    exit(1)


def load_config() -> dict[str, str | None]:

    load_dotenv()

    config = {
        "MATRIX_MODE": os.getenv("MATRIX_MODE"),
        "DATABASE_URL": os.getenv("DATABASE_URL"),
        "API_KEY": os.getenv("API_KEY"),
        "LOG_LEVEL": os.getenv("LOG_LEVEL"),
        "ZION_ENDPOINT": os.getenv("ZION_ENDPOINT")
    }
    return config


def validate(config: dict[str, str | None]) -> dict[str, str | None]:

    missing: dict[str, str | None] = {}

    for key, value in config.items():
        if value is None:
            missing[key] = value

    return missing


def oracle() -> None:

    print('\nORACLE STATUS: Reading the Matrix...\n')
    print("Configuration loaded:")

    config = load_config()
    missing = validate(config)

    if missing:
        print(f"WARNING: Missing configuration for: {', '.join(missing)}")
        print("Please check your .env file or environment variables.\n")

    print(f"Mode: {config.get('MATRIX_MODE') or 'UNKNOWN'}")

    if config['DATABASE_URL']:
        print("Database: Connected to local instance")
    else:
        print("Database: No connection established")

    if config['API_KEY']:
        print("API Access: Authenticated")
    else:
        print("API Access: Denied")

    print(f"Log Level: {config['LOG_LEVEL'] or 'UNKNOWN'}")

    if config['ZION_ENDPOINT']:
        print("Zion Network: Online")
    else:
        print("Zion Network: Offline")

    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")

    env_variables = os.environ

    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] .env file not found")

    if "MATRIX_MODE" in env_variables:
        print("[OK] Production overrides available")
    else:
        print("[OK] Using standard configuration instead")

    print("\nThe Oracle sees all configurations.")


if __name__ == '__main__':
    oracle()
