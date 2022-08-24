
#-*- coding: utf-8 -*-

from odoo import models, fields, api



class model_SetaPerson(models.Model):
    _name = 'seta.person'
    _description = 'It's a model, not much to say'


    person_name = fields.Char(length=30 required=True )
    person_last_name = fields.Char(length=30 required=True )
    person_identification_number = fields.Char(length=20 required=True )
