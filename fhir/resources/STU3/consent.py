# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Consent
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""


import sys

from . import backboneelement, domainresource


class Consent(domainresource.DomainResource):
    """ A healthcare consumer's policy choices to permits or denies recipients or
    roles to perform actions for specific purposes and periods of time.

    A record of a healthcare consumer’s policy choices, which permits or denies
    identified recipient(s) or recipient role(s) to perform one or more actions
    within a given policy context, for specific purposes and periods of time.
    """

    resource_type = "Consent"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.action = None
        """ Actions controlled by this consent.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.actor = None
        """ Who|what controlled by this consent (or group, by role).
        List of `ConsentActor` items (represented as `dict` in JSON). """

        self.category = None
        """ Classification of the consent statement - for indexing/retrieval.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.consentingParty = None
        """ Who is agreeing to the policy and exceptions.
        List of `FHIRReference` items referencing `['Organization'], ['Patient'], ['Practitioner'], ['RelatedPerson']` (represented as `dict` in JSON). """

        self.data = None
        """ Data controlled by this consent.
        List of `ConsentData` items (represented as `dict` in JSON). """

        self.dataPeriod = None
        """ Timeframe for data controlled by this consent.
        Type `Period` (represented as `dict` in JSON). """

        self.dateTime = None
        """ When this Consent was created or indexed.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.except_fhir = None
        """ Additional rule -  addition or removal of permissions.
        List of `ConsentExcept` items (represented as `dict` in JSON). """

        self.identifier = None
        """ Identifier for this record (external references).
        Type `Identifier` (represented as `dict` in JSON). """

        self.organization = None
        """ Custodian of the consent.
        List of `FHIRReference` items referencing `['Organization']` (represented as `dict` in JSON). """

        self.patient = None
        """ Who the consent applies to.
        Type `FHIRReference` referencing `['Patient']` (represented as `dict` in JSON). """

        self.period = None
        """ Period that this consent applies.
        Type `Period` (represented as `dict` in JSON). """

        self.policy = None
        """ Policies covered by this consent.
        List of `ConsentPolicy` items (represented as `dict` in JSON). """

        self.policyRule = None
        """ Policy that this consents to.
        Type `str`. """

        self.purpose = None
        """ Context of activities for which the agreement is made.
        List of `Coding` items (represented as `dict` in JSON). """

        self.securityLabel = None
        """ Security Labels that define affected resources.
        List of `Coding` items (represented as `dict` in JSON). """

        self.sourceAttachment = None
        """ Source from which this consent is taken.
        Type `Attachment` (represented as `dict` in JSON). """

        self.sourceIdentifier = None
        """ Source from which this consent is taken.
        Type `Identifier` (represented as `dict` in JSON). """

        self.sourceReference = None
        """ Source from which this consent is taken.
        Type `FHIRReference` referencing `['Consent'], ['DocumentReference'], ['Contract'], ['QuestionnaireResponse']` (represented as `dict` in JSON). """

        self.status = None
        """ draft | proposed | active | rejected | inactive | entered-in-error.
        Type `str`. """

        super(Consent, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Consent, self).elementProperties()
        js.extend(
            [
                (
                    "action",
                    "action",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    True,
                    None,
                    False,
                ),
                ("actor", "actor", ConsentActor, "ConsentActor", True, None, False),
                (
                    "category",
                    "category",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    True,
                    None,
                    False,
                ),
                (
                    "consentingParty",
                    "consentingParty",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
                ("data", "data", ConsentData, "ConsentData", True, None, False),
                (
                    "dataPeriod",
                    "dataPeriod",
                    period.Period,
                    "Period",
                    False,
                    None,
                    False,
                ),
                (
                    "dateTime",
                    "dateTime",
                    fhirdate.FHIRDate,
                    "dateTime",
                    False,
                    None,
                    False,
                ),
                (
                    "except_fhir",
                    "except",
                    ConsentExcept,
                    "ConsentExcept",
                    True,
                    None,
                    False,
                ),
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
                    "organization",
                    "organization",
                    fhirreference.FHIRReference,
                    "Reference",
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
                    True,
                ),
                ("period", "period", period.Period, "Period", False, None, False),
                ("policy", "policy", ConsentPolicy, "ConsentPolicy", True, None, False),
                ("policyRule", "policyRule", str, "uri", False, None, False),
                ("purpose", "purpose", coding.Coding, "Coding", True, None, False),
                (
                    "securityLabel",
                    "securityLabel",
                    coding.Coding,
                    "Coding",
                    True,
                    None,
                    False,
                ),
                (
                    "sourceAttachment",
                    "sourceAttachment",
                    attachment.Attachment,
                    "Attachment",
                    False,
                    "source",
                    False,
                ),
                (
                    "sourceIdentifier",
                    "sourceIdentifier",
                    identifier.Identifier,
                    "Identifier",
                    False,
                    "source",
                    False,
                ),
                (
                    "sourceReference",
                    "sourceReference",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    "source",
                    False,
                ),
                ("status", "status", str, "code", False, None, True),
            ]
        )
        return js


class ConsentActor(backboneelement.BackboneElement):
    """ Who|what controlled by this consent (or group, by role).

    Who or what is controlled by this consent. Use group to identify a set of
    actors by some property they share (e.g. 'admitting officers').
    """

    resource_type = "ConsentActor"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.reference = None
        """ Resource for the actor (or group, by role).
        Type `FHIRReference` referencing `['Device'], ['Group'], ['CareTeam'], ['Organization'], ['Patient'], ['Practitioner'], ['RelatedPerson']` (represented as `dict` in JSON). """

        self.role = None
        """ How the actor is involved.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        super(ConsentActor, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ConsentActor, self).elementProperties()
        js.extend(
            [
                (
                    "reference",
                    "reference",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    True,
                ),
                (
                    "role",
                    "role",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    True,
                ),
            ]
        )
        return js


class ConsentData(backboneelement.BackboneElement):
    """ Data controlled by this consent.

    The resources controlled by this consent, if specific resources are
    referenced.
    """

    resource_type = "ConsentData"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.meaning = None
        """ instance | related | dependents | authoredby.
        Type `str`. """

        self.reference = None
        """ The actual data reference.
        Type `FHIRReference` referencing `['Resource']` (represented as `dict` in JSON). """

        super(ConsentData, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ConsentData, self).elementProperties()
        js.extend(
            [
                ("meaning", "meaning", str, "code", False, None, True),
                (
                    "reference",
                    "reference",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    True,
                ),
            ]
        )
        return js


class ConsentExcept(backboneelement.BackboneElement):
    """ Additional rule -  addition or removal of permissions.

    An exception to the base policy of this consent. An exception can be an
    addition or removal of access permissions.
    """

    resource_type = "ConsentExcept"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.action = None
        """ Actions controlled by this exception.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.actor = None
        """ Who|what controlled by this exception (or group, by role).
        List of `ConsentExceptActor` items (represented as `dict` in JSON). """

        self.class_fhir = None
        """ e.g. Resource Type, Profile, or CDA etc.
        List of `Coding` items (represented as `dict` in JSON). """

        self.code = None
        """ e.g. LOINC or SNOMED CT code, etc in the content.
        List of `Coding` items (represented as `dict` in JSON). """

        self.data = None
        """ Data controlled by this exception.
        List of `ConsentExceptData` items (represented as `dict` in JSON). """

        self.dataPeriod = None
        """ Timeframe for data controlled by this exception.
        Type `Period` (represented as `dict` in JSON). """

        self.period = None
        """ Timeframe for this exception.
        Type `Period` (represented as `dict` in JSON). """

        self.purpose = None
        """ Context of activities covered by this exception.
        List of `Coding` items (represented as `dict` in JSON). """

        self.securityLabel = None
        """ Security Labels that define affected resources.
        List of `Coding` items (represented as `dict` in JSON). """

        self.type = None
        """ deny | permit.
        Type `str`. """

        super(ConsentExcept, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ConsentExcept, self).elementProperties()
        js.extend(
            [
                (
                    "action",
                    "action",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    True,
                    None,
                    False,
                ),
                (
                    "actor",
                    "actor",
                    ConsentExceptActor,
                    "ConsentExceptActor",
                    True,
                    None,
                    False,
                ),
                ("class_fhir", "class", coding.Coding, "Coding", True, None, False),
                ("code", "code", coding.Coding, "Coding", True, None, False),
                (
                    "data",
                    "data",
                    ConsentExceptData,
                    "ConsentExceptData",
                    True,
                    None,
                    False,
                ),
                (
                    "dataPeriod",
                    "dataPeriod",
                    period.Period,
                    "Period",
                    False,
                    None,
                    False,
                ),
                ("period", "period", period.Period, "Period", False, None, False),
                ("purpose", "purpose", coding.Coding, "Coding", True, None, False),
                (
                    "securityLabel",
                    "securityLabel",
                    coding.Coding,
                    "Coding",
                    True,
                    None,
                    False,
                ),
                ("type", "type", str, "code", False, None, True),
            ]
        )
        return js


class ConsentExceptActor(backboneelement.BackboneElement):
    """ Who|what controlled by this exception (or group, by role).

    Who or what is controlled by this Exception. Use group to identify a set of
    actors by some property they share (e.g. 'admitting officers').
    """

    resource_type = "ConsentExceptActor"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.reference = None
        """ Resource for the actor (or group, by role).
        Type `FHIRReference` referencing `['Device'], ['Group'], ['CareTeam'], ['Organization'], ['Patient'], ['Practitioner'], ['RelatedPerson']` (represented as `dict` in JSON). """

        self.role = None
        """ How the actor is involved.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        super(ConsentExceptActor, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ConsentExceptActor, self).elementProperties()
        js.extend(
            [
                (
                    "reference",
                    "reference",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    True,
                ),
                (
                    "role",
                    "role",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    True,
                ),
            ]
        )
        return js


class ConsentExceptData(backboneelement.BackboneElement):
    """ Data controlled by this exception.

    The resources controlled by this exception, if specific resources are
    referenced.
    """

    resource_type = "ConsentExceptData"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.meaning = None
        """ instance | related | dependents | authoredby.
        Type `str`. """

        self.reference = None
        """ The actual data reference.
        Type `FHIRReference` referencing `['Resource']` (represented as `dict` in JSON). """

        super(ConsentExceptData, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ConsentExceptData, self).elementProperties()
        js.extend(
            [
                ("meaning", "meaning", str, "code", False, None, True),
                (
                    "reference",
                    "reference",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    True,
                ),
            ]
        )
        return js


class ConsentPolicy(backboneelement.BackboneElement):
    """ Policies covered by this consent.

    The references to the policies that are included in this consent scope.
    Policies may be organizational, but are often defined jurisdictionally, or
    in law.
    """

    resource_type = "ConsentPolicy"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.authority = None
        """ Enforcement source for policy.
        Type `str`. """

        self.uri = None
        """ Specific policy covered by this consent.
        Type `str`. """

        super(ConsentPolicy, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ConsentPolicy, self).elementProperties()
        js.extend(
            [
                ("authority", "authority", str, "uri", False, None, False),
                ("uri", "uri", str, "uri", False, None, False),
            ]
        )
        return js


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
