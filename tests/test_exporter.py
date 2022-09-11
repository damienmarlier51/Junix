from pathlib import Path

from junix.junix import export_images, get_images

TEST_DIR = Path(__file__).resolve().parents[0]


def test_export_images(mocker):

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


def test_get_images():

    images = get_images(
        filepath=f"{TEST_DIR}/test.ipynb",
    )

    assert len(images) == 7

    for i in range(len(images)):
        assert images[i].pop("img_data") is not None

    assert images[0] == {
        "cell_idx": 1,
        "output_idx": 0,
        "content_type": "image/png",
    }

    assert images[1] == {
        "cell_idx": 1,
        "output_idx": 1,
        "content_type": "image/png",
    }

    assert images[2] == {
        "cell_idx": 2,
        "output_idx": 0,
        "content_type": "image/png",
    }

    assert images[3] == {
        "cell_idx": 2,
        "output_idx": 1,
        "content_type": "image/png",
    }

    assert images[4] == {
        "cell_idx": 3,
        "output_idx": 0,
        "content_type": "image/jpeg",
    }

    assert images[5] == {
        "cell_idx": 4,
        "output_idx": 0,
        "content_type": "image/png",
    }

    assert images[6] == {
        "cell_idx": 5,
        "output_idx": 0,
        "content_type": "image/svg+xml",
    }
