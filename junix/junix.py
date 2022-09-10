import base64
import json
import os
from typing import Dict, Generator, List, Optional


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


def get_image_from_cell_paths(notebook_dict: Dict, image_paths: Dict) -> List[Dict]:

    images = []

    for k, v in image_paths.items():

        for indexed_image_key in v:

            images.append(
                {
                    "cell_idx": k,
                    "output_idx": indexed_image_key[0],
                    "content": notebook_dict["cells"][k]["outputs"][
                        indexed_image_key[0]
                    ]["data"][indexed_image_key[1]],
                    "format": indexed_image_key[1].split("/")[1],
                }
            )

    return images


def get_images(notebook_dict: Dict) -> Generator:

    return (
        (cell_idx, output_idx, content_type, decode_image_data(content))
        for cell_idx, cell in enumerate(notebook_dict.get("cells", ()))
        for output_idx, output in enumerate(cell.get("outputs", ()))
        for content_type, content in output.get("data", {}).items()
        if content_type.startswith("image/")
    )


def decode_image_data(content):
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

    for cell_idx, output_idx, content_type, image_data in images:

        file_ext = content_type.split("/", 1)[1].split("+", 1)[0]

        filename = "{}_cell_{}_output_{}.{}".format(
            prefix, cell_idx, output_idx, file_ext
        )

        filepath = output_dir + os.sep + filename

        with open(filepath, "wb") as fw:
            fw.write(image_data)
