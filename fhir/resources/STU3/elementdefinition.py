# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ElementDefinition
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""


import sys

from . import element


class ElementDefinition(element.Element):
    """ Definition of an element in a resource or extension.

    Captures constraints on each element within the resource, profile, or
    extension.
    """

    resource_type = "ElementDefinition"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.alias = None
        """ Other names.
        List of `str` items. """

        self.base = None
        """ Base definition information for tools.
        Type `ElementDefinitionBase` (represented as `dict` in JSON). """

        self.binding = None
        """ ValueSet details if this is coded.
        Type `ElementDefinitionBinding` (represented as `dict` in JSON). """

        self.code = None
        """ Corresponding codes in terminologies.
        List of `Coding` items (represented as `dict` in JSON). """

        self.comment = None
        """ Comments about the use of this element.
        Type `str`. """

        self.condition = None
        """ Reference to invariant about presence.
        List of `str` items. """

        self.constraint = None
        """ Condition that must evaluate to true.
        List of `ElementDefinitionConstraint` items (represented as `dict` in JSON). """

        self.contentReference = None
        """ Reference to definition of content for the element.
        Type `str`. """

        self.defaultValueAddress = None
        """ Specified value if missing from instance.
        Type `Address` (represented as `dict` in JSON). """

        self.defaultValueAge = None
        """ Specified value if missing from instance.
        Type `Age` (represented as `dict` in JSON). """

        self.defaultValueAnnotation = None
        """ Specified value if missing from instance.
        Type `Annotation` (represented as `dict` in JSON). """

        self.defaultValueAttachment = None
        """ Specified value if missing from instance.
        Type `Attachment` (represented as `dict` in JSON). """

        self.defaultValueBase64Binary = None
        """ Specified value if missing from instance.
        Type `str`. """

        self.defaultValueBoolean = None
        """ Specified value if missing from instance.
        Type `bool`. """

        self.defaultValueCode = None
        """ Specified value if missing from instance.
        Type `str`. """

        self.defaultValueCodeableConcept = None
        """ Specified value if missing from instance.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.defaultValueCoding = None
        """ Specified value if missing from instance.
        Type `Coding` (represented as `dict` in JSON). """

        self.defaultValueContactPoint = None
        """ Specified value if missing from instance.
        Type `ContactPoint` (represented as `dict` in JSON). """

        self.defaultValueCount = None
        """ Specified value if missing from instance.
        Type `Count` (represented as `dict` in JSON). """

        self.defaultValueDate = None
        """ Specified value if missing from instance.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.defaultValueDateTime = None
        """ Specified value if missing from instance.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.defaultValueDecimal = None
        """ Specified value if missing from instance.
        Type `float`. """

        self.defaultValueDistance = None
        """ Specified value if missing from instance.
        Type `Distance` (represented as `dict` in JSON). """

        self.defaultValueDuration = None
        """ Specified value if missing from instance.
        Type `Duration` (represented as `dict` in JSON). """

        self.defaultValueHumanName = None
        """ Specified value if missing from instance.
        Type `HumanName` (represented as `dict` in JSON). """

        self.defaultValueId = None
        """ Specified value if missing from instance.
        Type `str`. """

        self.defaultValueIdentifier = None
        """ Specified value if missing from instance.
        Type `Identifier` (represented as `dict` in JSON). """

        self.defaultValueInstant = None
        """ Specified value if missing from instance.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.defaultValueInteger = None
        """ Specified value if missing from instance.
        Type `int`. """

        self.defaultValueMarkdown = None
        """ Specified value if missing from instance.
        Type `str`. """

        self.defaultValueMeta = None
        """ Specified value if missing from instance.
        Type `Meta` (represented as `dict` in JSON). """

        self.defaultValueMoney = None
        """ Specified value if missing from instance.
        Type `Money` (represented as `dict` in JSON). """

        self.defaultValueOid = None
        """ Specified value if missing from instance.
        Type `str`. """

        self.defaultValuePeriod = None
        """ Specified value if missing from instance.
        Type `Period` (represented as `dict` in JSON). """

        self.defaultValuePositiveInt = None
        """ Specified value if missing from instance.
        Type `int`. """

        self.defaultValueQuantity = None
        """ Specified value if missing from instance.
        Type `Quantity` (represented as `dict` in JSON). """

        self.defaultValueRange = None
        """ Specified value if missing from instance.
        Type `Range` (represented as `dict` in JSON). """

        self.defaultValueRatio = None
        """ Specified value if missing from instance.
        Type `Ratio` (represented as `dict` in JSON). """

        self.defaultValueReference = None
        """ Specified value if missing from instance.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.defaultValueSampledData = None
        """ Specified value if missing from instance.
        Type `SampledData` (represented as `dict` in JSON). """

        self.defaultValueSignature = None
        """ Specified value if missing from instance.
        Type `Signature` (represented as `dict` in JSON). """

        self.defaultValueString = None
        """ Specified value if missing from instance.
        Type `str`. """

        self.defaultValueTime = None
        """ Specified value if missing from instance.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.defaultValueTiming = None
        """ Specified value if missing from instance.
        Type `Timing` (represented as `dict` in JSON). """

        self.defaultValueUnsignedInt = None
        """ Specified value if missing from instance.
        Type `int`. """

        self.defaultValueUri = None
        """ Specified value if missing from instance.
        Type `str`. """

        self.definition = None
        """ Full formal definition as narrative text.
        Type `str`. """

        self.example = None
        """ Example value (as defined for type).
        List of `ElementDefinitionExample` items (represented as `dict` in JSON). """

        self.fixedAddress = None
        """ Value must be exactly this.
        Type `Address` (represented as `dict` in JSON). """

        self.fixedAge = None
        """ Value must be exactly this.
        Type `Age` (represented as `dict` in JSON). """

        self.fixedAnnotation = None
        """ Value must be exactly this.
        Type `Annotation` (represented as `dict` in JSON). """

        self.fixedAttachment = None
        """ Value must be exactly this.
        Type `Attachment` (represented as `dict` in JSON). """

        self.fixedBase64Binary = None
        """ Value must be exactly this.
        Type `str`. """

        self.fixedBoolean = None
        """ Value must be exactly this.
        Type `bool`. """

        self.fixedCode = None
        """ Value must be exactly this.
        Type `str`. """

        self.fixedCodeableConcept = None
        """ Value must be exactly this.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.fixedCoding = None
        """ Value must be exactly this.
        Type `Coding` (represented as `dict` in JSON). """

        self.fixedContactPoint = None
        """ Value must be exactly this.
        Type `ContactPoint` (represented as `dict` in JSON). """

        self.fixedCount = None
        """ Value must be exactly this.
        Type `Count` (represented as `dict` in JSON). """

        self.fixedDate = None
        """ Value must be exactly this.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.fixedDateTime = None
        """ Value must be exactly this.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.fixedDecimal = None
        """ Value must be exactly this.
        Type `float`. """

        self.fixedDistance = None
        """ Value must be exactly this.
        Type `Distance` (represented as `dict` in JSON). """

        self.fixedDuration = None
        """ Value must be exactly this.
        Type `Duration` (represented as `dict` in JSON). """

        self.fixedHumanName = None
        """ Value must be exactly this.
        Type `HumanName` (represented as `dict` in JSON). """

        self.fixedId = None
        """ Value must be exactly this.
        Type `str`. """

        self.fixedIdentifier = None
        """ Value must be exactly this.
        Type `Identifier` (represented as `dict` in JSON). """

        self.fixedInstant = None
        """ Value must be exactly this.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.fixedInteger = None
        """ Value must be exactly this.
        Type `int`. """

        self.fixedMarkdown = None
        """ Value must be exactly this.
        Type `str`. """

        self.fixedMeta = None
        """ Value must be exactly this.
        Type `Meta` (represented as `dict` in JSON). """

        self.fixedMoney = None
        """ Value must be exactly this.
        Type `Money` (represented as `dict` in JSON). """

        self.fixedOid = None
        """ Value must be exactly this.
        Type `str`. """

        self.fixedPeriod = None
        """ Value must be exactly this.
        Type `Period` (represented as `dict` in JSON). """

        self.fixedPositiveInt = None
        """ Value must be exactly this.
        Type `int`. """

        self.fixedQuantity = None
        """ Value must be exactly this.
        Type `Quantity` (represented as `dict` in JSON). """

        self.fixedRange = None
        """ Value must be exactly this.
        Type `Range` (represented as `dict` in JSON). """

        self.fixedRatio = None
        """ Value must be exactly this.
        Type `Ratio` (represented as `dict` in JSON). """

        self.fixedReference = None
        """ Value must be exactly this.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.fixedSampledData = None
        """ Value must be exactly this.
        Type `SampledData` (represented as `dict` in JSON). """

        self.fixedSignature = None
        """ Value must be exactly this.
        Type `Signature` (represented as `dict` in JSON). """

        self.fixedString = None
        """ Value must be exactly this.
        Type `str`. """

        self.fixedTime = None
        """ Value must be exactly this.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.fixedTiming = None
        """ Value must be exactly this.
        Type `Timing` (represented as `dict` in JSON). """

        self.fixedUnsignedInt = None
        """ Value must be exactly this.
        Type `int`. """

        self.fixedUri = None
        """ Value must be exactly this.
        Type `str`. """

        self.isModifier = None
        """ If this modifies the meaning of other elements.
        Type `bool`. """

        self.isSummary = None
        """ Include when _summary = true?.
        Type `bool`. """

        self.label = None
        """ Name for element to display with or prompt for element.
        Type `str`. """

        self.mapping = None
        """ Map element to another set of definitions.
        List of `ElementDefinitionMapping` items (represented as `dict` in JSON). """

        self.max = None
        """ Maximum Cardinality (a number or *).
        Type `str`. """

        self.maxLength = None
        """ Max length for strings.
        Type `int`. """

        self.maxValueDate = None
        """ Maximum Allowed Value (for some types).
        Type `FHIRDate` (represented as `str` in JSON). """

        self.maxValueDateTime = None
        """ Maximum Allowed Value (for some types).
        Type `FHIRDate` (represented as `str` in JSON). """

        self.maxValueDecimal = None
        """ Maximum Allowed Value (for some types).
        Type `float`. """

        self.maxValueInstant = None
        """ Maximum Allowed Value (for some types).
        Type `FHIRDate` (represented as `str` in JSON). """

        self.maxValueInteger = None
        """ Maximum Allowed Value (for some types).
        Type `int`. """

        self.maxValuePositiveInt = None
        """ Maximum Allowed Value (for some types).
        Type `int`. """

        self.maxValueQuantity = None
        """ Maximum Allowed Value (for some types).
        Type `Quantity` (represented as `dict` in JSON). """

        self.maxValueTime = None
        """ Maximum Allowed Value (for some types).
        Type `FHIRDate` (represented as `str` in JSON). """

        self.maxValueUnsignedInt = None
        """ Maximum Allowed Value (for some types).
        Type `int`. """

        self.meaningWhenMissing = None
        """ Implicit meaning when this element is missing.
        Type `str`. """

        self.min = None
        """ Minimum Cardinality.
        Type `int`. """

        self.minValueDate = None
        """ Minimum Allowed Value (for some types).
        Type `FHIRDate` (represented as `str` in JSON). """

        self.minValueDateTime = None
        """ Minimum Allowed Value (for some types).
        Type `FHIRDate` (represented as `str` in JSON). """

        self.minValueDecimal = None
        """ Minimum Allowed Value (for some types).
        Type `float`. """

        self.minValueInstant = None
        """ Minimum Allowed Value (for some types).
        Type `FHIRDate` (represented as `str` in JSON). """

        self.minValueInteger = None
        """ Minimum Allowed Value (for some types).
        Type `int`. """

        self.minValuePositiveInt = None
        """ Minimum Allowed Value (for some types).
        Type `int`. """

        self.minValueQuantity = None
        """ Minimum Allowed Value (for some types).
        Type `Quantity` (represented as `dict` in JSON). """

        self.minValueTime = None
        """ Minimum Allowed Value (for some types).
        Type `FHIRDate` (represented as `str` in JSON). """

        self.minValueUnsignedInt = None
        """ Minimum Allowed Value (for some types).
        Type `int`. """

        self.mustSupport = None
        """ If the element must supported.
        Type `bool`. """

        self.orderMeaning = None
        """ What the order of the elements means.
        Type `str`. """

        self.path = None
        """ Path of the element in the hierarchy of elements.
        Type `str`. """

        self.patternAddress = None
        """ Value must have at least these property values.
        Type `Address` (represented as `dict` in JSON). """

        self.patternAge = None
        """ Value must have at least these property values.
        Type `Age` (represented as `dict` in JSON). """

        self.patternAnnotation = None
        """ Value must have at least these property values.
        Type `Annotation` (represented as `dict` in JSON). """

        self.patternAttachment = None
        """ Value must have at least these property values.
        Type `Attachment` (represented as `dict` in JSON). """

        self.patternBase64Binary = None
        """ Value must have at least these property values.
        Type `str`. """

        self.patternBoolean = None
        """ Value must have at least these property values.
        Type `bool`. """

        self.patternCode = None
        """ Value must have at least these property values.
        Type `str`. """

        self.patternCodeableConcept = None
        """ Value must have at least these property values.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.patternCoding = None
        """ Value must have at least these property values.
        Type `Coding` (represented as `dict` in JSON). """

        self.patternContactPoint = None
        """ Value must have at least these property values.
        Type `ContactPoint` (represented as `dict` in JSON). """

        self.patternCount = None
        """ Value must have at least these property values.
        Type `Count` (represented as `dict` in JSON). """

        self.patternDate = None
        """ Value must have at least these property values.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.patternDateTime = None
        """ Value must have at least these property values.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.patternDecimal = None
        """ Value must have at least these property values.
        Type `float`. """

        self.patternDistance = None
        """ Value must have at least these property values.
        Type `Distance` (represented as `dict` in JSON). """

        self.patternDuration = None
        """ Value must have at least these property values.
        Type `Duration` (represented as `dict` in JSON). """

        self.patternHumanName = None
        """ Value must have at least these property values.
        Type `HumanName` (represented as `dict` in JSON). """

        self.patternId = None
        """ Value must have at least these property values.
        Type `str`. """

        self.patternIdentifier = None
        """ Value must have at least these property values.
        Type `Identifier` (represented as `dict` in JSON). """

        self.patternInstant = None
        """ Value must have at least these property values.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.patternInteger = None
        """ Value must have at least these property values.
        Type `int`. """

        self.patternMarkdown = None
        """ Value must have at least these property values.
        Type `str`. """

        self.patternMeta = None
        """ Value must have at least these property values.
        Type `Meta` (represented as `dict` in JSON). """

        self.patternMoney = None
        """ Value must have at least these property values.
        Type `Money` (represented as `dict` in JSON). """

        self.patternOid = None
        """ Value must have at least these property values.
        Type `str`. """

        self.patternPeriod = None
        """ Value must have at least these property values.
        Type `Period` (represented as `dict` in JSON). """

        self.patternPositiveInt = None
        """ Value must have at least these property values.
        Type `int`. """

        self.patternQuantity = None
        """ Value must have at least these property values.
        Type `Quantity` (represented as `dict` in JSON). """

        self.patternRange = None
        """ Value must have at least these property values.
        Type `Range` (represented as `dict` in JSON). """

        self.patternRatio = None
        """ Value must have at least these property values.
        Type `Ratio` (represented as `dict` in JSON). """

        self.patternReference = None
        """ Value must have at least these property values.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.patternSampledData = None
        """ Value must have at least these property values.
        Type `SampledData` (represented as `dict` in JSON). """

        self.patternSignature = None
        """ Value must have at least these property values.
        Type `Signature` (represented as `dict` in JSON). """

        self.patternString = None
        """ Value must have at least these property values.
        Type `str`. """

        self.patternTime = None
        """ Value must have at least these property values.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.patternTiming = None
        """ Value must have at least these property values.
        Type `Timing` (represented as `dict` in JSON). """

        self.patternUnsignedInt = None
        """ Value must have at least these property values.
        Type `int`. """

        self.patternUri = None
        """ Value must have at least these property values.
        Type `str`. """

        self.representation = None
        """ xmlAttr | xmlText | typeAttr | cdaText | xhtml.
        List of `str` items. """

        self.requirements = None
        """ Why this resource has been created.
        Type `str`. """

        self.short = None
        """ Concise definition for space-constrained presentation.
        Type `str`. """

        self.sliceName = None
        """ Name for this particular element (in a set of slices).
        Type `str`. """

        self.slicing = None
        """ This element is sliced - slices follow.
        Type `ElementDefinitionSlicing` (represented as `dict` in JSON). """

        self.type = None
        """ Data type and Profile for this element.
        List of `ElementDefinitionType` items (represented as `dict` in JSON). """

        super(ElementDefinition, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ElementDefinition, self).elementProperties()
        js.extend(
            [
                ("alias", "alias", str, "string", True, None, False),
                (
                    "base",
                    "base",
                    ElementDefinitionBase,
                    "ElementDefinitionBase",
                    False,
                    None,
                    False,
                ),
                (
                    "binding",
                    "binding",
                    ElementDefinitionBinding,
                    "ElementDefinitionBinding",
                    False,
                    None,
                    False,
                ),
                ("code", "code", coding.Coding, "Coding", True, None, False),
                ("comment", "comment", str, "markdown", False, None, False),
                ("condition", "condition", str, "id", True, None, False),
                (
                    "constraint",
                    "constraint",
                    ElementDefinitionConstraint,
                    "ElementDefinitionConstraint",
                    True,
                    None,
                    False,
                ),
                (
                    "contentReference",
                    "contentReference",
                    str,
                    "uri",
                    False,
                    None,
                    False,
                ),
                (
                    "defaultValueAddress",
                    "defaultValueAddress",
                    address.Address,
                    "Address",
                    False,
                    "defaultValue",
                    False,
                ),
                (
                    "defaultValueAge",
                    "defaultValueAge",
                    age.Age,
                    "Age",
                    False,
                    "defaultValue",
                    False,
                ),
                (
                    "defaultValueAnnotation",
                    "defaultValueAnnotation",
                    annotation.Annotation,
                    "Annotation",
                    False,
                    "defaultValue",
                    False,
                ),
                (
                    "defaultValueAttachment",
                    "defaultValueAttachment",
                    attachment.Attachment,
                    "Attachment",
                    False,
                    "defaultValue",
                    False,
                ),
                (
                    "defaultValueBase64Binary",
                    "defaultValueBase64Binary",
                    str,
                    "base64Binary",
                    False,
                    "defaultValue",
                    False,
                ),
                (
                    "defaultValueBoolean",
                    "defaultValueBoolean",
                    bool,
                    "boolean",
                    False,
                    "defaultValue",
                    False,
                ),
                (
                    "defaultValueCode",
                    "defaultValueCode",
                    str,
                    "code",
                    False,
                    "defaultValue",
                    False,
                ),
                (
                    "defaultValueCodeableConcept",
                    "defaultValueCodeableConcept",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    "defaultValue",
                    False,
                ),
                (
                    "defaultValueCoding",
                    "defaultValueCoding",
                    coding.Coding,
                    "Coding",
                    False,
                    "defaultValue",
                    False,
                ),
                (
                    "defaultValueContactPoint",
                    "defaultValueContactPoint",
                    contactpoint.ContactPoint,
                    "ContactPoint",
                    False,
                    "defaultValue",
                    False,
                ),
                (
                    "defaultValueCount",
                    "defaultValueCount",
                    count.Count,
                    "Count",
                    False,
                    "defaultValue",
                    False,
                ),
                (
                    "defaultValueDate",
                    "defaultValueDate",
                    fhirdate.FHIRDate,
                    "date",
                    False,
                    "defaultValue",
                    False,
                ),
                (
                    "defaultValueDateTime",
                    "defaultValueDateTime",
                    fhirdate.FHIRDate,
                    "dateTime",
                    False,
                    "defaultValue",
                    False,
                ),
                (
                    "defaultValueDecimal",
                    "defaultValueDecimal",
                    float,
                    "decimal",
                    False,
                    "defaultValue",
                    False,
                ),
                (
                    "defaultValueDistance",
                    "defaultValueDistance",
                    distance.Distance,
                    "Distance",
                    False,
                    "defaultValue",
                    False,
                ),
                (
                    "defaultValueDuration",
                    "defaultValueDuration",
                    duration.Duration,
                    "Duration",
                    False,
                    "defaultValue",
                    False,
                ),
                (
                    "defaultValueHumanName",
                    "defaultValueHumanName",
                    humanname.HumanName,
                    "HumanName",
                    False,
                    "defaultValue",
                    False,
                ),
                (
                    "defaultValueId",
                    "defaultValueId",
                    str,
                    "id",
                    False,
                    "defaultValue",
                    False,
                ),
                (
                    "defaultValueIdentifier",
                    "defaultValueIdentifier",
                    identifier.Identifier,
                    "Identifier",
                    False,
                    "defaultValue",
                    False,
                ),
                (
                    "defaultValueInstant",
                    "defaultValueInstant",
                    fhirdate.FHIRDate,
                    "instant",
                    False,
                    "defaultValue",
                    False,
                ),
                (
                    "defaultValueInteger",
                    "defaultValueInteger",
                    int,
                    "integer",
                    False,
                    "defaultValue",
                    False,
                ),
                (
                    "defaultValueMarkdown",
                    "defaultValueMarkdown",
                    str,
                    "markdown",
                    False,
                    "defaultValue",
                    False,
                ),
                (
                    "defaultValueMeta",
                    "defaultValueMeta",
                    meta.Meta,
                    "Meta",
                    False,
                    "defaultValue",
                    False,
                ),
                (
                    "defaultValueMoney",
                    "defaultValueMoney",
                    money.Money,
                    "Money",
                    False,
                    "defaultValue",
                    False,
                ),
                (
                    "defaultValueOid",
                    "defaultValueOid",
                    str,
                    "oid",
                    False,
                    "defaultValue",
                    False,
                ),
                (
                    "defaultValuePeriod",
                    "defaultValuePeriod",
                    period.Period,
                    "Period",
                    False,
                    "defaultValue",
                    False,
                ),
                (
                    "defaultValuePositiveInt",
                    "defaultValuePositiveInt",
                    int,
                    "positiveInt",
                    False,
                    "defaultValue",
                    False,
                ),
                (
                    "defaultValueQuantity",
                    "defaultValueQuantity",
                    quantity.Quantity,
                    "Quantity",
                    False,
                    "defaultValue",
                    False,
                ),
                (
                    "defaultValueRange",
                    "defaultValueRange",
                    range.Range,
                    "Range",
                    False,
                    "defaultValue",
                    False,
                ),
                (
                    "defaultValueRatio",
                    "defaultValueRatio",
                    ratio.Ratio,
                    "Ratio",
                    False,
                    "defaultValue",
                    False,
                ),
                (
                    "defaultValueReference",
                    "defaultValueReference",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    "defaultValue",
                    False,
                ),
                (
                    "defaultValueSampledData",
                    "defaultValueSampledData",
                    sampleddata.SampledData,
                    "SampledData",
                    False,
                    "defaultValue",
                    False,
                ),
                (
                    "defaultValueSignature",
                    "defaultValueSignature",
                    signature.Signature,
                    "Signature",
                    False,
                    "defaultValue",
                    False,
                ),
                (
                    "defaultValueString",
                    "defaultValueString",
                    str,
                    "string",
                    False,
                    "defaultValue",
                    False,
                ),
                (
                    "defaultValueTime",
                    "defaultValueTime",
                    fhirdate.FHIRDate,
                    "time",
                    False,
                    "defaultValue",
                    False,
                ),
                (
                    "defaultValueTiming",
                    "defaultValueTiming",
                    timing.Timing,
                    "Timing",
                    False,
                    "defaultValue",
                    False,
                ),
                (
                    "defaultValueUnsignedInt",
                    "defaultValueUnsignedInt",
                    int,
                    "unsignedInt",
                    False,
                    "defaultValue",
                    False,
                ),
                (
                    "defaultValueUri",
                    "defaultValueUri",
                    str,
                    "uri",
                    False,
                    "defaultValue",
                    False,
                ),
                ("definition", "definition", str, "markdown", False, None, False),
                (
                    "example",
                    "example",
                    ElementDefinitionExample,
                    "ElementDefinitionExample",
                    True,
                    None,
                    False,
                ),
                (
                    "fixedAddress",
                    "fixedAddress",
                    address.Address,
                    "Address",
                    False,
                    "fixed",
                    False,
                ),
                ("fixedAge", "fixedAge", age.Age, "Age", False, "fixed", False),
                (
                    "fixedAnnotation",
                    "fixedAnnotation",
                    annotation.Annotation,
                    "Annotation",
                    False,
                    "fixed",
                    False,
                ),
                (
                    "fixedAttachment",
                    "fixedAttachment",
                    attachment.Attachment,
                    "Attachment",
                    False,
                    "fixed",
                    False,
                ),
                (
                    "fixedBase64Binary",
                    "fixedBase64Binary",
                    str,
                    "base64Binary",
                    False,
                    "fixed",
                    False,
                ),
                (
                    "fixedBoolean",
                    "fixedBoolean",
                    bool,
                    "boolean",
                    False,
                    "fixed",
                    False,
                ),
                ("fixedCode", "fixedCode", str, "code", False, "fixed", False),
                (
                    "fixedCodeableConcept",
                    "fixedCodeableConcept",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    "fixed",
                    False,
                ),
                (
                    "fixedCoding",
                    "fixedCoding",
                    coding.Coding,
                    "Coding",
                    False,
                    "fixed",
                    False,
                ),
                (
                    "fixedContactPoint",
                    "fixedContactPoint",
                    contactpoint.ContactPoint,
                    "ContactPoint",
                    False,
                    "fixed",
                    False,
                ),
                (
                    "fixedCount",
                    "fixedCount",
                    count.Count,
                    "Count",
                    False,
                    "fixed",
                    False,
                ),
                (
                    "fixedDate",
                    "fixedDate",
                    fhirdate.FHIRDate,
                    "date",
                    False,
                    "fixed",
                    False,
                ),
                (
                    "fixedDateTime",
                    "fixedDateTime",
                    fhirdate.FHIRDate,
                    "dateTime",
                    False,
                    "fixed",
                    False,
                ),
                (
                    "fixedDecimal",
                    "fixedDecimal",
                    float,
                    "decimal",
                    False,
                    "fixed",
                    False,
                ),
                (
                    "fixedDistance",
                    "fixedDistance",
                    distance.Distance,
                    "Distance",
                    False,
                    "fixed",
                    False,
                ),
                (
                    "fixedDuration",
                    "fixedDuration",
                    duration.Duration,
                    "Duration",
                    False,
                    "fixed",
                    False,
                ),
                (
                    "fixedHumanName",
                    "fixedHumanName",
                    humanname.HumanName,
                    "HumanName",
                    False,
                    "fixed",
                    False,
                ),
                ("fixedId", "fixedId", str, "id", False, "fixed", False),
                (
                    "fixedIdentifier",
                    "fixedIdentifier",
                    identifier.Identifier,
                    "Identifier",
                    False,
                    "fixed",
                    False,
                ),
                (
                    "fixedInstant",
                    "fixedInstant",
                    fhirdate.FHIRDate,
                    "instant",
                    False,
                    "fixed",
                    False,
                ),
                ("fixedInteger", "fixedInteger", int, "integer", False, "fixed", False),
                (
                    "fixedMarkdown",
                    "fixedMarkdown",
                    str,
                    "markdown",
                    False,
                    "fixed",
                    False,
                ),
                ("fixedMeta", "fixedMeta", meta.Meta, "Meta", False, "fixed", False),
                (
                    "fixedMoney",
                    "fixedMoney",
                    money.Money,
                    "Money",
                    False,
                    "fixed",
                    False,
                ),
                ("fixedOid", "fixedOid", str, "oid", False, "fixed", False),
                (
                    "fixedPeriod",
                    "fixedPeriod",
                    period.Period,
                    "Period",
                    False,
                    "fixed",
                    False,
                ),
                (
                    "fixedPositiveInt",
                    "fixedPositiveInt",
                    int,
                    "positiveInt",
                    False,
                    "fixed",
                    False,
                ),
                (
                    "fixedQuantity",
                    "fixedQuantity",
                    quantity.Quantity,
                    "Quantity",
                    False,
                    "fixed",
                    False,
                ),
                (
                    "fixedRange",
                    "fixedRange",
                    range.Range,
                    "Range",
                    False,
                    "fixed",
                    False,
                ),
                (
                    "fixedRatio",
                    "fixedRatio",
                    ratio.Ratio,
                    "Ratio",
                    False,
                    "fixed",
                    False,
                ),
                (
                    "fixedReference",
                    "fixedReference",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    "fixed",
                    False,
                ),
                (
                    "fixedSampledData",
                    "fixedSampledData",
                    sampleddata.SampledData,
                    "SampledData",
                    False,
                    "fixed",
                    False,
                ),
                (
                    "fixedSignature",
                    "fixedSignature",
                    signature.Signature,
                    "Signature",
                    False,
                    "fixed",
                    False,
                ),
                ("fixedString", "fixedString", str, "string", False, "fixed", False),
                (
                    "fixedTime",
                    "fixedTime",
                    fhirdate.FHIRDate,
                    "time",
                    False,
                    "fixed",
                    False,
                ),
                (
                    "fixedTiming",
                    "fixedTiming",
                    timing.Timing,
                    "Timing",
                    False,
                    "fixed",
                    False,
                ),
                (
                    "fixedUnsignedInt",
                    "fixedUnsignedInt",
                    int,
                    "unsignedInt",
                    False,
                    "fixed",
                    False,
                ),
                ("fixedUri", "fixedUri", str, "uri", False, "fixed", False),
                ("isModifier", "isModifier", bool, "boolean", False, None, False),
                ("isSummary", "isSummary", bool, "boolean", False, None, False),
                ("label", "label", str, "string", False, None, False),
                (
                    "mapping",
                    "mapping",
                    ElementDefinitionMapping,
                    "ElementDefinitionMapping",
                    True,
                    None,
                    False,
                ),
                ("max", "max", str, "string", False, None, False),
                ("maxLength", "maxLength", int, "integer", False, None, False),
                (
                    "maxValueDate",
                    "maxValueDate",
                    fhirdate.FHIRDate,
                    "date",
                    False,
                    "maxValue",
                    False,
                ),
                (
                    "maxValueDateTime",
                    "maxValueDateTime",
                    fhirdate.FHIRDate,
                    "dateTime",
                    False,
                    "maxValue",
                    False,
                ),
                (
                    "maxValueDecimal",
                    "maxValueDecimal",
                    float,
                    "decimal",
                    False,
                    "maxValue",
                    False,
                ),
                (
                    "maxValueInstant",
                    "maxValueInstant",
                    fhirdate.FHIRDate,
                    "instant",
                    False,
                    "maxValue",
                    False,
                ),
                (
                    "maxValueInteger",
                    "maxValueInteger",
                    int,
                    "integer",
                    False,
                    "maxValue",
                    False,
                ),
                (
                    "maxValuePositiveInt",
                    "maxValuePositiveInt",
                    int,
                    "positiveInt",
                    False,
                    "maxValue",
                    False,
                ),
                (
                    "maxValueQuantity",
                    "maxValueQuantity",
                    quantity.Quantity,
                    "Quantity",
                    False,
                    "maxValue",
                    False,
                ),
                (
                    "maxValueTime",
                    "maxValueTime",
                    fhirdate.FHIRDate,
                    "time",
                    False,
                    "maxValue",
                    False,
                ),
                (
                    "maxValueUnsignedInt",
                    "maxValueUnsignedInt",
                    int,
                    "unsignedInt",
                    False,
                    "maxValue",
                    False,
                ),
                (
                    "meaningWhenMissing",
                    "meaningWhenMissing",
                    str,
                    "markdown",
                    False,
                    None,
                    False,
                ),
                ("min", "min", int, "unsignedInt", False, None, False),
                (
                    "minValueDate",
                    "minValueDate",
                    fhirdate.FHIRDate,
                    "date",
                    False,
                    "minValue",
                    False,
                ),
                (
                    "minValueDateTime",
                    "minValueDateTime",
                    fhirdate.FHIRDate,
                    "dateTime",
                    False,
                    "minValue",
                    False,
                ),
                (
                    "minValueDecimal",
                    "minValueDecimal",
                    float,
                    "decimal",
                    False,
                    "minValue",
                    False,
                ),
                (
                    "minValueInstant",
                    "minValueInstant",
                    fhirdate.FHIRDate,
                    "instant",
                    False,
                    "minValue",
                    False,
                ),
                (
                    "minValueInteger",
                    "minValueInteger",
                    int,
                    "integer",
                    False,
                    "minValue",
                    False,
                ),
                (
                    "minValuePositiveInt",
                    "minValuePositiveInt",
                    int,
                    "positiveInt",
                    False,
                    "minValue",
                    False,
                ),
                (
                    "minValueQuantity",
                    "minValueQuantity",
                    quantity.Quantity,
                    "Quantity",
                    False,
                    "minValue",
                    False,
                ),
                (
                    "minValueTime",
                    "minValueTime",
                    fhirdate.FHIRDate,
                    "time",
                    False,
                    "minValue",
                    False,
                ),
                (
                    "minValueUnsignedInt",
                    "minValueUnsignedInt",
                    int,
                    "unsignedInt",
                    False,
                    "minValue",
                    False,
                ),
                ("mustSupport", "mustSupport", bool, "boolean", False, None, False),
                ("orderMeaning", "orderMeaning", str, "string", False, None, False),
                ("path", "path", str, "string", False, None, True),
                (
                    "patternAddress",
                    "patternAddress",
                    address.Address,
                    "Address",
                    False,
                    "pattern",
                    False,
                ),
                ("patternAge", "patternAge", age.Age, "Age", False, "pattern", False),
                (
                    "patternAnnotation",
                    "patternAnnotation",
                    annotation.Annotation,
                    "Annotation",
                    False,
                    "pattern",
                    False,
                ),
                (
                    "patternAttachment",
                    "patternAttachment",
                    attachment.Attachment,
                    "Attachment",
                    False,
                    "pattern",
                    False,
                ),
                (
                    "patternBase64Binary",
                    "patternBase64Binary",
                    str,
                    "base64Binary",
                    False,
                    "pattern",
                    False,
                ),
                (
                    "patternBoolean",
                    "patternBoolean",
                    bool,
                    "boolean",
                    False,
                    "pattern",
                    False,
                ),
                ("patternCode", "patternCode", str, "code", False, "pattern", False),
                (
                    "patternCodeableConcept",
                    "patternCodeableConcept",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    "pattern",
                    False,
                ),
                (
                    "patternCoding",
                    "patternCoding",
                    coding.Coding,
                    "Coding",
                    False,
                    "pattern",
                    False,
                ),
                (
                    "patternContactPoint",
                    "patternContactPoint",
                    contactpoint.ContactPoint,
                    "ContactPoint",
                    False,
                    "pattern",
                    False,
                ),
                (
                    "patternCount",
                    "patternCount",
                    count.Count,
                    "Count",
                    False,
                    "pattern",
                    False,
                ),
                (
                    "patternDate",
                    "patternDate",
                    fhirdate.FHIRDate,
                    "date",
                    False,
                    "pattern",
                    False,
                ),
                (
                    "patternDateTime",
                    "patternDateTime",
                    fhirdate.FHIRDate,
                    "dateTime",
                    False,
                    "pattern",
                    False,
                ),
                (
                    "patternDecimal",
                    "patternDecimal",
                    float,
                    "decimal",
                    False,
                    "pattern",
                    False,
                ),
                (
                    "patternDistance",
                    "patternDistance",
                    distance.Distance,
                    "Distance",
                    False,
                    "pattern",
                    False,
                ),
                (
                    "patternDuration",
                    "patternDuration",
                    duration.Duration,
                    "Duration",
                    False,
                    "pattern",
                    False,
                ),
                (
                    "patternHumanName",
                    "patternHumanName",
                    humanname.HumanName,
                    "HumanName",
                    False,
                    "pattern",
                    False,
                ),
                ("patternId", "patternId", str, "id", False, "pattern", False),
                (
                    "patternIdentifier",
                    "patternIdentifier",
                    identifier.Identifier,
                    "Identifier",
                    False,
                    "pattern",
                    False,
                ),
                (
                    "patternInstant",
                    "patternInstant",
                    fhirdate.FHIRDate,
                    "instant",
                    False,
                    "pattern",
                    False,
                ),
                (
                    "patternInteger",
                    "patternInteger",
                    int,
                    "integer",
                    False,
                    "pattern",
                    False,
                ),
                (
                    "patternMarkdown",
                    "patternMarkdown",
                    str,
                    "markdown",
                    False,
                    "pattern",
                    False,
                ),
                (
                    "patternMeta",
                    "patternMeta",
                    meta.Meta,
                    "Meta",
                    False,
                    "pattern",
                    False,
                ),
                (
                    "patternMoney",
                    "patternMoney",
                    money.Money,
                    "Money",
                    False,
                    "pattern",
                    False,
                ),
                ("patternOid", "patternOid", str, "oid", False, "pattern", False),
                (
                    "patternPeriod",
                    "patternPeriod",
                    period.Period,
                    "Period",
                    False,
                    "pattern",
                    False,
                ),
                (
                    "patternPositiveInt",
                    "patternPositiveInt",
                    int,
                    "positiveInt",
                    False,
                    "pattern",
                    False,
                ),
                (
                    "patternQuantity",
                    "patternQuantity",
                    quantity.Quantity,
                    "Quantity",
                    False,
                    "pattern",
                    False,
                ),
                (
                    "patternRange",
                    "patternRange",
                    range.Range,
                    "Range",
                    False,
                    "pattern",
                    False,
                ),
                (
                    "patternRatio",
                    "patternRatio",
                    ratio.Ratio,
                    "Ratio",
                    False,
                    "pattern",
                    False,
                ),
                (
                    "patternReference",
                    "patternReference",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    "pattern",
                    False,
                ),
                (
                    "patternSampledData",
                    "patternSampledData",
                    sampleddata.SampledData,
                    "SampledData",
                    False,
                    "pattern",
                    False,
                ),
                (
                    "patternSignature",
                    "patternSignature",
                    signature.Signature,
                    "Signature",
                    False,
                    "pattern",
                    False,
                ),
                (
                    "patternString",
                    "patternString",
                    str,
                    "string",
                    False,
                    "pattern",
                    False,
                ),
                (
                    "patternTime",
                    "patternTime",
                    fhirdate.FHIRDate,
                    "time",
                    False,
                    "pattern",
                    False,
                ),
                (
                    "patternTiming",
                    "patternTiming",
                    timing.Timing,
                    "Timing",
                    False,
                    "pattern",
                    False,
                ),
                (
                    "patternUnsignedInt",
                    "patternUnsignedInt",
                    int,
                    "unsignedInt",
                    False,
                    "pattern",
                    False,
                ),
                ("patternUri", "patternUri", str, "uri", False, "pattern", False),
                ("representation", "representation", str, "code", True, None, False),
                ("requirements", "requirements", str, "markdown", False, None, False),
                ("short", "short", str, "string", False, None, False),
                ("sliceName", "sliceName", str, "string", False, None, False),
                (
                    "slicing",
                    "slicing",
                    ElementDefinitionSlicing,
                    "ElementDefinitionSlicing",
                    False,
                    None,
                    False,
                ),
                (
                    "type",
                    "type",
                    ElementDefinitionType,
                    "ElementDefinitionType",
                    True,
                    None,
                    False,
                ),
            ]
        )
        return js


class ElementDefinitionBase(element.Element):
    """ Base definition information for tools.

    Information about the base definition of the element, provided to make it
    unnecessary for tools to trace the deviation of the element through the
    derived and related profiles. This information is provided when the element
    definition is not the original definition of an element - i.g. either in a
    constraint on another type, or for elements from a super type in a snap
    shot.
    """

    resource_type = "ElementDefinitionBase"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.max = None
        """ Max cardinality of the base element.
        Type `str`. """

        self.min = None
        """ Min cardinality of the base element.
        Type `int`. """

        self.path = None
        """ Path that identifies the base element.
        Type `str`. """

        super(ElementDefinitionBase, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ElementDefinitionBase, self).elementProperties()
        js.extend(
            [
                ("max", "max", str, "string", False, None, True),
                ("min", "min", int, "unsignedInt", False, None, True),
                ("path", "path", str, "string", False, None, True),
            ]
        )
        return js


class ElementDefinitionBinding(element.Element):
    """ ValueSet details if this is coded.

    Binds to a value set if this element is coded (code, Coding,
    CodeableConcept, Quantity), or the data types (string, uri).
    """

    resource_type = "ElementDefinitionBinding"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.description = None
        """ Human explanation of the value set.
        Type `str`. """

        self.strength = None
        """ required | extensible | preferred | example.
        Type `str`. """

        self.valueSetReference = None
        """ Source of value set.
        Type `FHIRReference` referencing `['ValueSet']` (represented as `dict` in JSON). """

        self.valueSetUri = None
        """ Source of value set.
        Type `str`. """

        super(ElementDefinitionBinding, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ElementDefinitionBinding, self).elementProperties()
        js.extend(
            [
                ("description", "description", str, "string", False, None, False),
                ("strength", "strength", str, "code", False, None, True),
                (
                    "valueSetReference",
                    "valueSetReference",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    "valueSet",
                    False,
                ),
                ("valueSetUri", "valueSetUri", str, "uri", False, "valueSet", False),
            ]
        )
        return js


class ElementDefinitionConstraint(element.Element):
    """ Condition that must evaluate to true.

    Formal constraints such as co-occurrence and other constraints that can be
    computationally evaluated within the context of the instance.
    """

    resource_type = "ElementDefinitionConstraint"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.expression = None
        """ FHIRPath expression of constraint.
        Type `str`. """

        self.human = None
        """ Human description of constraint.
        Type `str`. """

        self.key = None
        """ Target of 'condition' reference above.
        Type `str`. """

        self.requirements = None
        """ Why this constraint is necessary or appropriate.
        Type `str`. """

        self.severity = None
        """ error | warning.
        Type `str`. """

        self.source = None
        """ Reference to original source of constraint.
        Type `str`. """

        self.xpath = None
        """ XPath expression of constraint.
        Type `str`. """

        super(ElementDefinitionConstraint, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(ElementDefinitionConstraint, self).elementProperties()
        js.extend(
            [
                ("expression", "expression", str, "string", False, None, True),
                ("human", "human", str, "string", False, None, True),
                ("key", "key", str, "id", False, None, True),
                ("requirements", "requirements", str, "string", False, None, False),
                ("severity", "severity", str, "code", False, None, True),
                ("source", "source", str, "uri", False, None, False),
                ("xpath", "xpath", str, "string", False, None, False),
            ]
        )
        return js


class ElementDefinitionExample(element.Element):
    """ Example value (as defined for type).

    A sample value for this element demonstrating the type of information that
    would typically be found in the element.
    """

    resource_type = "ElementDefinitionExample"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.label = None
        """ Describes the purpose of this example.
        Type `str`. """

        self.valueAddress = None
        """ Value of Example (one of allowed types).
        Type `Address` (represented as `dict` in JSON). """

        self.valueAge = None
        """ Value of Example (one of allowed types).
        Type `Age` (represented as `dict` in JSON). """

        self.valueAnnotation = None
        """ Value of Example (one of allowed types).
        Type `Annotation` (represented as `dict` in JSON). """

        self.valueAttachment = None
        """ Value of Example (one of allowed types).
        Type `Attachment` (represented as `dict` in JSON). """

        self.valueBase64Binary = None
        """ Value of Example (one of allowed types).
        Type `str`. """

        self.valueBoolean = None
        """ Value of Example (one of allowed types).
        Type `bool`. """

        self.valueCode = None
        """ Value of Example (one of allowed types).
        Type `str`. """

        self.valueCodeableConcept = None
        """ Value of Example (one of allowed types).
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.valueCoding = None
        """ Value of Example (one of allowed types).
        Type `Coding` (represented as `dict` in JSON). """

        self.valueContactPoint = None
        """ Value of Example (one of allowed types).
        Type `ContactPoint` (represented as `dict` in JSON). """

        self.valueCount = None
        """ Value of Example (one of allowed types).
        Type `Count` (represented as `dict` in JSON). """

        self.valueDate = None
        """ Value of Example (one of allowed types).
        Type `FHIRDate` (represented as `str` in JSON). """

        self.valueDateTime = None
        """ Value of Example (one of allowed types).
        Type `FHIRDate` (represented as `str` in JSON). """

        self.valueDecimal = None
        """ Value of Example (one of allowed types).
        Type `float`. """

        self.valueDistance = None
        """ Value of Example (one of allowed types).
        Type `Distance` (represented as `dict` in JSON). """

        self.valueDuration = None
        """ Value of Example (one of allowed types).
        Type `Duration` (represented as `dict` in JSON). """

        self.valueHumanName = None
        """ Value of Example (one of allowed types).
        Type `HumanName` (represented as `dict` in JSON). """

        self.valueId = None
        """ Value of Example (one of allowed types).
        Type `str`. """

        self.valueIdentifier = None
        """ Value of Example (one of allowed types).
        Type `Identifier` (represented as `dict` in JSON). """

        self.valueInstant = None
        """ Value of Example (one of allowed types).
        Type `FHIRDate` (represented as `str` in JSON). """

        self.valueInteger = None
        """ Value of Example (one of allowed types).
        Type `int`. """

        self.valueMarkdown = None
        """ Value of Example (one of allowed types).
        Type `str`. """

        self.valueMeta = None
        """ Value of Example (one of allowed types).
        Type `Meta` (represented as `dict` in JSON). """

        self.valueMoney = None
        """ Value of Example (one of allowed types).
        Type `Money` (represented as `dict` in JSON). """

        self.valueOid = None
        """ Value of Example (one of allowed types).
        Type `str`. """

        self.valuePeriod = None
        """ Value of Example (one of allowed types).
        Type `Period` (represented as `dict` in JSON). """

        self.valuePositiveInt = None
        """ Value of Example (one of allowed types).
        Type `int`. """

        self.valueQuantity = None
        """ Value of Example (one of allowed types).
        Type `Quantity` (represented as `dict` in JSON). """

        self.valueRange = None
        """ Value of Example (one of allowed types).
        Type `Range` (represented as `dict` in JSON). """

        self.valueRatio = None
        """ Value of Example (one of allowed types).
        Type `Ratio` (represented as `dict` in JSON). """

        self.valueReference = None
        """ Value of Example (one of allowed types).
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.valueSampledData = None
        """ Value of Example (one of allowed types).
        Type `SampledData` (represented as `dict` in JSON). """

        self.valueSignature = None
        """ Value of Example (one of allowed types).
        Type `Signature` (represented as `dict` in JSON). """

        self.valueString = None
        """ Value of Example (one of allowed types).
        Type `str`. """

        self.valueTime = None
        """ Value of Example (one of allowed types).
        Type `FHIRDate` (represented as `str` in JSON). """

        self.valueTiming = None
        """ Value of Example (one of allowed types).
        Type `Timing` (represented as `dict` in JSON). """

        self.valueUnsignedInt = None
        """ Value of Example (one of allowed types).
        Type `int`. """

        self.valueUri = None
        """ Value of Example (one of allowed types).
        Type `str`. """

        super(ElementDefinitionExample, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ElementDefinitionExample, self).elementProperties()
        js.extend(
            [
                ("label", "label", str, "string", False, None, True),
                (
                    "valueAddress",
                    "valueAddress",
                    address.Address,
                    "Address",
                    False,
                    "value",
                    True,
                ),
                ("valueAge", "valueAge", age.Age, "Age", False, "value", True),
                (
                    "valueAnnotation",
                    "valueAnnotation",
                    annotation.Annotation,
                    "Annotation",
                    False,
                    "value",
                    True,
                ),
                (
                    "valueAttachment",
                    "valueAttachment",
                    attachment.Attachment,
                    "Attachment",
                    False,
                    "value",
                    True,
                ),
                (
                    "valueBase64Binary",
                    "valueBase64Binary",
                    str,
                    "base64Binary",
                    False,
                    "value",
                    True,
                ),
                ("valueBoolean", "valueBoolean", bool, "boolean", False, "value", True),
                ("valueCode", "valueCode", str, "code", False, "value", True),
                (
                    "valueCodeableConcept",
                    "valueCodeableConcept",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    "value",
                    True,
                ),
                (
                    "valueCoding",
                    "valueCoding",
                    coding.Coding,
                    "Coding",
                    False,
                    "value",
                    True,
                ),
                (
                    "valueContactPoint",
                    "valueContactPoint",
                    contactpoint.ContactPoint,
                    "ContactPoint",
                    False,
                    "value",
                    True,
                ),
                (
                    "valueCount",
                    "valueCount",
                    count.Count,
                    "Count",
                    False,
                    "value",
                    True,
                ),
                (
                    "valueDate",
                    "valueDate",
                    fhirdate.FHIRDate,
                    "date",
                    False,
                    "value",
                    True,
                ),
                (
                    "valueDateTime",
                    "valueDateTime",
                    fhirdate.FHIRDate,
                    "dateTime",
                    False,
                    "value",
                    True,
                ),
                (
                    "valueDecimal",
                    "valueDecimal",
                    float,
                    "decimal",
                    False,
                    "value",
                    True,
                ),
                (
                    "valueDistance",
                    "valueDistance",
                    distance.Distance,
                    "Distance",
                    False,
                    "value",
                    True,
                ),
                (
                    "valueDuration",
                    "valueDuration",
                    duration.Duration,
                    "Duration",
                    False,
                    "value",
                    True,
                ),
                (
                    "valueHumanName",
                    "valueHumanName",
                    humanname.HumanName,
                    "HumanName",
                    False,
                    "value",
                    True,
                ),
                ("valueId", "valueId", str, "id", False, "value", True),
                (
                    "valueIdentifier",
                    "valueIdentifier",
                    identifier.Identifier,
                    "Identifier",
                    False,
                    "value",
                    True,
                ),
                (
                    "valueInstant",
                    "valueInstant",
                    fhirdate.FHIRDate,
                    "instant",
                    False,
                    "value",
                    True,
                ),
                ("valueInteger", "valueInteger", int, "integer", False, "value", True),
                (
                    "valueMarkdown",
                    "valueMarkdown",
                    str,
                    "markdown",
                    False,
                    "value",
                    True,
                ),
                ("valueMeta", "valueMeta", meta.Meta, "Meta", False, "value", True),
                (
                    "valueMoney",
                    "valueMoney",
                    money.Money,
                    "Money",
                    False,
                    "value",
                    True,
                ),
                ("valueOid", "valueOid", str, "oid", False, "value", True),
                (
                    "valuePeriod",
                    "valuePeriod",
                    period.Period,
                    "Period",
                    False,
                    "value",
                    True,
                ),
                (
                    "valuePositiveInt",
                    "valuePositiveInt",
                    int,
                    "positiveInt",
                    False,
                    "value",
                    True,
                ),
                (
                    "valueQuantity",
                    "valueQuantity",
                    quantity.Quantity,
                    "Quantity",
                    False,
                    "value",
                    True,
                ),
                (
                    "valueRange",
                    "valueRange",
                    range.Range,
                    "Range",
                    False,
                    "value",
                    True,
                ),
                (
                    "valueRatio",
                    "valueRatio",
                    ratio.Ratio,
                    "Ratio",
                    False,
                    "value",
                    True,
                ),
                (
                    "valueReference",
                    "valueReference",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    "value",
                    True,
                ),
                (
                    "valueSampledData",
                    "valueSampledData",
                    sampleddata.SampledData,
                    "SampledData",
                    False,
                    "value",
                    True,
                ),
                (
                    "valueSignature",
                    "valueSignature",
                    signature.Signature,
                    "Signature",
                    False,
                    "value",
                    True,
                ),
                ("valueString", "valueString", str, "string", False, "value", True),
                (
                    "valueTime",
                    "valueTime",
                    fhirdate.FHIRDate,
                    "time",
                    False,
                    "value",
                    True,
                ),
                (
                    "valueTiming",
                    "valueTiming",
                    timing.Timing,
                    "Timing",
                    False,
                    "value",
                    True,
                ),
                (
                    "valueUnsignedInt",
                    "valueUnsignedInt",
                    int,
                    "unsignedInt",
                    False,
                    "value",
                    True,
                ),
                ("valueUri", "valueUri", str, "uri", False, "value", True),
            ]
        )
        return js


class ElementDefinitionMapping(element.Element):
    """ Map element to another set of definitions.

    Identifies a concept from an external specification that roughly
    corresponds to this element.
    """

    resource_type = "ElementDefinitionMapping"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.comment = None
        """ Comments about the mapping or its use.
        Type `str`. """

        self.identity = None
        """ Reference to mapping declaration.
        Type `str`. """

        self.language = None
        """ Computable language of mapping.
        Type `str`. """

        self.map = None
        """ Details of the mapping.
        Type `str`. """

        super(ElementDefinitionMapping, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ElementDefinitionMapping, self).elementProperties()
        js.extend(
            [
                ("comment", "comment", str, "string", False, None, False),
                ("identity", "identity", str, "id", False, None, True),
                ("language", "language", str, "code", False, None, False),
                ("map", "map", str, "string", False, None, True),
            ]
        )
        return js


class ElementDefinitionSlicing(element.Element):
    """ This element is sliced - slices follow.

    Indicates that the element is sliced into a set of alternative definitions
    (i.e. in a structure definition, there are multiple different constraints
    on a single element in the base resource). Slicing can be used in any
    resource that has cardinality ..* on the base resource, or any resource
    with a choice of types. The set of slices is any elements that come after
    this in the element sequence that have the same path, until a shorter path
    occurs (the shorter path terminates the set).
    """

    resource_type = "ElementDefinitionSlicing"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.description = None
        """ Text description of how slicing works (or not).
        Type `str`. """

        self.discriminator = None
        """ Element values that are used to distinguish the slices.
        List of `ElementDefinitionSlicingDiscriminator` items (represented as `dict` in JSON). """

        self.ordered = None
        """ If elements must be in same order as slices.
        Type `bool`. """

        self.rules = None
        """ closed | open | openAtEnd.
        Type `str`. """

        super(ElementDefinitionSlicing, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ElementDefinitionSlicing, self).elementProperties()
        js.extend(
            [
                ("description", "description", str, "string", False, None, False),
                (
                    "discriminator",
                    "discriminator",
                    ElementDefinitionSlicingDiscriminator,
                    "ElementDefinitionSlicingDiscriminator",
                    True,
                    None,
                    False,
                ),
                ("ordered", "ordered", bool, "boolean", False, None, False),
                ("rules", "rules", str, "code", False, None, True),
            ]
        )
        return js


class ElementDefinitionSlicingDiscriminator(element.Element):
    """ Element values that are used to distinguish the slices.

    Designates which child elements are used to discriminate between the slices
    when processing an instance. If one or more discriminators are provided,
    the value of the child elements in the instance data SHALL completely
    distinguish which slice the element in the resource matches based on the
    allowed values for those elements in each of the slices.
    """

    resource_type = "ElementDefinitionSlicingDiscriminator"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.path = None
        """ Path to element value.
        Type `str`. """

        self.type = None
        """ value | exists | pattern | type | profile.
        Type `str`. """

        super(ElementDefinitionSlicingDiscriminator, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(ElementDefinitionSlicingDiscriminator, self).elementProperties()
        js.extend(
            [
                ("path", "path", str, "string", False, None, True),
                ("type", "type", str, "code", False, None, True),
            ]
        )
        return js


class ElementDefinitionType(element.Element):
    """ Data type and Profile for this element.

    The data type or resource that the value of this element is permitted to
    be.
    """

    resource_type = "ElementDefinitionType"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.aggregation = None
        """ contained | referenced | bundled - how aggregated.
        List of `str` items. """

        self.code = None
        """ Data type or Resource (reference to definition).
        Type `str`. """

        self.profile = None
        """ Profile (StructureDefinition) to apply (or IG).
        Type `str`. """

        self.targetProfile = None
        """ Profile (StructureDefinition) to apply to reference target (or IG).
        Type `str`. """

        self.versioning = None
        """ either | independent | specific.
        Type `str`. """

        super(ElementDefinitionType, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ElementDefinitionType, self).elementProperties()
        js.extend(
            [
                ("aggregation", "aggregation", str, "code", True, None, False),
                ("code", "code", str, "uri", False, None, True),
                ("profile", "profile", str, "uri", False, None, False),
                ("targetProfile", "targetProfile", str, "uri", False, None, False),
                ("versioning", "versioning", str, "code", False, None, False),
            ]
        )
        return js


try:
    from . import address
except ImportError:
    address = sys.modules[__package__ + ".address"]
try:
    from . import age
except ImportError:
    age = sys.modules[__package__ + ".age"]
try:
    from . import annotation
except ImportError:
    annotation = sys.modules[__package__ + ".annotation"]
try:
    from . import attachment
except ImportError:
    attachment = sys.modules[__package__ + ".attachment"]
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + ".codeableconcept"]
try:
    from . import coding
except ImportError:
    coding = sys.modules[__package__ + ".coding"]
try:
    from . import contactpoint
except ImportError:
    contactpoint = sys.modules[__package__ + ".contactpoint"]
try:
    from . import count
except ImportError:
    count = sys.modules[__package__ + ".count"]
try:
    from . import distance
except ImportError:
    distance = sys.modules[__package__ + ".distance"]
try:
    from . import duration
except ImportError:
    duration = sys.modules[__package__ + ".duration"]
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + ".fhirdate"]
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + ".fhirreference"]
try:
    from . import humanname
except ImportError:
    humanname = sys.modules[__package__ + ".humanname"]
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + ".identifier"]
try:
    from . import meta
except ImportError:
    meta = sys.modules[__package__ + ".meta"]
try:
    from . import money
except ImportError:
    money = sys.modules[__package__ + ".money"]
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
    from . import ratio
except ImportError:
    ratio = sys.modules[__package__ + ".ratio"]
try:
    from . import sampleddata
except ImportError:
    sampleddata = sys.modules[__package__ + ".sampleddata"]
try:
    from . import signature
except ImportError:
    signature = sys.modules[__package__ + ".signature"]
try:
    from . import timing
except ImportError:
    timing = sys.modules[__package__ + ".timing"]
