# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Snippet(models.Model):
    code = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    language = models.CharField(
        choices=LANGUAGE_CHOICES, default="python", max_length=100
    )
    linenos = models.BooleanField(default=False)
    style = models.CharField(choices=STYLE_CHOICES, default="friendly", max_length=100)
    title = models.CharField(max_length=100, blank=True, default="")

    class Meta:
        ordering = ["created"]

    def __str__(self):
        return self.code

