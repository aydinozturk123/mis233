from django.db import models
from django.contrib.auth.models import UserManager

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior     
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.



class Answer(models.Model):
    answertext = models.CharField(db_column='AnswerText', blank=True, null=True, max_length=10000, verbose_name= "Answer")  # Field name made lowercase.
    surveyid = models.IntegerField(db_column='SurveyID', blank=True, null=True, verbose_name= "Survey ID")  # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID', blank=True, null=True, verbose_name= "User ID")  # Field name made lowercase.
    questionid = models.IntegerField(db_column='QuestionID', blank=True, null=True, verbose_name= "Question ID")  # Field name made lowercase.
    answerid = models.IntegerField(db_column='AnswerID', blank=True, verbose_name= "Answer ID", primary_key=True)
    objects = UserManager()
    def __str__(self):
        return "Survey: " + str(self.surveyid) + " Question ID: " + str(self.questionid) + " User ID: " + str(self.userid) + " Answer ID: " + str(self.answerid)
    

    class Meta:
        managed = True
        db_table = 'Answer'


class Question(models.Model):
    questiontext = models.CharField(blank=True, null=True, max_length=1000, verbose_name= "Question")
    questionexplanation = models.CharField(blank=True, null=True, max_length=1000)
    questionid = models.IntegerField(blank=True, verbose_name= "Question ID", primary_key=True)
    objects = UserManager()
    def __str__(self):
        return "Question ID: " + str(self.questionid)

    class Meta:
        managed = True
        db_table = 'Question'


class Survey(models.Model):
    surveyid = models.AutoField(db_column='SurveyID', primary_key=True, verbose_name= "Survey ID")  # Field name made lowercase.
    description = models.CharField(db_column='Description', blank=True, null=True, max_length=255, verbose_name= "Description")  # Field name made lowercase.
    objects = UserManager()

    def __str__(self):
        return "Survey ID: " + str(self.surveyid)


    class Meta:
        managed = True
        db_table = 'Survey'

