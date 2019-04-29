"""cli.py: command line interface for working with content."""

import os
from shutil import copyfile
import re
from pathlib import Path
import click
import frontmatter
import markdown
from jinja2 import FileSystemLoader, Environment


fs_loader = FileSystemLoader('template/')


# IMPORTANT: Since no autoescape is enabled
# It's my responsibity to manual autoescape
# See more at: http://jinja.pocoo.org/docs/2.10/templates/#working-with-manual-escaping
template_env = Environment(loader=fs_loader)


CONTENT_DIR = 'content/'
PUBLIC_DIR = 'public/'


def gen_html(md_file):
    """Build build a markdown content file to html, and write down."""
    fm = frontmatter.load(md_file)
    template = template_env.get_template(fm['template'])
    content = markdown.markdown(fm.content)
    context = {
        'title': fm['title'],
        'content': content
    }

    rendered = template.render(context)
    f_out = calculate_out_path(md_file)
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

    md_files = [str(path) for path in p.glob('**/*.md')]
    for md in md_files:
        gen_html(md)

    pdf_files = [str(path) for path in p.glob('**/*.pdf')]
    for pdf in pdf_files:
        gen_pdf(pdf)
