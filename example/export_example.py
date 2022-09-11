import json

import junix

if __name__ == "__main__":

    with open("example/example.ipynb", "r") as f:
        notebook_dict = json.load(f)

    with open("example/example.json", "w") as f:
        json.dump(notebook_dict, f)

    junix.export_images(
        filepath="example/example.ipynb",
        output_dir="example/example_images_1",
        prefix="nb",
    )
