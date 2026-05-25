# 🚀 Hatem Shalaby | Operations Excellence & Process Automation Expert

> **Transforming chaotic workflows into data-driven, automated engines.**  
> *Specializing in Workforce Management (WFM), Real-Time Analytics, and SOP Standardization.*

[![Portfolio Live](https://img.shields.io/badge/🌐_Portfolio-Live-00d4aa?style=for-the-badge)](https://hatemismail2011shalaby.github.io/RTA-Operations-Portfolio/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/hatem-shalaby-7359611a2)
[![Email](https://img.shields.io/badge/Email-Hire_Me-EA4335?style=for-the-badge&logo=gmail)](mailto:hatemismail2011shalaby@gmail.com)

## 📊 The Edge
I don't just report data; I engineer the systems that generate it. My work bridges the gap between **Operations Strategy** and **Technical Execution**.
- **Impact:** Reduced manual reporting time by **65%** via automated SQL/Pipeline scripts.
- **Precision:** Implemented WFM forecasting models with **<5% variance** accuracy.
- **Scalability:** Designed SOPs that scaled from 10 to 200+ agents without degradation.

---

## 🛠️ Tech Stack
| Domain | Tools |
| :--- | :--- |
| **Data Engineering** | SQL (Advanced), Python (Pandas, NumPy), Excel (VBA/Macros) |
| **Visualization** | Power BI, Tableau, Looker Studio |
| **Operations** | WFM Systems (NICE, Aspect), RTA Dashboards, Six Sigma |
| **Automation** | GitHub Actions, Git, CI/CD Pipelines |

---

## 📂 Repository Contents
This repo is a live demonstration of my operational toolkit. It is **not** a template; it is a functional archive of deployed solutions.

### 📁 Core Deliverables
- **`RTA Command Center.xlsx`**: Real-Time Adherence & Performance Tracker.
  - *Feature:* Dynamic variance analysis and auto-alert thresholds.
- **`WFM.xlsx`**: Workforce Forecasting & Scheduling Engine.
  - *Feature:* Erlang C implementation for optimal staffing levels.
- **`docs/`**: Technical documentation for SOPs, Playbooks, and Case Studies.
- **`SQL_Demos/`**: Production-grade query libraries for complex operational data.
- **`Python_Automation/`**: Scripts for data cleaning, ETL, and report generation.

### 📈 Live Demos (GitHub Pages)
- **[Interactive Dashboard Demo](https://hatemismail2011shalaby.github.io/RTA-Operations-Portfolio/)**: Live index.html rendering of key metrics.
- **[SOP Library](https://hatemismail2011shalaby.github.io/RTA-Operations-Portfolio/docs/sops.html)**: Digital Standard Operating Procedures.

---

## 💻 Code Samples

### 🔹 Advanced SQL (Window Functions & CTEs)
*Calculating real-time agent adherence with rolling averages.*
```sql
WITH AgentMetrics AS (
    SELECT 
        agent_id,
        timestamp,
        status,
        ROW_NUMBER() OVER (PARTITION BY agent_id ORDER BY timestamp) as rn
    FROM call_center_logs
    WHERE date >= CURRENT_DATE - INTERVAL '30 days'
)
SELECT 
    agent_id,
    COUNT(*) FILTER (WHERE status = 'ADHERENT') * 1.0 / COUNT(*) as adherence_rate,
    AVG(average_handle_time) OVER (PARTITION BY agent_id ROWS BETWEEN 5 PRECEDING AND CURRENT ROW) as rolling_ath
FROM AgentMetrics
GROUP BY agent_id, adherence_rate;
