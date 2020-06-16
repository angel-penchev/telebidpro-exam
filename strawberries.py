import re


def main():
    K, L, R = parse_user_input(3)
    AX, AY = parse_user_input(2)
    try:
        BX, BY = parse_user_input()
    except UnboundLocalError:
        pass

    field = [[1 for j in range(L)] for i in range(K)]
    field[AX - 1][AY - 1] = 0
    field[BX - 1][BY - 1] = 0
    # print_field(field)

    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    for _ in range(R):
        new_field = [row.copy() for row in field]
        for i, row in enumerate(field):
            for j, cell in enumerate(row):
                if cell == 0:
                    for direction in directions:
                        if not i - direction[0] < 0 and not j - direction[1] < 0:
                            try:
                                new_field[i - direction[0]][j - direction[1]] = 0
                            except IndexError:
                                pass
        field = new_field
        # print_field(field)

    print(sum([row.count(1) for row in field]))


def parse_user_input(required_outputs=None):
    data = input()
    data = data.strip(' \t\n\r')
    data = re.split(r',\s', data)
    if required_outputs and len(data) != required_outputs:
        raise IOError
    return [int(i) for i in data]


def print_field(field):
    for row in field:
        print(row)
    print('\n')


if __name__ == "__main__":
    main()
