#!/usr/bin/python3

def ft_crisis_response() -> None:

    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    file_list = [
            'lost_archive.txt',
            'classified_data.txt',
            'standard_archive.txt'
            ]

    for file in file_list:
        try:
            with open(file, 'r') as f:
                content = f.read()
                print(f"ROUTINE ACCESS: Attempting access to '{file}'...")
                print(f"SUCCESS: Archive recovered - ``{content}''")
                print("STATUS: Normal operations resumed\n")
        except PermissionError:
            print(f"CRISIS ALERT: Attempting access to '{file}'...")
            print("RESPONSE: Security protocols deny access")
            print("STATUS: Crisis handled, security maintained\n")
        except FileNotFoundError:
            print(f"CRISIS ALERT: Attempting access to '{file}'...")
            print("RESPONSE: Archive not found in storage matrix")
            print("STATUS: Crisis handled, system stable\n")
    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    ft_crisis_response()
