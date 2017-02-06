# coding: utf-8

from __future__ import unicode_literals
import glob
import codecs
import os
import html2text
import pytest

here = os.path.dirname(os.path.realpath(__file__))


def _get_html_source(filename):
    with codecs.open('{}/data/{}.html'.format(here, filename), 'r', 'utf-8') as f:
        return f.read()


def _get_markdown_file(filename):
    with codecs.open('{}/data/{}.md'.format(here, filename), 'r', 'utf-8') as f:
        return f.read()

def get_html_and_markdown(filename):
    return _get_html_source(filename), _get_markdown_file(filename)


@pytest.fixture
def list_of_test_files():
    files = glob.glob('{}/data/*.html'.format(here))
    return map(lambda x: os.path.splitext(x)[0], map(os.path.basename, files))


@pytest.mark.parametrize(
    "name", [filename for filename in list_of_test_files()]
)
def test_html_converts_in_expected_markdown(name):
        html_source, expected = get_html_and_markdown(name)
        converted = html2text.html2text(html_source)
        assert converted == expected


class TestExtras:

    # To be completed, these are mostly corner cases that deal with flips and switches
    # that we don't really use...

    def test_bodywidth_newline(self):
        html_source, expected = get_html_and_markdown('extras/bodywidth_newline')
        html2text.config.BODY_WIDTH = 0
        converted = html2text.html2text(html_source)
        assert converted == expected


    def test_default_image_alt(self):
        html_source, expected = get_html_and_markdown('extras/default_image_alt')
        html2text.config.DEFAULT_IMAGE_ALT = 'Image'
        converted = html2text.html2text(html_source)
        assert converted == expected


    def test_doc_with_table_bypass(self):
        # TODO: Doesn't look too good - revisit
        html_source, expected = get_html_and_markdown('extras/doc_with_table_bypass')
        html2text.config.BYPASS_TABLES = True
        converted = html2text.html2text(html_source)
        assert converted == expected

    def test_flip_emphasis(self):
        html_source, expected = get_html_and_markdown('extras/flip_emphasis')
        h = html2text.HTML2Text()
        h.emphasis_mark = '*'
        h.strong_mark = '__'
        converted = h.handle(html_source)
        assert converted == expected
