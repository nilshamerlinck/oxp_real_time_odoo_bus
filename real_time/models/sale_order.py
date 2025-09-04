from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.model_create_multi
    def create(self, vals_list):
        orders = super().create(vals_list)
        if orders:
            self.env.ref('real_time.group_sale_dashboard')._bus_send(
                'sale_order_update',
                {
                    'message': 'New SOs Created',
                },
            )
        return orders

    @api.model
    def get_dashboard_data(self):
        sales_today = self.env['sale.order'].search(
            [('create_date', '>=', fields.Date.today())],
        )
        return {
            'sales_today': len(sales_today),
            'last_so_name': sales_today[:1].name or '',
        }
