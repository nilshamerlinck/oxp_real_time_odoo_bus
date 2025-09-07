from odoo import fields, models
from odoo.exceptions import UserError


class ClickerGame(models.Model):
    _name = 'clicker.game'
    _description = 'Collaborative Clicker Game'
    _inherit = ['bus.listener.mixin']

    name = fields.Char(required=True)
    clicks = fields.Integer(default=0)
    increment = fields.Integer(default=1)

    def action_click(self):
        self.ensure_one()
        self.clicks += self.increment

    def action_improve_increment(self):
        self.ensure_one()
        required = self.increment * 5
        if self.clicks < required:
            raise UserError(f"You need at least {required} clicks to improve your clicker.")
        self.increment += 1
        self.clicks -= required

    def write(self, vals):
        res = super().write(vals)
        if 'clicks' in vals or 'increment' in vals:
            for game in self:
                game._bus_send(
                    'game_updated',
                    {
                        'clicks': game.clicks,
                        'increment': game.increment,
                    }
                )
        return res
