
def EnsureInt(value) -> int:
    try:
        return int(value)
    except (ValueError):
        return 0
