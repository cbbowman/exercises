def isIsomorphic(s: str, t: str) -> bool:
    len_s = len(set(s))
    len_t = len(set(t))
    len_st = len(set(zip(s, t)))

    return len_s == len_t == len_st


print(isIsomorphic("title", "paper"))
