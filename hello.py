def greet(name):
    """Return a friendly greeting for the given name."""
    if any("\u4e00" <= char <= "\u9fff" for char in name):
        return f"你好，{name}！"
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(greet("Codex"))
