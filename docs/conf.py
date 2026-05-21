# Configuration file for the Sphinx documentation builder.

project = 'PyPSA-GH'
copyright = '2026, Engr Kwaku Duah'
author = 'Engr Kwaku Duah'
release = '0.1.0'

extensions = [
    "nbsphinx",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = "pydata_sphinx_theme"
html_static_path = ['_static']
html_title = "PyPSA-GH"

html_theme_options = {
    "navbar_start": ["navbar-logo"],
    "navigation_with_keys": True,
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/kwaku-duah/pypsa-gh",
            "icon": "fa-brands fa-github",
        }
    ],
}

nbsphinx_execute = "never"