


def get_platform_name () -> str:
	root_path = str(__file__)
	
	if "var/mobile" in root_path and "Pythonista3/Documents" in root_path:
		return "pythonista"
	
	return "else"