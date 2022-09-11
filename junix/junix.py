import base64
import json
import os
from typing import Dict, List, Optional


def has_image_key(data_output: Dict) -> bool:

    return (
        len(
            [
                key
                for key in list(data_output.keys())
                if "/" in key and key.split("/")[0] == "image"
            ]
        )
        == 1
    )


def convert_file_to_json(filepath: str) -> Dict:

    with open(filepath, "r") as f:
        contents = f.read()
        f.close()

    return json.loads(contents)


def get_images(notebook_dict: Dict) -> List[Dict]:

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


def export_images(
    filepath: str, output_dir: Optional[str] = None, prefix: Optional[str] = None
):

    with open(filepath, "r") as fr:
        notebook_dict = json.load(fr)

    if prefix is None:
        prefix = os.path.basename(filepath).split(".")[0]

    if output_dir is None:
        output_dir = "."

    if os.path.exists(output_dir) is False:
        os.mkdir(output_dir)

    images = get_images(notebook_dict=notebook_dict)

    for image_dict in images:

        file_ext = image_dict["content_type"].split("/", 1)[1].split("+", 1)[0]

        filename = "{}_cell_{}_output_{}.{}".format(
            prefix, image_dict["cell_idx"], image_dict["output_idx"], file_ext
        )

        filepath = output_dir + os.sep + filename

        with open(filepath, "wb") as fw:
            fw.write(image_dict["img_data"])
