from junix.exporter import export_images, export_pdf
import argparse


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('filepath', type=str, help='Notebook filepath')
    parser.add_argument('-o', '--output_dir', type=str, default=None, help='Directory where to export the images')
    parser.add_argument('-p', '--output_pdf', type=str, default=None, help='Filename to export a PDF; takes precedence over -o')

    args = parser.parse_args()
    notebook_filepath = args.filepath
    output_directory = args.output_dir
    output_pdf = args.output_pdf

    if output_pdf is not None:
        export_pdf(notebook_filepath, output_pdf)
    else:
        export_images(notebook_filepath, output_directory)
