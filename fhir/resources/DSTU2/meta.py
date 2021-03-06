#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 (http://hl7.org/fhir/StructureDefinition/Meta) on 2019-05-14.
#  2019, SMART Health IT.


from . import coding, element, fhirdate


class Meta(element.Element):
    """ Metadata about a resource.
    
    The metadata about a resource. This is content in the resource that is
    maintained by the infrastructure. Changes to the content may not always be
    associated with version changes to the resource.
    """

    resource_name = "Meta"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.lastUpdated = None
        """ When the resource version last changed.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.profile = None
        """ Profiles this resource claims to conform to.
        List of `str` items. """

        self.security = None
        """ Security Labels applied to this resource.
        List of `Coding` items (represented as `dict` in JSON). """

        self.tag = None
        """ Tags applied to this resource.
        List of `Coding` items (represented as `dict` in JSON). """

        self.versionId = None
        """ Version specific identifier.
        Type `str`. """

        super(Meta, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Meta, self).elementProperties()
        js.extend(
            [
                ("lastUpdated", "lastUpdated", fhirdate.FHIRDate, False, None, False),
                ("profile", "profile", str, True, None, False),
                ("security", "security", coding.Coding, True, None, False),
                ("tag", "tag", coding.Coding, True, None, False),
                ("versionId", "versionId", str, False, None, False),
            ]
        )
        return js
