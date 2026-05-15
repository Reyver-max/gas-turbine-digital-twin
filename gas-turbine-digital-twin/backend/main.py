from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from datetime import datetime
import psycopg2
import os


app = FastAPI(title="Gas Turbine Digital Twin API")


class Telemetry(BaseModel):
    timestamp: datetime

    compressor_inlet_temp: float
    compressor_outlet_temp: float
    compressor_pressure_ratio: float
    compressor_efficiency: float

    combustion_temperature: float
    fuel_flow_rate: float

    turbine_inlet_temp: float
    turbine_outlet_temp: float
    turbine_efficiency: float
    shaft_rpm: float
    power_output_mw: float

    vibration_level: float
    bearing_temperature: float
    exhaust_temperature: float

    thermal_efficiency: float
    maintenance_risk: float
    status: str


def get_db_connection():
    return psycopg2.connect(
        host=os.getenv("POSTGRES_HOST", "postgres"),
        database=os.getenv("POSTGRES_DB", "turbine_db"),
        user=os.getenv("POSTGRES_USER", "turbine_user"),
        password=os.getenv("POSTGRES_PASSWORD", "turbine_password"),
        port=os.getenv("POSTGRES_PORT", "5432"),
    )


@app.get("/health")
def health_check():
    return {"status": "API is running"}


@app.post("/telemetry")
def create_telemetry(reading: Telemetry):
    try:
        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute(
            """
            INSERT INTO turbine_telemetry (
                timestamp,
                compressor_inlet_temp,
                compressor_outlet_temp,
                compressor_pressure_ratio,
                compressor_efficiency,
                combustion_temperature,
                fuel_flow_rate,
                turbine_inlet_temp,
                turbine_outlet_temp,
                turbine_efficiency,
                shaft_rpm,
                power_output_mw,
                vibration_level,
                bearing_temperature,
                exhaust_temperature,
                thermal_efficiency,
                maintenance_risk,
                status
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (
                reading.timestamp,
                reading.compressor_inlet_temp,
                reading.compressor_outlet_temp,
                reading.compressor_pressure_ratio,
                reading.compressor_efficiency,
                reading.combustion_temperature,
                reading.fuel_flow_rate,
                reading.turbine_inlet_temp,
                reading.turbine_outlet_temp,
                reading.turbine_efficiency,
                reading.shaft_rpm,
                reading.power_output_mw,
                reading.vibration_level,
                reading.bearing_temperature,
                reading.exhaust_temperature,
                reading.thermal_efficiency,
                reading.maintenance_risk,
                reading.status,
            ),
        )

        conn.commit()
        cur.close()
        conn.close()

        return {"message": "Telemetry stored successfully"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/telemetry/latest")
def get_latest_telemetry():
    try:
        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute(
            """
            SELECT * FROM turbine_telemetry
            ORDER BY timestamp DESC
            LIMIT 1
            """
        )

        row = cur.fetchone()
        cur.close()
        conn.close()

        if row is None:
            return {"message": "No telemetry data available yet"}

        columns = [
            "id",
            "timestamp",
            "compressor_inlet_temp",
            "compressor_outlet_temp",
            "compressor_pressure_ratio",
            "compressor_efficiency",
            "combustion_temperature",
            "fuel_flow_rate",
            "turbine_inlet_temp",
            "turbine_outlet_temp",
            "turbine_efficiency",
            "shaft_rpm",
            "power_output_mw",
            "vibration_level",
            "bearing_temperature",
            "exhaust_temperature",
            "thermal_efficiency",
            "maintenance_risk",
            "status",
        ]

        return dict(zip(columns, row))

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/telemetry/history")
def get_telemetry_history(limit: int = 50):
    try:
        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute(
            """
            SELECT * FROM turbine_telemetry
            ORDER BY timestamp DESC
            LIMIT %s
            """,
            (limit,),
        )

        rows = cur.fetchall()
        cur.close()
        conn.close()

        columns = [
            "id",
            "timestamp",
            "compressor_inlet_temp",
            "compressor_outlet_temp",
            "compressor_pressure_ratio",
            "compressor_efficiency",
            "combustion_temperature",
            "fuel_flow_rate",
            "turbine_inlet_temp",
            "turbine_outlet_temp",
            "turbine_efficiency",
            "shaft_rpm",
            "power_output_mw",
            "vibration_level",
            "bearing_temperature",
            "exhaust_temperature",
            "thermal_efficiency",
            "maintenance_risk",
            "status",
        ]

        return [dict(zip(columns, row)) for row in rows]

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
