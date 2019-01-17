#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.1.11917 on 2019-01-17.
#  2019, SMART Health IT.

import os
import pytest
import io
import unittest
import json

from .fixtures import force_bytes
from .. import enrollmentrequest
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class EnrollmentRequestTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("EnrollmentRequest", js["resourceType"])
        return enrollmentrequest.EnrollmentRequest(js)
    
    def testEnrollmentRequest1(self):
        inst = self.instantiate_from("enrollmentrequest-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a EnrollmentRequest instance")
        self.implEnrollmentRequest1(inst)
        
        js = inst.as_json()
        self.assertEqual("EnrollmentRequest", js["resourceType"])
        inst2 = enrollmentrequest.EnrollmentRequest(js)
        self.implEnrollmentRequest1(inst2)
    
    def implEnrollmentRequest1(self, inst):
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(force_bytes(inst.id), force_bytes("22345"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://happyvalley.com/enrollmentrequest"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("EN22345"))
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.div), force_bytes("<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the EnrollmentRequest.</div>"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

