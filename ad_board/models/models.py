# -*- coding: utf-8 -*-
from django.db import models

class Advertisement(models.Model):

    title = models.CharField(max_length=35, verbose_name='Название')
    price = models.PositiveIntegerField(blank=True, null=True, verbose_name='Цена')
    content = models.TextField(blank=True, null=True, verbose_name='Описание')
    date_published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации')
    category = models.ForeignKey('Category', null=True, on_delete=models.PROTECT, verbose_name='Категория')

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ['-date_published']


class Category(models.Model):
    name = models.CharField(max_length=25, verbose_name='Категория', db_index=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']

    def __str__(self):
        return self.name
