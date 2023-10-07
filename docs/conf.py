# MIT License
#
# Copyright (c) 2023 Andrey Rybakov (rybakov.ad@icloud.com)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import sys
from datetime import datetime
from os.path import abspath

from pre_commit_hooks import __version__ as version

sys.path.insert(0, abspath("."))


# Project information
project = "Custom hooks for pre-commit"
author = "Andrey Rybakov"
copyright = f"2023-{datetime.now().year}, {author}"


# Extentions
extensions = [
    "sphinx.ext.duration",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.viewcode",
    "sphinx.ext.extlinks",
    "numpydoc",
    "sphinx_copybutton",
    "sphinx.ext.intersphinx",
]

autosummary_generate = True
autodoc_member_order = "alphabetical"

smartquotes = False

# Extlinks
extlinks = {
    "issue": ("https://github.com/adrybakov/pre-commit-hooks/issues/%s", "issue #%s"),
}


# Solve the problem with warnings
numpydoc_class_members_toctree = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]


# Options for HTML output

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.

html_theme = "furo"
html_static_path = ["_static"]
html_css_files = ["custom.css"]

html_title = f"{project} {version}"

html_theme_options = {}

# fix problem with autosummary and numpydoc:
numpydoc_show_class_members = False


# Custom variables with access from .rst files and docstrings

variables_to_export = [
    "project",
    "copyright",
    "version",
]

frozen_locals = dict(locals())
rst_epilog = "\n".join(
    map(lambda x: f".. |{x}| replace:: {frozen_locals[x]}", variables_to_export)
)
del frozen_locals
