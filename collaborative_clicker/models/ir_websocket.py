from odoo import models
from odoo.exceptions import AccessError


class IrWebsocket(models.AbstractModel):
    _inherit = "ir.websocket"

    def _build_bus_channel_list(self, channels):
        if self.env.uid:  # Only allowed for logged in users
            for channel in channels:
                if not isinstance(channel, str):
                    continue
                if channel.startswith("clicker.game"):
                    record = self._check_click_game_channel(channel)  # Check access to the record
                    if record:
                        channels.append(record)
        return super()._build_bus_channel_list(channels)

    def _check_click_game_channel(self, channel):
        res_id = channel.split(":")[-1]
        try:
            res_id = int(res_id)
        except ValueError:
            return
        record = self.env['clicker.game'].browse(res_id).exists()
        try:
            record.check_access('read')
        except AccessError:
            return
        return record
