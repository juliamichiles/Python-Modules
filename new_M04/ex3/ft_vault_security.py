#!/usr/bin/python3


def ft_vault_security() -> None:

    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print("\nInitiating secure vault access...")

    file_1 = "classified_data.txt"
    file_2 = "security_protocols.txt"

    try:
        print("Vault connection established with failsafe protocols\n")
        with open(file_1, "r") as f1:
            print("SECURE EXTRACTION:")
            cont1 = f1.read()
            print(cont1)
        with open(file_2, "r") as f2:
            print("\nSECURE PRESERVATION:")
            cont2 = f2.read()
            print(cont2)
    except PermissionError:
        print("ERROR: No permission to access storage vault")
    print("Vault automatically sealed upon completion\n")
    print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    ft_vault_security()
