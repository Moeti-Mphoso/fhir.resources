# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/EnrollmentRequest
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""


import sys

from . import domainresource


class EnrollmentRequest(domainresource.DomainResource):
    """ Enrollment request.

    This resource provides the insurance enrollment details to the insurer
    regarding a specified coverage.
    """

    resource_type = "EnrollmentRequest"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.coverage = None
        """ Insurance information.
        Type `FHIRReference` referencing `['Coverage']` (represented as `dict` in JSON). """

        self.created = None
        """ Creation date.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.identifier = None
        """ Business Identifier.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.insurer = None
        """ Target.
        Type `FHIRReference` referencing `['Organization']` (represented as `dict` in JSON). """

        self.organization = None
        """ Responsible organization.
        Type `FHIRReference` referencing `['Organization']` (represented as `dict` in JSON). """

        self.provider = None
        """ Responsible practitioner.
        Type `FHIRReference` referencing `['Practitioner']` (represented as `dict` in JSON). """

        self.status = None
        """ active | cancelled | draft | entered-in-error.
        Type `str`. """

        self.subject = None
        """ The subject of the Products and Services.
        Type `FHIRReference` referencing `['Patient']` (represented as `dict` in JSON). """

        super(EnrollmentRequest, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(EnrollmentRequest, self).elementProperties()
        js.extend(
            [
                (
                    "coverage",
                    "coverage",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                (
                    "created",
                    "created",
                    fhirdate.FHIRDate,
                    "dateTime",
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
                (
                    "insurer",
                    "insurer",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                (
                    "organization",
                    "organization",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                (
                    "provider",
                    "provider",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                ("status", "status", str, "code", False, None, False),
                (
                    "subject",
                    "subject",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
            ]
        )
        return js


try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + ".fhirdate"]
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + ".fhirreference"]
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + ".identifier"]
