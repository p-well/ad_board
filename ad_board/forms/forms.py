# -*- coding: utf-8 -*-
from django.forms import ModelForm

from ad_board.models.models import Advertisement


class AdForm(ModelForm):
    class Meta:
        model = Advertisement
        fields = ('title', 'content', 'price', 'category')
