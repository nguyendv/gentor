"""Test heplers function for sitegenerator.main ."""

from sitegenerator.main import calculate_out_path


def test_calculate_out_path():
    """Test calculate_out_path function."""
    assert calculate_out_path('content/md/index.md') == 'output/md/index.html'
