from odoo import api, fields, models, _

class TranslationField(models.Model):
    _name = "translation.field"
    _description = "TODO"

    translation_line_ids = fields.One2many(
            "translation.line",
            "translation_field_id",
            )

    default_language = fields.Char("en_US")
    default_translation = fields.Many2one("translation.line")

    def _get_translation_record(self, fallback=True):
        if translation_line := self.translation_line_ids.search(['language', '=', self.user.env.lang]):
            return translation_line
        elif fallback is True:
            return self._get_default_translation()
        else:
            return None

    def get_translation(self):
        return self._get_translation_record().translation

    def add_translation(self, translation, language=None):
        if language is None:
            language = self.env.user.lang

        translation_line = self.env['translation.line'].sudo().create({
            'language': language,
            'translation': translation,
            'translation_field_id': self.id,
            })

        return translation_line

    @api.depends("default_language")
    def _update_default_language(self):
        for rec in self:
            rec.default_translation = None
            rec._get_default_language()

    def _update_translation(self, translation):
        translation_line = self.get_translation_record(fallback=False)
        if translation_line:
            translation_line.translation = translation
        else:
            self.add_translation(translation)

    def _get_default_language(self):
        if not self.default_translation:
            self.default_translation = self.translation_line_ids.search(
                    ['language', '=', self.default_language])
        return self.default_translation


class TranslationLine(models.Model):
    _name = "translation.line"
    _description = "TODO"

   language = fields.Char()
   translation = fields.Char()

   translation_field_id = fields.Many2one("translation.field")

