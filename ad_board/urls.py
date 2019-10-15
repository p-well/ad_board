from django.urls import path

from ad_board.views.views import show_main_page, show_by_category, AdCreateView

urlpatterns = [
    path('', show_main_page, name='main'),
    path('<int:category_id>/', show_by_category, name='by_category'),
    path('additem/', AdCreateView.as_view(), name='add_item'),
]