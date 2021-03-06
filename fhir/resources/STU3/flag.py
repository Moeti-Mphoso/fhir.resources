# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Flag
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""


import sys

from . import domainresource


class Flag(domainresource.DomainResource):
    """ Key information to flag to healthcare providers.

    Prospective warnings of potential issues when providing care to the
    patient.
    """

    resource_type = "Flag"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.author = None
        """ Flag creator.
        Type `FHIRReference` referencing `['Device'], ['Organization'], ['Patient'], ['Practitioner']` (represented as `dict` in JSON). """

        self.category = None
        """ Clinical, administrative, etc..
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.code = None
        """ Coded or textual message to display to user.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.encounter = None
        """ Alert relevant during encounter.
        Type `FHIRReference` referencing `['Encounter']` (represented as `dict` in JSON). """

        self.identifier = None
        """ Business identifier.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.period = None
        """ Time period when flag is active.
        Type `Period` (represented as `dict` in JSON). """

        self.status = None
        """ active | inactive | entered-in-error.
        Type `str`. """

        self.subject = None
        """ Who/What is flag about?.
        Type `FHIRReference` referencing `['Patient'], ['Location'], ['Group'], ['Organization'], ['Practitioner'], ['PlanDefinition'], ['Medication'], ['Procedure']` (represented as `dict` in JSON). """

        super(Flag, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Flag, self).elementProperties()
        js.extend(
            [
                (
                    "author",
                    "author",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                (
                    "category",
                    "category",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                (
                    "code",
                    "code",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    True,
                ),
                (
                    "encounter",
                    "encounter",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                (
                    "identifier",
                    "identifier",
                    identifier.Identifier,
                    "Identifier",
                    True,
                    None,
                    False,
                ),
                ("period", "period", period.Period, "Period", False, None, False),
                ("status", "status", str, "code", False, None, True),
                (
                    "subject",
                    "subject",
                    fhirreference.FHIRReference,
                    "Reference",
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
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + ".identifier"]
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + ".period"]
