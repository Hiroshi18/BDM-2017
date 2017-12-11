# Django
from django.db import models

# Local Django

class WorkEnt(models.Model):
    identifier = models.CharField(max_length=1000, blank=True, null=True)
    titleOfTheWork = models.CharField(max_length=1000, blank=True, null=True)
    formOfWork = models.CharField(max_length=1000, blank=True, null=True)
    dateOfTheWork = models.CharField(max_length=1000, blank=True, null=True)
    otherDistinguishingCharacteristic = models.CharField(max_length=1000, blank=True, null=True)
    intendedTermination = models.CharField(max_length=1000, blank=True, null=True)
    intendedAudience = models.CharField(max_length=1000, blank=True, null=True)
    contextForTheWork = models.CharField(max_length=1000, blank=True, null=True)
    mediumOfPerformance = models.CharField(max_length=1000, blank=True, null=True)
    numericDesignation = models.CharField(max_length=1000, blank=True, null=True)
    key = models.CharField(max_length=1000, blank=True, null=True)
    coordinates = models.CharField(max_length=1000, blank=True, null=True)
    equinox = models.CharField(max_length=1000, blank=True, null=True)
    subjectOfTheWork = models.CharField(max_length=1000, blank=True, null=True)
    placeOfOriginOfTheWork = models.CharField(max_length=1000, blank=True, null=True)
    history = models.CharField(max_length=1000, blank=True, null=True)



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
