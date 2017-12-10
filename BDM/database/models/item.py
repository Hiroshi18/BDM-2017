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
# class ItemAttrib(models.Model):
#     item_attrib_id = models.AutoField(db_column='ITEM_ATTRIB_ID', primary_key=True)  # Field name made lowercase.
#     item_attrib_version = models.IntegerField(db_column='ITEM_ATTRIB_VERSION', blank=True, null=True)  # Field name made lowercase.
#     item_attrib_class = models.CharField(db_column='ITEM_ATTRIB_CLASS', max_length=64, blank=True, null=True)  # Field name made lowercase.
#     attrib_list_order = models.IntegerField(db_column='ATTRIB_LIST_ORDER', blank=True, null=True)  # Field name made lowercase.
#     text_val = models.CharField(db_column='TEXT_VAL', max_length=20480, blank=True, null=True)  # Field name made lowercase.
#     avail_val = models.CharField(db_column='AVAIL_VAL', max_length=64, blank=True, null=True)  # Field name made lowercase.
#     funct_val = models.CharField(db_column='FUNCT_VAL', max_length=64, blank=True, null=True)  # Field name made lowercase.
#     juris_val = models.CharField(db_column='JURIS_VAL', max_length=64, blank=True, null=True)  # Field name made lowercase.
#     normal_val = models.CharField(db_column='NORMAL_VAL', max_length=64, blank=True, null=True)  # Field name made lowercase.
#     offset_val = models.IntegerField(db_column='OFFSET_VAL', blank=True, null=True)  # Field name made lowercase.
#     quant_val = models.IntegerField(db_column='QUANT_VAL', blank=True, null=True)  # Field name made lowercase.
#     time_val = models.CharField(db_column='TIME_VAL', max_length=64, blank=True, null=True)  # Field name made lowercase.
#     type_val = models.CharField(db_column='TYPE_VAL', max_length=64, blank=True, null=True)  # Field name made lowercase.
#     vocab_val = models.CharField(db_column='VOCAB_VAL', max_length=64, blank=True, null=True)  # Field name made lowercase.
#     item_ent = models.ForeignKey('ItemEnt', models.DO_NOTHING, db_column='ITEM_ENT_ID', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'ITEM_ATTRIB'
#
#
# class ItemEnt(models.Model):
#     item_ent_id = models.AutoField(db_column='ITEM_ENT_ID', primary_key=True)  # Field name made lowercase.
#     item_ent_version = models.IntegerField(db_column='ITEM_ENT_VERSION', blank=True, null=True)  # Field name made lowercase.
#     item_ent_uri = models.CharField(db_column='ITEM_ENT_URI', max_length=512, blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'ITEM_ENT'
#
#
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
