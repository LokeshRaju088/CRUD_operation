from django.db import models
from django.apps import apps


# Create your models here.

class Eventdetails(models.Model):
    event = models.CharField(max_length=255)

    def __str__(self):
        return self.event


class Jobrequisition(models.Model):
    jobposition = models.CharField(max_length=255)

    def __str__(self):
        return self.jobposition


class Persona(models.Model):
    PERSONA_CHOICES = [
        ('choice1', 'Choice 1'),
        ('choice2', 'Choice 2'),
        # Add more choices as needed
    ]
    persona = models.CharField(max_length=255, choices=PERSONA_CHOICES)

    def __str__(self):
        return self.persona


class Screeningmode(models.Model):
    screening_mode = models.CharField(max_length=255)

    def __str__(self):
        return self.screening_mode


class Gender(models.Model):
    gender = models.CharField(max_length=255)

    def __str__(self):
        return self.gender


class Maritalstatus(models.Model):
    marital_status = models.CharField(max_length=255)

    def __str__(self):
        return self.marital_status


class Employeedirectory(models.Model):
    referred_by = models.CharField(max_length=255)

    def __str__(self):
        return self.referred_by


class City(models.Model):
    city = models.CharField(max_length=255)

    def __str__(self):
        return self.city


class Experiencelevel(models.Model):
    experience_level = models.CharField(max_length=255)

    def __str__(self):
        return self.experience_level


class Educationlevel(models.Model):
    education_level = models.CharField(max_length=255)

    def __str__(self):
        return self.education_level


class Educationqualification(models.Model):
    education_qualification = models.CharField(max_length=255)

    def __str__(self):
        return self.education_qualification


class Educationspecialization(models.Model):
    education_specialization = models.CharField(max_length=255)

    def __str__(self):
        return self.education_specialization


class Source(models.Model):
    source = models.CharField(max_length=255)

    def __str__(self):
        return self.source


class Sourcetype(models.Model):
    source_type = models.CharField(max_length=255)

    def __str__(self):
        return self.source_type


class Reasonforchange(models.Model):
    reason_for_change = models.CharField(max_length=255)

    def __str__(self):
        return self.reason_for_change


# Create your models here.
class Candidatedirectory(models.Model):
    event = models.ForeignKey("Eventdetails", models.DO_NOTHING, db_column="event", blank=True, null=True)
    job_position = models.ForeignKey("Jobrequisition", models.DO_NOTHING, db_column="job_position", blank=True,
                                     null=True, )
    recruiter_alert = models.CharField(max_length=50, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    persona = models.ForeignKey("Persona", models.DO_NOTHING, db_column="persona", blank=True, null=True, )
    role = models.IntegerField(blank=True, null=True)
    screening_mode = models.ForeignKey("Screeningmode", models.DO_NOTHING, db_column="screening_mode", blank=True,
                                       null=True, )
    dob = models.DateField(blank=True, null=True)
    gender = models.ForeignKey("Gender", models.DO_NOTHING, db_column="gender", blank=True, null=True)
    marital_status = models.ForeignKey("Maritalstatus", models.DO_NOTHING, db_column="marital_status", blank=True,
                                       null=True, )
    contact_no_primary = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    contact_no_alternate = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    referred_by = models.ForeignKey("Employeedirectory", models.DO_NOTHING, db_column="referred_by", blank=True,
                                    null=True, )
    referred_by_other = models.CharField(max_length=250, blank=True, null=True)
    address_line = models.CharField(max_length=255, blank=True, null=True)
    city = models.ForeignKey("City", models.DO_NOTHING, db_column="city", blank=True, null=True)
    pincode = models.DecimalField(max_digits=6, decimal_places=0, blank=True, null=True)
    experience_level = models.ForeignKey("Experiencelevel", models.DO_NOTHING, db_column="experience_level", blank=True,
                                         null=True, )
    education_level = models.ForeignKey("Educationlevel", models.DO_NOTHING, db_column="education_level", blank=True,
                                        null=True, )
    education_qualification = models.ForeignKey("Educationqualification", models.DO_NOTHING,
                                                db_column="education_qualification", blank=True, null=True, )
    education_specialization = models.ForeignKey("Educationspecialization", models.DO_NOTHING,
                                                 db_column="education_specialization", blank=True, null=True, )
    education_specialization_other = models.TextField(blank=True, null=True)  # This field type is a guess.
    education_institution = models.ForeignKey("Source", models.DO_NOTHING, db_column="education_institution",
                                              blank=True, null=True, )
    education_institution_other = models.TextField(blank=True, null=True)  # This field type is a guess.
    source = models.ForeignKey("Source", models.DO_NOTHING, db_column="source", blank=True, null=True,
                               related_name="source_for_candidate_details", )
    source_type = models.ForeignKey("Sourcetype", models.DO_NOTHING, db_column="source_type", blank=True, null=True)
    years_of_experience = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    current_employer = models.CharField(max_length=100, blank=True, null=True)
    current_designation = models.TextField(blank=True, null=True)  # This field type is a guess.
    current_monthly_salary = models.IntegerField(blank=True, null=True)
    expected_monthly_salary = models.IntegerField(blank=True, null=True)
    notice_period = models.CharField(max_length=50, blank=True, null=True)
    reason_for_change = models.ForeignKey("Reasonforchange", models.DO_NOTHING, db_column="reason_for_change",
                                          blank=True, null=True, )
    photo_path = models.TextField(blank=True, null=True)  # This field type is a guess.
    resume_path = models.TextField(blank=True, null=True)  # This field type is a guess.
    login_time = models.DateTimeField(blank=True, null=True)
    logout_time = models.DateTimeField(blank=True, null=True)
    ip_address = models.CharField(max_length=15, blank=True, null=True)
    geo_location = models.CharField(max_length=50, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    modified_date = models.DateTimeField(blank=True, null=True)
    modified_by = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(default=1)


class Meta:
    managed = False
    db_table = "CandidateDirectory"

    constraints = [models.UniqueConstraint(fields=['first_name', 'last_name'], name='full_name')]
