from typing import Optional

import click

from junix import junix


@click.command()
@click.option("-f", "--filepath", "filepath", required=True)
@click.option("-o", "--output_dir", "output_dir", default=None)
@click.option("-p", "--prefix", "prefix", default=None)
def export_images(
    filepath: str, output_dir: Optional[str] = None, prefix: Optional[str] = None
):

    junix.export_images(filepath=filepath, output_dir=output_dir, prefix=prefix)


if __name__ == "__main__":
    export_images()
