# Junix (JUpyter Notebook Image eXporter)

Finding it troublesome to export images from notebook?<br/>
Junix is a simple python package to export plots within Jupyter Notebook.

Output formats include a directory of images or a PDF file (via [img2pdf](https://pypi.org/project/img2pdf/)).

## Installation

### Using pip
```pip install junix```

### Using source code
```
git clone https://github.com/damienmarlier51/JupyterNotebookImageExporter.git
cd JupyterNotebookImageExporter; python setup.py install
```

## Usage

### From command line
```junix /path/to/notebook -o path/to/output/directory```

*filepath*: Notebook filepath<br/>
*-o* is an optional argument. If -o is not specified, output directory is current directory (pwd).<br/>
  
### From Python
```import junix; junix.export_images(filepath, output_dir)```

*filepath*: Notebook filepath<br/>
*output_dir*: Directory where to output notebook images<br/>

### Exporting PDFs
```junix /path/to/notebook -p path/to/output.pdf```

or from Python,

```import junix; junix.export_pdf(filepath, output_pdf)```

### Example

Let's consider the following notebook ```example.ipynb```:

<img width="865" alt="Screenshot 2019-09-15 at 2 06 49 PM" src="https://user-images.githubusercontent.com/9989010/64917363-2cfe4780-d7c2-11e9-8174-ed2924d17e31.png">

By running the following commands:
- ```junix example.ipynb``` (with command line) <br/>
- ```import junix; junix.export_images(filepath="example.ipynb")``` (within python terminal) <br/>

2 image files will be generated in the same folder as the notebook file (see screenshot below): <br/>

<img width="333" alt="Screenshot 2019-09-15 at 1 52 45 PM" src="https://user-images.githubusercontent.com/9989010/64917371-5fa84000-d7c2-11e9-9f65-e9a53fc7d781.png"> 

## License
This project is licensed under the MIT License
