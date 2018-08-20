"""Test heplers function for gentor.main ."""

from gentor.main import calculate_out_path
from gentor.main import list_md_files


def test_calculate_out_path():
    """Test calculate_out_path() function."""
    assert calculate_out_path('content/md/index.md') == 'public/md/index.html'


def test_list_md_files():
    """Test the list_md_files() function."""
    md_files = list_md_files('sample-md/')
    assert set(md_files) == set([
        'sample-md/helloworld.md',
        'sample-md/posts/index.md',
        'sample-md/posts/post1.md',
        'sample-md/posts/post2.md'
    ])
