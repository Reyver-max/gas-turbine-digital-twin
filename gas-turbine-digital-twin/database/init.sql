CREATE TABLE IF NOT EXISTS turbine_telemetry (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP NOT NULL,

    compressor_inlet_temp FLOAT,
    compressor_outlet_temp FLOAT,
    compressor_pressure_ratio FLOAT,
    compressor_efficiency FLOAT,

    combustion_temperature FLOAT,
    fuel_flow_rate FLOAT,

    turbine_inlet_temp FLOAT,
    turbine_outlet_temp FLOAT,
    turbine_efficiency FLOAT,
    shaft_rpm FLOAT,
    power_output_mw FLOAT,

    vibration_level FLOAT,
    bearing_temperature FLOAT,
    exhaust_temperature FLOAT,

    thermal_efficiency FLOAT,
    maintenance_risk FLOAT,
    status TEXT
);
