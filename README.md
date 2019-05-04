# Sphinx XDev Theme

XDev branded sphinx theme that inherits from sphinx_rtd_theme.

This theme is based off of the sphinx_rtd_theme, from which it inherits, but the CSS styling
has been altered for easier reading on a variety of platforms and browsers.


## Installation

You can apply this theme to your current documents by installing this repository like any other python package:

Either from GIT:
```
pip install -e git+https://github.com/NCAR/sphinx_xdev_theme.git
```

or
```
# install from pypi release
pip install sphinx_xdev_theme
```

## Adding to your Sphinx docs

If you haven't already created your Sphinx documentation, you can start sphinx with
`sphinx-quickstart` and follow the guided steps. When you are finished,
add these lines to your `conf.py` file:
```
import sphinx_xdev_theme
html_theme = 'sphinx_xdev_theme'
html_theme_path = [sphinx_xdev_theme.get_html_theme_path()]
```

## Making this theme work on Readthedocs
Add the following lines to your documentations conf.py file:
```
import sphinx
import sphinx_xdev_theme

def setup(app):
    app.add_stylesheet("xdev.css")

on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
if on_rtd:
    extensions.append('sphinx.ext.mathjax')

else:
    extensions.append('sphinx.ext.imgmath')    
```
Finally, when setting up your documentation build on readthedocs, make sure to include a requirements file which installs this theme. The `sphinx_rtd_theme` that it inherits from should already be there.