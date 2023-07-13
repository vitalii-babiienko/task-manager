from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.db.models import QuerySet

from manager.forms import (
    PositionSearchForm,
    WorkerSearchForm,
    WorkerCreationForm,
    WorkerPositionUpdateForm,
    TaskTypeSearchForm,
    TaskSearchForm,
    TaskForm,
)
from manager.models import (
    Task,
    TaskType,
    Position,
    Worker,
)


class IndexView(generic.TemplateView):
    template_name = "manager/index.html"

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)

        context["number_of_workers"] = get_user_model().objects.count()
        context["number_of_tasks"] = Task.objects.count()
        context["number_of_task_types"] = TaskType.objects.count()

        return context


class PositionListView(LoginRequiredMixin, generic.ListView):
    model = Position
    paginate_by = 5

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)

        name = self.request.GET.get("name", "")

        context["search_form"] = PositionSearchForm(
            initial={
                "name": name,
            }
        )

        return context

    def get_queryset(self) -> QuerySet:
        queryset = Position.objects.all()

        form = PositionSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(
                name__icontains=form.cleaned_data["name"],
            )

        return queryset


class PositionCreateView(LoginRequiredMixin, generic.CreateView):
    model = Position
    fields = "__all__"
    success_url = reverse_lazy("manager:position-list")


class PositionUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Position
    fields = "__all__"
    success_url = reverse_lazy("manager:position-list")


class PositionDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Position
    success_url = reverse_lazy("manager:position-list")
