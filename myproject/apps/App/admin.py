from django.contrib import admin
from .models import Candidate
from .forms import CandidateForm
from django.utils.html import format_html

class CandidateAdmin(admin.ModelAdmin):
    radio_fields = {"smoker": admin.HORIZONTAL}
    # form = CandidateForm
    list_filter = ['situation']
    list_display = ['name','job', 'email', 'create_at', 'status', '_']
    search_fields = ['firstname', 'lastname', 'email', 'situation']
    list_per_page = 10

    # Readonly section
    # readonly_fields = ['experience', 'gender', 'firstname', 'lastname', 'job', 'email', 'phone', 'salary',
    #                    'birth', 'personality', 'smoker', 'file', 'image', 'message', 'status_course',
    #                    'started_course', 'finished_course', 'course', 'institution', 'about_course',
    #                    'started_job', 'finished_job', 'company', 'position', 'about_job', 'employed',
    #                    'remote', 'travel']

    # Fieldset
    fieldsets = [
        # HR operations
        ('HR OPERATIONS', {'fields': ['situation']}),
        # Personal
        ('PERSONAL', {'fields': ['experience', 'gender', 'job', 'email', 'phone',
         'salary', 'birth', 'personality', 'smoker', 'file', 'image', 'message']}
         ),
        # Educational
        ('EDUCATIONAL', {"fields": ['status_course','started_course', 'finished_course',
        'course', 'institution', 'about_course',]}
        ),
        # Profesional
        ('PROFESIONAL', {"fields": ['started_job', 'finished_job', 'company', 'position', 'about_job'
        ]}
        ),
        # Note
        ('NOTE', {"fields": ['employed','remote', 'travel']}
        )
    ]

    # function to hide f-name and l-name (when clicking over the candidate - Rows)
    def get_fields(self, request, obj = None):
        fields = super().get_fields(request, obj)
        if obj:
            fields.remove('firstname')
            fields.remove('lastname')
        return fields

    # function to change the icons
    def _(self, obj):
        if obj.situation == 'Approved':
            return True
        elif obj.situation == 'Pending':
            return None
        else:
            return False

    _.boolean = True

    # function to color the text
    def status(self, obj):
        if obj.situation == 'Approved':
            color = '#28a745'
        elif obj.situation == 'Pending':
            color = '#fea95e'
        else:
            color = 'red'
        return format_html('<strong><p style="color: {}">{}</p></strong>'.format(color, obj.situation))
    status.allow_tags = True

admin.site.register(Candidate, CandidateAdmin)
