Gentor: another Python static site generator, currently used for my personal website[https://dvnguyen.com](https://dvnguyen.com)



# Usage
## Directory Structure
`content`: Contains content written in Markdown. You write your site's content here.

`public`: Contains generated html files. Static assets are also copied here after `build` command.

`template`: Contains Jinja2 template files. You can modify the templates here.

`static`: Contains static assets, including js, css, and images.

## Write content
To write your site's content, add and edit the markdown files in the `content` directory.

### `content` directory structure
The structure of `content` directory assembles your site's structure. For instance, if following is your site's structure:

```
example.com
example.com/about.html
example.com/contact.html
example.com/posts/post1.html
example.com/posts/post2.html
```

,then the `content` directory will be:

```
content/index.md
content/about.md
content/contact.md
content/posts/index.md
content/posts/post1.md
content/posts/post2.md
```

### Frontmatter in Markdown files
The frontmatter section of each Markdown file allows you to specify the template file. Template files can be found and editted in the `template` directory. All the keys are required at this moment (better default settings will be added in the future). The frontmatter uses YAML syntax.

```
---
draft: True
title: Page title
template: base.html
---

```

# Technical Decisions
This section lists our technical decisions for the site generator.

## Dependencies
- `jinja2` for html template
- `markdown` for rendering Markdown content.
- `python-frontmatter` for parsing YAML frontmatter from a Markdown file
- `click` for handling cli arguments