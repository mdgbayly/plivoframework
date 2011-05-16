# -*- coding: utf-8 -*-
# Copyright (c) 2011 Plivo Team. See LICENSE for details.


class RESTFormatException(Exception):
    pass


class RESTSyntaxException(Exception):
    pass


class UnrecognizedGrammarException(Exception):
    pass


class RESTAttributeException(Exception):
    pass


class RESTDownloadException(Exception):
    pass


class RESTRedirectException(Exception):
    def __init__(self, url=None, method=None):
        self.url = url
        self.method = method

    def get_url(self):
        return self.url

    def get_method(self):
        return self.method
