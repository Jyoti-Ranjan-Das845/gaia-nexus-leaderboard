-- DuckDB query to generate GAIA Nexus leaderboard
-- AgentBeats automatically creates 'results' table from /results/*.json files

SELECT
    agent_id AS id,
    agent_name AS "Agent Name",
    level AS "GAIA Level",
    ROUND(accuracy, 2) AS "Accuracy (%)",
    score AS "Correct",
    total AS "Total",
    ROUND(avg_time, 2) AS "Avg Time (s)",
    timestamp AS "Evaluated",
    status AS "Status"
FROM results
WHERE status NOT IN ('failed', 'pending')
ORDER BY accuracy DESC, avg_time ASC
LIMIT 100;
