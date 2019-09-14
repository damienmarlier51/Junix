from nimgex.notebook_image_importer import NotebookImageImporter
import click


@click.command()
@click.option('-f', '--filepath', required=True, help='Notebook filepath')
def main(filepath):
    nimgex = NotebookImageImporter(filepath)
    nimgex.save_images()


if __name__ == "__main__":
    main()
