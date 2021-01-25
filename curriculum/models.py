import datetime

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
from django.utils import timezone
from django.utils.datetime_safe import time


class Identity(models.Model):

    def __str__(self):
        return self.last_name + ", " + self.name

    def savePath(self, name):
        return f"{self.dni}/{self.modification_date}{name}"

    def sendEmail(self):
        url = "mailto:" + self.email + "?subject=Contacted via online CV"
        return url.replace(" ", "%20")

    dni = models.CharField(max_length=9, unique=True, blank=False)
    name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=60)
    photo = models.ImageField(upload_to=savePath)
    birthdate = models.DateField()
    email = models.EmailField(max_length=60, blank=False)
    address = models.ForeignKey('Address', on_delete=models.SET_NULL, null=True)
    phone = models.IntegerField(blank=False)
    modification_date = models.DateField(auto_now=True, editable=False)
    creation_date = models.DateField(auto_now_add=True, editable=False)
    summary = models.ForeignKey('summary', on_delete=models.SET_NULL, null=True)
    motto = models.CharField(max_length=60)


class Address(models.Model):
    def __str__(self):
        return self.mail_address + ',' + self.cp_address + ', ' + self.city + ', ' + self.state + ', ' + self.country

    def googleMap(self):
        addres = self.mail_address.replace("/", "-").replace(",", "-")
        url = "https://www.google.com/maps/place/" + addres[:addres.index("-")] \
              + " " + self.cp_address + " " + self.city + " " + self.state + "/"
        return url

    mail_address = models.CharField(max_length=100)
    cp_address = models.CharField(max_length=12)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=30)


class Summary(models.Model):
    def __str__(self):
        return self.summary

    summary = models.TextField(max_length=600)
    skills = models.ManyToManyField('Skill')
    achievement = models.ManyToManyField('Achievement')


class WorkExperience(models.Model):
    def __str__(self):
        return self.job + '(' + self.enterprise + ')'

    def enterprisePath(self, name):
        return f"logo_enterprise/{self.enterprise}-{name}"

    def yearWorking(self):
        return (self.date_finish.year - self.date_start.year)

    def monthWorking(self):
        return (self.date_finish.month - self.date_start.month)

    identity = models.ForeignKey('Identity', on_delete=models.CASCADE)
    job = models.CharField(max_length=50, blank=False)
    date_start = models.DateField(blank=False)
    date_finish = models.DateField(blank=False)
    enterprise = models.CharField(max_length=80, blank=False)
    logo = models.ImageField(upload_to=enterprisePath, null=True)
    summary = models.ForeignKey('Summary', on_delete=models.SET_NULL, null=True)


class Skill(models.Model):
    def __str__(self):
        return self.skill + '(' + self.sector + ')' + ('*' * self.level)

    sector = models.CharField(max_length=50)
    skill = models.CharField(max_length=50, blank=False)
    level = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)], blank=False)


class Achievement(models.Model):
    def __str__(self):
        return self.achieved

    achieved = models.CharField(max_length=100, blank=False)


class Education(models.Model):
    def __str__(self):
        return self.level + self.specialization

    identity = models.ForeignKey('Identity', on_delete=models.CASCADE)
    level = models.CharField(max_length=50, blank=False)
    specialization = models.CharField(max_length=60, blank=False)
    study_center = models.CharField(max_length=60, blank=False)
    date_start = models.DateField(blank=False)
    date_finish = models.DateField(blank=False)
    web_study_center = models.URLField(max_length=200)
    summary = models.ForeignKey('Summary', on_delete=models.SET_NULL, null=True)


class LanguageSkills(models.Model):
    def __str__(self):
        return "[" + str(
            self.identity) + "] " + self.language.name + ' (L:' + self.listening + ' W:' + self.writing + ' R:' + self.reading + ' S:' + self.speaking + ")"

    identity = models.ForeignKey('Identity', on_delete=models.CASCADE)
    language = models.ForeignKey('Language', on_delete=models.CASCADE)
    listening = models.CharField(max_length=10)
    writing = models.CharField(max_length=10)
    reading = models.CharField(max_length=10)
    speaking = models.CharField(max_length=10)


class Language(models.Model):
    def __str__(self):
        return self.name

    def flagPath(self, name):
        return f"flags/{self.name}-{name}"

    name = models.CharField(max_length=30)
    flag = models.ImageField(upload_to=flagPath, null=True)
