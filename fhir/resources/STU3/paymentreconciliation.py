# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/PaymentReconciliation
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""


import sys

from . import backboneelement, domainresource


class PaymentReconciliation(domainresource.DomainResource):
    """ PaymentReconciliation resource.

    This resource provides payment details and claim references supporting a
    bulk payment.
    """

    resource_type = "PaymentReconciliation"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.created = None
        """ Creation date.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.detail = None
        """ List of settlements.
        List of `PaymentReconciliationDetail` items (represented as `dict` in JSON). """

        self.disposition = None
        """ Disposition Message.
        Type `str`. """

        self.form = None
        """ Printed Form Identifier.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.identifier = None
        """ Business Identifier.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.organization = None
        """ Insurer.
        Type `FHIRReference` referencing `['Organization']` (represented as `dict` in JSON). """

        self.outcome = None
        """ complete | error | partial.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.period = None
        """ Period covered.
        Type `Period` (represented as `dict` in JSON). """

        self.processNote = None
        """ Processing comments.
        List of `PaymentReconciliationProcessNote` items (represented as `dict` in JSON). """

        self.request = None
        """ Claim reference.
        Type `FHIRReference` referencing `['ProcessRequest']` (represented as `dict` in JSON). """

        self.requestOrganization = None
        """ Responsible organization.
        Type `FHIRReference` referencing `['Organization']` (represented as `dict` in JSON). """

        self.requestProvider = None
        """ Responsible practitioner.
        Type `FHIRReference` referencing `['Practitioner']` (represented as `dict` in JSON). """

        self.status = None
        """ active | cancelled | draft | entered-in-error.
        Type `str`. """

        self.total = None
        """ Total amount of Payment.
        Type `Money` (represented as `dict` in JSON). """

        super(PaymentReconciliation, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(PaymentReconciliation, self).elementProperties()
        js.extend(
            [
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
                    "detail",
                    "detail",
                    PaymentReconciliationDetail,
                    "PaymentReconciliationDetail",
                    True,
                    None,
                    False,
                ),
                ("disposition", "disposition", str, "string", False, None, False),
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
                ("period", "period", period.Period, "Period", False, None, False),
                (
                    "processNote",
                    "processNote",
                    PaymentReconciliationProcessNote,
                    "PaymentReconciliationProcessNote",
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
                ("total", "total", money.Money, "Money", False, None, False),
            ]
        )
        return js


class PaymentReconciliationDetail(backboneelement.BackboneElement):
    """ List of settlements.

    List of individual settlement amounts and the corresponding transaction.
    """

    resource_type = "PaymentReconciliationDetail"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.amount = None
        """ Amount being paid.
        Type `Money` (represented as `dict` in JSON). """

        self.date = None
        """ Invoice date.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.payee = None
        """ Organization which is receiving the payment.
        Type `FHIRReference` referencing `['Organization']` (represented as `dict` in JSON). """

        self.request = None
        """ Claim.
        Type `FHIRReference` referencing `['Resource']` (represented as `dict` in JSON). """

        self.response = None
        """ Claim Response.
        Type `FHIRReference` referencing `['Resource']` (represented as `dict` in JSON). """

        self.submitter = None
        """ Organization which submitted the claim.
        Type `FHIRReference` referencing `['Organization']` (represented as `dict` in JSON). """

        self.type = None
        """ Type code.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        super(PaymentReconciliationDetail, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(PaymentReconciliationDetail, self).elementProperties()
        js.extend(
            [
                ("amount", "amount", money.Money, "Money", False, None, False),
                ("date", "date", fhirdate.FHIRDate, "date", False, None, False),
                (
                    "payee",
                    "payee",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
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
                    "response",
                    "response",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                (
                    "submitter",
                    "submitter",
                    fhirreference.FHIRReference,
                    "Reference",
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
                    True,
                ),
            ]
        )
        return js


class PaymentReconciliationProcessNote(backboneelement.BackboneElement):
    """ Processing comments.

    Suite of notes.
    """

    resource_type = "PaymentReconciliationProcessNote"

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

        super(PaymentReconciliationProcessNote, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(PaymentReconciliationProcessNote, self).elementProperties()
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
try:
    from . import money
except ImportError:
    money = sys.modules[__package__ + ".money"]
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + ".period"]
