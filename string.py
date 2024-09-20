
inp: str = input("Digite sua string:\n")


def reverse_string(string: str) -> str:
    output = ""
    for i in range(len(inp)-1, -1, -1):
        output += inp[i]

    return output


print(reverse_string(inp))
