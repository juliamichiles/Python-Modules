#!/usr/bin/env python3
import sys
import site
import os


def construct() -> None:

    pckg_path = site.getsitepackages()[0]
    current_python = sys.executable
    venv = os.path.basename(sys.prefix)
    env_path = sys.prefix

    if sys.prefix != sys.base_prefix:
        print("\nMATRIX STATUS: Welcome to the construct\n")
        print(f"Current Python: {current_python}")
        print(f"Virtual Environment: {venv}")
        print(f"Environment Path: {env_path}")
        print("\nSUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.")
        print("\nPackage installation path:")
        print(pckg_path)
    else:
        print("\nMATRIX STATUS: You're still plugged in\n")
        print(f"Current Python: {current_python}")
        print("Virtual Environment: None detected")
        print("\nWARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print("\nTo enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\\Scripts\\activate # On Windows")
        print("\nThen run this program again.")


if __name__ == '__main__':
    construct()
