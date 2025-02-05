"""Constants for the Solcast Solar integration."""

from __future__ import annotations

from typing import Final

from homeassistant.helpers import selector

DOMAIN = "solcast_solar"
SOLCAST_URL = "https://api.solcast.com.au"

CONF_PV_ESTIMATE = "pv_estimate"

ATTR_ENTRY_TYPE: Final = "entry_type"
ENTRY_TYPE_SERVICE: Final = "service"

ATTRIBUTION: Final = "Data retrieved from Solcast"

CUSTOM_HOUR_SENSOR = "customhoursensor"

SERVICE_UPDATE = "update_forecasts"
SERVICE_CLEAR_DATA = "clear_all_solcast_data"
SERVICE_QUERY_FORECAST_DATA = "query_forecast_data"
SERVICE_SET_DAMPENING = "set_dampening"
SERVICE_SET_PV_ESTIMATE = "set_pv_estimate"

#new 4.0.8 - integration config options menu
#new 4.0.15 - integration config options for custom hour (option 3)
#new 4.0.16 - integration config options for pv_estimate (option4)
CONFIG_OPTIONS = [
    selector.SelectOptionDict(value="configure_api", label="option1"),
    selector.SelectOptionDict(value="configure_dampening", label="option2"),
    selector.SelectOptionDict(value="configure_customsensor", label="option3"),
    selector.SelectOptionDict(value="configure_pv_estimate", label="option4"),
]