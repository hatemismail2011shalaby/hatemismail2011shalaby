-- FILE: agent_adherence.sql
-- PURPOSE: Calculate real-time adherence with rolling 30-day averages
-- AUTHOR: Hatem Shalaby

WITH DailyStats AS (
    SELECT 
        DATE(timestamp) as activity_date,
        agent_id,
        SUM(CASE WHEN status = 'ADHERENT' THEN 1 ELSE 0 END) as adherent_minutes,
        SUM(CASE WHEN status = 'BREAK' OR status = 'LATE' THEN 1 ELSE 0 END) as deviation_minutes,
        COUNT(*) as total_minutes
    FROM call_center_activity
    WHERE timestamp >= CURRENT_DATE - INTERVAL '90 days'
    GROUP BY DATE(timestamp), agent_id
),
RollingMetrics AS (
    SELECT 
        activity_date,
        agent_id,
        adherent_minutes,
        deviation_minutes,
        total_minutes,
        ROUND((adherent_minutes * 100.0 / NULLIF(total_minutes, 0)), 2) as daily_adherence_pct,
        AVG((adherent_minutes * 100.0 / NULLIF(total_minutes, 0))) OVER (
            PARTITION BY agent_id 
            ORDER BY activity_date 
            ROWS BETWEEN 29 PRECEDING AND CURRENT ROW
        ) as rolling_30d_adherence
    FROM DailyStats
)
SELECT 
    agent_id,
    activity_date,
    daily_adherence_pct,
    rolling_30d_adherence,
    CASE 
        WHEN rolling_30d_adherence < 85 THEN 'CRITICAL'
        WHEN rolling_30d_adherence < 90 THEN 'WARNING'
        ELSE 'OPTIMAL'
    END as status
FROM RollingMetrics
ORDER BY agent_id, activity_date DESC;
