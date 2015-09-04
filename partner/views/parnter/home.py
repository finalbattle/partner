# -*- coding: utf-8 -*-

from partner.config import url
from partner.handlers import Handler


@url("/", name="partner.home")
class HomeHandler(Handler):
    def get(self):
        return self.render("partner/home.html")