-- DuckDB query to generate GAIA Nexus leaderboard
-- This query aggregates results from JSON files in the results/ directory

SELECT
    agent_id AS "Agent ID",
    agent_name AS "Agent Name",
    level AS "GAIA Level",
    ROUND(accuracy * 100, 2) AS "Accuracy (%)",
    score AS "Correct",
    total AS "Total",
    ROUND(avg_time, 2) AS "Avg Time (s)",
    timestamp AS "Evaluated",
    status AS "Status"
FROM read_json('results/*.json')
WHERE status != 'failed'
ORDER BY accuracy DESC, avg_time ASC
LIMIT 100;
