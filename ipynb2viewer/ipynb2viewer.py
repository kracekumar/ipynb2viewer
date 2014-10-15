#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Upload `.ipynb` files  to gist.github.com as anonymous user and returns nbviewr url.

Usage:
  ipynb2viewer all <path>
  ipynb2viewer file <filename>
  ipynb2viewer file <filename> --private
  ipynb2viewer file <filename> --open
  ipynb2viewer file <filename> --open --private
  ipynb2viewer all <path> --open

Arguments:
  filename ipynb file name or json.

Options:
  -h --help Display all the options.
  --version Show version.
  --open
"""

import os
import sys
import webbrowser
try:
    import json
except ImportError:
    import simplejson as json
import requests
from docopt import docopt


def get_all_ipynb_files(path):
    return [filename for filename in os.listdir(path) if filename.endswith('.ipynb')]


def upload_file_to_gist(filename, path=None, public=True):
    if path:
        full_path = os.path.join(path, filename)
    else:
        full_path = filename

    data = json.dumps(
        {'files':
            {'{}'.format(filename.replace('/', '_')):
             {'content': "".join(open(full_path).readlines())}},
         'public': public}
    )
    r = requests.post("https://api.github.com/gists", data=data)
    return r.json()


def create_nbviewer_url(gist_url):
    data = {'gistnorurl': gist_url}
    r = requests.post("http://nbviewer.ipython.org/create", data=data)
    if r.ok:
        return r.url
    r.raise_for_status()


def create_and_upload_to_nbviewer(arguments, filename, path=None):
    # If private is present, make public as False
    public = not arguments.get('--private')
    details = upload_file_to_gist(filename, path, public=public)
    gist_url = details.get('html_url')
    sys.stdout.write("Uploaded {} file to gist {}\n".format(filename, gist_url))
    nbviewer_url = create_nbviewer_url(gist_url)
    sys.stdout.write("nbviewer url: {}\n".format(nbviewer_url))
    if arguments.get('--open'):
        webbrowser.open(nbviewer_url)


def all_argument_call(arguments):
    path = arguments.get('<path>')
    if not os.path.isdir(path):
        sys.stderr.write("{} isn't directory\n".format(path))
        exit(1)

    files = get_all_ipynb_files(path)

    if files:
        for filename in files:
            create_and_upload_to_nbviewer(arguments, filename, path)
    else:
        sys.stderr.write("No ipynb files found in {}\n".format(path))
        exit(1)


def file_argument_call(arguments):
    filename = arguments.get('<filename>')
    if not os.path.isfile(filename):
        sys.stderr.write("{} file doesn't exit\n".format(filename))
        exit(1)

    create_and_upload_to_nbviewer(arguments, filename)


def main():
    arguments = docopt(__doc__, argv=sys.argv[1:], help=True, version='0.0.2')
    try:
        if arguments.get('all'):
            all_argument_call(arguments)
        elif arguments.get('file'):
            file_argument_call(arguments)
    except (requests.ConnectionError, Exception) as e:
        raise e
        sys.stderr.write(e)


if __name__ == "__main__":
    main()
