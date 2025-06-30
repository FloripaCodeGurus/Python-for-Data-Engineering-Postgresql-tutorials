WITH PeopleCountPerCity AS (
    SELECT
        c.city_name,
        COUNT(p.id) AS people_count
    FROM people p
    JOIN cities c ON p.city_id = c.id
    GROUP BY c.city_name
)
SELECT
    city_name,
    people_count
FROM PeopleCountPerCity
WHERE people_count > 1
ORDER BY people_count DESC;

-- Exemplo de consulta SQL CTE:
-- Obtenha a contagem de pessoas por cidade, mostrando apenas cidades com mais de 1 habitantes

-- Explicação:
    -- CTE (PeopleCountPerCity) calcula o número de pessoas residentes em cada cidade.
    -- A consulta principal seleciona cidades do CTE com mais de 5 habitantes.
    -- A ordenação é decrescente por people_count, mostrando claramente as cidades com as maiores populações primeiro.