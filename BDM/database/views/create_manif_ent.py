# Django
from django.views.generic import CreateView
from django.urls import reverse
from django.http import HttpResponseRedirect

# Local Django
from database.forms import CreateManifEntForm
from database.models import ManifEnt, ExprEnt


class CreateManifEntView(CreateView):
    template_name = 'create_manif_ent.html'
    sucesss_url = 'create_manif_ent.html'
    form_class = CreateManifEntForm

    def get_success_url(self):
        return reverse('create_manif_ent')

    def form_valid(self, form):
        identifier = form.cleaned_data['identifier']
        titleOfTheManifestation = form.cleaned_data['titleOfTheManifestation']
        statementOfResponsibility = form.cleaned_data['statementOfResponsibility']
        editionIssueDesignation = form.cleaned_data['editionIssueDesignation']
        placeOfPublicationDistribution = form.cleaned_data['placeOfPublicationDistribution']
        publisherDistributor = form.cleaned_data['publisherDistributor']
        dateOfPublicationDistribution = form.cleaned_data['dateOfPublicationDistribution']
        fabricatorManufacturer = form.cleaned_data['fabricatorManufacturer']
        seriesStatement = form.cleaned_data['seriesStatement']
        formOfCarrier = form.cleaned_data['formOfCarrier']
        extentOfTheCarrier = form.cleaned_data['extentOfTheCarrier']
        physicalMedium = form.cleaned_data['physicalMedium']
        captureMode = form.cleaned_data['captureMode']
        dimensionsOfTheCarrier = form.cleaned_data['dimensionsOfTheCarrier']
        manifestationIdentifier = form.cleaned_data['manifestationIdentifier']
        sourceForAcquisitionAccessAuthorization = form.cleaned_data['sourceForAcquisitionAccessAuthorization']
        termsOfAvailability = form.cleaned_data['termsOfAvailability']
        accessRestrictionsOnTheManifestation = form.cleaned_data['accessRestrictionsOnTheManifestation']
        typeface = form.cleaned_data['typeface']
        typeSize = form.cleaned_data['typeSize']
        foliation = form.cleaned_data['foliation']
        collation = form.cleaned_data['collation']
        publicationStatus = form.cleaned_data['publicationStatus']
        numbering = form.cleaned_data['numbering']
        playingSpeed = form.cleaned_data['playingSpeed']
        grooveWidth = form.cleaned_data['grooveWidth']
        kindOfCutting = form.cleaned_data['kindOfCutting']
        tapeConfiguration = form.cleaned_data['tapeConfiguration']
        kindOfSound = form.cleaned_data['kindOfSound']
        specialReproductionCharacteristic = form.cleaned_data['specialReproductionCharacteristic']
        colour = form.cleaned_data['colour']
        reductionRatio = form.cleaned_data['reductionRatio']
        polarity = form.cleaned_data['polarity']
        generation = form.cleaned_data['generation']
        presentationFormat = form.cleaned_data['presentationFormat']
        systemRequirements = form.cleaned_data['systemRequirements']
        fileCharacteristics = form.cleaned_data['fileCharacteristics']
        modeOfAccess = form.cleaned_data['modeOfAccess']
        accessAddress = form.cleaned_data['accessAddress']
        relatedExprEnt = form.cleaned_data['relatedExprEnt']

        manif = ManifEnt()
        manif.identifier = identifier
        manif.titleOfTheManifestation = titleOfTheManifestation
        manif.statementOfResponsibility = statementOfResponsibility
        manif.editionIssueDesignation = editionIssueDesignation
        manif.placeOfPublicationDistribution = placeOfPublicationDistribution
        manif.publisherDistributor = publisherDistributor
        manif.dateOfPublicationDistribution = dateOfPublicationDistribution
        manif.fabricatorManufacturer = fabricatorManufacturer
        manif.seriesStatement = seriesStatement
        manif.formOfCarrier = formOfCarrier
        manif.extentOfTheCarrier = extentOfTheCarrier
        manif.physicalMedium = physicalMedium
        manif.captureMode = captureMode
        manif.dimensionsOfTheCarrier = dimensionsOfTheCarrier
        manif.manifestationIdentifier = manifestationIdentifier
        manif.sourceForAcquisitionAccessAuthorization = sourceForAcquisitionAccessAuthorization
        manif.termsOfAvailability = termsOfAvailability
        manif.accessRestrictionsOnTheManifestation = accessRestrictionsOnTheManifestation
        manif.typeface = typeface
        manif.typeSize = typeSize
        manif.foliation = foliation
        manif.collation = collation
        manif.publicationStatus = publicationStatus
        manif.numbering = numbering
        manif.playingSpeed = playingSpeed
        manif.grooveWidth = grooveWidth
        manif.kindOfCutting = kindOfCutting
        manif.tapeConfiguration = tapeConfiguration
        manif.kindOfSound = kindOfSound
        manif.specialReproductionCharacteristic = specialReproductionCharacteristic
        manif.colour = colour
        manif.reductionRatio = reductionRatio
        manif.polarity = polarity
        manif.generation = generation
        manif.presentationFormat = presentationFormat
        manif.systemRequirements = systemRequirements
        manif.fileCharacteristics = fileCharacteristics
        manif.modeOfAccess = modeOfAccess
        manif.accessAddress = accessAddress
        manif.relatedExprEnt = relatedExprEnt
        manif.save()

        expr = ExprEnt.objects.get(pk=manif.relatedExprEnt.pk)
        expr.relatedManifList.add(manif)

        return HttpResponseRedirect(reverse('create_manif_ent'))
