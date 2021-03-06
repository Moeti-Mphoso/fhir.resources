# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ProcessResponse
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""


import sys

from . import backboneelement, domainresource


class ProcessResponse(domainresource.DomainResource):
    """ ProcessResponse resource.

    This resource provides processing status, errors and notes from the
    processing of a resource.
    """

    resource_type = "ProcessResponse"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.communicationRequest = None
        """ Request for additional information.
        List of `FHIRReference` items referencing `['CommunicationRequest']` (represented as `dict` in JSON). """

        self.created = None
        """ Creation date.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.disposition = None
        """ Disposition Message.
        Type `str`. """

        self.error = None
        """ Error code.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.form = None
        """ Printed Form Identifier.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.identifier = None
        """ Business Identifier.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.organization = None
        """ Authoring Organization.
        Type `FHIRReference` referencing `['Organization']` (represented as `dict` in JSON). """

        self.outcome = None
        """ Processing outcome.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.processNote = None
        """ Processing comments or additional requirements.
        List of `ProcessResponseProcessNote` items (represented as `dict` in JSON). """

        self.request = None
        """ Request reference.
        Type `FHIRReference` referencing `['Resource']` (represented as `dict` in JSON). """

        self.requestOrganization = None
        """ Responsible organization.
        Type `FHIRReference` referencing `['Organization']` (represented as `dict` in JSON). """

        self.requestProvider = None
        """ Responsible Practitioner.
        Type `FHIRReference` referencing `['Practitioner']` (represented as `dict` in JSON). """

        self.status = None
        """ active | cancelled | draft | entered-in-error.
        Type `str`. """

        super(ProcessResponse, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ProcessResponse, self).elementProperties()
        js.extend(
            [
                (
                    "communicationRequest",
                    "communicationRequest",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
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
                ("disposition", "disposition", str, "string", False, None, False),
                (
                    "error",
                    "error",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    True,
                    None,
                    False,
                ),
                (
                    "form",
                    "form",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
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
                    "organization",
                    "organization",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                (
                    "outcome",
                    "outcome",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                (
                    "processNote",
                    "processNote",
                    ProcessResponseProcessNote,
                    "ProcessResponseProcessNote",
                    True,
                    None,
                    False,
                ),
                (
                    "request",
                    "request",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                (
                    "requestOrganization",
                    "requestOrganization",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                (
                    "requestProvider",
                    "requestProvider",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                ("status", "status", str, "code", False, None, False),
            ]
        )
        return js


class ProcessResponseProcessNote(backboneelement.BackboneElement):
    """ Processing comments or additional requirements.

    Suite of processing notes or additional requirements if the processing has
    been held.
    """

    resource_type = "ProcessResponseProcessNote"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.text = None
        """ Comment on the processing.
        Type `str`. """

        self.type = None
        """ display | print | printoper.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        super(ProcessResponseProcessNote, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(ProcessResponseProcessNote, self).elementProperties()
        js.extend(
            [
                ("text", "text", str, "string", False, None, False),
                (
                    "type",
                    "type",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
            ]
        )
        return js


try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + ".codeableconcept"]
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
