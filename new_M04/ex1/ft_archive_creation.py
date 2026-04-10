#!/usr/bin/python3
import sys


def ft_archive_creation() -> None:

    ac = len(sys.argv)
    if ac != 2:
        print("Usage: ft_archive_creation <file>\n")
        return

    file = sys.argv[1]
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{file}'")
    try:

        f = open(file, "r")
        og_content = f.read()
        print("---\n")
        print(og_content)
        print("---")
        f.close()
        print(f"File '{file}' closed.\n")
        print("Transform data:\n---\n")

        new_lines = []
        for line in og_content.splitlines():
            new_lines.append(line + "#")

        new_cont = "\n".join(new_lines) + "\n"
        print(new_cont)
        print("---")
        new_name = input("Enter new file name (or empty): ")
        if new_name == "":
            print("Not saving data.")
        else:
            print(f"Saving data to '{new_name}'")
            outfile = open(new_name, "w")
            outfile.write(new_cont)
            outfile.close()
            print(f"Data saved in file '{new_name}'.")

    except Exception as e:
        print(f"Error opening file '{file}': {e}\n")


if __name__ == "__main__":
    ft_archive_creation()
