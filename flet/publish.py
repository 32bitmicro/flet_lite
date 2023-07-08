from .cli_tools.publish import PublishDistSet
import sys, os



if len(sys.argv) == 1:
    sys.exit("Exit: You need to specify a file path.")

# get the file name
print("Check file exist..")
file_path = ""
for fp in sys.argv[1:]:
    if file_path == "":
        file_path = file_path + fp
    else:
        file_path = file_path + " " + fp

if not os.path.isfile (file_path):
    raise FileNotFoundError(f"No python file at {file_path}")


# start generating
assets_dir = input("What is your assets name (insert `!none` if there is not): ")
print("Start generating the dist..")

if assets_dir.replace(" ", "") == "!none":
    PublishDistSet(assets_dir_path=None, main_python_file=file_path)
else:
    if os.path.isdir(assets_dir):
        PublishDistSet(assets_dir_path=assets_dir, main_python_file=file_path)
    else:
        PublishDistSet(assets_dir_path=None, main_python_file=file_path)

print("""
Done creating your dist. To check it you can use this command:
$ python3 -m http.server --directory dist
Then open the localhost URL in the browser.
""")