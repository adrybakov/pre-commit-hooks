# MIT License
#
# Copyright (c) 2023-2025 Andrey Rybakov (rybakov.ad@icloud.com)
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


from argparse import ArgumentParser
from datetime import datetime


def ensure_license(
    filenames,
    license_template,
    start_year=None,
    author_name=None,
    author_email=None,
    verbose=False,
):
    r"""
    Insert license text at the top of the file.

    Every line at the beginning of the file,
    which is empty (consists only of spaces and a newline character at the end)
    or starts with a hash symbol ("#") is removed.

    Parameters
    ----------
    filenames : list of str
        List of file to which the license is added.
    license_template : list of str
        Path to the file with the template of the license.
    start_year : str
        Value for the placeholder ``{{start-year}}`` in the license template.
    author_name : list of str
        Value for the placeholder ``{{author-name}}`` in the license template.
        Used as ``author_name = " ".join(author_name)``.
    author-email : str
        Value for the placeholder ``{{author-email}}`` in the license template.
    """

    license_start = f"# {' LICENSE ':=^78}\n"
    license_end = f"# {' END LICENSE ':=^78}\n"

    # Read license text from the template
    with open(license_template, "r") as f:
        license_text = f.read()

    # Update placeholders with the data
    def get_data(placeholder_name):
        if placeholder_name == "start-year":
            if start_year is None:
                raise ValueError(
                    "start-year is not provided, "
                    "please add an argument to the pre-commit config."
                )
            return start_year

        if placeholder_name == "current-year":
            return str(datetime.now().year)

        if placeholder_name == "author-name":
            if author_name is None:
                raise ValueError(
                    "author-name is not provided, "
                    "please add an argument to the pre-commit config."
                )
            return " ".join(author_name)

        if placeholder_name == "author-email":
            if author_email is None:
                raise ValueError(
                    "author-email is not provided, "
                    "please add an argument to the pre-commit config."
                )
            return author_email

        raise ValueError(f'Placeholder "{placeholder_name}" is not supported.')

    license_text = license_text.split("{{")

    tmp_text = []
    if len(license_text) >= 1:
        tmp_text.append(license_text[0])

    for i in range(1, len(license_text)):
        text_portion = license_text[i].split("}}")

        if len(text_portion) == 1:
            raise ValueError(
                "data placeholder must be enclosed in the double figure "
                'parenthesis, for example: "{{data-placeholder}}". Did not find closing '
                f'"}}" for the opening "{{" number {i}.'
            )

        if len(text_portion) != 2:
            raise ValueError(
                f'Expected only one closing "}}", found {len(text_portion) - 1}.'
            )

        tmp_text.append(get_data(text_portion[0]))
        tmp_text.append(text_portion[1])

    license_text = "# " + "\n# ".join("".join(tmp_text).split("\n")) + "\n"

    # Insert license text into the files
    for file in filenames:
        with open(file, "r") as f:
            lines = f.readlines()

        try:
            license_start_index = lines.index(license_start)
        except ValueError:
            license_start_index = None

        try:
            license_end_index = lines.index(license_end)
        except ValueError:
            license_end_index = None

        if license_start_index is None and license_end_index is None:
            lines = [license_start, license_text, license_end] + lines
        elif license_start_index is not None and license_end_index is not None:
            lines = (
                lines[: license_start_index + 1]
                + [license_text]
                + lines[license_end_index:]
            )
        else:
            raise ValueError(
                "License end and start are inconsistent. "
                f"Start index: {license_start_index}, end index: {license_end_index}."
            )

        with open(file, "w", encoding="utf-8") as f:
            f.writelines(lines)

        if verbose:
            print(f"Add license to the file {file}")


def main():
    parser = ArgumentParser()
    parser.add_argument(
        "filenames",
        nargs="*",
        help="Files to which the license text is added.",
    )
    parser.add_argument(
        "-lt",
        "--license-template",
        default="LICENSE",
        help="Path to the template file of the license",
    )
    parser.add_argument(
        "--start-year",
        type=str,
        default=None,
        help="One of the data placeholders for the license template.",
    )
    parser.add_argument(
        "--author-name",
        type=str,
        default=None,
        nargs="*",
        help="One of the data placeholders for the license template.",
    )
    parser.add_argument(
        "--author-email",
        type=str,
        default=None,
        help="One of the data placeholders for the license template.",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        default=False,
        action="store_true",
        help="Whether to indicate which files are updated.",
    )
    args = parser.parse_args()

    ensure_license(**vars(args))


if __name__ == "__main__":
    main()
