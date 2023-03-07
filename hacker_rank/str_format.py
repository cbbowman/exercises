def get_col_width(number):
    col_width = 1
    i = 0
    n = number
    while n > 1:
        n = n // 2
        i += 1
    col_width += i
    return col_width


def num_in_base(num, base, width):
    nb = ""
    hex_vals = ["A", "B", "C", "D", "E", "F"]
    leading_zero = True
    for c in range(width-1, -1, -1):
        divisor = base**(c)
        dm = divmod(num, divisor)
        if dm[0] == 0 and leading_zero:
            nb = nb + " "
        elif dm[0] > 9:
            nb = nb + hex_vals[dm[0]-10]
            leading_zero = False
        else:
            nb = nb + str(dm[0])
            leading_zero = False
        num = dm[1]
    return nb


def new_line(n, col_width):
    bases = [10, 8, 16, 2]
    vals = []
    for b in bases:
        num = num_in_base(n, b, col_width)
        vals.append(num)
    line = f"{vals[0]} {vals[1]} {vals[2]} {vals[3]}"
    return line


def print_formatted(number):
    col_width = get_col_width(number)
    for i in range(1, number+1):
        line = new_line(i, col_width)
        print(f"{line}")

print_formatted(60)

assert new_line(10, 5) == "   10    12     A  1010"
assert num_in_base(17, 8, 4) == "  21"
assert num_in_base(3, 2, 5) == "   11"
assert num_in_base(17, 16, 5) == "   11"
assert num_in_base(14, 16, 7) == "      E"
assert get_col_width(6) == 3
assert get_col_width(2) == 2
assert get_col_width(16) == 5
assert get_col_width(8) == 4
