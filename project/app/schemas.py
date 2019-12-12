# -*- coding: utf-8 -*-
from datetime import datetime

import numpy
from dateutil.parser import parse

from marshmallow import Schema, ValidationError, fields, validate


def validate_dataset(value):
    """Function to validate if value is NaN"""
    if value == numpy.nan or value == 'nan':
        raise ValidationError("Element is None")


class DataSetSchema(Schema):
    """Schema for dataset"""
    ra_report_ = fields.Int(
        validate=[validate_dataset, validate.Equal(int)])
    ra_caers_created_date = fields.DateTime(
        format="m%-d%-Y%", validate=[
            validate_dataset
        ])
    aec_event_start_date = fields.DateTime(
        format="m%-d%-Y%", validate=[
            validate_dataset
        ])
    pri_product_role = fields.String(
        validate=[validate_dataset, validate.Equal(str)])
    pri_reported_brand_product_name = fields.String(
        validate=[validate_dataset, validate.Equal(str)])
    pri_fda_industry_code = fields.Int(
        validate=[validate_dataset, validate.Equal(int)])
    pri_fda_industry_name = fields.String(
        validate=[validate_dataset, validate.Equal(str)])
    ci_age_at_adverse_event = fields.Int(
        validate=[validate_dataset, validate.Equal(int)])
    ci_age_unit = fields.String(
        validate=[validate_dataset, validate.Equal(str)])
    ci_gender = fields.String(
        validate=[validate_dataset, validate.Equal(str)])
    aec_one_row_outcomes = fields.String(
        validate=[validate_dataset, validate.Equal(str)])
    sym_one_row_coded_symptoms = fields.String(
        validate=[validate_dataset, validate.Equal(str)])
