# Django
from django.views.generic import CreateView
from django.urls import reverse

# Local Django
from database.models import ExprEnt


class CreateExprEntView(CreateView):
    template_name = 'create_expr_ent.html'
    sucesss_url = 'create_expr_ent.html'
    model = ExprEnt
    fields = (    
                'identifier',
                'titleOfTheExpression',
                'formOfExpression',
                'dateOfExpression',
                'languageOfExpression',
                'otherDistinguishingCharacteristic',
                'extensibilityOfExpression',
                'revisabilityOfExpression',
                'extentOfTheExpression',
                'summarizationOfContent',
                'contextForTheExpression',
                'criticalResponseToTheExpression',
                'useRestrictionsOnTheExpression',
                'sequencingPattern',
                'expectedRegularityOfIssue',
                'expectedFrequencyOfIssue',
                'typeOfScore',
                'mediumOfPerformance',
                'scale',
                'projection',
                'presentationTechnique',
                'representationOfRelief',
                'geodeticGridAndVerticalMeasurement',
                'recordingTechnique',
                'specialCharacteristic',
                'technique',
                'relatedWorkEnt'
            )
    

    def get_success_url(self):
        return reverse('create_expr_ent')