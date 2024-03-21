from typing import Dict
from django.db.models.query import QuerySet
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name: str = "main/index.html"

    def get_context_data(self, **kwargs) -> Dict[str, QuerySet]:
        context: Dict[str, QuerySet] = super().get_context_data(**kwargs)
        return context
