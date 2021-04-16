def custom_range(stop, *args, start=None, step=1) -> list[str]:
    str = ""
    for el in args:
        str += el
    stopChar = str.index(stop)
    if start is not None:
        startChar = str.index(start)
    else:
        startChar = start
    return list(str[startChar:stopChar:step])


custom_range("w", *["string.ascii_lowercase", "one"])
