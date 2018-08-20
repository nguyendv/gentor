"""Test `python-frontmatter`.

a dependency that parses frontmatter content of a Markdown file.
"""

import frontmatter


def test_frontmatter():
    """Test the lib by loading a markdown file with frontmatter."""
    fm = frontmatter.load('sample-md/helloworld.md')

    assert fm['draft'] is True
    assert fm['title'] == 'Hello World'
    assert fm['template'] == 'base.html'
