# Real-Time Gas Turbine Digital Twin & Monitoring Platform

A real-time industrial observability platform that simulates a gas turbine power system and monitors operational telemetry through a containerized DevOps architecture.

This project combines:
- industrial telemetry simulation,
- FastAPI backend services,
- PostgreSQL storage,
- Grafana observability dashboards,
- Dockerized infrastructure,
- predictive maintenance concepts,
- anomaly detection logic,
- thermodynamics-inspired monitoring.

The platform generates synthetic turbine telemetry and visualizes system health, efficiency, vibration, temperatures, and maintenance risk in real time.

---

# Architecture

```text
Gas Turbine Simulator
        ↓
FastAPI Backend
        ↓
PostgreSQL Database
        ↓
Grafana Dashboards
```

---

# Features

## Real-Time Telemetry Simulation
The simulator generates synthetic industrial sensor data including:
- compressor temperatures,
- pressure ratio,
- turbine efficiency,
- combustion temperature,
- shaft RPM,
- vibration levels,
- bearing temperature,
- exhaust temperature,
- power output,
- maintenance risk.

---

## FastAPI Backend
The backend:
- receives telemetry,
- validates payloads,
- stores readings into PostgreSQL,
- exposes API endpoints for querying telemetry data.

Endpoints:
- `/health`
- `/telemetry`
- `/telemetry/latest`
- `/telemetry/history`

---

## PostgreSQL Persistence
Telemetry data is stored historically for:
- trend analysis,
- operational monitoring,
- anomaly detection,
- dashboard visualization.

---

## Grafana Industrial Dashboards
Grafana visualizes:
- power output,
- turbine efficiency,
- vibration trends,
- bearing temperature,
- thermal efficiency,
- maintenance risk,
- system status.

The dashboard behaves similarly to industrial monitoring and observability systems used in:
- energy infrastructure,
- manufacturing,
- industrial IoT,
- Industry 4.0 environments.

---

# Anomaly Detection

The simulator includes rule-based anomaly generation for:
- abnormal vibration,
- bearing overheating,
- turbine efficiency degradation,
- reduced thermal efficiency.

System states:
- NORMAL
- WARNING
- CRITICAL

Maintenance risk is dynamically calculated based on operational conditions.

---

# Tech Stack

## Backend
- FastAPI
- Python

## Database
- PostgreSQL

## Observability
- Grafana

## Infrastructure
- Docker
- Docker Compose

## DevOps
- GitHub Actions (CI/CD)

---

# Running the Project

## Start the platform

```bash
docker compose up -d --build
```

---

## Open Grafana

```text
http://localhost:3000
```

Default credentials:

```text
username: admin
password: admin
```

---

## API Health Check

```bash
curl http://localhost:8000/health
```

---

## Latest Telemetry

```bash
curl http://localhost:8000/telemetry/latest
```

---

# Example Telemetry Payload

```json
{
  "timestamp": "2026-05-15T18:22:31",
  "power_output_mw": 41.3,
  "turbine_efficiency": 0.88,
  "vibration_level": 2.1,
  "bearing_temperature": 94.7,
  "maintenance_risk": 28.4,
  "status": "NORMAL"
}
```

---

# Engineering Context

This project was inspired by:
- gas turbine monitoring systems,
- Brayton cycle principles,
- industrial predictive maintenance,
- real-time telemetry systems,
- industrial observability platforms.

The telemetry model reflects real operational concepts such as:
- compressor efficiency,
- turbine efficiency,
- thermal losses,
- vibration monitoring,
- bearing condition monitoring,
- operational risk assessment.

---

# Future Improvements

Potential future upgrades:
- MQTT streaming
- Prometheus integration
- Kubernetes deployment
- ML-based anomaly detection
- custom React frontend
- alerting system
- digital twin visualization
- InfluxDB time-series storage

---

# Screenshots

<img width="1531" height="631" alt="Screenshot 2026-05-15 at 21 53 11" src="https://github.com/user-attachments/assets/ff44c830-a5af-42fd-a14a-56f63041d9eb" />

<img width="1498" height="597" alt="Screenshot 2026-05-15 at 21 53 26" src="https://github.com/user-attachments/assets/8cce08e9-0eab-43d3-b622-c1410878d3b2" />


<img width="1498" height="601" alt="Screenshot 2026-05-15 at 21 53 37" src="https://github.com/user-attachments/assets/a2bd14fc-64a1-4c61-8dcf-501b4d6de670" />

---

# Author

Built by Reyver Serna as a DevOps + industrial systems engineering project.
