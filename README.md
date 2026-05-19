# Codex 入门练习仓库

这是一个最小 Python 学习项目，用来练习让 Codex 创建、阅读、修改和测试代码。

## 文件说明

- `hello.py`：包含一个简单的 `greet(name)` 函数，并在直接运行时打印示例结果。
- `test_hello.py`：包含一个最小测试，用来验证 `greet("Codex")` 的返回结果。
- `requirements.txt`：记录项目依赖。本项目不需要第三方依赖。

## 如何运行示例程序

在仓库根目录运行：

```bash
python hello.py
```

你应该会看到类似输出：

```text
Hello, Codex!
```

## 如何运行测试

在仓库根目录运行：

```bash
python -m unittest test_hello.py
```

如果测试通过，说明 `greet(name)` 的行为符合预期。
