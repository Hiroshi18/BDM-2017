# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from __future__ import unicode_literals

from django.db import models


class WorkAttrib(models.Model):
    work_attrib_id = models.AutoField(db_column='WORK_ATTRIB_ID', primary_key=True)  # Field name made lowercase.
    work_attrib_version = models.IntegerField(db_column='WORK_ATTRIB_VERSION', blank=True, null=True)  # Field name made lowercase.
    work_attrib_class = models.CharField(db_column='WORK_ATTRIB_CLASS', max_length=64, blank=True, null=True)  # Field name made lowercase.
    attrib_list_order = models.IntegerField(db_column='ATTRIB_LIST_ORDER', blank=True, null=True)  # Field name made lowercase.
    text_val = models.CharField(db_column='TEXT_VAL', max_length=20480, blank=True, null=True)  # Field name made lowercase.
    avail_val = models.CharField(db_column='AVAIL_VAL', max_length=64, blank=True, null=True)  # Field name made lowercase.
    funct_val = models.CharField(db_column='FUNCT_VAL', max_length=64, blank=True, null=True)  # Field name made lowercase.
    juris_val = models.CharField(db_column='JURIS_VAL', max_length=64, blank=True, null=True)  # Field name made lowercase.
    normal_val = models.CharField(db_column='NORMAL_VAL', max_length=512, blank=True, null=True)  # Field name made lowercase.
    offset_val = models.IntegerField(db_column='OFFSET_VAL', blank=True, null=True)  # Field name made lowercase.
    quant_val = models.IntegerField(db_column='QUANT_VAL', blank=True, null=True)  # Field name made lowercase.
    time_val = models.CharField(db_column='TIME_VAL', max_length=64, blank=True, null=True)  # Field name made lowercase.
    type_val = models.CharField(db_column='TYPE_VAL', max_length=64, blank=True, null=True)  # Field name made lowercase.
    vocab_val = models.CharField(db_column='VOCAB_VAL', max_length=64, blank=True, null=True)  # Field name made lowercase.
    work_ent = models.ForeignKey('WorkEnt', models.DO_NOTHING, db_column='WORK_ENT_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WORK_ATTRIB'


class WorkEnt(models.Model):
    work_ent_id = models.AutoField(db_column='WORK_ENT_ID', primary_key=True)  # Field name made lowercase.
    work_ent_version = models.IntegerField(db_column='WORK_ENT_VERSION', blank=True, null=True)  # Field name made lowercase.
    work_ent_uri = models.CharField(db_column='WORK_ENT_URI', max_length=512, blank=True, null=True)  # Field name made lowercase.
    work_ent_authident = models.CharField(db_column='WORK_ENT_AUTHIDENT', max_length=2048, blank=True, null=True)  # Field name made lowercase.
    uniform_title = models.CharField(db_column='UNIFORM_TITLE', max_length=2048, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WORK_ENT'


# class Work2Expr(models.Model):
#     work2expr_id = models.AutoField(db_column='WORK2EXPR_ID', primary_key=True)  # Field name made lowercase.
#     work2expr_version = models.IntegerField(db_column='WORK2EXPR_VERSION', blank=True, null=True)  # Field name made lowercase.
#     rel_type = models.CharField(db_column='REL_TYPE', max_length=32, blank=True, null=True)  # Field name made lowercase.
#     rel_role = models.CharField(db_column='REL_ROLE', max_length=32, blank=True, null=True)  # Field name made lowercase.
#     rel_category = models.CharField(db_column='REL_CATEGORY', max_length=32, blank=True, null=True)  # Field name made lowercase.
#     rel_list_order = models.IntegerField(db_column='REL_LIST_ORDER', blank=True, null=True)  # Field name made lowercase.
#     source_work = models.ForeignKey('WorkEnt', models.DO_NOTHING, db_column='SOURCE_WORK_ID')  # Field name made lowercase.
#     target_expr = models.ForeignKey('ExprEnt', models.DO_NOTHING, db_column='TARGET_EXPR_ID')  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'WORK2EXPR'
#
#
# class Work2Item(models.Model):
#     work2item_id = models.AutoField(db_column='WORK2ITEM_ID', primary_key=True)  # Field name made lowercase.
#     work2item_version = models.IntegerField(db_column='WORK2ITEM_VERSION', blank=True, null=True)  # Field name made lowercase.
#     rel_type = models.CharField(db_column='REL_TYPE', max_length=32, blank=True, null=True)  # Field name made lowercase.
#     rel_role = models.CharField(db_column='REL_ROLE', max_length=32, blank=True, null=True)  # Field name made lowercase.
#     rel_category = models.CharField(db_column='REL_CATEGORY', max_length=32, blank=True, null=True)  # Field name made lowercase.
#     rel_list_order = models.IntegerField(db_column='REL_LIST_ORDER', blank=True, null=True)  # Field name made lowercase.
#     source_work = models.ForeignKey('WorkEnt', models.DO_NOTHING, db_column='SOURCE_WORK_ID')  # Field name made lowercase.
#     target_item = models.ForeignKey('ItemEnt', models.DO_NOTHING, db_column='TARGET_ITEM_ID')  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'WORK2ITEM'
#
#
# class Work2Manif(models.Model):
#     work2manif_id = models.AutoField(db_column='WORK2MANIF_ID', primary_key=True)  # Field name made lowercase.
#     work2manif_version = models.IntegerField(db_column='WORK2MANIF_VERSION', blank=True, null=True)  # Field name made lowercase.
#     rel_type = models.CharField(db_column='REL_TYPE', max_length=32, blank=True, null=True)  # Field name made lowercase.
#     rel_role = models.CharField(db_column='REL_ROLE', max_length=32, blank=True, null=True)  # Field name made lowercase.
#     rel_category = models.CharField(db_column='REL_CATEGORY', max_length=32, blank=True, null=True)  # Field name made lowercase.
#     rel_list_order = models.IntegerField(db_column='REL_LIST_ORDER', blank=True, null=True)  # Field name made lowercase.
#     source_work = models.ForeignKey('WorkEnt', models.DO_NOTHING, db_column='SOURCE_WORK_ID')  # Field name made lowercase.
#     target_manif = models.ForeignKey('ManifEnt', models.DO_NOTHING, db_column='TARGET_MANIF_ID')  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'WORK2MANIF'
#
#
# class Work2Respon(models.Model):
#     work2respon_id = models.AutoField(db_column='WORK2RESPON_ID', primary_key=True)  # Field name made lowercase.
#     work2respon_version = models.IntegerField(db_column='WORK2RESPON_VERSION', blank=True, null=True)  # Field name made lowercase.
#     rel_class = models.CharField(db_column='REL_CLASS', max_length=256, blank=True, null=True)  # Field name made lowercase.
#     rel_type = models.CharField(db_column='REL_TYPE', max_length=32, blank=True, null=True)  # Field name made lowercase.
#     rel_role = models.CharField(db_column='REL_ROLE', max_length=32, blank=True, null=True)  # Field name made lowercase.
#     rel_category = models.CharField(db_column='REL_CATEGORY', max_length=32, blank=True, null=True)  # Field name made lowercase.
#     rel_list_order = models.IntegerField(db_column='REL_LIST_ORDER', blank=True, null=True)  # Field name made lowercase.
#     source_work = models.ForeignKey('WorkEnt', models.DO_NOTHING, db_column='SOURCE_WORK_ID')  # Field name made lowercase.
#     target_respon = models.ForeignKey('ResponEnt', models.DO_NOTHING, db_column='TARGET_RESPON_ID')  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'WORK2RESPON'
#
#
# class Work2Subj(models.Model):
#     work2subj_id = models.AutoField(db_column='WORK2SUBJ_ID', primary_key=True)  # Field name made lowercase.
#     work2subj_version = models.IntegerField(db_column='WORK2SUBJ_VERSION', blank=True, null=True)  # Field name made lowercase.
#     rel_class = models.CharField(db_column='REL_CLASS', max_length=256, blank=True, null=True)  # Field name made lowercase.
#     rel_type = models.CharField(db_column='REL_TYPE', max_length=32, blank=True, null=True)  # Field name made lowercase.
#     rel_role = models.CharField(db_column='REL_ROLE', max_length=32, blank=True, null=True)  # Field name made lowercase.
#     rel_category = models.CharField(db_column='REL_CATEGORY', max_length=32, blank=True, null=True)  # Field name made lowercase.
#     rel_list_order = models.IntegerField(db_column='REL_LIST_ORDER', blank=True, null=True)  # Field name made lowercase.
#     source_work = models.ForeignKey('WorkEnt', models.DO_NOTHING, db_column='SOURCE_WORK_ID')  # Field name made lowercase.
#     target_subj = models.ForeignKey('SubjEnt', models.DO_NOTHING, db_column='TARGET_SUBJ_ID')  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'WORK2SUBJ'
#
#
# class Work2Work(models.Model):
#     work2work_id = models.AutoField(db_column='WORK2WORK_ID', primary_key=True)  # Field name made lowercase.
#     work2work_version = models.IntegerField(db_column='WORK2WORK_VERSION', blank=True, null=True)  # Field name made lowercase.
#     rel_type = models.CharField(db_column='REL_TYPE', max_length=32, blank=True, null=True)  # Field name made lowercase.
#     rel_role = models.CharField(db_column='REL_ROLE', max_length=32, blank=True, null=True)  # Field name made lowercase.
#     rel_category = models.CharField(db_column='REL_CATEGORY', max_length=32, blank=True, null=True)  # Field name made lowercase.
#     rel_list_order = models.IntegerField(db_column='REL_LIST_ORDER', blank=True, null=True)  # Field name made lowercase.
#     source_work = models.ForeignKey('WorkEnt', models.DO_NOTHING, db_column='SOURCE_WORK_ID')  # Field name made lowercase.
#     target_work = models.ForeignKey('WorkEnt', models.DO_NOTHING, db_column='TARGET_WORK_ID')  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'WORK2WORK'
#
