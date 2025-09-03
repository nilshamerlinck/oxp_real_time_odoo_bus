import { Component } from '@odoo/owl';
import { registry } from '@web/core/registry';
import { useState, onWillStart } from '@odoo/owl';
import { useService } from '@web/core/utils/hooks';


export class SaleDashboard extends Component {
    static template = "real_time.SaleDashboard";

    setup() {
        this.orm = useService("orm");
        this.state = useState({
            salesToday: 0,
            lastSaleOrderName: null,
        })
        onWillStart(() => {
            this._fetchData();
        })
        this.busService = this.env.services.bus_service;
        this.busService.addChannel('sale_dashboard');
        this.busService.subscribe('sale_order_update', this._handleNotification.bind(this));
    }

    async _fetchData() {
        const { sales_today, last_so_name } = await this.orm.call(
            'sale.order',
            'get_dashboard_data',
            [],
        )
        this.state.salesToday = sales_today;
        this.state.lastSaleOrderName = last_so_name;
    }

    _handleNotification(payload) {
        const { n_sos, last_so_name } = payload;
        this.state.salesToday += n_sos;
        this.state.lastSaleOrderName = last_so_name;
    }
}

export const saleDashboard = {
    component: SaleDashboard,
};
registry.category("view_widgets").add("sale_dashboard", saleDashboard);
