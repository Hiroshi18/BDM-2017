# Django
from django.db import models

# Local Django


class ExprEnt(models.Model):
    identifier = models.CharField(max_length=1000, blank=True, null=True)
    titleOfTheExpression = models.CharField(max_length=1000, blank=True, null=True)
    formOfExpression = models.CharField(max_length=1000, blank=True, null=True)
    dateOfExpression = models.CharField(max_length=1000, blank=True, null=True)
    languageOfExpression = models.CharField(max_length=1000, blank=True, null=True)
    otherDistinguishingCharacteristic = models.CharField(max_length=1000, blank=True, null=True)
    extensibilityOfExpression = models.CharField(max_length=1000, blank=True, null=True)
    revisabilityOfExpression = models.CharField(max_length=1000, blank=True, null=True)
    extentOfTheExpression = models.CharField(max_length=1000, blank=True, null=True)
    summarizationOfContent = models.CharField(max_length=1000, blank=True, null=True)
    contextForTheExpression = models.CharField(max_length=1000, blank=True, null=True)
    criticalResponseToTheExpression = models.CharField(max_length=1000, blank=True, null=True)
    useRestrictionsOnTheExpression = models.CharField(max_length=1000, blank=True, null=True)
    sequencingPattern = models.CharField(max_length=1000, blank=True, null=True)
    expectedRegularityOfIssue = models.CharField(max_length=1000, blank=True, null=True)
    expectedFrequencyOfIssue = models.CharField(max_length=1000, blank=True, null=True)
    typeOfScore = models.CharField(max_length=1000, blank=True, null=True)
    mediumOfPerformance = models.CharField(max_length=1000, blank=True, null=True)
    scale = models.CharField(max_length=1000, blank=True, null=True)
    projection = models.CharField(max_length=1000, blank=True, null=True)
    presentationTechnique = models.CharField(max_length=1000, blank=True, null=True)
    representationOfRelief = models.CharField(max_length=1000, blank=True, null=True)
    geodeticGridAndVerticalMeasurement = models.CharField(max_length=1000, blank=True, null=True)
    recordingTechnique = models.CharField(max_length=1000, blank=True, null=True)
    specialCharacteristic = models.CharField(max_length=1000, blank=True, null=True)
    technique = models.CharField(max_length=1000, blank=True, null=True)


#
#
# class Expr2Expr(models.Model):
#     expr2expr_id = models.AutoField(db_column='EXPR2EXPR_ID', primary_key=True)  # Field name made lowercase.
#     expr2expr_version = models.IntegerField(db_column='EXPR2EXPR_VERSION', blank=True, null=True)  # Field name made lowercase.
#     rel_type = models.CharField(db_column='REL_TYPE', max_length=32, blank=True, null=True)  # Field name made lowercase.
#     rel_role = models.CharField(db_column='REL_ROLE', max_length=32, blank=True, null=True)  # Field name made lowercase.
#     rel_category = models.CharField(db_column='REL_CATEGORY', max_length=32, blank=True, null=True)  # Field name made lowercase.
#     rel_list_order = models.IntegerField(db_column='REL_LIST_ORDER', blank=True, null=True)  # Field name made lowercase.
#     source_expr = models.ForeignKey('ExprEnt', models.DO_NOTHING, db_column='SOURCE_EXPR_ID')  # Field name made lowercase.
#     target_expr = models.ForeignKey('ExprEnt', models.DO_NOTHING, db_column='TARGET_EXPR_ID')  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'EXPR2EXPR'
#
#
# class Expr2Manif(models.Model):
#     expr2manif_id = models.AutoField(db_column='EXPR2MANIF_ID', primary_key=True)  # Field name made lowercase.
#     expr2manif_version = models.IntegerField(db_column='EXPR2MANIF_VERSION', blank=True, null=True)  # Field name made lowercase.
#     rel_type = models.CharField(db_column='REL_TYPE', max_length=32, blank=True, null=True)  # Field name made lowercase.
#     rel_role = models.CharField(db_column='REL_ROLE', max_length=32, blank=True, null=True)  # Field name made lowercase.
#     rel_category = models.CharField(db_column='REL_CATEGORY', max_length=32, blank=True, null=True)  # Field name made lowercase.
#     rel_list_order = models.IntegerField(db_column='REL_LIST_ORDER', blank=True, null=True)  # Field name made lowercase.
#     source_expr = models.ForeignKey('ExprEnt', models.DO_NOTHING, db_column='SOURCE_EXPR_ID')  # Field name made lowercase.
#     target_manif = models.ForeignKey('ManifEnt', models.DO_NOTHING, db_column='TARGET_MANIF_ID')  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'EXPR2MANIF'
#
#
# class Expr2Respon(models.Model):
#     expr2respon_id = models.AutoField(db_column='EXPR2RESPON_ID', primary_key=True)  # Field name made lowercase.
#     expr2respon_version = models.IntegerField(db_column='EXPR2RESPON_VERSION', blank=True, null=True)  # Field name made lowercase.
#     rel_class = models.CharField(db_column='REL_CLASS', max_length=256, blank=True, null=True)  # Field name made lowercase.
#     rel_type = models.CharField(db_column='REL_TYPE', max_length=32, blank=True, null=True)  # Field name made lowercase.
#     rel_role = models.CharField(db_column='REL_ROLE', max_length=32, blank=True, null=True)  # Field name made lowercase.
#     rel_category = models.CharField(db_column='REL_CATEGORY', max_length=32, blank=True, null=True)  # Field name made lowercase.
#     rel_list_order = models.IntegerField(db_column='REL_LIST_ORDER', blank=True, null=True)  # Field name made lowercase.
#     source_expr = models.ForeignKey('ExprEnt', models.DO_NOTHING, db_column='SOURCE_EXPR_ID')  # Field name made lowercase.
#     target_respon = models.ForeignKey('ResponEnt', models.DO_NOTHING, db_column='TARGET_RESPON_ID')  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'EXPR2RESPON'
#
#
# class Expr2Work(models.Model):
#     expr2work_id = models.AutoField(db_column='EXPR2WORK_ID', primary_key=True)  # Field name made lowercase.
#     expr2work_version = models.IntegerField(db_column='EXPR2WORK_VERSION', blank=True, null=True)  # Field name made lowercase.
#     rel_type = models.CharField(db_column='REL_TYPE', max_length=32, blank=True, null=True)  # Field name made lowercase.
#     rel_role = models.CharField(db_column='REL_ROLE', max_length=32, blank=True, null=True)  # Field name made lowercase.
#     rel_category = models.CharField(db_column='REL_CATEGORY', max_length=32, blank=True, null=True)  # Field name made lowercase.
#     rel_list_order = models.IntegerField(db_column='REL_LIST_ORDER', blank=True, null=True)  # Field name made lowercase.
#     source_expr = models.ForeignKey('ExprEnt', models.DO_NOTHING, db_column='SOURCE_EXPR_ID')  # Field name made lowercase.
#     target_work = models.ForeignKey('WorkEnt', models.DO_NOTHING, db_column='TARGET_WORK_ID')  # Field name made lowercase.
#
#     class Meta:
#         managed = False
#         db_table = 'EXPR2WORK'
