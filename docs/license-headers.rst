***************
license-headers
***************

.. versionadded:: 0.1.0


Description
===========

Add summary of the license to the top of every \*.py file of the project.
By default it takes the content of the "LICENSE" file from the root directory and
adds it to the top of every \*.py file of the project, prepending it with a comment
symbol "#".

Configuration
=============

.. code-block:: yaml

    - repo: https://github.com/adrybakov/pre-commit-hooks
      rev: 0.1.0                # Check available tags on the GitHub page
      hooks:
        - id: license-headers   # Required
          args:                 # Optional (as the next lines)
            - --license-file    # If license summary is not in a "LICENSE" file
            - LICENSE.txt       # Path to the license summary file
            - --update-year     # If you want to automatically update the year

See `pre-commit docs <https://pre-commit.com/index.html#pre-commit-configyaml---hooks>`_
for the list of additional parameters.

Details
=======

.. currentmodule:: pre_commit_hooks.license_headers

Text of the license is added via the call to the function:

.. autofunction:: apply_license

If ``--update-year`` is set to ``True`` then the year is update via the call
to the function on the text of the license:

.. autofunction:: update_year

The above example will be equivalent to the following code:

.. code-block:: bash

    python3 license-headers some-filename-1.py some-filename-2.py --license-file LICENSE.txt --update-year
