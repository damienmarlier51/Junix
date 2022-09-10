# Junix (JUpyter Notebook Image eXporter)

Junix is a simple python package to export images from a Jupyter Notebook.

## Installation

### Using pip

```pip install junix```

### Using source code

```
git clone https://github.com/damienmarlier51/JupyterNotebookImageExporter.git
cd JupyterNotebookImageExporter; python setup.py install
```

## Getting started

### From command line

```junix -f /path/to/notebook -o path/to/output/directory``` or ```junix --filepath /path/to/notebook --output_dir path/to/output/directory```

*filepath*: Notebook filepath<br/>
*-o* is an optional argument. If -o is not specified, output directory is current directory (pwd).<br/>

### From Python

```import junix; junix.export_images(filepath=filepath, output_dir=output_dir)```

### Example

One example can be found ```example/example.ipynb```.

With that example, you can test the python API by running the following command from root directory:
```python -m example.export_example```

It will export images into folder ```example/example_images_1```.
The command has already been pre-run in this repository to show what the output exports look like.

You can test as well the CLI by running the following command from root directory:
```junix -f example/example.ipynb -o example/example_images_2```

It will export images into folder ```example/example_images_2```.
The example has already been pre-run in this repository to show what the output exports look like.

## Test

Run ```pytest``` from root directory.
