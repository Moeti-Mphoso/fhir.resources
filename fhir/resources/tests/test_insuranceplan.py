# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/InsurancePlan
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""

import io
import json
import os
import unittest

import pytest

from .. import insuranceplan
from ..fhirdate import FHIRDate
from .fixtures import force_bytes


@pytest.mark.usefixtures("base_settings")
class InsurancePlanTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get("FHIR_UNITTEST_DATADIR") or ""
        with io.open(os.path.join(datadir, filename), "r", encoding="utf-8") as handle:
            js = json.load(handle)
            self.assertEqual("InsurancePlan", js["resourceType"])
        return insuranceplan.InsurancePlan(js)

    def testInsurancePlan1(self):
        inst = self.instantiate_from("insuranceplan-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a InsurancePlan instance")
        self.implInsurancePlan1(inst)

        js = inst.as_json()
        self.assertEqual("InsurancePlan", js["resourceType"])
        inst2 = insuranceplan.InsurancePlan(js)
        self.implInsurancePlan1(inst2)

    def implInsurancePlan1(self, inst):
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(force_bytes(inst.name), force_bytes("foo"))
        self.assertEqual(
            force_bytes(inst.text.div),
            force_bytes(
                '<div xmlns="http://www.w3.org/1999/xhtml"><p><b>Generated Narrative with Details</b></p><p><b>id</b>: example</p><p><b>name</b>: foo</p></div>'
            ),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
