"""Test helpers function for gentor.main ."""

from gentor.main import calculate_out_path


def test_calculate_out_path():
    """Test calculate_out_path() function."""
    assert calculate_out_path('content/md/index.md') == 'public/md/index.html'
    assert calculate_out_path('content/resume.pdf') == 'public/resume.pdf'
