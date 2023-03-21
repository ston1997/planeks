from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.edit import FormMixin

from .forms import SchemaForm, DataSetForm, SchemaColumnInline
from .models import Schema

from django.views.generic import ListView, DetailView

from django.shortcuts import redirect, get_object_or_404

from extra_views import CreateWithInlinesView, UpdateWithInlinesView

from .utils import generate_data_set


class CreateSchema(LoginRequiredMixin, CreateWithInlinesView):
    model = Schema
    form_class = SchemaForm
    inlines = [
        SchemaColumnInline,
    ]
    template_name = "new_schema.html"

    def get_initial(self):
        data = {"owner": self.request.user}
        return data

    def get_success_url(self):
        if "action" in self.request.POST:
            if self.request.POST["action"] == "submit":
                return reverse("list")
            if self.request.POST["action"] == "add_column":
                schema = self.object
                return reverse("edit", kwargs={"pk": schema.pk})

        else:
            return reverse("list")


class SchemeList(LoginRequiredMixin, ListView):
    template_name = 'data_schemas.html'
    context_object_name = "schema"

    def get_queryset(self):

        return Schema.objects.filter(owner=self.request.user)


class EditSchema(LoginRequiredMixin, UserPassesTestMixin, UpdateWithInlinesView):
    model = Schema
    form_class = SchemaForm
    inlines = [
        SchemaColumnInline,
    ]
    template_name = "new_schema.html"

    def test_func(self):
        # checking if request user is owner of selected schema
        obj = self.get_object()
        if obj.owner == self.request.user:
            return True

    def get_success_url(self):
        if "action" in self.request.POST:
            if self.request.POST["action"] == "submit":
                return reverse("list")
            if self.request.POST["action"] == "add_column":
                obj = self.object
                return reverse("edit", kwargs={"pk": obj.pk})

        else:
            return reverse("list")


def delete(request, pk):
    data = get_object_or_404(Schema, pk=pk)
    data.delete()
    return redirect('list')


class SchemeDetail(LoginRequiredMixin, FormMixin, DetailView):
    """
    Return the list user-created schemas.
    """

    model = Schema
    context_object_name = "schema"
    template_name = "schema_detail.html"

    form_class = DataSetForm

    def get_queryset(self):
        return Schema.objects.filter(owner=self.request.user)

    def post(self, request, *args, **kwargs):
        schema = self.get_object()
        generate_data_set(schema, number_of_rows=int(request.POST["rows"]))
        return HttpResponseRedirect(
            reverse("schema-detail", kwargs={"pk": self.get_object().pk})
        )
