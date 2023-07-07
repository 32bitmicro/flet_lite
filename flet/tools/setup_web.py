from ..tools.append_assets_to_dist import append_assets_to_dist
import shutil
import os
import tarfile
import zipfile


class WebDirSet:
    def __init__ (self, localhost_api_url:str, assets_dir_path:str):
        
        # step1: Clean up then Generate the `web` dir on user's current path.
        self.setup_web_folder()

        self.create_localhost_url_file(url=localhost_api_url)

        # step2: Add assets dir to app
        if assets_dir_path != None:
            self.append_the_assets_to_app(assets_path=assets_dir_path)

        # step2: Setup the tar.gz file
        self.compress_the_web_app()

    def setup_web_folder (self):
        web_folder_path = str(__file__)
        web_folder_path = web_folder_path.replace("tools/setup_web.py", "web/development.zip")

        # check if web file not exist.
        if not os.path.isfile(web_folder_path):
            raise FileNotFoundError("Cannot find 'web/development.zip' dir on the package.")
        
        # copy the web dir to user's current path.
        if os.path.isdir("web"): shutil.rmtree("web")
        if os.path.isdir("_web"): shutil.rmtree("_web")
        
        # unZipp the file on local `web` dir.
        with zipfile.ZipFile(web_folder_path, "r") as zip_ref:
            zip_ref.extractall("_web/")
        
        # get the `dist` from the unzipped and rename it
        shutil.copytree("_web/dist/", "web/")

        # remove the `_web` folder
        shutil.rmtree("_web")
    


    def append_the_assets_to_app (self, assets_path:str):
        append_assets_to_dist(assets_path, dist_name="web")

    
    def compress_the_web_app (self):
        web_app_folder = "web/app/"

        # remove the existence `app.tar.gz`
        if os.path.isfile("web/app.tar.gz"):
            os.remove("web/app.tar.gz")
        
        # tar.gz a folder
        the_folder_to_tar = web_app_folder
        with tarfile.open("web/app.tar.gz", "w:gz") as tar:
            for fn in os.listdir(the_folder_to_tar):
                p = os.path.join(the_folder_to_tar, fn)
                tar.add(p, arcname=fn)
        

        # remove the app file
        shutil.rmtree(web_app_folder)
    

    def create_localhost_url_file (self, url):
        """Create the file on the `web` dir so pyodide can communicate with current python using it."""
        open("web/app/localhost_api_url.txt", "w+", encoding="utf-8").write(url)