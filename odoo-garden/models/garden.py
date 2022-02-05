
from odoo import models, fields, api, _

class Garden(models.Model):
    _name = 'garden'

    name = fields.Char(string='Name')
    plantbeds_ids = fields.One2manny(string='Plantbeds', comodel_name='garden.plantbed')

class Plantbed(models.Model):
    _name = 'plantbed'

    name = fields.Char(string='Name')
    plants_ids = fields.Manny2manny(string='Plants', comodel_name='garden.plantbed')

class Plant(models.Model):
    _name = 'plant'

    latin_name = fields.Char(string='Latin Name')
    local_name = fields.Char(string='Local Name')
    perennial = fields.Bool(string='Perennial')
    pregrow = fields.Manny2manny(string='Pregrow', comodel_name='garden.month')
    plant_period = fields.Manny2manny(string='Plant Period', comodel_name='garden.month')
    flower_period = fields.Manny2manny(string='Flower Period', comodel_name='garden.month')
    zone = fields.Manny2manny(string='Growth Zone', comodel_name='garden.zone')
    plantbed_ids = fields.Manny2manny(string='Plant Beds', comodel_name='garden.plantbed')
    main_image = ''
    images = ''
    description = fields.Char(string='Description')
    external_link = fields.Char(string='Link')

class Month(models.Model):
    _name = 'month'

    name = fields.Char(string='Month Name')
