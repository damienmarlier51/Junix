import base64
import json
import os
from typing import Dict, List, Optional


def get_images_from_notebook_dict(notebook_dict: Dict) -> List[Dict]:

    return [
        {
            "cell_idx": cell_idx,
            "output_idx": output_idx,
            "content_type": content_type,
            "img_data": decode_img_data(content),
        }
        for cell_idx, cell in enumerate(notebook_dict.get("cells", ()))
        for output_idx, output in enumerate(cell.get("outputs", ()))
        for content_type, content in output.get("data", {}).items()
        if content_type.startswith("image/")
    ]


def decode_img_data(content):

    if isinstance(content, list):
        return "".join(content).encode("utf-8")
    else:
        return base64.b64decode(content)


def write_contents(contents: Dict):

    for filepath, content in contents.items():

        os.makedirs(os.path.dirname(filepath), exist_ok=True)

        with open(filepath, "wb") as fw:
            fw.write(content)


def get_export_contents(images: List[Dict], prefix: str, output_dir: str) -> Dict:

    contents = {}

    for image_dict in images:

        file_ext = image_dict["content_type"].split("/", 1)[1].split("+", 1)[0]
        filename = "{}_cell_{}_output_{}.{}".format(
            prefix, image_dict["cell_idx"], image_dict["output_idx"], file_ext
        )
        filepath = output_dir + os.sep + filename

        contents.update({filepath: image_dict["img_data"]})

    return contents


def get_images(filepath: str) -> List[Dict]:

    with open(filepath, "r") as fr:
        notebook_dict = json.load(fr)

    images = get_images_from_notebook_dict(notebook_dict=notebook_dict)

    return images


def export_images(
    filepath: str, output_dir: Optional[str] = None, prefix: Optional[str] = None
) -> Dict:

    with open(filepath, "r") as fr:
        notebook_dict = json.load(fr)

    if prefix is None:
        prefix = os.path.basename(filepath).split(".")[0]

    if output_dir is None:
        output_dir = "."

    images = get_images_from_notebook_dict(notebook_dict=notebook_dict)
    export_contents = get_export_contents(
        images=images, prefix=prefix, output_dir=output_dir
    )

    write_contents(contents=export_contents)

    return export_contents
