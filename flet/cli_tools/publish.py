from ..tools.append_assets_to_dist import append_assets_to_dist
import shutil
import os
import tarfile
import zipfile


class PublishDistSet:
    """Set the publish dist dir"""
    def __init__ (self, assets_dir_path:str, main_python_file:str):
        self.main_python_file = main_python_file
        # step1: Clean up then Generate the `web` dir on user's current path.
        self.setup_web_folder()

        # step2: Add assets dir to app
        if assets_dir_path != None:
            self.append_the_assets_to_app(assets_path=assets_dir_path)
        
        # step3: Get all files around
        self.get_all_files_around()

        # step4: set the main file of the app
        self.set_the_main_python_file()

        # step5: Setup the tar.gz file
        self.compress_the_web_app()

    def setup_web_folder (self):
        web_folder_path = str(__file__)
        web_folder_path = web_folder_path.replace(os.path.join("cli_tools", "publish.py"), os.path.join("web", "dist.zip"))

        # check if web file not exist.
        if not os.path.isfile(web_folder_path):
            raise FileNotFoundError("Cannot find 'web/dist.zip' dir on the package.")
        
        # copy the web dir to user's current path.
        if os.path.isdir("dist"): shutil.rmtree("dist")
        if os.path.isdir("_dist"): shutil.rmtree("_dist")
        
        # unZipp the file on local `web` dir.
        with zipfile.ZipFile(web_folder_path, "r") as zip_ref:
            zip_ref.extractall("_dist/")
        
        # get the `dist` from the unzipped and rename it
        shutil.copytree("_dist/dist/", "dist/")

        # remove the `_web` folder
        shutil.rmtree("_dist")

    
    def get_all_files_around (self):
        for f in os.listdir("."):
            if os.path.isfile (os.path.join(".", f)):
                shutil.copy(os.path.join(".", f), os.path.join("dist/app/", f))
            elif os.path.isdir (os.path.join(".", f)):
                if str(f) in ["dist", "flet", "venv"]:pass
                else:
                    shutil.copytree(os.path.join(".", f), os.path.join("dist/app/", f))
                
    

    def set_the_main_python_file (self):
        index_file = open(os.path.join("dist", "index.html"), encoding="utf-8").read()

        index_file = index_file.replace("<user_python_script_file>", str(self.main_python_file).replace(".py", ""))

        open(os.path.join("dist", "index.html"), "w+", encoding="utf-8").write(index_file)


    def append_the_assets_to_app (self, assets_path:str):
        append_assets_to_dist(assets_path, dist_name="dist")

    
    def compress_the_web_app (self):
        web_app_folder = "dist/app/"

        # remove the existence `app.tar.gz`
        if os.path.isfile("dist/app.tar.gz"):
            os.remove("dist/app.tar.gz")
        
        # tar.gz a folder
        the_folder_to_tar = web_app_folder
        with tarfile.open("dist/app.tar.gz", "w:gz") as tar:
            for fn in os.listdir(the_folder_to_tar):
                p = os.path.join(the_folder_to_tar, fn)
                tar.add(p, arcname=fn)
        

        # remove the app file
        shutil.rmtree(web_app_folder)