import re


def main():
    K, L, R = parse_user_input()
    AX, AY = parse_user_input()
    BX, BY = parse_user_input()

    field = [[1 for j in range(L)] for i in range(K)]
    field[AX][AY] = 0
    field[BX][BY] = 0
    print_field(field)

    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    for _ in range(R):
        new_field = [row.copy() for row in field]
        for i, row in enumerate(field):
            for j, cell in enumerate(row):
                if cell == 0:
                    for direction in directions:
                        try:
                            new_field[i - direction[0]][j - direction[1]] = 0
                        except IndexError:
                            pass
        field = new_field
        print_field(field)

def parse_user_input():
    data = input()
    data = data.strip(' \t\n\r')
    data = re.split(r',\s', data)
    return [int(i) for i in data]


def print_field(field):
    for row in field:
        print(row)
    print('\n')


if __name__ == "__main__":
    main()
