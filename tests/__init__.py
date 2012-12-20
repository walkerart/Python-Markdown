
try:
    import nose
except ImportError:
    raise ImportError("The nose testing framework is required to run " \
                       "Python-Markdown tests. Run `easy_install nose` " \
                       "to install the latest version.")
from .plugins import HtmlOutput, Markdown

def run():
    nose.main(addplugins=[HtmlOutput(), Markdown()])

