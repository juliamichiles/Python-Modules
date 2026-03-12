#!/usr/bin/python3


def ft_ancient_text() -> None:

    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    file_name = "ancient_fragment.txt"
    try:
        print(f"Accessing Storage Vault: {file_name}")
        print("Connection established...")
        with open(file_name, "r") as file:
            content = file.read()
            print(content)
        print("RECOVERED DATA:")
        print("\nData recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")
    except PermissionError:
        print("ERROR: No permission to access storage vault")


if __name__ == "__main__":
    ft_ancient_text()
