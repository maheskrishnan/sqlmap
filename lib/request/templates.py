#!/usr/bin/env python

"""
Copyright (c) 2006-2012 sqlmap developers (http://www.sqlmap.org/)
See the file 'doc/COPYING' for copying permission
"""

from lib.core.data import kb
from lib.request.connect import Connect as Request

def getPageTemplate(payload, place):
    retVal = (kb.originalPage, kb.errorIsNone)

    if payload and place:
        if (payload, place) not in kb.pageTemplates:
            page, _ = Request.queryPage(payload, place, content=True)
            kb.pageTemplates[(payload, place)] = (page, kb.lastParserStatus is None)

        retVal = kb.pageTemplates[(payload, place)]

    return retVal

