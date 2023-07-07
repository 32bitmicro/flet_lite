import os, shutil, json



def append_assets_to_dist (assets_dir:str, dist_name:str):
    if not os.path.isdir(assets_dir):
        print(f"Pass exception: Could not find the assets dir on '{assets_dir}'.")
        return
    
    app_path = os.path.join(dist_name, "app")
    shutil.copytree(f"{assets_dir}", os.path.join(app_path, assets_dir))

    for f in os.listdir(assets_dir):
        path = os.path.join(assets_dir, f)
        to_root_assets = os.path.join(dist_name, "assets")
        if os.path.isfile(path):
            basnam = os.path.basename(path)
            if not os.path.isfile(os.path.join(dist_name, basnam)):
                shutil.copy(path, os.path.join(dist_name, basnam))
            
            if not os.path.isfile (os.path.join(to_root_assets, basnam)):
                shutil.copy(path, os.path.join(to_root_assets, basnam))
            
        elif os.path.isdir (path):
            basnam = os.path.basename(path)
            if not os.path.isdir (os.path.join(dist_name, basnam)):
                shutil.copytree(path, os.path.join(dist_name, basnam))
            
            if not os.path.isdir (os.path.join(to_root_assets, basnam)):
                shutil.copytree(path, os.path.join(to_root_assets, basnam))

    app_data_content = {
        "assets_dir" : assets_dir
    }

    open(os.path.join(app_path, "app_data.json"), "w+", encoding="utf-8").write(json.dumps(app_data_content))