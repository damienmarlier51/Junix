from junix.junix import get_images


def test_get_images(notebook_as_json):

    images = get_images(notebook_dict=notebook_as_json)

    assert len(images) == 10
    assert sorted([key for x in images for key in x.keys()]) == sorted(
        ["cell_idx"] * 10 + ["output_idx"] * 10 + ["content"] * 10 + ["format"] * 10
    )
