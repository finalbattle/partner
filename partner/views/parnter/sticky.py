# -*- coding: utf-8 -*-

from partner.config import url
from partner.handlers import Handler


@url("/sticky", name="partner.sticky")
class StickyHandler(Handler):
    def get(self):
        return self.render("partner/sticky.html")