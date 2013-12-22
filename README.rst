===============================
ipynb2viewer
===============================

.. image:: https://badge.fury.io/py/ipynb2viewer.png
    :target: http://badge.fury.io/py/ipynb2viewer

.. image:: https://travis-ci.org/kracekumar/ipynb2viewer.png?branch=master
        :target: https://travis-ci.org/kracekumar/ipynb2viewer

.. image:: https://pypip.in/d/ipynb2viewer/badge.png
        :target: https://crate.io/packages/ipynb2viewer?version=latest


Post IPython notebook files to nbviewer. IPython notebook content will be posted to gist.github.com.

Install
-----
* `pip install ipynb2viewer`

Usage
-----
Upload all ipynb files in the given path to gist.github.com and return nbviewer urls.

* ipynb2viewer all <path>

Upload mentioned file to gist.github.com and return nbviewer url.

* ipynb2viewer file <filename>

Upload mentioned file to gist.github.com and open nbviewer url in webbrowser.

* ipynb2viewer file <filename> --open

Upload all ipynb files in the given path to gist.github.com and open nbviewer urls in webbrowser.

* ipynb2viewer all <path> --open

* Free software: BSD license
* Documentation: http://ipynb2viewer.rtfd.org.
