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
# class SubjAttrib(models.Model):
#     subj_attrib_id = models.AutoField(db_column='SUBJ_ATTRIB_ID', primary_key=True)  # Field name made lowercase.
#     subj_attrib_version = models.IntegerField(db_column='SUBJ_ATTRIB_VERSION', blank=True, null=True)  # Field name made lowercase.
#     subj_attrib_class = models.CharField(db_column='SUBJ_ATTRIB_CLASS', max_length=256, blank=True, null=True)  # Field name made lowercase.
#     attrib_list_order = models.IntegerField(db_column='ATTRIB_LIST_ORDER', blank=True, null=True)  # Field name made lowercase.
#     text_val = models.CharField(db_column='TEXT_VAL', max_length=2024, blank=True, null=True)  # Field name made lowercase.
#     avail_val = models.CharField(db_column='AVAIL_VAL', max_length=2024, blank=True, null=True)  # Field name made lowercase.
#     funct_val = models.CharField(db_column='FUNCT_VAL', max_length=2024, blank=True, null=True)  # Field name made lowercase.
#     juris_val = models.CharField(db_column='JURIS_VAL', max_length=2024, blank=True, null=True)  # Field name made lowercase.
#     normal_val = models.CharField(db_column='NORMAL_VAL', max_length=2024, blank=True, null=True)  # Field name made lowercase.
#     offset_val = models.IntegerField(db_column='OFFSET_VAL', blank=True, null=True)  # Field name made lowercase.
#     quant_val = models.IntegerField(db_column='QUANT_VAL', blank=True, null=True)  # Field name made lowercase.
#     time_val = models.CharField(db_column='TIME_VAL', max_length=2024, blank=True, null=True)  # Field name made lowercase.
#     type_val = models.CharField(db_column='TYPE_VAL', max_length=2024, blank=True, null=True)  # Field name made lowercase.
#     vocab_val = models.CharField(db_column='VOCAB_VAL', max_length=2024, blank=True, null=True)  # Field name made lowercase.
#     subj_ent = models.ForeignKey('SubjEnt', models.DO_NOTHING, db_column='SUBJ_ENT_ID', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'SUBJ_ATTRIB'
#
#
# class SubjEnt(models.Model):
#     subj_ent_id = models.AutoField(db_column='SUBJ_ENT_ID', primary_key=True)  # Field name made lowercase.
#     subj_ent_version = models.IntegerField(db_column='SUBJ_ENT_VERSION', blank=True, null=True)  # Field name made lowercase.
#     subj_class = models.CharField(db_column='SUBJ_CLASS', max_length=256, blank=True, null=True)  # Field name made lowercase.
#     subj_ent_uri = models.CharField(db_column='SUBJ_ENT_URI', max_length=2024, blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'SUBJ_ENT'
