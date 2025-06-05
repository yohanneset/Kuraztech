from rest_framework import viewsets, filters
from django.views.generic import TemplateView

from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-created_at')
    serializer_class = TaskSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

    def get_queryset(self):
        queryset = super().get_queryset()
        status = self.request.query_params.get('status')
        if status == 'finished':
            queryset = queryset.filter(is_completed=True)
        elif status == 'pending':
            queryset = queryset.filter(is_completed=False)
        return queryset


class APIHomeView(TemplateView):
    template_name = "tasks/api_home.html"

