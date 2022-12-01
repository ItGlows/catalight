import os
import sys
sys.path.insert(0, os.path.abspath('../../photoreactor_code/'))
sys.path.insert(0, os.path.abspath('../../photoreactor_code/data_analysis/'))
sys.path.insert(0, os.path.abspath('../..'))
print(sys.path)
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'photoreactor'
copyright = '2022, Briley Bourgeois, Claire Carlin'
author = 'Briley Bourgeois, Claire Carlin'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.napoleon', 'sphinx.ext.autodoc']

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
exclude_patterns = ['photoreactor_code/data_analysis/IntegrationTesting.rst']

napoleon_google_docstring = False
napoleon_numpy_docstring = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']