***************************
Custom hooks for pre-commit
***************************

Typically one need to install |pre-commit|_ first:

Via pip:

.. code-block:: bash

    pip install pre-commit

Via `homebrew <https://brew.sh>`_:

.. code-block:: bash

    brew install pre-commit

Via `conda <https://conda.io>`_:

.. code-block:: bash

    conda install -c conda-forge pre-commit

Once installed, you can check the version with:

.. code-block:: bash

    pre-commit --version

Next step is to create a configuration file **.pre-commit-config.yaml**
in the root of the repository. It's content typically looks like this:

.. code-block:: yaml

    - repo: https://github.com/adrybakov/pre-commit-hooks
      rev: 0.2.1                       # Check available tags on the GitHub page
      hooks:
        - id: <first-hook-id>          # Required
          ....                         # Optional arguments for the first hook
        - id: <second-hook-id>         # Required
          ....                         # Optional arguments for the second hook

For the content of the file see page for each individual hook:

.. toctree::
    :caption: Hooks
    :maxdepth: 1

    license-headers

Then install the git hook scripts:

.. code-block:: bash

    pre-commit install

See `documentation <https://pre-commit.com/>`_ for more details.


Standalone usage
================

Every hook is written in python and can be used as a standalone script.

One would need to clone the repository:

.. code-block:: bash

    git clone https://github.com/adrybakov/pre-commit-hooks.git

And install the package:

.. code-block:: bash

    cd pre-commit-hooks
    pip install .

Then the hook can be used as a standalone script:

.. code-block:: bash

    <hook-name> <arguments> ...

You can display the help message for each script with the command:

.. code-block:: bash

    <hook-name> --help
