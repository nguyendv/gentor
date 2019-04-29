"""cli.py: command line interface for working with content."""

import os
from shutil import copyfile
import re
from pathlib import Path
import click
import markdown
from jinja2 import FileSystemLoader, Environment


fs_loader = FileSystemLoader('template/')


# IMPORTANT: Since no autoescape is enabled
# It's my responsibity to manual autoescape
# See more at: http://jinja.pocoo.org/docs/2.10/templates/#working-with-manual-escaping
template_env = Environment(loader=fs_loader)


CONTENT_DIR = 'content/'
PUBLIC_DIR = 'public/'

class Error(Exception):
    """ Base class for exceptions in this module"""
    pass

class InvalidFrontMatter(Error):
    """ Exception raised for invalid frontmatter

    Attributes:
        filename: Input file which contains invalid frontmatter
        message: explanation of the error
    """

    def __init__(self, filename, message):
        self.filename = filename
        self.message = message

def load_frontmatter(markdown_file):
    import frontmatter
    fm = frontmatter.load(markdown_file)
    if 'template' not in fm:
        raise InvalidFrontMatter(markdown_file, message='No template key found in frontmatter')
    elif 'title' not in fm:
        raise InvalidFrontMatter(markdown_file, message='No title found in frontmatter')

    return fm

def gen_html(markdown_file):
    """Build build a markdown content file to html, and write down."""
    frontmatter = load_frontmatter(markdown_file)
    template = template_env.get_template(frontmatter['template'])
    content = markdown.markdown(frontmatter.content)
    context = {
        'title': frontmatter['title'],
        'content': content
    }

    rendered = template.render(context)
    f_out = calculate_out_path(markdown_file)
    dirname = os.path.dirname(f_out)
    if not os.path.exists(dirname):
        os.makedirs(dirname, exist_ok=True)
    with open(f_out, 'w') as f:
        f.write(rendered)


def gen_pdf(pdf_file):
    """Copy a pdf_file to the public directory"""
    f_out = calculate_out_path(pdf_file)
    dirname = os.path.dirname(f_out)
    if not os.path.exists(dirname):
        os.makedirs(dirname, exist_ok=True)
    copyfile(pdf_file, f_out)


def calculate_out_path(content_file: str) -> str:
    """Calculate output public path in `public` directory for a Markdown or PDF file from `content`."""
    out = re.sub('^' + CONTENT_DIR, PUBLIC_DIR, content_file)
    if content_file.endswith('.md'):
        out = re.sub('.md$', '.html', out)
    return out


@click.group()
def cli():
    """Group cli to support multiple commands."""
    pass


@cli.command()
def build():
    """`build` command`."""
    p = Path(CONTENT_DIR)

    markdown_files = [str(path) for path in p.glob('**/*.md')]
    for md in markdown_files:
        gen_html(md)

    pdf_files = [str(path) for path in p.glob('**/*.pdf')]
    for pdf in pdf_files:
        gen_pdf(pdf)
