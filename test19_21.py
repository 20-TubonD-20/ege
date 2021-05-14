from functools import lru_cache
def moves(h):
    a,b = h
    return (a+1,b),(a,b+1),(a*4,b),(a,b*4)

@lru_cache(None)
def f(h):
    if(sum(h) >= 151):
        return 'END'
    if(any(f(x) == 'END' for x in moves(h))):
        return 'П1'
    if(all(f(x) == 'П1' for x in moves(h))):
        return 'В1'
    if(any(f(x) == 'В1' for x in moves(h))):
        return 'П2'
    if(all(f(x) == 'П1' or f(x) == 'П2'for x in moves(h))):
        return 'В2'

for i in range(1,142):
    h = 9, i
    print(i, (f(h)))
