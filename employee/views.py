from django.views.generic.edit import FormView, DeleteView, UpdateView
from django.views.generic.list import ListView
from .models import Employee
from .forms import EmployeeForm, QualificationFormSet


class EmployeeListView(ListView):

    model = Employee
    template_name = 'employee/employee_list.html'


class EmployeeCreateView(FormView):

    template_name = 'employee/employee_form.html'
    form_class = EmployeeForm
    success_url = '/employees/'

    def get_context_data(self, **kwargs):
        data = super(EmployeeCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            data['qualifications'] = QualificationFormSet(self.request.POST)
        else:
            data['qualifications'] = QualificationFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        qualifications = context['qualifications']
        self.object = form.save()
        if qualifications.is_valid():
            qualifications.instance = self.object
            qualifications.save()

        return super(EmployeeCreateView, self).form_valid(form)


class EmployeeUpdateView(UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employee/employee_form.html'
    success_url = '/employees/'

    def get_context_data(self, **kwargs):
        data = super(EmployeeUpdateView, self).get_context_data(**kwargs)
        if self.request.POST:
            data['qualifications'] = QualificationFormSet(self.request.POST, instance=self.object)
        else:
            data['qualifications'] = QualificationFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        qualifications = context['qualifications']
        self.object = form.save()
        if qualifications.is_valid():
            qualifications.instance = self.object
            qualifications.save()

        return super(EmployeeUpdateView, self).form_valid(form)


class EmployeeDeleteView(DeleteView):
    model = Employee
    success_url = '/employees/'
