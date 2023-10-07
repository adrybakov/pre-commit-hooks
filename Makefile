.DEFAULT_GOAL := help

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     =
BUILDDIR      = _build

help:
	@echo "\x1b[31m"
	@echo "Please specify what do you want to do!"
	@echo "\x1b[0m"
	@echo "Available options are:\n"
	@echo "    help - show this message"
	@echo "    html - build the html docs"
	@echo "    clean - clean all files from docs and pip routines"
	@echo "    install - install the package"
	@echo

# $(O) is meant as a shortcut for $(SPHINXOPTS).
html: install
	@$(SPHINXBUILD) -M html "docs/$(SOURCEDIR)" "docs/$(BUILDDIR)" $(SPHINXOPTS) $(O)

clean-html: clean install html
	@echo "Done"

install:
	@python3 -m pip install .

clean:
	-@rm -r docs/_build
