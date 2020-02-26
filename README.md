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
```import junix; junix.export_images(filepath, output_dir)```

*filepath*: Notebook filepath<br/>
*output_dir*: Directory where to output notebook images<br/>

### Example

Let's consider the following notebook ```example.ipynb```:

<img width="865" alt="Screenshot 2019-09-15 at 2 06 49 PM" src="https://user-images.githubusercontent.com/9989010/64917363-2cfe4780-d7c2-11e9-8174-ed2924d17e31.png">

By running the following commands:
- ```junix example.ipynb``` (with command line) <br/>
- ```import junix; junix.export_images(filepath="example.ipynb")``` (within python terminal) <br/>

2 image files will be generated in the same folder as the notebook file (see screenshot below): <br/>

<img width="333" alt="Screenshot 2019-09-15 at 1 52 45 PM" src="https://user-images.githubusercontent.com/9989010/64917371-5fa84000-d7c2-11e9-9f65-e9a53fc7d781.png"> 

## Resources

## Authors
Damien Marlier

## License
This project is licensed under the MIT License
