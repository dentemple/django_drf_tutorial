# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from pygments.formatters.html import HtmlFormatter
from pygments import highlight
from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Snippet(models.Model):
    code = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    highlighted = models.TextField()
    language = models.CharField(
        choices=LANGUAGE_CHOICES, default="python", max_length=100
    )
    linenos = models.BooleanField(default=False)
    owner = models.ForeignKey(
        "auth.User", related_name="snippets", on_delete=models.CASCADE
    )
    style = models.CharField(choices=STYLE_CHOICES, default="friendly", max_length=100)
    title = models.CharField(max_length=100, blank=True, default="")

    class Meta:
        ordering = ["created"]

    def __str__(self):
        return self.code

    def save(self, *args, **kwargs):
        lexer = get_lexer_by_name(self.language)
        linenos = "table" if self.linenos else False
        options = {"title": self.title} if self.title else {}

        formatter = HtmlFormatter(
            style=self.style, linenos=linenos, full=True, **options
        )
        self.highlighted = highlight(self.code, lexer, formatter)

        super(Snippet, self).save(*args, **kwargs)

