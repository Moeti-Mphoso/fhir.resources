# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MedicinalProductContraindication
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""


import sys

from . import backboneelement, domainresource


class MedicinalProductContraindication(domainresource.DomainResource):
    """ MedicinalProductContraindication.

    The clinical particulars - indications, contraindications etc. of a
    medicinal product, including for regulatory purposes.
    """

    resource_type = "MedicinalProductContraindication"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.comorbidity = None
        """ A comorbidity (concurrent condition) or coinfection.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.disease = None
        """ The disease, symptom or procedure for the contraindication.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.diseaseStatus = None
        """ The status of the disease or symptom for the contraindication.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.otherTherapy = None
        """ Information about the use of the medicinal product in relation to
        other therapies described as part of the indication.
        List of `MedicinalProductContraindicationOtherTherapy` items (represented as `dict` in JSON). """

        self.population = None
        """ The population group to which this applies.
        List of `Population` items (represented as `dict` in JSON). """

        self.subject = None
        """ The medication for which this is an indication.
        List of `FHIRReference` items referencing `['MedicinalProduct', 'Medication']` (represented as `dict` in JSON). """

        self.therapeuticIndication = None
        """ Information about the use of the medicinal product in relation to
        other therapies as part of the indication.
        List of `FHIRReference` items referencing `['MedicinalProductIndication']` (represented as `dict` in JSON). """

        super(MedicinalProductContraindication, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(MedicinalProductContraindication, self).elementProperties()
        js.extend(
            [
                (
                    "comorbidity",
                    "comorbidity",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    True,
                    None,
                    False,
                ),
                (
                    "disease",
                    "disease",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                (
                    "diseaseStatus",
                    "diseaseStatus",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                (
                    "otherTherapy",
                    "otherTherapy",
                    MedicinalProductContraindicationOtherTherapy,
                    "MedicinalProductContraindicationOtherTherapy",
                    True,
                    None,
                    False,
                ),
                (
                    "population",
                    "population",
                    population.Population,
                    "Population",
                    True,
                    None,
                    False,
                ),
                (
                    "subject",
                    "subject",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
                (
                    "therapeuticIndication",
                    "therapeuticIndication",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
            ]
        )
        return js


class MedicinalProductContraindicationOtherTherapy(backboneelement.BackboneElement):
    """ Information about the use of the medicinal product in relation to other
    therapies described as part of the indication.
    """

    resource_type = "MedicinalProductContraindicationOtherTherapy"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.medicationCodeableConcept = None
        """ Reference to a specific medication (active substance, medicinal
        product or class of products) as part of an indication or
        contraindication.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.medicationReference = None
        """ Reference to a specific medication (active substance, medicinal
        product or class of products) as part of an indication or
        contraindication.
        Type `FHIRReference` referencing `['MedicinalProduct', 'Medication', 'Substance', 'SubstanceSpecification']` (represented as `dict` in JSON). """

        self.therapyRelationshipType = None
        """ The type of relationship between the medicinal product indication
        or contraindication and another therapy.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        super(MedicinalProductContraindicationOtherTherapy, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(
            MedicinalProductContraindicationOtherTherapy, self
        ).elementProperties()
        js.extend(
            [
                (
                    "medicationCodeableConcept",
                    "medicationCodeableConcept",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    "medication",
                    True,
                ),
                (
                    "medicationReference",
                    "medicationReference",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    "medication",
                    True,
                ),
                (
                    "therapyRelationshipType",
                    "therapyRelationshipType",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    True,
                ),
            ]
        )
        return js


try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + ".codeableconcept"]
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + ".fhirreference"]
try:
    from . import population
except ImportError:
    population = sys.modules[__package__ + ".population"]
