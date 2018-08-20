"""cli.py: command line interface for working with content."""

import os
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
    fout = calculate_out_path(md_file)
    dirname = os.path.dirname(fout)
    if not os.path.exists(dirname):
        os.makedirs(dirname, exist_ok=True)
    with open(fout, 'w') as f:
        f.write(rendered)


def list_md_files(directory):
    """Recursively list all .md files of a directory."""
    p = Path(directory)
    return [str(path) for path in p.glob('**/*.md')]


def calculate_out_path(md_file: str) -> str:
    """Calculate output public path in `public` directory for a Markdown file from `content`."""
    out = re.sub('^' + CONTENT_DIR, PUBLIC_DIR, md_file)
    out = re.sub('.md$', '.html', out)
    return out


@click.group()
def cli():
    """Group cli to support multiple commands."""
    pass


@cli.command()
def build():
    """`build` command`."""
    md_files = list_md_files(CONTENT_DIR)
    for md in md_files:
        gen_html(md)
