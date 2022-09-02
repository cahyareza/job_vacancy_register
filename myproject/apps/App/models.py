from django.db import models
from PIL import Image

SITUATION = (
    ('Pending', 'Pending'),
    ('Approved', 'Approved'),
    ('Disapproved', 'Disapproved')
)

PERSONALITY = (
    ('I am outgoing', 'I am outgoing'),
    ('I am sociable', 'I am sociable'),
    ('I am antisocial', 'I am antisocial'),
    ('I am discreet', 'I am discreet'),
    ('I am serious', 'I am serious')
)

SMOKER = (
    ('1', 'Yes'),
    ('2', 'No')
)

# Education
STATUS_COURSE = (
    ('', 'Select your status'),
    ("I'm studying", "I'm studying"),
    ("I took a break", 'I took a break'),
    ('Completed', 'Completed'),
)


class Candidate(models.Model):
    # PERSONAL (CARD 1)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    job = models.CharField(max_length=5)
    # age = models.CharField(max_length=3)
    birth = models.DateField(auto_now=False, auto_now_add=False, verbose_name="Birthday")
    phone = models.CharField(max_length=25)

    personality = models.CharField(max_length=50, null=True, choices=PERSONALITY)
    salary = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    experience = models.BooleanField(null=True)
    smoker = models.CharField(max_length=10, choices=SMOKER, default="")

    email = models.EmailField(max_length=50)
    message = models.TextField()
    file = models.FileField(upload_to='resume', blank=True, verbose_name='Resume')
    image = models.ImageField(upload_to='photo', blank=True, verbose_name='Photo')
    create_at = models.DateTimeField(auto_now_add=True)
    situation = models.CharField(max_length=50, null=True, choices=SITUATION, default='Pending')
    # EDUCATIONAL (CARD 2)
    institution = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    started_course = models.DateField(auto_now=False, auto_now_add=False)
    finished_course = models.DateField(auto_now=False, auto_now_add=False)
    about_course = models.TextField()
    status_course = models.CharField(max_length=50, null=True, choices=STATUS_COURSE)
    #PROFESIONAL (CARD3)
    company = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    started_job = models.DateField(auto_now=False, auto_now_add=False)
    finished_job = models.DateField(auto_now=False, auto_now_add=False)
    about_job = models.TextField()
    employed = models.BooleanField(null=True, verbose_name="I am employed")
    remote = models.BooleanField(null=True, verbose_name="I agree to work remotely")
    travel = models.BooleanField(null=True, verbose_name="I am available for travel")

    def __str__(self):
        return self.firstname

    # Capitalize (F-name and L-name)
    def clean(self):
        self.firstname = self.firstname.capitalize()
        self.lastname = self.lastname.capitalize()

    # Concatenate f-name and l-name (Admin table)
    def name(obj):
        return "%s %s" % (obj.firstname, obj.lastname)

    # Concatenate (when clicking over the candidates)
    def __str__(self):
        return self.firstname + ' ' + self.lastname