DROP FUNCTION IF EXISTS count_people_by_age_group(TEXT);

CREATE OR REPLACE FUNCTION count_people_by_age_group(country_name TEXT)
RETURNS TABLE(
    returned_age_group TEXT,
    total_people BIGINT
)
LANGUAGE plpgsql AS $$
BEGIN
    RETURN QUERY
    SELECT
        age_group_internal AS returned_age_group,
        COUNT(*) AS total_people
    FROM (
        SELECT
            CASE
                WHEN p.age < 30 THEN 'Young'
                WHEN p.age BETWEEN 30 AND 60 THEN 'Adult'
                ELSE 'Senior'
            END AS age_group_internal
        FROM people p
        JOIN cities c ON p.city_id = c.id
        JOIN states s ON c.state_id = s.id
        JOIN countries co ON s.country_id = co.id
        WHERE co.name = count_people_by_age_group.country_name
    ) AS subquery
    GROUP BY age_group_internal
    ORDER BY age_group_internal;
END;
$$;


SELECT * FROM count_people_by_age_group('Brazil');
