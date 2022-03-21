def main():
    with open("./Dane/liczby.txt") as f:
        lines = f.readlines()
        
    strs = [x.strip() for x in lines]
    numbers = [int(x, 2) for x in strs]
        
    even = len([x for x in numbers if x % 2 == 0])
    biggest = max(numbers)
    niners = [int(x, 2) for x in strs if len(x) == 9]

    with open("./zadanie6.txt", "w") as f:
        f.write(f"a) {even}\n")
        f.write(f"b) {biggest}, {bin(biggest)}\n")
        f.write(f"c) {len(niners)}, {bin(sum(niners))}\n")
    
if __name__ == "__main__":
    main()