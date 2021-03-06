# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/SupplyRequest
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""


import sys

from . import backboneelement, domainresource


class SupplyRequest(domainresource.DomainResource):
    """ Request for a medication, substance or device.

    A record of a request for a medication, substance or device used in the
    healthcare setting.
    """

    resource_type = "SupplyRequest"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.authoredOn = None
        """ When the request was made.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.category = None
        """ The kind of supply (central, non-stock, etc.).
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.deliverFrom = None
        """ The origin of the supply.
        Type `FHIRReference` referencing `['Organization', 'Location']` (represented as `dict` in JSON). """

        self.deliverTo = None
        """ The destination of the supply.
        Type `FHIRReference` referencing `['Organization', 'Location', 'Patient']` (represented as `dict` in JSON). """

        self.identifier = None
        """ Business Identifier for SupplyRequest.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.itemCodeableConcept = None
        """ Medication, Substance, or Device requested to be supplied.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.itemReference = None
        """ Medication, Substance, or Device requested to be supplied.
        Type `FHIRReference` referencing `['Medication', 'Substance', 'Device']` (represented as `dict` in JSON). """

        self.occurrenceDateTime = None
        """ When the request should be fulfilled.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.occurrencePeriod = None
        """ When the request should be fulfilled.
        Type `Period` (represented as `dict` in JSON). """

        self.occurrenceTiming = None
        """ When the request should be fulfilled.
        Type `Timing` (represented as `dict` in JSON). """

        self.parameter = None
        """ Ordered item details.
        List of `SupplyRequestParameter` items (represented as `dict` in JSON). """

        self.priority = None
        """ routine | urgent | asap | stat.
        Type `str`. """

        self.quantity = None
        """ The requested amount of the item indicated.
        Type `Quantity` (represented as `dict` in JSON). """

        self.reasonCode = None
        """ The reason why the supply item was requested.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.reasonReference = None
        """ The reason why the supply item was requested.
        List of `FHIRReference` items referencing `['Condition', 'Observation', 'DiagnosticReport', 'DocumentReference']` (represented as `dict` in JSON). """

        self.requester = None
        """ Individual making the request.
        Type `FHIRReference` referencing `['Practitioner', 'PractitionerRole', 'Organization', 'Patient', 'RelatedPerson', 'Device']` (represented as `dict` in JSON). """

        self.status = None
        """ draft | active | suspended +.
        Type `str`. """

        self.supplier = None
        """ Who is intended to fulfill the request.
        List of `FHIRReference` items referencing `['Organization', 'HealthcareService']` (represented as `dict` in JSON). """

        super(SupplyRequest, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(SupplyRequest, self).elementProperties()
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
                    "category",
                    "category",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                (
                    "deliverFrom",
                    "deliverFrom",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                (
                    "deliverTo",
                    "deliverTo",
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
                (
                    "itemCodeableConcept",
                    "itemCodeableConcept",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    "item",
                    True,
                ),
                (
                    "itemReference",
                    "itemReference",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    "item",
                    True,
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
                    SupplyRequestParameter,
                    "SupplyRequestParameter",
                    True,
                    None,
                    False,
                ),
                ("priority", "priority", str, "code", False, None, False),
                (
                    "quantity",
                    "quantity",
                    quantity.Quantity,
                    "Quantity",
                    False,
                    None,
                    True,
                ),
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
                    "supplier",
                    "supplier",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
            ]
        )
        return js


class SupplyRequestParameter(backboneelement.BackboneElement):
    """ Ordered item details.

    Specific parameters for the ordered item.  For example, the size of the
    indicated item.
    """

    resource_type = "SupplyRequestParameter"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.code = None
        """ Item detail.
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

        super(SupplyRequestParameter, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(SupplyRequestParameter, self).elementProperties()
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
