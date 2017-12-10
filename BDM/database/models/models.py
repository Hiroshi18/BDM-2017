# # This is an auto-generated Django model module.
# # You'll have to do the following manually to clean this up:
# #   * Rearrange models' order
# #   * Make sure each model has one field with primary_key=True
# #   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
# #   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# # Feel free to rename the models, but don't rename db_table values or field names.
#
# from __future__ import unicode_literals
#
# from django.db import models
#
#
# class FizRepG2Bib(models.Model):
#     db_id = models.IntegerField(db_column='DB_ID', primary_key=True)  # Field name made lowercase.
#     contrib_type = models.CharField(db_column='CONTRIB_TYPE', max_length=16, blank=True, null=True)  # Field name made lowercase.
#     contrib_name = models.CharField(db_column='CONTRIB_NAME', max_length=2048, blank=True, null=True)  # Field name made lowercase.
#     contrib_date = models.CharField(db_column='CONTRIB_DATE', max_length=512, blank=True, null=True)  # Field name made lowercase.
#     contrib_authident = models.CharField(db_column='CONTRIB_AUTHIDENT', max_length=2048, blank=True, null=True)  # Field name made lowercase.
#     bibrec_ident = models.CharField(db_column='BIBREC_IDENT', max_length=32, blank=True, null=True)  # Field name made lowercase.
#     bibfield_tag = models.CharField(db_column='BIBFIELD_TAG', max_length=8, blank=True, null=True)  # Field name made lowercase.
#     bibfield_string = models.CharField(db_column='BIBFIELD_STRING', max_length=2048, blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'FIZ_REP_G2BIB'
#
#
# class FizRepManifnowork(models.Model):
#     db_id = models.IntegerField(db_column='DB_ID', primary_key=True)  # Field name made lowercase.
#     title = models.CharField(db_column='TITLE', max_length=2048, blank=True, null=True)  # Field name made lowercase.
#     contrib_type = models.CharField(db_column='CONTRIB_TYPE', max_length=16, blank=True, null=True)  # Field name made lowercase.
#     contrib_authname = models.CharField(db_column='CONTRIB_AUTHNAME', max_length=2048, blank=True, null=True)  # Field name made lowercase.
#     contrib_authident = models.CharField(db_column='CONTRIB_AUTHIDENT', max_length=2048, blank=True, null=True)  # Field name made lowercase.
#     contrib_role = models.CharField(db_column='CONTRIB_ROLE', max_length=64, blank=True, null=True)  # Field name made lowercase.
#     bibrec_id = models.CharField(db_column='BIBREC_ID', max_length=32, blank=True, null=True)  # Field name made lowercase.
#     bibrec_group = models.CharField(db_column='BIBREC_GROUP', max_length=32, blank=True, null=True)  # Field name made lowercase.
#     marc_filename = models.CharField(db_column='MARC_FILENAME', max_length=1024, blank=True, null=True)  # Field name made lowercase.
#     marc_recnum = models.IntegerField(db_column='MARC_RECNUM', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'FIZ_REP_MANIFNOWORK'
#
#
# class FizRepWork(models.Model):
#     db_id = models.IntegerField(db_column='DB_ID', primary_key=True)  # Field name made lowercase.
#     uniform_title = models.CharField(db_column='UNIFORM_TITLE', max_length=2048, blank=True, null=True)  # Field name made lowercase.
#     cmp_auth_name = models.CharField(db_column='CMP_AUTH_NAME', max_length=2048, blank=True, null=True)  # Field name made lowercase.
#     date_text = models.CharField(db_column='DATE_TEXT', max_length=1024, blank=True, null=True)  # Field name made lowercase.
#     ident_group = models.CharField(db_column='IDENT_GROUP', max_length=32, blank=True, null=True)  # Field name made lowercase.
#     ident_algor = models.CharField(db_column='IDENT_ALGOR', max_length=16, blank=True, null=True)  # Field name made lowercase.
#     bibrec_id = models.CharField(db_column='BIBREC_ID', max_length=32, blank=True, null=True)  # Field name made lowercase.
#     bibfield_tag = models.CharField(db_column='BIBFIELD_TAG', max_length=8, blank=True, null=True)  # Field name made lowercase.
#     authrec_id = models.CharField(db_column='AUTHREC_ID', max_length=32, blank=True, null=True)  # Field name made lowercase.
#     marc_filename = models.CharField(db_column='MARC_FILENAME', max_length=1024, blank=True, null=True)  # Field name made lowercase.
#     marc_recnum = models.IntegerField(db_column='MARC_RECNUM', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'FIZ_REP_WORK'
#
#
#
# class DjangoMigrations(models.Model):
#     app = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     applied = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'django_migrations'
