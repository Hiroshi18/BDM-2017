# Standard Library
from datetime import date

# Django
from django.db import models

# Local Django


class ItemEnt(models.Model):
    identifier = models.CharField(max_length=1000, blank=True, null=True)
    itemIdentifier = models.CharField(max_length=1000, blank=True, null=True)
    fingerprint = models.CharField(max_length=1000, blank=True, null=True)
    provenanceOfTheItem = models.CharField(max_length=1000, blank=True, null=True)
    marksInscriptions = models.CharField(max_length=1000, blank=True, null=True)
    exhibitionHistory = models.CharField(max_length=1000, blank=True, null=True)
    conditionOfTheItem = models.CharField(max_length=1000, blank=True, null=True)
    treatmentHistory = models.CharField(max_length=1000, blank=True, null=True)
    scheduledTreatment = models.CharField(max_length=1000, blank=True, null=True)
    accessRestrictionsOnTheItem = models.CharField(max_length=1000, blank=True, null=True)
    locationOfItem = models.CharField(max_length=1000, blank=True, null=True)
    custodialHistoryOfItem = models.CharField(max_length=1000, blank=True, null=True)
    immediateSourceOfAcquisitionOfItem = models.CharField(max_length=1000, blank=True, null=True)

# class Item2Item(models.Model):
#     item2item_id = models.AutoField(db_column='ITEM2ITEM_ID', primary_key=True)  # Field name made lowercase.
#     item2item_version = models.IntegerField(db_column='ITEM2ITEM_VERSION', blank=True, null=True)  # Field name made lowercase.
#     rel_type = models.CharField(db_column='REL_TYPE', max_length=32, blank=True, null=True)  # Field name made lowercase.
#     rel_role = models.CharField(db_column='REL_ROLE', max_length=32, blank=True, null=True)  # Field name made lowercase.
#     rel_category = models.CharField(db_column='REL_CATEGORY', max_length=32, blank=True, null=True)  # Field name made lowercase.
#     rel_list_order = models.IntegerField(db_column='REL_LIST_ORDER', blank=True, null=True)  # Field name made lowercase.
#     source_item = models.ForeignKey('ItemEnt', models.DO_NOTHING, db_column='SOURCE_ITEM_ID')  # Field name made lowercase.
#     target_item = models.ForeignKey('ItemEnt', models.DO_NOTHING, db_column='TARGET_ITEM_ID')  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'ITEM2ITEM'
#
#
# class Item2Respon(models.Model):
#     item2respon_id = models.AutoField(db_column='ITEM2RESPON_ID', primary_key=True)  # Field name made lowercase.
#     item2respon_version = models.IntegerField(db_column='ITEM2RESPON_VERSION', blank=True, null=True)  # Field name made lowercase.
#     rel_class = models.CharField(db_column='REL_CLASS', max_length=256, blank=True, null=True)  # Field name made lowercase.
#     rel_type = models.CharField(db_column='REL_TYPE', max_length=32, blank=True, null=True)  # Field name made lowercase.
#     rel_role = models.CharField(db_column='REL_ROLE', max_length=32, blank=True, null=True)  # Field name made lowercase.
#     rel_category = models.CharField(db_column='REL_CATEGORY', max_length=32, blank=True, null=True)  # Field name made lowercase.
#     rel_list_order = models.IntegerField(db_column='REL_LIST_ORDER', blank=True, null=True)  # Field name made lowercase.
#     source_item = models.ForeignKey('ItemEnt', models.DO_NOTHING, db_column='SOURCE_ITEM_ID')  # Field name made lowercase.
#     target_respon = models.ForeignKey('ResponEnt', models.DO_NOTHING, db_column='TARGET_RESPON_ID')  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'ITEM2RESPON'
