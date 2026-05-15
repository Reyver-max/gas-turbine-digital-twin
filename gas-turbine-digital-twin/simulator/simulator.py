import random
import time
from datetime import datetime
import requests


API_URL = "http://backend:8000/telemetry"


def calculate_status(bearing_temperature, vibration_level, turbine_efficiency):
    if bearing_temperature > 130 or vibration_level > 9 or turbine_efficiency < 0.70:
        return "CRITICAL"

    if bearing_temperature > 110 or vibration_level > 6 or turbine_efficiency < 0.80:
        return "WARNING"

    return "NORMAL"


def calculate_maintenance_risk(bearing_temperature, vibration_level, turbine_efficiency):
    risk = 0

    risk += max(0, bearing_temperature - 80) * 1.2
    risk += vibration_level * 5
    risk += max(0, 0.9 - turbine_efficiency) * 100

    return min(round(risk, 2), 100)


def generate_operating_mode():
    probability = random.random()

    if probability < 0.75:
        return "NORMAL"
    elif probability < 0.93:
        return "WARNING"
    else:
        return "CRITICAL"


def generate_reading():
    operating_mode = generate_operating_mode()

    compressor_inlet_temp = round(random.uniform(15, 35), 2)
    compressor_pressure_ratio = round(random.uniform(10, 18), 2)
    compressor_efficiency = round(random.uniform(0.82, 0.92), 3)

    compressor_outlet_temp = round(
        compressor_inlet_temp + compressor_pressure_ratio * random.uniform(18, 25),
        2,
    )

    fuel_flow_rate = round(random.uniform(2.5, 5.5), 2)
    combustion_temperature = round(random.uniform(900, 1250), 2)

    turbine_inlet_temp = round(combustion_temperature - random.uniform(20, 80), 2)
    turbine_efficiency = round(random.uniform(0.80, 0.92), 3)

    turbine_outlet_temp = round(
        turbine_inlet_temp - turbine_efficiency * random.uniform(350, 520),
        2,
    )

    shaft_rpm = round(random.uniform(2950, 3050), 2)
    power_output_mw = round(fuel_flow_rate * turbine_efficiency * random.uniform(8, 12), 2)

    vibration_level = round(random.uniform(1.0, 5.5), 2)
    bearing_temperature = round(random.uniform(70, 105), 2)
    exhaust_temperature = round(turbine_outlet_temp + random.uniform(20, 60), 2)
    thermal_efficiency = round(random.uniform(0.30, 0.42), 3)

    if operating_mode == "WARNING":
        vibration_level = round(random.uniform(6.2, 8.8), 2)
        bearing_temperature = round(random.uniform(111, 128), 2)
        turbine_efficiency = round(random.uniform(0.72, 0.79), 3)
        thermal_efficiency = round(random.uniform(0.25, 0.31), 3)

    if operating_mode == "CRITICAL":
        vibration_level = round(random.uniform(9.2, 11.5), 2)
        bearing_temperature = round(random.uniform(131, 150), 2)
        turbine_efficiency = round(random.uniform(0.62, 0.69), 3)
        thermal_efficiency = round(random.uniform(0.18, 0.25), 3)

    maintenance_risk = calculate_maintenance_risk(
        bearing_temperature,
        vibration_level,
        turbine_efficiency,
    )

    status = calculate_status(
        bearing_temperature,
        vibration_level,
        turbine_efficiency,
    )

    return {
        "timestamp": datetime.utcnow().isoformat(),
        "compressor_inlet_temp": compressor_inlet_temp,
        "compressor_outlet_temp": compressor_outlet_temp,
        "compressor_pressure_ratio": compressor_pressure_ratio,
        "compressor_efficiency": compressor_efficiency,
        "combustion_temperature": combustion_temperature,
        "fuel_flow_rate": fuel_flow_rate,
        "turbine_inlet_temp": turbine_inlet_temp,
        "turbine_outlet_temp": turbine_outlet_temp,
        "turbine_efficiency": turbine_efficiency,
        "shaft_rpm": shaft_rpm,
        "power_output_mw": power_output_mw,
        "vibration_level": vibration_level,
        "bearing_temperature": bearing_temperature,
        "exhaust_temperature": exhaust_temperature,
        "thermal_efficiency": thermal_efficiency,
        "maintenance_risk": maintenance_risk,
        "status": status,
    }


def main():
    print("Starting gas turbine telemetry simulator with anomaly detection...")

    while True:
        reading = generate_reading()

        try:
            response = requests.post(API_URL, json=reading, timeout=5)
            print(
                f"Sent telemetry: {reading['status']} | "
                f"Risk: {reading['maintenance_risk']} | "
                f"Bearing Temp: {reading['bearing_temperature']} | "
                f"Vibration: {reading['vibration_level']} | "
                f"Turbine Eff: {reading['turbine_efficiency']} | "
                f"Response: {response.status_code}"
            )

        except requests.exceptions.RequestException as error:
            print(f"Failed to send telemetry: {error}")

        time.sleep(3)


if __name__ == "__main__":
    main()
