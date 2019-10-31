def maskify(cc):
    result = ''
    i = 0
    while i < len(cc)-4:
        result += '#'
        i += 1
    result += cc[-4:]
    return result