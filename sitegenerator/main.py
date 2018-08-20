"""cli.py: command line interface for working with content."""

import re
import click
from jinja2 import FileSystemLoader, Environment, select_autoescape


fs_loader = FileSystemLoader('template/')
template_env = Environment(loader=fs_loader, autoescape=select_autoescape)


def write_html(md_file, template_file, context):
    """Build build a markdown content file to html, and write down."""
    template = template_env.get_template(template_file)
    rendered = template.render(context)


def calculate_out_path(md_file: str) -> str:
    """Calculate output path in `output` directory for a Markdown file from `content`."""
    CONTENT_DIR = 'content/'
    OUTPUT_DIR = 'output/'
    out = re.sub('^' + CONTENT_DIR, OUTPUT_DIR, md_file)
    out = re.sub('.md$', '.html', out)
    return out


@click.command()
def build():
    """`build` command`."""
    template = template_env.get_template('base.html')
    rendered = template.render(title='Hello', content='Hello World')
    with open('output/index.html', mode='w') as f:
        f.write(rendered)
