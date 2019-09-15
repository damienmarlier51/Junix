from junix.exporter import export_images
import argparse


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('filepath', type=str, help='Notebook filepath')
    parser.add_argument('-o', '--output_dir', type=str, default=None, help='Directory where to export the images')

    args = parser.parse_args()
    notebook_filepath = args.filepath
    output_directory = args.output_dir

    export_images(notebook_filepath, output_directory)
