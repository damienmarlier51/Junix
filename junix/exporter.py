import base64
import json
import os


def export_images(filepath,
                  output_dir=None):

    notebook_image_exporter = NotebookImageExporter(filepath,
                                                    output_dir)

    notebook_image_exporter.save_images()


def has_image_key(data_output):

    return len([key for key in list(data_output.keys()) if "/" in key and key.split("/")[0] == "image"]) == 1


def get_image_key(data_output):

    return [key for key in list(data_output.keys()) if "/" in key and key.split("/")[0] == "image"][0]


def convert_file_to_json(filepath):

    with open(filepath, "r") as f:
        contents = f.read()
        f.close()

    return json.loads(contents)


class NotebookImageExporter():

    def __init__(self,
                 notebook_filepath=None,
                 output_directory=None):

        self.notebook_filepath = notebook_filepath
        self.output_directory = output_directory

        self.notebook_filename = notebook_filepath.split(os.sep)[-1]
        self.notebook_directory = os.sep.join(notebook_filepath.split(os.sep)[:-1]) if os.sep in notebook_filepath else "."
        self.notebook_dict = convert_file_to_json(notebook_filepath)

    def get_image_cell_paths(self):

        image_paths = {}

        for cell_idx, cell in enumerate(self.notebook_dict["cells"]):
            if "outputs" not in cell:
                continue
            indexed_data_outputs = [(output_idx, cell_output["data"]) for output_idx, cell_output in enumerate(cell["outputs"]) if "data" in cell_output]
            cell_image_keys = [(indexed_data_output[0], get_image_key(indexed_data_output[1])) for indexed_data_output in indexed_data_outputs if has_image_key(indexed_data_output[1])]
            if len(cell_image_keys) > 0:
                image_paths[cell_idx] = cell_image_keys

        return image_paths

    def get_image_from_cell_paths(self, image_paths):

        images = []

        for k, v in image_paths.items():
            for indexed_image_key in v:
                image_dict = {}
                image_dict["cell_idx"] = k
                image_dict["output_idx"] = indexed_image_key[0]
                image_dict["content"] = self.notebook_dict["cells"][k]["outputs"][indexed_image_key[0]]["data"][indexed_image_key[1]]
                image_dict["format"] = indexed_image_key[1].split("/")[-1]
                images.append(image_dict)

        return images

    def get_images(self):

        image_paths = self.get_image_cell_paths()
        images = self.get_image_from_cell_paths(image_paths)

        return images

    def save_images(self):

        if self.output_directory is None:
            output_directory = "."
        else:
            output_directory = self.output_directory

        if os.path.exists(output_directory) is False:
            os.mkdir(output_directory)

        images = self.get_images()

        for image in images:
            img_data = base64.b64decode(image["content"])
            filename = "{}_cell_{}_output_{}.{}".format(self.notebook_filename.replace(".ipynb", ""),
                                                        image["cell_idx"],
                                                        image["output_idx"],
                                                        image["format"])
            filepath = output_directory + os.sep + filename
            with open(filepath, 'wb') as f:
                f.write(img_data)
