# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Media
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""

import io
import json
import os
import unittest

import pytest

from .. import media
from ..fhirdate import FHIRDate
from .fixtures import force_bytes


@pytest.mark.usefixtures("base_settings")
class MediaTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get("FHIR_UNITTEST_DATADIR") or ""
        with io.open(os.path.join(datadir, filename), "r", encoding="utf-8") as handle:
            js = json.load(handle)
            self.assertEqual("Media", js["resourceType"])
        return media.Media(js)

    def testMedia1(self):
        inst = self.instantiate_from("media-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a Media instance")
        self.implMedia1(inst)

        js = inst.as_json()
        self.assertEqual("Media", js["resourceType"])
        inst2 = media.Media(js)
        self.implMedia1(inst2)

    def implMedia1(self, inst):
        self.assertEqual(
            force_bytes(inst.content.contentType), force_bytes("image/gif")
        )
        self.assertEqual(inst.content.creation.date, FHIRDate("2009-09-03").date)
        self.assertEqual(inst.content.creation.as_json(), "2009-09-03")
        self.assertEqual(force_bytes(inst.content.id), force_bytes("a1"))
        self.assertEqual(inst.frames, 1)
        self.assertEqual(inst.height, 145)
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(
            force_bytes(inst.subtype.coding[0].code), force_bytes("diagram")
        )
        self.assertEqual(
            force_bytes(inst.subtype.coding[0].system),
            force_bytes("http://hl7.org/fhir/media-subtype"),
        )
        self.assertEqual(
            force_bytes(inst.text.div),
            force_bytes(
                '<div xmlns="http://www.w3.org/1999/xhtml">Diagram for Patient Henry Levin (MRN 12345):<br/><img src="#11" alt="diagram"/></div>'
            ),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type), force_bytes("photo"))
        self.assertEqual(inst.width, 126)

    def testMedia2(self):
        inst = self.instantiate_from("media-example-dicom.json")
        self.assertIsNotNone(inst, "Must have instantiated a Media instance")
        self.implMedia2(inst)

        js = inst.as_json()
        self.assertEqual("Media", js["resourceType"])
        inst2 = media.Media(js)
        self.implMedia2(inst2)

    def implMedia2(self, inst):
        self.assertEqual(
            force_bytes(inst.content.contentType), force_bytes("application/dicom")
        )
        self.assertEqual(
            force_bytes(inst.extension[0].url),
            force_bytes("http://nema.org/fhir/extensions#0002-0010"),
        )
        self.assertEqual(
            force_bytes(inst.extension[0].valueUri),
            force_bytes("urn:oid:1.2.840.10008.1.2.1"),
        )
        self.assertEqual(inst.height, 480)
        self.assertEqual(
            force_bytes(inst.id),
            force_bytes("1.2.840.11361907579238403408700.3.0.14.19970327150033"),
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].system), force_bytes("urn:ietf:rfc:3986")
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].type.text), force_bytes("InstanceUID")
        )
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("official"))
        self.assertEqual(
            force_bytes(inst.identifier[0].value),
            force_bytes(
                "urn:oid:1.2.840.11361907579238403408700.3.0.14.19970327150033"
            ),
        )
        self.assertEqual(
            force_bytes(inst.identifier[1].system),
            force_bytes("http://acme-imaging.com/accession/2012"),
        )
        self.assertEqual(
            force_bytes(inst.identifier[1].type.text), force_bytes("accessionNo")
        )
        self.assertEqual(force_bytes(inst.identifier[1].value), force_bytes("1234567"))
        self.assertEqual(
            force_bytes(inst.identifier[2].system), force_bytes("urn:ietf:rfc:3986")
        )
        self.assertEqual(
            force_bytes(inst.identifier[2].type.text), force_bytes("studyId")
        )
        self.assertEqual(
            force_bytes(inst.identifier[2].value),
            force_bytes("urn:oid:1.2.840.113619.2.21.848.34082.0.538976288.3"),
        )
        self.assertEqual(
            force_bytes(inst.identifier[3].system), force_bytes("urn:ietf:rfc:3986")
        )
        self.assertEqual(
            force_bytes(inst.identifier[3].type.text), force_bytes("seriesId")
        )
        self.assertEqual(
            force_bytes(inst.identifier[3].value),
            force_bytes("urn:oid:1.2.840.113619.2.21.3408.700.0.757923840.3.0"),
        )
        self.assertEqual(force_bytes(inst.subtype.coding[0].code), force_bytes("US"))
        self.assertEqual(
            force_bytes(inst.subtype.coding[0].system),
            force_bytes("http://dicom.nema.org/resources/ontology/DCM"),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type), force_bytes("photo"))
        self.assertEqual(
            force_bytes(inst.view.coding[0].code), force_bytes("399067008")
        )
        self.assertEqual(
            force_bytes(inst.view.coding[0].display), force_bytes("Lateral projection")
        )
        self.assertEqual(
            force_bytes(inst.view.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(inst.width, 640)

    def testMedia3(self):
        inst = self.instantiate_from("media-example-xray.json")
        self.assertIsNotNone(inst, "Must have instantiated a Media instance")
        self.implMedia3(inst)

        js = inst.as_json()
        self.assertEqual("Media", js["resourceType"])
        inst2 = media.Media(js)
        self.implMedia3(inst2)

    def implMedia3(self, inst):
        self.assertEqual(
            force_bytes(inst.bodySite.coding[0].code), force_bytes("85151006")
        )
        self.assertEqual(
            force_bytes(inst.bodySite.coding[0].display),
            force_bytes("Structure of left hand (body structure)"),
        )
        self.assertEqual(
            force_bytes(inst.bodySite.coding[0].system),
            force_bytes("http://snomed.info.sct"),
        )
        self.assertEqual(
            force_bytes(inst.content.contentType), force_bytes("image/jpeg")
        )
        self.assertEqual(inst.content.creation.date, FHIRDate("2016-03-15").date)
        self.assertEqual(inst.content.creation.as_json(), "2016-03-15")
        self.assertEqual(force_bytes(inst.content.id), force_bytes("a1"))
        self.assertEqual(
            force_bytes(inst.content.url),
            force_bytes("http://someimagingcenter.org/fhir/Binary/A12345"),
        )
        self.assertEqual(inst.height, 432)
        self.assertEqual(force_bytes(inst.id), force_bytes("xray"))
        self.assertEqual(inst.occurrenceDateTime.date, FHIRDate("2016-03-15").date)
        self.assertEqual(inst.occurrenceDateTime.as_json(), "2016-03-15")
        self.assertEqual(
            force_bytes(inst.subtype.coding[0].code), force_bytes("39714003")
        )
        self.assertEqual(
            force_bytes(inst.subtype.coding[0].display),
            force_bytes("Skeletal X-ray of wrist and hand"),
        )
        self.assertEqual(
            force_bytes(inst.subtype.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.text.div),
            force_bytes(
                '<div xmlns="http://www.w3.org/1999/xhtml">Xray of left hand for Patient Henry Levin (MRN 12345) 2016-03-15</div>'
            ),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type), force_bytes("photo"))
        self.assertEqual(inst.width, 640)

    def testMedia4(self):
        inst = self.instantiate_from("media-example-sound.json")
        self.assertIsNotNone(inst, "Must have instantiated a Media instance")
        self.implMedia4(inst)

        js = inst.as_json()
        self.assertEqual("Media", js["resourceType"])
        inst2 = media.Media(js)
        self.implMedia4(inst2)

    def implMedia4(self, inst):
        self.assertEqual(
            force_bytes(inst.content.contentType), force_bytes("audio/mpeg")
        )
        self.assertEqual(
            force_bytes(inst.content.data),
            force_bytes("dG9vIGJpZyB0b28gaW5jbHVkZSB0aGUgd2hvbGU="),
        )
        self.assertEqual(force_bytes(inst.content.id), force_bytes("a1"))
        self.assertEqual(inst.duration, 65)
        self.assertEqual(force_bytes(inst.id), force_bytes("sound"))
        self.assertEqual(
            force_bytes(inst.text.div),
            force_bytes(
                '<div xmlns="http://www.w3.org/1999/xhtml">Sound recording of speech example for Patient Henry Levin (MRN 12345):<br/><img src="#11" alt="diagram"/></div>'
            ),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.type), force_bytes("video"))
