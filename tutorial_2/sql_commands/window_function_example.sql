SELECT
    p.first_name || ' ' || p.last_name AS full_name,
    p.age,
    c.city_name,
    RANK() OVER (PARTITION BY c.city_name ORDER BY p.age DESC) AS age_rank_in_city
FROM people p
JOIN cities c ON p.city_id = c.id
ORDER BY c.city_name, age_rank_in_city;

-- SQL Window Function Example:
    -- Recupere o nome completo, idade e nome da cidade de cada pessoa, juntamente com uma classificação por 
    -- idade dentro de cada cidade (o mais antigo primeiro)

    -- Explicação:
    --     RANK() atribui um rank numérico às linhas, reiniciando de 1 para cada cidade (partição).
    --     PARTITION BY c.city_name significa ranking resets para cada cidade distinta.
    --     O ENCOMÉRDA POR P.age DESC classifica os indivíduos mais velhos em primeiro lugar.
    --     Os resultados são ordenados claramente pela cidade e classificação para a legibilidade.  