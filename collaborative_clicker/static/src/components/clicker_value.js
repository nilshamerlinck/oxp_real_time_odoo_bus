import { Component } from '@odoo/owl';
import { registry } from '@web/core/registry';
import { useState, onWillStart, onWillDestroy } from '@odoo/owl';


export class ClickerValue extends Component {
    static template = "collaborative_clicker.ClickerValue";

    setup() {
        this.state = useState({
            clicks: this.props.record.data.clicks || 0,
        })
        this.busService = this.env.services.bus_service;
        onWillStart(() => {
            const { resId, resModel } = this.props.record._config;
            if (resId) {
                this.channelName = `${resModel}:${resId}`;
                this.busService.addChannel(this.channelName);
                this.busService.subscribe('game_updated', this._handleNotification.bind(this));
                // In a real example, you would want to subscribe also after the record is saved
            }
        });
        onWillDestroy(() => {
            this.busService.deleteChannel(this.channelName);
        });
    }

    async _handleNotification(payload) {
        const { clicks } = payload;
        this.state.clicks = clicks;
    }
}

export const clickerValue = {
    component: ClickerValue,
};
registry.category("view_widgets").add("clicker_value", clickerValue);
