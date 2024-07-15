def stringConstruction(s):
    # The minimum cost is the number of unique characters in the string
    return len(set(s))

if __name__ == "__main__":
    n = int(input().strip())  # Read the number of strings
    for _ in range(n):
        s = input().strip()  # Read each string
        print(stringConstruction(s))  # Print the minimum cost for each string
