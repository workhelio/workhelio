# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Workhelio'
copyright = '2025, Workhelio'
author = 'Workhelio'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

# -- Options for static files
html_static_path = ['_static']

# -- Additional options to consider
# Ensuring that the image paths are treated correctly
html_extra_path = ['_extra']

# Optional: Ensuring that Read the Docs uses the correct master doc
master_doc = 'index'
