# -*- coding: utf-8 -*-
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.template import loader
from django.views.generic.edit import CreateView

from ad_board.models.models import Advertisement, Category
from ad_board.forms.forms import AdForm


def show_main_page(request):
    template = loader.get_template('main.html')
    advertisements = Advertisement.objects.all()
    categories = Category.objects.all()
    context = {
        'advertisements': advertisements,
        'categories': categories,
    }
    document = template.render(context, request)
    return HttpResponse(document)


def show_by_category(request, category_id):
    advertisements = Advertisement.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    current_category = categories.get(id=category_id)
    template = loader.get_template('by_category.html')
    context = {
        'advertisements': advertisements,
        'categories': categories,
        'current_category': current_category,
    }
    document = template.render(context, request)
    return HttpResponse(document)


class AdCreateView(CreateView):
    template_name = 'add_item.html'
    form_class = AdForm
    success_url = reverse_lazy('main')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context.update({'categories': Category.objects.all()})
        return context
