#-*- coding: utf-8 -*-

from odoo import models, fields, api


class model_class_name_replace(models.Model):
    _name = 'model_class_dotted_name_replace'
    _description = 'description_replace'

    field_one_replace = fields.Char()
    field_two_replace = fields.Integer()
