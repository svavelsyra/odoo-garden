
from odoo import models, fields, api, _

class Garden(models.Model):
    _name = 'garden'

    name = fields.Char(string='Name')
    plantbed_ids = fields.One2many(string='Plantbeds', comodel_name='plantbed', inverse_name='garden_id')

class Plantbed(models.Model):
    _name = 'plantbed'

    name = fields.Char(string='Name')
    garden_id = fields.Many2one(comodel_name='garden')
    plants_ids = fields.Many2many(string='Plants', comodel_name='plant')

class Plant(models.Model):
    _name = 'plant'

    latin_name = fields.Char(string='Latin Name')
    local_name = fields.Char(string='Local Name', translate=True)
    perennial = fields.Boolean(string='Perennial')
    #pregrow = fields.Many2many(string='Pregrow', comodel_name='pregrow_period_tag')
    plant_period = fields.Many2many(string='Plant Period', comodel_name='plant_period_tag')
    flower_period = fields.Many2many(string='Flower Period', comodel_name='flower_period_tag')
    zone = fields.Many2many(string='Growth Zone', comodel_name='garden_zone')
    plantbed_ids = fields.Many2many(string='Plant Beds', comodel_name='plantbed')
    image = fields.Binary()
    description = fields.Char(string='Description', translate=True)
    external_link = fields.Char(string='Link')


class Pregrow_Period_Tag(models.Model):
    _name = 'pregrow_period_tag'
    name = fields.Char(string='Month Name')
    number = fields.Integer(string='Month number')
    

class Plant_Period_Tag(models.Model):
    _name = 'plant_period_tag'
    name = fields.Char(string='Month Name')
    number = fields.Integer(string='Month number')


class Flower_Period_Tag(models.Model):
    _name = 'flower_period_tag'
    name = fields.Char(string='Month Name')
    number = fields.Integer(string='Month number')
    

class Zone(models.Model):
    _name = 'garden_zone'

    name = fields.Char(string='Zone')
