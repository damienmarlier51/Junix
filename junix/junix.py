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


def get_image_key(data_output: Dict) -> str:

    return [
        key
        for key in list(data_output.keys())
        if "/" in key and key.split("/")[0] == "image"
    ][0]


def convert_file_to_json(filepath: str) -> Dict:

    with open(filepath, "r") as f:
        contents = f.read()
        f.close()

    return json.loads(contents)


def get_image_cell_paths(notebook_dict: Dict) -> Dict:

    image_paths = {}

    for cell_idx, cell in enumerate(notebook_dict["cells"]):

        if "outputs" not in cell:
            continue

        indexed_data_outputs = [
            (output_idx, cell_output["data"])
            for output_idx, cell_output in enumerate(cell["outputs"])
            if "data" in cell_output
        ]

        cell_image_keys = [
            (indexed_data_output[0], get_image_key(indexed_data_output[1]))
            for indexed_data_output in indexed_data_outputs
            if has_image_key(indexed_data_output[1])
        ]

        if len(cell_image_keys) > 0:
            image_paths[cell_idx] = cell_image_keys

    return image_paths


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


def get_images(notebook_dict: Dict) -> List[Dict]:

    image_paths = get_image_cell_paths(notebook_dict=notebook_dict)
    images = get_image_from_cell_paths(
        notebook_dict=notebook_dict, image_paths=image_paths
    )

    return images


def export_images(filepath: str, output_dir: Optional[str] = None):

    notebook_filename = filepath.split(os.sep)[-1]
    notebook_dict = convert_file_to_json(filepath=filepath)

    if output_dir is None:
        output_dir = "."

    if os.path.exists(output_dir) is False:
        os.mkdir(output_dir)

    images = get_images(notebook_dict=notebook_dict)

    for image in images:

        img_data = base64.b64decode(image["content"])

        filename = "{}_cell_{}_output_{}.{}".format(
            notebook_filename.replace(".ipynb", ""),
            image["cell_idx"],
            image["output_idx"],
            image["format"],
        )

        filepath = output_dir + os.sep + filename
        with open(filepath, "wb") as f:
            f.write(img_data)
