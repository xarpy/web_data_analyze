# -*- coding: utf-8 -*-
from datetime import datetime

from dateutil.parser import parse

from marshmallow import Schema, ValidationError, fields, validate


class DataSetSchema(Schema):
    ra_report_ = fields.Int(
        validate=[validate_dataset, validate.Equal(int)])
    ra_caers_created_date = fields.DateTime(
        format="m%-d%-Y%", validate=[
            validate_dataset,
            validate_date
        ])
    aec_event_start_date = fields.DateTime(
        format="m%-d%-Y%", validate=[
            validate_dataset,
            validate_date
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

    def validate_dataset(n):
        if n == 'nan':
            raise ValidationError("Element is None")

# TODO: Analisar utilidade
    # def validate_date(n):
    #     if datetime(parse(n)):
    #         raise ValidationError('Element is not date')
