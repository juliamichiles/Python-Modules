#!/usr/bin/python3
import sys
import typing

def ft_stream_management() -> None:

    ac = len(sys.argv)
    if ac != 2:
        sys.stderr.write(f"Usage: {sys.argv[0]} <file>\n")
        return

    file = sys.argv[1]
    sys.stdout.write("=== Cyber Archives Recovery & Preservation ===\n")
    sys.stdout.write(f"Accessing file '{file}'\n")
    
    try:
        # opening file and printing content
        f = open(file, "r")
        og_content = f.read()
        sys.stdout.write("---\n\n")
        sys.stdout.write(og_content)
        sys.stdout.write("\n---\n")
        f.close()
        sys.stdout.write(f"File '{file}' closed.\n\n")
        sys.stdout.write("Transform data:\n---\n\n")
        
        # modifying list with
        new_lines = []
        for line in og_content.splitlines():
            new_lines.append(line + "#")

        new_cont = "\n".join(new_lines) + "\n"
        sys.stdout.write(new_cont + "\n")
        sys.stdout.write("---\n")
        sys.stdout.write("Enter new file name (or empty): ")
        sys.stdout.flush()
        user_input = sys.stdin.readline()
        new_name = user_input.strip()

        if new_name == "":
            sys.stdout.write("Not saving data.\n")
        else:
            sys.stdout.write(f"Saving data to '{new_name}'\n")
            try:
                outfile = open(new_name, "w")
                outfile.write(new_cont)
                outfile.close()
                sys.stdout.write(f"Data saved in file '{new_name}'.\n")
            except Exception as e:
                sys.stderr.write(f"[STDERR] Error opening file '{new_name}': {e}\n")
                sys.stdout.write("Data not saved.\n")
    except Exception as e:
        sys.stderr.write(f"[STDERR] Error opening file '{file}': {e}\n")


if __name__ == "__main__":
    ft_stream_management()
