def merge_files(src="src.txt", dest="dest.txt", out="out.txt") -> None:
    try:
        with open(out, 'w', encoding='utf-8') as outfile:
            with open(src, 'r', encoding='utf-8') as f1:
                outfile.write(f1.read() + "\n")
            with open(dest, 'r', encoding='utf-8') as f2:
                outfile.write(f2.read() + "\n")
        print(f"Files '{src}' and '{dest}' merged into '{out}'.")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

merge_files()

