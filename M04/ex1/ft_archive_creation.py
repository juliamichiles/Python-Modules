#!/usr/bin/python3

class FileError(Exception):
    pass


def ft_archive_creation() -> None:
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")

    file_name = "new_discovery.txt"
    if file_name != "new_discovery.txt":
        raise FileError("ERROR: invalid file name!")
    text = (
        "[ENTRY 001] New quantum algorithm discovered\n"
        "[ENTRY 002] Efficiency increased by 347%\n"
        "[ENTRY 003] Archived by Data Archivist trainee\n"
        )

    try:
        with open(file_name, "w") as file:
            file.write(text)
        with open(file_name, "r") as file:
            content = file.read()
            print("Initializing new storage unit: new_discovery.txt")
            print("Storage unit created successfully...\n")
            print("Inscribing preservation data...")
            print(content)
            print("\nData inscription complete. Storage unit sealed.")
            print("Archive 'new_discovery.txt'"
                  "ready for long-term preservation.")
    except PermissionError:
        print("ERROR: No permission to access storage vault")
    except FileError as e:
        print(f"{e}")


if __name__ == "__main__":
    ft_archive_creation()
