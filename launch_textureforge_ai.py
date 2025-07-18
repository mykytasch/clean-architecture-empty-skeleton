# launch_textureforge_ai.py
# This script creates a clean architecture skeleton for a Python project.

import os

structure = {
    "texture_forge_ai": {
        "api": ["__init__.py", "mission_routes.py", "profile_routes.py"],
        "core": ["__init__.py", "config.py"],
        "services": ["__init__.py", "ai_service.py", "dispatcher.py", "module_service.py"],
        "database": ["__init__.py", "json_handler.py"],
        "modules": [],
        ".": ["main.py", "models.py", "requirements.txt"]
    }
}

file_templates = {
    "main.py": '# Main launcher for TextureForge AI\nprint("Welcome to TextureForge AI!")\n',
    "models.py": '# Data models using Pydantic\n',
    "requirements.txt": 'fastapi\nuvicorn\npydantic\n',
}

def create_structure(base_path, structure):
    for root, dirs in structure.items():
        root_path = os.path.join(base_path, root)
        os.makedirs(root_path, exist_ok=True)
        for subdir, files in dirs.items():
            dir_path = os.path.join(root_path, subdir) if subdir != "." else root_path
            os.makedirs(dir_path, exist_ok=True)
            for file in files:
                file_path = os.path.join(dir_path, file)
                with open(file_path, "w") as f:
                    content = file_templates.get(file, f"# {file} stub\n")
                    f.write(content)

if __name__ == "__main__":
    create_structure(os.getcwd(), structure)
    print("Project skeleton created.")
