def main():
    sample = [1, 2, 3]

    copy_ref = sample

    copy_value = sample[:]

    sample[2] = 4
    print("sample:", sample)
    print("copy_ref:", copy_ref)
    print("copy_value:", copy_value)


if __name__ == "__main__":
    main()
