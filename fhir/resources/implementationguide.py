# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ImplementationGuide
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""


import sys

from . import backboneelement, domainresource


class ImplementationGuide(domainresource.DomainResource):
    """ A set of rules about how FHIR is used.

    A set of rules of how a particular interoperability or standards problem is
    solved - typically through the use of FHIR resources. This resource is used
    to gather all the parts of an implementation guide into a logical whole and
    to publish a computable definition of all the parts.
    """

    resource_type = "ImplementationGuide"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.contact = None
        """ Contact details for the publisher.
        List of `ContactDetail` items (represented as `dict` in JSON). """

        self.copyright = None
        """ Use and/or publishing restrictions.
        Type `str`. """

        self.date = None
        """ Date last changed.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.definition = None
        """ Information needed to build the IG.
        Type `ImplementationGuideDefinition` (represented as `dict` in JSON). """

        self.dependsOn = None
        """ Another Implementation guide this depends on.
        List of `ImplementationGuideDependsOn` items (represented as `dict` in JSON). """

        self.description = None
        """ Natural language description of the implementation guide.
        Type `str`. """

        self.experimental = None
        """ For testing purposes, not real usage.
        Type `bool`. """

        self.fhirVersion = None
        """ FHIR Version(s) this Implementation Guide targets.
        List of `str` items. """

        self.global_fhir = None
        """ Profiles that apply globally.
        List of `ImplementationGuideGlobal` items (represented as `dict` in JSON). """

        self.jurisdiction = None
        """ Intended jurisdiction for implementation guide (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.license = None
        """ SPDX license code for this IG (or not-open-source).
        Type `str`. """

        self.manifest = None
        """ Information about an assembled IG.
        Type `ImplementationGuideManifest` (represented as `dict` in JSON). """

        self.name = None
        """ Name for this implementation guide (computer friendly).
        Type `str`. """

        self.packageId = None
        """ NPM Package name for IG.
        Type `str`. """

        self.publisher = None
        """ Name of the publisher (organization or individual).
        Type `str`. """

        self.status = None
        """ draft | active | retired | unknown.
        Type `str`. """

        self.title = None
        """ Name for this implementation guide (human friendly).
        Type `str`. """

        self.url = None
        """ Canonical identifier for this implementation guide, represented as
        a URI (globally unique).
        Type `str`. """

        self.useContext = None
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """

        self.version = None
        """ Business version of the implementation guide.
        Type `str`. """

        super(ImplementationGuide, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ImplementationGuide, self).elementProperties()
        js.extend(
            [
                (
                    "contact",
                    "contact",
                    contactdetail.ContactDetail,
                    "ContactDetail",
                    True,
                    None,
                    False,
                ),
                ("copyright", "copyright", str, "markdown", False, None, False),
                ("date", "date", fhirdate.FHIRDate, "dateTime", False, None, False),
                (
                    "definition",
                    "definition",
                    ImplementationGuideDefinition,
                    "ImplementationGuideDefinition",
                    False,
                    None,
                    False,
                ),
                (
                    "dependsOn",
                    "dependsOn",
                    ImplementationGuideDependsOn,
                    "ImplementationGuideDependsOn",
                    True,
                    None,
                    False,
                ),
                ("description", "description", str, "markdown", False, None, False),
                ("experimental", "experimental", bool, "boolean", False, None, False),
                ("fhirVersion", "fhirVersion", str, "code", True, None, True),
                (
                    "global_fhir",
                    "global",
                    ImplementationGuideGlobal,
                    "ImplementationGuideGlobal",
                    True,
                    None,
                    False,
                ),
                (
                    "jurisdiction",
                    "jurisdiction",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    True,
                    None,
                    False,
                ),
                ("license", "license", str, "code", False, None, False),
                (
                    "manifest",
                    "manifest",
                    ImplementationGuideManifest,
                    "ImplementationGuideManifest",
                    False,
                    None,
                    False,
                ),
                ("name", "name", str, "string", False, None, True),
                ("packageId", "packageId", str, "id", False, None, True),
                ("publisher", "publisher", str, "string", False, None, False),
                ("status", "status", str, "code", False, None, True),
                ("title", "title", str, "string", False, None, False),
                ("url", "url", str, "uri", False, None, True),
                (
                    "useContext",
                    "useContext",
                    usagecontext.UsageContext,
                    "UsageContext",
                    True,
                    None,
                    False,
                ),
                ("version", "version", str, "string", False, None, False),
            ]
        )
        return js


class ImplementationGuideDefinition(backboneelement.BackboneElement):
    """ Information needed to build the IG.

    The information needed by an IG publisher tool to publish the whole
    implementation guide.
    """

    resource_type = "ImplementationGuideDefinition"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.grouping = None
        """ Grouping used to present related resources in the IG.
        List of `ImplementationGuideDefinitionGrouping` items (represented as `dict` in JSON). """

        self.page = None
        """ Page/Section in the Guide.
        Type `ImplementationGuideDefinitionPage` (represented as `dict` in JSON). """

        self.parameter = None
        """ Defines how IG is built by tools.
        List of `ImplementationGuideDefinitionParameter` items (represented as `dict` in JSON). """

        self.resource = None
        """ Resource in the implementation guide.
        List of `ImplementationGuideDefinitionResource` items (represented as `dict` in JSON). """

        self.template = None
        """ A template for building resources.
        List of `ImplementationGuideDefinitionTemplate` items (represented as `dict` in JSON). """

        super(ImplementationGuideDefinition, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(ImplementationGuideDefinition, self).elementProperties()
        js.extend(
            [
                (
                    "grouping",
                    "grouping",
                    ImplementationGuideDefinitionGrouping,
                    "ImplementationGuideDefinitionGrouping",
                    True,
                    None,
                    False,
                ),
                (
                    "page",
                    "page",
                    ImplementationGuideDefinitionPage,
                    "ImplementationGuideDefinitionPage",
                    False,
                    None,
                    False,
                ),
                (
                    "parameter",
                    "parameter",
                    ImplementationGuideDefinitionParameter,
                    "ImplementationGuideDefinitionParameter",
                    True,
                    None,
                    False,
                ),
                (
                    "resource",
                    "resource",
                    ImplementationGuideDefinitionResource,
                    "ImplementationGuideDefinitionResource",
                    True,
                    None,
                    True,
                ),
                (
                    "template",
                    "template",
                    ImplementationGuideDefinitionTemplate,
                    "ImplementationGuideDefinitionTemplate",
                    True,
                    None,
                    False,
                ),
            ]
        )
        return js


class ImplementationGuideDefinitionGrouping(backboneelement.BackboneElement):
    """ Grouping used to present related resources in the IG.

    A logical group of resources. Logical groups can be used when building
    pages.
    """

    resource_type = "ImplementationGuideDefinitionGrouping"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.description = None
        """ Human readable text describing the package.
        Type `str`. """

        self.name = None
        """ Descriptive name for the package.
        Type `str`. """

        super(ImplementationGuideDefinitionGrouping, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(ImplementationGuideDefinitionGrouping, self).elementProperties()
        js.extend(
            [
                ("description", "description", str, "string", False, None, False),
                ("name", "name", str, "string", False, None, True),
            ]
        )
        return js


class ImplementationGuideDefinitionPage(backboneelement.BackboneElement):
    """ Page/Section in the Guide.

    A page / section in the implementation guide. The root page is the
    implementation guide home page.
    """

    resource_type = "ImplementationGuideDefinitionPage"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.generation = None
        """ html | markdown | xml | generated.
        Type `str`. """

        self.nameReference = None
        """ Where to find that page.
        Type `FHIRReference` referencing `['Binary']` (represented as `dict` in JSON). """

        self.nameUrl = None
        """ Where to find that page.
        Type `str`. """

        self.page = None
        """ Nested Pages / Sections.
        List of `ImplementationGuideDefinitionPage` items (represented as `dict` in JSON). """

        self.title = None
        """ Short title shown for navigational assistance.
        Type `str`. """

        super(ImplementationGuideDefinitionPage, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(ImplementationGuideDefinitionPage, self).elementProperties()
        js.extend(
            [
                ("generation", "generation", str, "code", False, None, True),
                (
                    "nameReference",
                    "nameReference",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    "name",
                    True,
                ),
                ("nameUrl", "nameUrl", str, "url", False, "name", True),
                (
                    "page",
                    "page",
                    ImplementationGuideDefinitionPage,
                    "ImplementationGuideDefinitionPage",
                    True,
                    None,
                    False,
                ),
                ("title", "title", str, "string", False, None, True),
            ]
        )
        return js


class ImplementationGuideDefinitionParameter(backboneelement.BackboneElement):
    """ Defines how IG is built by tools.
    """

    resource_type = "ImplementationGuideDefinitionParameter"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.code = None
        """ apply | path-resource | path-pages | path-tx-cache | expansion-
        parameter | rule-broken-links | generate-xml | generate-json |
        generate-turtle | html-template.
        Type `str`. """

        self.value = None
        """ Value for named type.
        Type `str`. """

        super(ImplementationGuideDefinitionParameter, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(ImplementationGuideDefinitionParameter, self).elementProperties()
        js.extend(
            [
                ("code", "code", str, "code", False, None, True),
                ("value", "value", str, "string", False, None, True),
            ]
        )
        return js


class ImplementationGuideDefinitionResource(backboneelement.BackboneElement):
    """ Resource in the implementation guide.

    A resource that is part of the implementation guide. Conformance resources
    (value set, structure definition, capability statements etc.) are obvious
    candidates for inclusion, but any kind of resource can be included as an
    example resource.
    """

    resource_type = "ImplementationGuideDefinitionResource"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.description = None
        """ Reason why included in guide.
        Type `str`. """

        self.exampleBoolean = None
        """ Is an example/What is this an example of?.
        Type `bool`. """

        self.exampleCanonical = None
        """ Is an example/What is this an example of?.
        Type `str` referencing `['StructureDefinition']`. """

        self.fhirVersion = None
        """ Versions this applies to (if different to IG).
        List of `str` items. """

        self.groupingId = None
        """ Grouping this is part of.
        Type `str`. """

        self.name = None
        """ Human Name for the resource.
        Type `str`. """

        self.reference = None
        """ Location of the resource.
        Type `FHIRReference` referencing `['Resource']` (represented as `dict` in JSON). """

        super(ImplementationGuideDefinitionResource, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(ImplementationGuideDefinitionResource, self).elementProperties()
        js.extend(
            [
                ("description", "description", str, "string", False, None, False),
                (
                    "exampleBoolean",
                    "exampleBoolean",
                    bool,
                    "boolean",
                    False,
                    "example",
                    False,
                ),
                (
                    "exampleCanonical",
                    "exampleCanonical",
                    str,
                    "canonical",
                    False,
                    "example",
                    False,
                ),
                ("fhirVersion", "fhirVersion", str, "code", True, None, False),
                ("groupingId", "groupingId", str, "id", False, None, False),
                ("name", "name", str, "string", False, None, False),
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


class ImplementationGuideDefinitionTemplate(backboneelement.BackboneElement):
    """ A template for building resources.
    """

    resource_type = "ImplementationGuideDefinitionTemplate"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.code = None
        """ Type of template specified.
        Type `str`. """

        self.scope = None
        """ The scope in which the template applies.
        Type `str`. """

        self.source = None
        """ The source location for the template.
        Type `str`. """

        super(ImplementationGuideDefinitionTemplate, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(ImplementationGuideDefinitionTemplate, self).elementProperties()
        js.extend(
            [
                ("code", "code", str, "code", False, None, True),
                ("scope", "scope", str, "string", False, None, False),
                ("source", "source", str, "string", False, None, True),
            ]
        )
        return js


class ImplementationGuideDependsOn(backboneelement.BackboneElement):
    """ Another Implementation guide this depends on.

    Another implementation guide that this implementation depends on.
    Typically, an implementation guide uses value sets, profiles etc.defined in
    other implementation guides.
    """

    resource_type = "ImplementationGuideDependsOn"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.packageId = None
        """ NPM Package name for IG this depends on.
        Type `str`. """

        self.uri = None
        """ Identity of the IG that this depends on.
        Type `str` referencing `['ImplementationGuide']`. """

        self.version = None
        """ Version of the IG.
        Type `str`. """

        super(ImplementationGuideDependsOn, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(ImplementationGuideDependsOn, self).elementProperties()
        js.extend(
            [
                ("packageId", "packageId", str, "id", False, None, False),
                ("uri", "uri", str, "canonical", False, None, True),
                ("version", "version", str, "string", False, None, False),
            ]
        )
        return js


class ImplementationGuideGlobal(backboneelement.BackboneElement):
    """ Profiles that apply globally.

    A set of profiles that all resources covered by this implementation guide
    must conform to.
    """

    resource_type = "ImplementationGuideGlobal"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.profile = None
        """ Profile that all resources must conform to.
        Type `str` referencing `['StructureDefinition']`. """

        self.type = None
        """ Type this profile applies to.
        Type `str`. """

        super(ImplementationGuideGlobal, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(ImplementationGuideGlobal, self).elementProperties()
        js.extend(
            [
                ("profile", "profile", str, "canonical", False, None, True),
                ("type", "type", str, "code", False, None, True),
            ]
        )
        return js


class ImplementationGuideManifest(backboneelement.BackboneElement):
    """ Information about an assembled IG.

    Information about an assembled implementation guide, created by the
    publication tooling.
    """

    resource_type = "ImplementationGuideManifest"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.image = None
        """ Image within the IG.
        List of `str` items. """

        self.other = None
        """ Additional linkable file in IG.
        List of `str` items. """

        self.page = None
        """ HTML page within the parent IG.
        List of `ImplementationGuideManifestPage` items (represented as `dict` in JSON). """

        self.rendering = None
        """ Location of rendered implementation guide.
        Type `str`. """

        self.resource = None
        """ Resource in the implementation guide.
        List of `ImplementationGuideManifestResource` items (represented as `dict` in JSON). """

        super(ImplementationGuideManifest, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(ImplementationGuideManifest, self).elementProperties()
        js.extend(
            [
                ("image", "image", str, "string", True, None, False),
                ("other", "other", str, "string", True, None, False),
                (
                    "page",
                    "page",
                    ImplementationGuideManifestPage,
                    "ImplementationGuideManifestPage",
                    True,
                    None,
                    False,
                ),
                ("rendering", "rendering", str, "url", False, None, False),
                (
                    "resource",
                    "resource",
                    ImplementationGuideManifestResource,
                    "ImplementationGuideManifestResource",
                    True,
                    None,
                    True,
                ),
            ]
        )
        return js


class ImplementationGuideManifestPage(backboneelement.BackboneElement):
    """ HTML page within the parent IG.

    Information about a page within the IG.
    """

    resource_type = "ImplementationGuideManifestPage"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.anchor = None
        """ Anchor available on the page.
        List of `str` items. """

        self.name = None
        """ HTML page name.
        Type `str`. """

        self.title = None
        """ Title of the page, for references.
        Type `str`. """

        super(ImplementationGuideManifestPage, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(ImplementationGuideManifestPage, self).elementProperties()
        js.extend(
            [
                ("anchor", "anchor", str, "string", True, None, False),
                ("name", "name", str, "string", False, None, True),
                ("title", "title", str, "string", False, None, False),
            ]
        )
        return js


class ImplementationGuideManifestResource(backboneelement.BackboneElement):
    """ Resource in the implementation guide.

    A resource that is part of the implementation guide. Conformance resources
    (value set, structure definition, capability statements etc.) are obvious
    candidates for inclusion, but any kind of resource can be included as an
    example resource.
    """

    resource_type = "ImplementationGuideManifestResource"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.exampleBoolean = None
        """ Is an example/What is this an example of?.
        Type `bool`. """

        self.exampleCanonical = None
        """ Is an example/What is this an example of?.
        Type `str` referencing `['StructureDefinition']`. """

        self.reference = None
        """ Location of the resource.
        Type `FHIRReference` referencing `['Resource']` (represented as `dict` in JSON). """

        self.relativePath = None
        """ Relative path for page in IG.
        Type `str`. """

        super(ImplementationGuideManifestResource, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(ImplementationGuideManifestResource, self).elementProperties()
        js.extend(
            [
                (
                    "exampleBoolean",
                    "exampleBoolean",
                    bool,
                    "boolean",
                    False,
                    "example",
                    False,
                ),
                (
                    "exampleCanonical",
                    "exampleCanonical",
                    str,
                    "canonical",
                    False,
                    "example",
                    False,
                ),
                (
                    "reference",
                    "reference",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    True,
                ),
                ("relativePath", "relativePath", str, "url", False, None, False),
            ]
        )
        return js


try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + ".codeableconcept"]
try:
    from . import contactdetail
except ImportError:
    contactdetail = sys.modules[__package__ + ".contactdetail"]
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + ".fhirdate"]
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + ".fhirreference"]
try:
    from . import usagecontext
except ImportError:
    usagecontext = sys.modules[__package__ + ".usagecontext"]
