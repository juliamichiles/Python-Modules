#!/usr/bin/python3
import typing
import sys


def ft_archive_creation() -> None:

    ac = len(sys.argv)
    if ac != 2:
        print("Usage: ft_ancient_text.py <file>\n")
        return

    file = sys.argv[1]
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{file}'")
    try:

        print("---\n")
        f = open(file, "r")        
        og_content = f.read()
        print(og_content)
        print("\n---")
        f.close()
        print("File '{file}' closed.")
        
        new_lines = []
        for line in og_content.splitlines():
            new_lines.append(line + "#")

        new_cont = "\n".join(new_lines) + "\n"

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
        print(f"Error: {e}")


if __name__ == "__main__":
    ft_archive_creation()
