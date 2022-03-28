def main():
    with open("./Dane/dane.txt") as f:
        strs = [x.strip() for x in f.readlines()]

    first_last = [x for x in strs if x[0] == x[-1]]

    decimal = [str(int(x, 8)) for x in strs]
    first_last_decimal = [x for x in decimal if x[0] == x[-1]]

    ascending = [int(x, 8) for x in strs if [*x] == sorted([*x])]

    results = (
        f"a) {len(first_last)}\n"
        f"b) {len(first_last_decimal)}\n"
        f"c) {len(ascending)}, największa: {max(ascending)}, najmniejsza: {min(ascending)}\n"
    )

    print(results)

    with open("./wyniki6.txt", "w") as f:
        f.write(results)


if __name__ == "__main__":
    main()
