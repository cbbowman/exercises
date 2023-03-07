def print_rangoli(size):
    start = ord("a")
    total_rows = (2 * size) - 1
    total_cols = (2 * total_rows) - 1
    rang = []
    for i in range(total_rows):
        new_row = []
        for j in range(total_cols):
            new_row.append("-")
        new_row.append("\n")
        rang.append(new_row)

    for i, r in enumerate(rang):
        v_off = abs(i - (size - 1))
        for j, c in enumerate(r):
            h_off = abs((j // 2) - (size - 1))
            offset = v_off + h_off
            if j % 2 == 0:
                if offset < size:
                    r[j] = chr(start + offset)

    s = ""
    result = []
    for r in rang:
        result.append(s.join(r))
    result = s.join(result)
    return result
    # your code goes here


r = print_rangoli(7)

print(r)

if __name__ == "__main__":
    pass
