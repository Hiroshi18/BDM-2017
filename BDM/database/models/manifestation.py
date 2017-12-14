# Standard Library
from datetime import date

# Django
from django.db import models

# Local Django
from database.models import ExprEnt


class ManifEnt(models.Model):
    identifier = models.CharField(max_length=1000, blank=True, null=True)
    titleOfTheManifestation = models.CharField(max_length=1000, blank=True, null=True)
    statementOfResponsibility = models.CharField(max_length=1000, blank=True, null=True)
    editionIssueDesignation = models.CharField(max_length=1000, blank=True, null=True)
    placeOfPublicationDistribution = models.CharField(max_length=1000, blank=True, null=True)
    publisherDistributor = models.CharField(max_length=1000, blank=True, null=True)
    dateOfPublicationDistribution = models.DateField(blank=False, default=date.today)
    fabricatorManufacturer = models.CharField(max_length=1000, blank=True, null=True)
    seriesStatement = models.CharField(max_length=1000, blank=True, null=True)
    formOfCarrier = models.CharField(max_length=1000, blank=True, null=True)
    extentOfTheCarrier = models.CharField(max_length=1000, blank=True, null=True)
    physicalMedium = models.CharField(max_length=1000, blank=True, null=True)
    captureMode = models.CharField(max_length=1000, blank=True, null=True)
    dimensionsOfTheCarrier = models.CharField(max_length=1000, blank=True, null=True)
    manifestationIdentifier = models.CharField(max_length=1000, blank=True, null=True)
    sourceForAcquisitionAccessAuthorization = models.CharField(max_length=1000, blank=True, null=True)
    termsOfAvailability = models.CharField(max_length=1000, blank=True, null=True)
    accessRestrictionsOnTheManifestation = models.CharField(max_length=1000, blank=True, null=True)
    typeface = models.CharField(max_length=1000, blank=True, null=True)
    typeSize = models.CharField(max_length=1000, blank=True, null=True)
    foliation = models.CharField(max_length=1000, blank=True, null=True)
    collation = models.CharField(max_length=1000, blank=True, null=True)
    publicationStatus = models.CharField(max_length=1000, blank=True, null=True)
    numbering = models.CharField(max_length=1000, blank=True, null=True)
    playingSpeed = models.CharField(max_length=1000, blank=True, null=True)
    grooveWidth = models.CharField(max_length=1000, blank=True, null=True)
    kindOfCutting = models.CharField(max_length=1000, blank=True, null=True)
    tapeConfiguration = models.CharField(max_length=1000, blank=True, null=True)
    kindOfSound = models.CharField(max_length=1000, blank=True, null=True)
    specialReproductionCharacteristic = models.CharField(max_length=1000, blank=True, null=True)
    colour = models.CharField(max_length=1000, blank=True, null=True)
    reductionRatio = models.CharField(max_length=1000, blank=True, null=True)
    polarity = models.CharField(max_length=1000, blank=True, null=True)
    generation = models.CharField(max_length=1000, blank=True, null=True)
    presentationFormat = models.CharField(max_length=1000, blank=True, null=True)
    systemRequirements = models.CharField(max_length=1000, blank=True, null=True)
    fileCharacteristics = models.CharField(max_length=1000, blank=True, null=True)
    modeOfAccess = models.CharField(max_length=1000, blank=True, null=True)
    accessAddress = models.CharField(max_length=1000, blank=True, null=True)
    relatedExprEnt = models.ForeignKey(ExprEnt, related_name="relatedExprEnt")

    def __unicode__(self):
        return '%s' % self.titleOfTheManifestation

    def __str__(self):
        return '%s' % self.titleOfTheManifestation

# class ManifPub(models.Model):
#     manif_pub_id = models.AutoField(db_column='MANIF_PUB_ID', primary_key=True)  # Field name made lowercase.
#     manif_ent_id = models.IntegerField(db_column='MANIF_ENT_ID')  # Field name made lowercase.
#     manif_pub_version = models.IntegerField(db_column='MANIF_PUB_VERSION', blank=True, null=True)  # Field name made lowercase.
#     manif_pub_list_order = models.IntegerField(db_column='MANIF_PUB_LIST_ORDER', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'MANIF_PUB'
#
#
# class ManifPubAttrib(models.Model):
#     manif_pub_attrib_id = models.AutoField(db_column='MANIF_PUB_ATTRIB_ID', primary_key=True)  # Field name made lowercase.
#     manif_pub_attrib_version = models.IntegerField(db_column='MANIF_PUB_ATTRIB_VERSION', blank=True, null=True)  # Field name made lowercase.
#     manif_pub_attrib_class = models.CharField(db_column='MANIF_PUB_ATTRIB_CLASS', max_length=64, blank=True, null=True)  # Field name made lowercase.
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
#     manif_pub = models.ForeignKey('ManifPub', models.DO_NOTHING, db_column='MANIF_PUB_ID', blank=True, null=True)  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'MANIF_PUB_ATTRIB'
#
#
# class Manif2Item(models.Model):
#     manif2item_id = models.AutoField(db_column='MANIF2ITEM_ID', primary_key=True)  # Field name made lowercase.
#     manif2item_version = models.IntegerField(db_column='MANIF2ITEM_VERSION', blank=True, null=True)  # Field name made lowercase.
#     rel_type = models.CharField(db_column='REL_TYPE', max_length=32, blank=True, null=True)  # Field name made lowercase.
#     rel_role = models.CharField(db_column='REL_ROLE', max_length=32, blank=True, null=True)  # Field name made lowercase.
#     rel_category = models.CharField(db_column='REL_CATEGORY', max_length=32, blank=True, null=True)  # Field name made lowercase.
#     rel_list_order = models.IntegerField(db_column='REL_LIST_ORDER', blank=True, null=True)  # Field name made lowercase.
#     source_manif = models.ForeignKey('ManifEnt', models.DO_NOTHING, db_column='SOURCE_MANIF_ID')  # Field name made lowercase.
#     target_item = models.ForeignKey('ItemEnt', models.DO_NOTHING, db_column='TARGET_ITEM_ID')  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'MANIF2ITEM'
#
#
# class Manif2Manif(models.Model):
#     manif2manif_id = models.AutoField(db_column='MANIF2MANIF_ID', primary_key=True)  # Field name made lowercase.
#     manif2manif_version = models.IntegerField(db_column='MANIF2MANIF_VERSION', blank=True, null=True)  # Field name made lowercase.
#     rel_type = models.CharField(db_column='REL_TYPE', max_length=32, blank=True, null=True)  # Field name made lowercase.
#     rel_role = models.CharField(db_column='REL_ROLE', max_length=32, blank=True, null=True)  # Field name made lowercase.
#     rel_category = models.CharField(db_column='REL_CATEGORY', max_length=32, blank=True, null=True)  # Field name made lowercase.
#     rel_list_order = models.IntegerField(db_column='REL_LIST_ORDER', blank=True, null=True)  # Field name made lowercase.
#     source_manif = models.ForeignKey('ManifEnt', models.DO_NOTHING, db_column='SOURCE_MANIF_ID')  # Field name made lowercase.
#     target_manif = models.ForeignKey('ManifEnt', models.DO_NOTHING, db_column='TARGET_MANIF_ID')  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'MANIF2MANIF'
#
#
# class Manif2Respon(models.Model):
#     manif2respon_id = models.AutoField(db_column='MANIF2RESPON_ID', primary_key=True)  # Field name made lowercase.
#     manif2respon_version = models.IntegerField(db_column='MANIF2RESPON_VERSION', blank=True, null=True)  # Field name made lowercase.
#     rel_class = models.CharField(db_column='REL_CLASS', max_length=256, blank=True, null=True)  # Field name made lowercase.
#     rel_type = models.CharField(db_column='REL_TYPE', max_length=32, blank=True, null=True)  # Field name made lowercase.
#     rel_role = models.CharField(db_column='REL_ROLE', max_length=32, blank=True, null=True)  # Field name made lowercase.
#     rel_category = models.CharField(db_column='REL_CATEGORY', max_length=32, blank=True, null=True)  # Field name made lowercase.
#     rel_list_order = models.IntegerField(db_column='REL_LIST_ORDER', blank=True, null=True)  # Field name made lowercase.
#     source_manif = models.ForeignKey('ManifEnt', models.DO_NOTHING, db_column='SOURCE_MANIF_ID')  # Field name made lowercase.
#     target_respon = models.ForeignKey('ResponEnt', models.DO_NOTHING, db_column='TARGET_RESPON_ID')  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'MANIF2RESPON'
#
