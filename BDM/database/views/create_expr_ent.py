# Django
from django.views.generic import CreateView
from django.urls import reverse
from django.http import HttpResponseRedirect

# Local Django
from database.models import ExprEnt, WorkEnt
from database.forms import CreateExprEntForm


class CreateExprEntView(CreateView):
    template_name = 'create_expr_ent.html'
    sucesss_url = 'create_expr_ent.html'
    form_class = CreateExprEntForm

    def get_success_url(self):
        return reverse('create_expr_ent')

    def form_valid(self, form):
        identifier = form.cleaned_data['identifier']
        titleOfTheExpression = form.cleaned_data['titleOfTheExpression']
        formOfExpression = form.cleaned_data['formOfExpression']
        dateOfExpression = form.cleaned_data['dateOfExpression']
        languageOfExpression = form.cleaned_data['languageOfExpression']
        otherDistinguishingCharacteristic = form.cleaned_data['otherDistinguishingCharacteristic']
        extensibilityOfExpression = form.cleaned_data['extensibilityOfExpression']
        revisabilityOfExpression = form.cleaned_data['revisabilityOfExpression']
        extentOfTheExpression = form.cleaned_data['extentOfTheExpression']
        summarizationOfContent = form.cleaned_data['summarizationOfContent']
        contextForTheExpression = form.cleaned_data['contextForTheExpression']
        criticalResponseToTheExpression = form.cleaned_data['criticalResponseToTheExpression']
        useRestrictionsOnTheExpression = form.cleaned_data['useRestrictionsOnTheExpression']
        sequencingPattern = form.cleaned_data['sequencingPattern']
        expectedRegularityOfIssue = form.cleaned_data['expectedRegularityOfIssue']
        expectedFrequencyOfIssue = form.cleaned_data['expectedFrequencyOfIssue']
        typeOfScore = form.cleaned_data['typeOfScore']
        mediumOfPerformance = form.cleaned_data['mediumOfPerformance']
        scale = form.cleaned_data['scale']
        projection = form.cleaned_data['projection']
        presentationTechnique = form.cleaned_data['presentationTechnique']
        representationOfRelief = form.cleaned_data['representationOfRelief']
        geodeticGridAndVerticalMeasurement = form.cleaned_data['geodeticGridAndVerticalMeasurement']
        recordingTechnique = form.cleaned_data['recordingTechnique']
        specialCharacteristic = form.cleaned_data['specialCharacteristic']
        technique = form.cleaned_data['technique']
        relatedWorkEnt = form.cleaned_data['relatedWorkEnt']

        expr = ExprEnt()
        expr.identifier = identifier
        expr.titleOfTheExpression = titleOfTheExpression
        expr.formOfExpression = formOfExpression
        expr.dateOfExpression = dateOfExpression
        expr.languageOfExpression = languageOfExpression
        expr.otherDistinguishingCharacteristic = otherDistinguishingCharacteristic
        expr.extensibilityOfExpression = extensibilityOfExpression
        expr.revisabilityOfExpression = revisabilityOfExpression
        expr.extentOfTheExpression = extentOfTheExpression
        expr.summarizationOfContent = summarizationOfContent
        expr.contextForTheExpression = contextForTheExpression
        expr.criticalResponseToTheExpression = criticalResponseToTheExpression
        expr.useRestrictionsOnTheExpression = useRestrictionsOnTheExpression
        expr.sequencingPattern = sequencingPattern
        expr.expectedRegularityOfIssue = expectedRegularityOfIssue
        expr.expectedFrequencyOfIssue = expectedFrequencyOfIssue
        expr.typeOfScore = typeOfScore
        expr.mediumOfPerformance = mediumOfPerformance
        expr.scale = scale
        expr.projection = projection
        expr.presentationTechnique = presentationTechnique
        expr.representationOfRelief = representationOfRelief
        expr.geodeticGridAndVerticalMeasurement = geodeticGridAndVerticalMeasurement
        expr.recordingTechnique = recordingTechnique
        expr.specialCharacteristic = specialCharacteristic
        expr.technique = technique
        expr.relatedWorkEnt = relatedWorkEnt
        expr.save()

        work = WorkEnt.objects.get(pk=expr.relatedWorkEnt.pk)
        work.relatedExprList.add(expr)

        return HttpResponseRedirect(reverse('create_expr_ent'))
