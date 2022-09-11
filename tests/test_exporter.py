from pathlib import Path

from junix.junix import export_images

TEST_DIR = Path(__file__).resolve().parents[0]


def test_get_images(mocker):

    mocker.patch("junix.junix.write_contents")

    output_dir = f"{TEST_DIR}/test_images"

    contents = export_images(
        filepath=f"{TEST_DIR}/test.ipynb",
        output_dir=output_dir,
        prefix="nb",
    )

    assert sorted(contents.keys()) == [
        f"{output_dir}/nb_cell_1_output_0.png",
        f"{output_dir}/nb_cell_1_output_1.png",
        f"{output_dir}/nb_cell_2_output_0.png",
        f"{output_dir}/nb_cell_2_output_1.png",
        f"{output_dir}/nb_cell_3_output_0.jpeg",
        f"{output_dir}/nb_cell_4_output_0.png",
        f"{output_dir}/nb_cell_5_output_0.svg",
    ]

    contents = export_images(
        filepath=f"{TEST_DIR}/test.ipynb",
    )

    assert sorted(contents.keys()) == [
        "./test_cell_1_output_0.png",
        "./test_cell_1_output_1.png",
        "./test_cell_2_output_0.png",
        "./test_cell_2_output_1.png",
        "./test_cell_3_output_0.jpeg",
        "./test_cell_4_output_0.png",
        "./test_cell_5_output_0.svg",
    ]
