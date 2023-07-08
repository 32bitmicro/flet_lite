# flet-lite
`flet-lite` is tiny version of flet that is compatible with with devices like iPadOS and iOS. Its not using `subprocess` or `multiprocess` which are not supported on mobile and iPad as will. Its just magic how everything is work properly 🪄!

|| **Why flet-lite 🙃?**

When I was trying to use my iPad for programming, I was miss something, which is my favourite UI library [flet](https://flet.dev/)!. Flet is a python library that allow you to code flutter apps in python without using dart or flutter. Everything is perfectly pythonic. Due to iPadOS limitations I was not able to code flet on python for iPad version. Then I came up with an idea of making a tiny version of the library for iPad, so me (and anyone) can use this powerful package just on iPad!!.

|| **What code editor to use 👨‍💻?**

You can use any code editor that support `pip` on mobile or iPad, these are some recommends:
- [Code App](https://apps.apple.com/app/id1512938504): Its a paid app that provide a powerful tools for coding. Also its a vscode like theme. Its include a terminal that support python and `pip`.
- [a-shell](https://apps.apple.com/app/id1473805438): Its a free app that provide a linux-like shell, its include python by default, also supports `pip`.


|| **Is this for production 🌐?**

This package is not prepared to use for production cases so its a development only, use the original [flet](https://flet.dev) for production. The only tool here for production is the command `python3 -m flet.publish script.py` which is a custom command tool the present similer usage for the original `flet publish script.py`.

## installation ⬇️
- uninstall `flet` if you did install it before: `pip uninstall flet`.
- uninstall `flet-core` if you did install flet before: `pip uninstall flet-core`.
Using `pip`, enter:
```zsh
pip install flet_lite --upgrade
```

## docs 📖
This `flet-lite` is a custom clone of `flet` version v0.7.4

Everything is the same on original flet, read the docs here:
[flet.dev](https://flet.dev/)👈

## flet commands 
Due iOS, iPadOS and Android limits, you cant use many of `flet` commands. The supported commands is:
- **`python3 -m flet.publish myapp.py`**: This is used to create a pyodide site of your flet application so it can work on a normal web host (Any host that support static files, for example php servers).

## limitations in code
- This package does not support flet async features.
- The API manager here is a customized http host, thats why its slower than original flet.
- You must use the Literal values insted of Literal classes. For example instead of using `alignment=MainAxisAlignment.CENTER`, just use `alignment="center"`.

## best usage practice
soon
- Do NOT make the host run on background on mobile, because mobile can NOT keep the app running on background. Try to run the browser and the host together.