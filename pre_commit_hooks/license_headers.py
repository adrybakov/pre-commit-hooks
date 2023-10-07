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

import re
from argparse import ArgumentParser


def update_year(license_text):
    r"""
    Update the year in the license text to the current year.
    It assumes that the year in the license file is written in one of the following formats:

    * 2019
        Updated to 2019-2023.
    * 2019-2020
        Updated to 2019-2023.
    * 2019 - 2020
        Updated to 2019 - 2023.

    Every sequence of four digits, starting from 1 or 2, is considered a year.

    Parameters
    ----------
    license_text : list of str
        The license text as a list of lines.

    Returns
    -------
    license_text : list of str
        The updated license text.
    """

    pattern1 = r"[1,2]\d{3}"
    pattern2 = r"-[1,2]\d{3}"
    pattern3 = r" - [1,2]\d{3}"

    from datetime import datetime

    for i, line in enumerate(license_text):
        if re.search(pattern1 + pattern2, license_text[i]):
            license_text[i] = re.sub(
                pattern2,
                f"-{datetime.now().year}",
                line,
            )
        elif re.search(pattern1 + pattern3, license_text[i]):
            license_text[i] = re.sub(
                pattern3,
                f" - {datetime.now().year}",
                line,
            )
        elif re.search(pattern1, license_text[i]):
            license_year = re.findall(pattern1, license_text[i])[0]
            if int(license_year) < datetime.now().year:
                license_text[i] = re.sub(
                    pattern1,
                    f"{license_year}-{datetime.now().year}",
                    line,
                )
    return license_text


def apply_license(file, license_text):
    r"""
    Insert license text at the top of the file.

    Every line at the beginning of the file, which starts with a hash or
    is empty (consist of only a spaces and a newline character), is removed.

    Parameters
    ----------
    file : str
        The file to apply the license to.
    license_text : list of str
        The license text as a list of lines.
    """

    with open(file, "r") as f:
        lines = f.readlines()
    i = 0
    if len(lines) > 0:
        while i < len(lines) and (
            re.fullmatch(r" *\n", lines[i]) or lines[i].startswith("#")
        ):
            i += 1
        lines = lines[i:]

    license_text = [
        f"# {line}" if not re.fullmatch(r" *\n", line) else "#\n"
        for line in license_text
    ]

    with open(file, "w", encoding="utf-8") as f:
        f.writelines(license_text)
        f.write("\n")
        f.writelines(lines)


def main():
    parser = ArgumentParser()
    parser.add_argument("filenames", nargs="*", help="Filenames to fix")
    parser.add_argument(
        "-lf",
        "--license-file",
        default="LICENSE",
        help="Path to license file with the text for the headers",
    )
    parser.add_argument(
        "-uy",
        "--update-year",
        default=True,
        help="Update the year in the license text",
    )
    args = parser.parse_args()

    with open(args.license_file, "r") as f:
        license_text = f.readlines()
    if args.update_year:
        license_text = update_year(license_text)

    for file in args.filenames:
        apply_license(file, license_text)


if __name__ == "__main__":
    main()
