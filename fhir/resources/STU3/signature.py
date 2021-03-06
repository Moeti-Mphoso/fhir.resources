# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Signature
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""


import sys

from . import element


class Signature(element.Element):
    """ A digital Signature - XML DigSig, JWT, Graphical image of signature, etc..

    A digital signature along with supporting context. The signature may be
    electronic/cryptographic in nature, or a graphical image representing a
    hand-written signature, or a signature process. Different signature
    approaches have different utilities.
    """

    resource_type = "Signature"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.blob = None
        """ The actual signature content (XML DigSig. JWT, picture, etc.).
        Type `str`. """

        self.contentType = None
        """ The technical format of the signature.
        Type `str`. """

        self.onBehalfOfReference = None
        """ The party represented.
        Type `FHIRReference` referencing `['Practitioner'], ['RelatedPerson'], ['Patient'], ['Device'], ['Organization']` (represented as `dict` in JSON). """

        self.onBehalfOfUri = None
        """ The party represented.
        Type `str`. """

        self.type = None
        """ Indication of the reason the entity signed the object(s).
        List of `Coding` items (represented as `dict` in JSON). """

        self.when = None
        """ When the signature was created.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.whoReference = None
        """ Who signed.
        Type `FHIRReference` referencing `['Practitioner'], ['RelatedPerson'], ['Patient'], ['Device'], ['Organization']` (represented as `dict` in JSON). """

        self.whoUri = None
        """ Who signed.
        Type `str`. """

        super(Signature, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Signature, self).elementProperties()
        js.extend(
            [
                ("blob", "blob", str, "base64Binary", False, None, False),
                ("contentType", "contentType", str, "code", False, None, False),
                (
                    "onBehalfOfReference",
                    "onBehalfOfReference",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    "onBehalfOf",
                    False,
                ),
                (
                    "onBehalfOfUri",
                    "onBehalfOfUri",
                    str,
                    "uri",
                    False,
                    "onBehalfOf",
                    False,
                ),
                ("type", "type", coding.Coding, "Coding", True, None, True),
                ("when", "when", fhirdate.FHIRDate, "instant", False, None, True),
                (
                    "whoReference",
                    "whoReference",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    "who",
                    True,
                ),
                ("whoUri", "whoUri", str, "uri", False, "who", True),
            ]
        )
        return js


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
