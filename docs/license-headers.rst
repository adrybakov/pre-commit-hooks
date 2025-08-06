***************
license-headers
***************

.. versionadded:: 0.1.0


Description
===========

Add summary of the license to the top of every **.py** file of the project.
By default it takes the content of the **LICENSE** file from the root directory and
adds it to the top of every **.py** file of the project, prepending it with a comment
symbol **#**.

Configuration
=============

.. code-block:: yaml

    - repo: https://github.com/adrybakov/pre-commit-hooks
      rev: 0.3.0                          # Check available tags on the GitHub page
      hooks:
        - id: license-headers             # Required
          args:                           # Optional (as the next lines)
            - --license-template          # If license summary is not in a "LICENSE" file
            - LICENSE.template            # Path to the license summary file
            - --start-year                # If you use {{start-year}} in the template
            - 2021                        # Value for {{start-year}}
            - --author-name               # If you use {{author-name}} in the template
            - Name Surname Extra Name     # Value for {{author-name}} (any amount of words)
            - --author-email              # If you use {{author-email}} in the template
            - some-email@some-address.com # Value for {{author-e-mail}}

See `pre-commit docs <https://pre-commit.com/index.html#pre-commit-configyaml---hooks>`_
for the list of additional parameters.

License template
================

File with the license template support some dynamic placeholders:

============================= ============================= =============================
Placeholder                   User-provided value           Generated value
============================= ============================= =============================
``{{start-year}}``            Value of ``--start-year``     Unapplicable
``{{current-year}}``          Unapplicable                  ``datetime.now().year``
``{{author-name}}``           Value of ``--author-name``    Unapplicable
``{{author-email}}``          Value of ``--author-email``   Unapplicable
============================= ============================= =============================

An example template is

.. literalinclude:: ../LICENSE.template
   :language: text

Standalone usage
================

The above example will be equivalent to the following code (assuming that you
:ref:`installed it with pip <standalone-usage>`):

.. code-block:: bash

    license-headers some-filename-1.py some-filename-2.py --license-template LICENSE.template --start-year 2021 --author-name Name Surname Extra Name --author-email some-email@some-address.com

Implementation details
======================

.. currentmodule:: pre_commit_hooks.license_headers

Text of the license is added via the call of the function:

.. autofunction:: ensure_license
