def HASH(s: str):
    import zlib

    # if _mode in [MODE.VERBOSE, MODE.READABLE]:
    return f"HASH({s})"
    # else:
    # return zlib.crc32(s.encode("utf-8")) & 0xFFFFFFFF


def sleep(seconds: float | str):
    return f"sleep {seconds}"
