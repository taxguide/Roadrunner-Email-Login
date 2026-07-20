# Configuration file for the Sphinx documentation builder.

project = 'Roadrunner Email Login'
author = 'Roadrunner Email Login'
release = '1.0'

extensions = [
    'sphinx_sitemap',
]

# Templates
templates_path = ['_templates']

exclude_patterns = []

html_theme = 'alabaster'

# Static files
html_static_path = ['_static']

language = 'en'

html_title = "Roadrunner Email Login"

# Sitemap
html_baseurl = "https://roadrunner-email-login-roadrunner-email-login.readthedocs-hosted.com/en/latest/"
sitemap_url_scheme = "{link}"
