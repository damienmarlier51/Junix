# Junix (JUpyter Notebook Image eXporter)

Finding troublesome to export images from your notebook?<br/>
Junix is a simple python package to export plots embed in a Jupyter Notebook.

## Installation

### Using pip
```pip install junix```

### Using source code
```
git clone https://github.com/damienmarlier51/JupyterNotebookImageExporter.git
cd JupyterNotebookImageExporter
python setup.py install
```

## Usage

### From command line
```junix filepath -o output_dir```

*filepath*: Notebook filepath<br/>
*-o* is an optional argument. If -o is not specified, output directory is current directory (pwd).<br/>
  
### From Python
```import junix; junix.export_images(filepath, output_directory)```

*filepath*: Notebook filepath<br/>
*output_directory*: Directory where to output notebook images<br/>

### Example

Let's consider 

Running 

## Resources

## Authors
Damien Marlier

## License
This project is licensed under the MIT License
