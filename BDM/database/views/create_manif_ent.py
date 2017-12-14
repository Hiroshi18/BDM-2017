# Django
from django.views.generic import CreateView
from django.urls import reverse

# Local Django
from database.models import ManifEnt


class CreateManifEntView(CreateView):
    template_name = 'create_manif_ent.html'
    sucesss_url = 'create_manif_ent.html'
    model = ManifEnt
    fields = (
                'identifier',
                'titleOfTheManifestation',
                'statementOfResponsibility',
                'editionIssueDesignation',
                'placeOfPublicationDistribution',
                'publisherDistributor',
                'dateOfPublicationDistribution',
                'fabricatorManufacturer',
                'seriesStatement',
                'formOfCarrier',
                'extentOfTheCarrier',
                'physicalMedium',
                'captureMode',
                'dimensionsOfTheCarrier',
                'manifestationIdentifier',
                'sourceForAcquisitionAccessAuthorization',
                'termsOfAvailability',
                'accessRestrictionsOnTheManifestation',
                'typeface',
                'typeSize',
                'foliation',
                'collation',
                'publicationStatus',
                'numbering',
                'playingSpeed',
                'grooveWidth',
                'kindOfCutting',
                'tapeConfiguration',
                'kindOfSound',
                'specialReproductionCharacteristic',
                'colour',
                'reductionRatio',
                'polarity',
                'generation',
                'presentationFormat',
                'systemRequirements',
                'fileCharacteristics',
                'modeOfAccess',
                'accessAddress',
                'relatedExprEnt',
        )

    def get_success_url(self):
        return reverse('create_manif_ent')