def read_file(file):
    with open(file, 'r') as f:
        return f.read()


def write_file(file, content):
    with open(file, 'w') as f:
        f.write(content)


def is_continue():
    """ask if continue

    Returns:
        bool: whether continue
    """
    text = input("Do you want to continue([y]/n)?")
    if text == '':
        text = 'y'
    if text.lower() == 'y':
        return True
    else:
        return False


def main():
    print("This program will exchange the contents of two files you input.")

    while True:
        filename_a = input("Now please input the name of first file>")
        filename_b = input("Then input another>")
        if filename_a == filename_b:
            print("[-]The files should be different files.")
            if is_continue():
                continue
            else:
                break
        try:
            content_a = read_file(filename_a)
            content_b = read_file(filename_b)
            write_file(filename_a, content_b)
            write_file(filename_b, content_a)
            print(
                f"[+]The contents of {filename_a} and {filename_b} have exchanged!")
            break
        except:
            print("[-]Error: input an incorrect filename.Please try again.")
            if is_continue():
                continue
            else:
                break


if __name__ == "__main__":
    main()
