
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
    local_name = fields.Char(string='Local Name',
            compute='get_local_name',
            inverse='set_local_name')
    local_name_translation_id = fields.Many2one('translation.field')

    perennial = fields.Boolean(string='Perennial')
    pregrow = fields.Many2many(string='Pregrow', comodel_name='month')
    # plant_period = fields.Many2many(string='Plant Period', comodel_name='garden.month')
    # flower_period = fields.Many2many(string='Flower Period', comodel_name='garden.month')
    # zone = fields.Many2many(string='Growth Zone', comodel_name='garden.zone')
    # plantbed_ids = fields.Many2many(string='Plant Beds', comodel_name='garden.plantbed')
    main_image = fields.Binary()
    images = fields.Binary()
    description = fields.Char(string='Description')
    external_link = fields.Char(string='Link')

    def _get_local_name(self):
        return local_name_translation_id.get_translation()

    def _set_local_name(self):
        local_name_translation_id.update_translation(self.local_name)


class Month(models.Model):
    _name = 'month'

    name = fields.Char(string='Month Name')
