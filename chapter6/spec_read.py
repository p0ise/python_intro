def count_words(text: str) -> int:
    """count words in the given text.
       A word is a single series of consecutive letters.

    Args:
        text (str): a text

    Returns:
        int: the number of words
    """
    return len(text.split(" "))


def main():
    filename = "example"
    with open(filename, 'r') as f:
        for line_number, content in enumerate(f.readlines()):
            if line_number == 0:
                continue
            line = "{:4d} : {:4d} words | {}".format(
                line_number+1, count_words(content), content.strip())
            print(line)


if __name__ == "__main__":
    main()
