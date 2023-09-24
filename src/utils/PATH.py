# Crates
from os import path

project_path = path.dirname(path.dirname(path.dirname(path.abspath(__file__))))  # This output the project path
src_utils_path = path.join(project_path, "src", "utils")  # This output the src/utils path
src_ui_path = path.join(project_path, "src", "ui")  # This output the src/ui path
src_utils_paths = path.join(project_path, "src", "utils", "PATH.py")  # This output the src/utils/PATH.py path
