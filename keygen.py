import random

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'


def sdvig_symb(symb, sdvig):
    index = alphabet.find(symb)
    return alphabet[(index + sdvig) % 36]


def sdvig_all(block, sdvig):
    return ''.join([sdvig_symb(symb, sdvig) for symb in block])


def keygen(vvod):
    first = "".join([random.choice(alphabet) for i in range(5)])
    blocks = [first]

    previous_block = first
    for i, digit in enumerate(vvod):
        digit = int(digit)
        direct = 1 if i % 2 == 0 else -1
        next = previous_block[:-1]
        sdvig_block = sdvig_all(next, direct * digit)
        blocks.append(sdvig_block)
        previous_block = sdvig_block

    return "-".join(blocks)


if __name__ == "__main__":
    for i in range(3):
        print(keygen("000"))
