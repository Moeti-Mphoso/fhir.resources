# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Specimen
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""


import sys

from . import backboneelement, domainresource


class Specimen(domainresource.DomainResource):
    """ Sample for analysis.

    A sample to be used for analysis.
    """

    resource_type = "Specimen"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.accessionIdentifier = None
        """ Identifier assigned by the lab.
        Type `Identifier` (represented as `dict` in JSON). """

        self.collection = None
        """ Collection details.
        Type `SpecimenCollection` (represented as `dict` in JSON). """

        self.container = None
        """ Direct container of specimen (tube/slide, etc.).
        List of `SpecimenContainer` items (represented as `dict` in JSON). """

        self.identifier = None
        """ External Identifier.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.note = None
        """ Comments.
        List of `Annotation` items (represented as `dict` in JSON). """

        self.parent = None
        """ Specimen from which this specimen originated.
        List of `FHIRReference` items referencing `['Specimen']` (represented as `dict` in JSON). """

        self.processing = None
        """ Processing and processing step details.
        List of `SpecimenProcessing` items (represented as `dict` in JSON). """

        self.receivedTime = None
        """ The time when specimen was received for processing.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.request = None
        """ Why the specimen was collected.
        List of `FHIRReference` items referencing `['ProcedureRequest']` (represented as `dict` in JSON). """

        self.status = None
        """ available | unavailable | unsatisfactory | entered-in-error.
        Type `str`. """

        self.subject = None
        """ Where the specimen came from. This may be from the patient(s) or
        from the environment or a device.
        Type `FHIRReference` referencing `['Patient'], ['Group'], ['Device'], ['Substance']` (represented as `dict` in JSON). """

        self.type = None
        """ Kind of material that forms the specimen.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        super(Specimen, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Specimen, self).elementProperties()
        js.extend(
            [
                (
                    "accessionIdentifier",
                    "accessionIdentifier",
                    identifier.Identifier,
                    "Identifier",
                    False,
                    None,
                    False,
                ),
                (
                    "collection",
                    "collection",
                    SpecimenCollection,
                    "SpecimenCollection",
                    False,
                    None,
                    False,
                ),
                (
                    "container",
                    "container",
                    SpecimenContainer,
                    "SpecimenContainer",
                    True,
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
                    "note",
                    "note",
                    annotation.Annotation,
                    "Annotation",
                    True,
                    None,
                    False,
                ),
                (
                    "parent",
                    "parent",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
                (
                    "processing",
                    "processing",
                    SpecimenProcessing,
                    "SpecimenProcessing",
                    True,
                    None,
                    False,
                ),
                (
                    "receivedTime",
                    "receivedTime",
                    fhirdate.FHIRDate,
                    "dateTime",
                    False,
                    None,
                    False,
                ),
                (
                    "request",
                    "request",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
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


class SpecimenCollection(backboneelement.BackboneElement):
    """ Collection details.

    Details concerning the specimen collection.
    """

    resource_type = "SpecimenCollection"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.bodySite = None
        """ Anatomical collection site.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.collectedDateTime = None
        """ Collection time.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.collectedPeriod = None
        """ Collection time.
        Type `Period` (represented as `dict` in JSON). """

        self.collector = None
        """ Who collected the specimen.
        Type `FHIRReference` referencing `['Practitioner']` (represented as `dict` in JSON). """

        self.method = None
        """ Technique used to perform collection.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.quantity = None
        """ The quantity of specimen collected.
        Type `Quantity` (represented as `dict` in JSON). """

        super(SpecimenCollection, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(SpecimenCollection, self).elementProperties()
        js.extend(
            [
                (
                    "bodySite",
                    "bodySite",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                (
                    "collectedDateTime",
                    "collectedDateTime",
                    fhirdate.FHIRDate,
                    "dateTime",
                    False,
                    "collected",
                    False,
                ),
                (
                    "collectedPeriod",
                    "collectedPeriod",
                    period.Period,
                    "Period",
                    False,
                    "collected",
                    False,
                ),
                (
                    "collector",
                    "collector",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                (
                    "method",
                    "method",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                (
                    "quantity",
                    "quantity",
                    quantity.Quantity,
                    "Quantity",
                    False,
                    None,
                    False,
                ),
            ]
        )
        return js


class SpecimenContainer(backboneelement.BackboneElement):
    """ Direct container of specimen (tube/slide, etc.).

    The container holding the specimen.  The recursive nature of containers;
    i.e. blood in tube in tray in rack is not addressed here.
    """

    resource_type = "SpecimenContainer"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.additiveCodeableConcept = None
        """ Additive associated with container.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.additiveReference = None
        """ Additive associated with container.
        Type `FHIRReference` referencing `['Substance']` (represented as `dict` in JSON). """

        self.capacity = None
        """ Container volume or size.
        Type `Quantity` (represented as `dict` in JSON). """

        self.description = None
        """ Textual description of the container.
        Type `str`. """

        self.identifier = None
        """ Id for the container.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.specimenQuantity = None
        """ Quantity of specimen within container.
        Type `Quantity` (represented as `dict` in JSON). """

        self.type = None
        """ Kind of container directly associated with specimen.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        super(SpecimenContainer, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(SpecimenContainer, self).elementProperties()
        js.extend(
            [
                (
                    "additiveCodeableConcept",
                    "additiveCodeableConcept",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    "additive",
                    False,
                ),
                (
                    "additiveReference",
                    "additiveReference",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    "additive",
                    False,
                ),
                (
                    "capacity",
                    "capacity",
                    quantity.Quantity,
                    "Quantity",
                    False,
                    None,
                    False,
                ),
                ("description", "description", str, "string", False, None, False),
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
                    "specimenQuantity",
                    "specimenQuantity",
                    quantity.Quantity,
                    "Quantity",
                    False,
                    None,
                    False,
                ),
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


class SpecimenProcessing(backboneelement.BackboneElement):
    """ Processing and processing step details.

    Details concerning processing and processing steps for the specimen.
    """

    resource_type = "SpecimenProcessing"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.additive = None
        """ Material used in the processing step.
        List of `FHIRReference` items referencing `['Substance']` (represented as `dict` in JSON). """

        self.description = None
        """ Textual description of procedure.
        Type `str`. """

        self.procedure = None
        """ Indicates the treatment step  applied to the specimen.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.timeDateTime = None
        """ Date and time of specimen processing.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.timePeriod = None
        """ Date and time of specimen processing.
        Type `Period` (represented as `dict` in JSON). """

        super(SpecimenProcessing, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(SpecimenProcessing, self).elementProperties()
        js.extend(
            [
                (
                    "additive",
                    "additive",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
                ("description", "description", str, "string", False, None, False),
                (
                    "procedure",
                    "procedure",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                (
                    "timeDateTime",
                    "timeDateTime",
                    fhirdate.FHIRDate,
                    "dateTime",
                    False,
                    "time",
                    False,
                ),
                (
                    "timePeriod",
                    "timePeriod",
                    period.Period,
                    "Period",
                    False,
                    "time",
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
