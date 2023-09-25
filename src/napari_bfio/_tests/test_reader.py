from napari_bfio import napari_get_reader


# tmp_path is a pytest fixture
def test_reader(tmp_path):
    """An example of how you might test your plugin."""

    # write some fake data using your supported file format
    dummy_var = 1
    assert dummy_var == 1
    pass


def test_get_reader_pass():
    reader = napari_get_reader("fake.file")
    assert reader is None
