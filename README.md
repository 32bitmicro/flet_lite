# flet-lite
`flet-lite` is tiny version of flet that is compatible with with devices like iPadOS and iOS. Its not using `subprocess` or `multiprocess` which are not supported on mobile and iPad as will. Its just magic how everything is work properly 🪄!

|| **Why flet-lite 🙃?**

When I was trying to use my iPad for programming, I was miss something, which is my favourite UI library [flet](https://flet.dev/)!. Flet is a python library that allow you to code flutter apps in python without using dart or flutter. Everything is perfectly pythonic. Due to iPadOS limitations I was not able to code flet on python for iPad version. Then I came up with an idea of making a tiny version of the library for iPad, so me (and anyone) can use this powerful package just on iPad!!.

|| **What code editor to use 👨‍💻?**

You can use any code editor that support `pip` on mobile or iPad, these are some recommends:
- [Code App](https://apps.apple.com/app/id1512938504): Its a paid app that provide a powerful tools for coding. Also its a vscode like theme. Its include a terminal that support python and `pip`.
- [a-shell](https://apps.apple.com/app/id1473805438): Its a free app that provide a linux-like shell, its include python by default, also supports `pip`.


## installation ⬇️

Using `pip`, enter:
- **Soon**
```zsh
pip install flet_lite --upgrade
```

To use the beta version, install it from `git` command:
```zsh
pip install git+https://github.com/SKbarbon/flet_lite.git --upgrade
```

## docs 📖
This `flet-lite` is using the `flet` version v0.7.4

Everything is the same on original flet, read the docs here:
[flet.dev](https://flet.dev/)👈

## flet commands 
Due iPadOS limits, you cant use many of `flet` commands. The supported command is:
- **`python3 -m flet.publish myapp.py`**: This is used to create a pyodide site of your flet application so it can work on a normal web host (Any host that support static files, for example php servers).

## best usage practice
soon