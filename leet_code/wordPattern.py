def wordPattern(pattern: str, s: str) -> bool:
    p_list = list(pattern)
    s_list = s.split(" ")

    if len(p_list) != len(s_list):
        return False
    p_set = set(p_list)
    s_set = set(s_list)
    len_pattern = len(p_set)
    len_s = len(s_set)
    len_ps = len(set(zip(p_list, s_list)))

    return len_pattern == len_s == len_ps


p = "abbacba"
s = "cat dog dog dog burger dog cat"

print(wordPattern(p, s))
