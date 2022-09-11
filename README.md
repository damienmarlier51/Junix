![build](https://app.travis-ci.com/damienmarlier51/JupyterNotebookImageExporter.svg?branch=master)
![pytest](https://github.com/damienmarlier51/JupyterNotebookImageExporter/actions/workflows/test.yaml/badge.svg)

# Junix (JUpyter Notebook Image eXporter)

Junix is a simple python package to export images from a Jupyter Notebook.

Given a notebook like the one below, Junix will export its images into separate files.

**Input**<br/>
<img width="865" alt="Screenshot 2019-09-15 at 2 06 49 PM" src="https://user-images.githubusercontent.com/9989010/64917363-2cfe4780-d7c2-11e9-8174-ed2924d17e31.png">

**Output**<br/>
<img width="333" alt="Screenshot 2019-09-15 at 1 52 45 PM" src="https://user-images.githubusercontent.com/9989010/64917371-5fa84000-d7c2-11e9-9f65-e9a53fc7d781.png">


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

```junix --filepath /path/to/notebook --output_dir path/to/output/directory```
```junix -f /path/to/notebook -o path/to/output/directory```

**--filepath**: Notebook filepath<br/>
**--output_dir** (Optional). Default value is current directory (pwd).<br/>
**--prefix** (Optional). Default value is notebook filename.<br/>

### From Python

```import junix; junix.export_images(filepath=filepath, output_dir=output_dir, prefix=prefix)```

### Example

Example can be found ```example/example.ipynb```.

You can test the python API by running the following command from root directory:<br/>
```python -m example.export_example```

It will export images into folder ```example/example_images_1```.<br/>

You can test as well the CLI by running the following command from root directory:<br/>
```junix -f example/example.ipynb -o example/example_images_2 -p nb```

It will export images into folder ```example/example_images_2```.

## Test

Run ```pytest``` from root directory

## Reference

Medium blog post: https://medium.com/analytics-vidhya/export-images-from-jupyter-notebook-with-a-single-command-422db2b66e92
