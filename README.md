# bibconvert
A CLI program to convert citation files to a rg-db-public citation style yaml files.

## Installation

Clone the git repo to your local computer.

``git clone https://github.com/st3107/bibconvert.git``

Install the required packages.

``pip install -e . -r requirement.txt``

Add the following bash script to your .bashrc or .bash_profile files.
Substitute the the ``<path to the main.py>`` with the absolute path to the main.py inside bibconvert folder.
And then restart the terminal.

``alias bibconvert='python <path to the main.py>'``

In the terminal, run the following code to see the usage of the program.

``bibconvert --help``
