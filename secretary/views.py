from django.shortcuts import render, redirect
# Create your views here.
from .models import Diploma
from django.views.generic.edit import CreateView
from django.forms import ModelForm
from django.views.generic import DetailView
from django.core.urlresolvers import reverse_lazy
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, HTML, Field
from crispy_forms.bootstrap import FormActions

def show_base(request):
    return render(request, 'base.html')

def show_page(request):
    # Дізнатися хто ти?(Студік чи лектор)
    ansDiploma = Diploma.objects.filter(profile__user=request.user)
    # зареквестити відповідну модель
    return render(request, 'diploma_list.html', {"tasks": ansDiploma})


class BaseForm(ModelForm):
    class Meta:
        model = Diploma
        fields = "__all__"

    def __init__(self, *args, **kwargs):

        super(ModelForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)

        # set form tag attributes
        # self.helper.form_action = reverse_lazy('task_add')
        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-horizontal'

        # set form field properties
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-10'
        self.helper.render_unmentioned_fields = True
        self.helper.layout[-1] = Layout(
            Field('description', css_class='input-xlarge'),
            FormActions(Submit('add_button', u'Зберегти', css_id='submit-id-send_button')))


class DiplomaCreateForm(BaseForm):

    def __init__(self, *args, **kwargs):
        BaseForm.__init__(self, *args, **kwargs)
        self.helper.form_action = reverse_lazy('diploma_add')


class DiplomaCreate(CreateView):
    model = Diploma
    form_class = DiplomaCreateForm
    template_name = "diploma_add.html"

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.save()
        return redirect(self.get_success_url())

    def get_success_url(self):
        return "%s?status_message=Завдання успішно додано" % reverse_lazy("home")


class DiplomaDetail(DetailView):
    model = Diploma
    context_object_name = "task"
    template_name = 'diploma_edit.html'

    def get_object(self):
        """
        Task view
        """
        object_task = super(TaskDetail, self).get_object()
        return object_task