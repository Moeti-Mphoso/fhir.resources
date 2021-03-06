# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/DetectedIssue
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""


import sys

from . import backboneelement, domainresource


class DetectedIssue(domainresource.DomainResource):
    """ Clinical issue with action.

    Indicates an actual or potential clinical issue with or between one or more
    active or proposed clinical actions for a patient; e.g. Drug-drug
    interaction, Ineffective treatment frequency, Procedure-condition conflict,
    etc.
    """

    resource_type = "DetectedIssue"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.author = None
        """ The provider or device that identified the issue.
        Type `FHIRReference` referencing `['Practitioner'], ['Device']` (represented as `dict` in JSON). """

        self.category = None
        """ Issue Category, e.g. drug-drug, duplicate therapy, etc..
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.date = None
        """ When identified.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.detail = None
        """ Description and context.
        Type `str`. """

        self.identifier = None
        """ Unique id for the detected issue.
        Type `Identifier` (represented as `dict` in JSON). """

        self.implicated = None
        """ Problem resource.
        List of `FHIRReference` items referencing `['Resource']` (represented as `dict` in JSON). """

        self.mitigation = None
        """ Step taken to address.
        List of `DetectedIssueMitigation` items (represented as `dict` in JSON). """

        self.patient = None
        """ Associated patient.
        Type `FHIRReference` referencing `['Patient']` (represented as `dict` in JSON). """

        self.reference = None
        """ Authority for issue.
        Type `str`. """

        self.severity = None
        """ high | moderate | low.
        Type `str`. """

        self.status = None
        """ registered | preliminary | final | amended +.
        Type `str`. """

        super(DetectedIssue, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(DetectedIssue, self).elementProperties()
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
                ("date", "date", fhirdate.FHIRDate, "dateTime", False, None, False),
                ("detail", "detail", str, "string", False, None, False),
                (
                    "identifier",
                    "identifier",
                    identifier.Identifier,
                    "Identifier",
                    False,
                    None,
                    False,
                ),
                (
                    "implicated",
                    "implicated",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
                (
                    "mitigation",
                    "mitigation",
                    DetectedIssueMitigation,
                    "DetectedIssueMitigation",
                    True,
                    None,
                    False,
                ),
                (
                    "patient",
                    "patient",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                ("reference", "reference", str, "uri", False, None, False),
                ("severity", "severity", str, "code", False, None, False),
                ("status", "status", str, "code", False, None, True),
            ]
        )
        return js


class DetectedIssueMitigation(backboneelement.BackboneElement):
    """ Step taken to address.

    Indicates an action that has been taken or is committed to to reduce or
    eliminate the likelihood of the risk identified by the detected issue from
    manifesting.  Can also reflect an observation of known mitigating factors
    that may reduce/eliminate the need for any action.
    """

    resource_type = "DetectedIssueMitigation"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.action = None
        """ What mitigation?.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.author = None
        """ Who is committing?.
        Type `FHIRReference` referencing `['Practitioner']` (represented as `dict` in JSON). """

        self.date = None
        """ Date committed.
        Type `FHIRDate` (represented as `str` in JSON). """

        super(DetectedIssueMitigation, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(DetectedIssueMitigation, self).elementProperties()
        js.extend(
            [
                (
                    "action",
                    "action",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    True,
                ),
                (
                    "author",
                    "author",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                ("date", "date", fhirdate.FHIRDate, "dateTime", False, None, False),
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
