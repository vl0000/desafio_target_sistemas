def reverse_string(string: str) -> str:
    output = ""
    for i in range(len(inp)-1, -1, -1):
        output += inp[i]

    return output


if __name__ == "__main__":
    inp: str = input("Digite sua string:\n")
    print(reverse_string(inp))
