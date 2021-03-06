# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/DeviceRequest
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""


import sys

from . import backboneelement, domainresource


class DeviceRequest(domainresource.DomainResource):
    """ Medical device request.

    Represents a request for a patient to employ a medical device. The device
    may be an implantable device, or an external assistive device, such as a
    walker.
    """

    resource_type = "DeviceRequest"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.authoredOn = None
        """ When recorded.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.basedOn = None
        """ What request fulfills.
        List of `FHIRReference` items referencing `['Resource']` (represented as `dict` in JSON). """

        self.codeCodeableConcept = None
        """ Device requested.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.codeReference = None
        """ Device requested.
        Type `FHIRReference` referencing `['Device']` (represented as `dict` in JSON). """

        self.encounter = None
        """ Encounter motivating request.
        Type `FHIRReference` referencing `['Encounter']` (represented as `dict` in JSON). """

        self.groupIdentifier = None
        """ Identifier of composite request.
        Type `Identifier` (represented as `dict` in JSON). """

        self.identifier = None
        """ External Request identifier.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.instantiatesCanonical = None
        """ Instantiates FHIR protocol or definition.
        List of `str` items referencing `['ActivityDefinition', 'PlanDefinition']`. """

        self.instantiatesUri = None
        """ Instantiates external protocol or definition.
        List of `str` items. """

        self.insurance = None
        """ Associated insurance coverage.
        List of `FHIRReference` items referencing `['Coverage', 'ClaimResponse']` (represented as `dict` in JSON). """

        self.intent = None
        """ proposal | plan | directive | order | original-order | reflex-order
        | filler-order | instance-order | option.
        Type `str`. """

        self.note = None
        """ Notes or comments.
        List of `Annotation` items (represented as `dict` in JSON). """

        self.occurrenceDateTime = None
        """ Desired time or schedule for use.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.occurrencePeriod = None
        """ Desired time or schedule for use.
        Type `Period` (represented as `dict` in JSON). """

        self.occurrenceTiming = None
        """ Desired time or schedule for use.
        Type `Timing` (represented as `dict` in JSON). """

        self.parameter = None
        """ Device details.
        List of `DeviceRequestParameter` items (represented as `dict` in JSON). """

        self.performer = None
        """ Requested Filler.
        Type `FHIRReference` referencing `['Practitioner', 'PractitionerRole', 'Organization', 'CareTeam', 'HealthcareService', 'Patient', 'Device', 'RelatedPerson']` (represented as `dict` in JSON). """

        self.performerType = None
        """ Filler role.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.priorRequest = None
        """ What request replaces.
        List of `FHIRReference` items referencing `['Resource']` (represented as `dict` in JSON). """

        self.priority = None
        """ routine | urgent | asap | stat.
        Type `str`. """

        self.reasonCode = None
        """ Coded Reason for request.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.reasonReference = None
        """ Linked Reason for request.
        List of `FHIRReference` items referencing `['Condition', 'Observation', 'DiagnosticReport', 'DocumentReference']` (represented as `dict` in JSON). """

        self.relevantHistory = None
        """ Request provenance.
        List of `FHIRReference` items referencing `['Provenance']` (represented as `dict` in JSON). """

        self.requester = None
        """ Who/what is requesting diagnostics.
        Type `FHIRReference` referencing `['Device', 'Practitioner', 'PractitionerRole', 'Organization']` (represented as `dict` in JSON). """

        self.status = None
        """ draft | active | on-hold | revoked | completed | entered-in-error |
        unknown.
        Type `str`. """

        self.subject = None
        """ Focus of request.
        Type `FHIRReference` referencing `['Patient', 'Group', 'Location', 'Device']` (represented as `dict` in JSON). """

        self.supportingInfo = None
        """ Additional clinical information.
        List of `FHIRReference` items referencing `['Resource']` (represented as `dict` in JSON). """

        super(DeviceRequest, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(DeviceRequest, self).elementProperties()
        js.extend(
            [
                (
                    "authoredOn",
                    "authoredOn",
                    fhirdate.FHIRDate,
                    "dateTime",
                    False,
                    None,
                    False,
                ),
                (
                    "basedOn",
                    "basedOn",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
                (
                    "codeCodeableConcept",
                    "codeCodeableConcept",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    "code",
                    True,
                ),
                (
                    "codeReference",
                    "codeReference",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    "code",
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
                    "groupIdentifier",
                    "groupIdentifier",
                    identifier.Identifier,
                    "Identifier",
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
                    "instantiatesCanonical",
                    "instantiatesCanonical",
                    str,
                    "canonical",
                    True,
                    None,
                    False,
                ),
                ("instantiatesUri", "instantiatesUri", str, "uri", True, None, False),
                (
                    "insurance",
                    "insurance",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
                ("intent", "intent", str, "code", False, None, True),
                (
                    "note",
                    "note",
                    annotation.Annotation,
                    "Annotation",
                    True,
                    None,
                    False,
                ),
                (
                    "occurrenceDateTime",
                    "occurrenceDateTime",
                    fhirdate.FHIRDate,
                    "dateTime",
                    False,
                    "occurrence",
                    False,
                ),
                (
                    "occurrencePeriod",
                    "occurrencePeriod",
                    period.Period,
                    "Period",
                    False,
                    "occurrence",
                    False,
                ),
                (
                    "occurrenceTiming",
                    "occurrenceTiming",
                    timing.Timing,
                    "Timing",
                    False,
                    "occurrence",
                    False,
                ),
                (
                    "parameter",
                    "parameter",
                    DeviceRequestParameter,
                    "DeviceRequestParameter",
                    True,
                    None,
                    False,
                ),
                (
                    "performer",
                    "performer",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                (
                    "performerType",
                    "performerType",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                (
                    "priorRequest",
                    "priorRequest",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
                ("priority", "priority", str, "code", False, None, False),
                (
                    "reasonCode",
                    "reasonCode",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    True,
                    None,
                    False,
                ),
                (
                    "reasonReference",
                    "reasonReference",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
                (
                    "relevantHistory",
                    "relevantHistory",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
                (
                    "requester",
                    "requester",
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
                    True,
                ),
                (
                    "supportingInfo",
                    "supportingInfo",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
            ]
        )
        return js


class DeviceRequestParameter(backboneelement.BackboneElement):
    """ Device details.

    Specific parameters for the ordered item.  For example, the prism value for
    lenses.
    """

    resource_type = "DeviceRequestParameter"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.code = None
        """ Device detail.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.valueBoolean = None
        """ Value of detail.
        Type `bool`. """

        self.valueCodeableConcept = None
        """ Value of detail.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.valueQuantity = None
        """ Value of detail.
        Type `Quantity` (represented as `dict` in JSON). """

        self.valueRange = None
        """ Value of detail.
        Type `Range` (represented as `dict` in JSON). """

        super(DeviceRequestParameter, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(DeviceRequestParameter, self).elementProperties()
        js.extend(
            [
                (
                    "code",
                    "code",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                (
                    "valueBoolean",
                    "valueBoolean",
                    bool,
                    "boolean",
                    False,
                    "value",
                    False,
                ),
                (
                    "valueCodeableConcept",
                    "valueCodeableConcept",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    "value",
                    False,
                ),
                (
                    "valueQuantity",
                    "valueQuantity",
                    quantity.Quantity,
                    "Quantity",
                    False,
                    "value",
                    False,
                ),
                (
                    "valueRange",
                    "valueRange",
                    range.Range,
                    "Range",
                    False,
                    "value",
                    False,
                ),
            ]
        )
        return js


try:
    from . import annotation
except ImportError:
    annotation = sys.modules[__package__ + ".annotation"]
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
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + ".period"]
try:
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + ".quantity"]
try:
    from . import range
except ImportError:
    range = sys.modules[__package__ + ".range"]
try:
    from . import timing
except ImportError:
    timing = sys.modules[__package__ + ".timing"]
