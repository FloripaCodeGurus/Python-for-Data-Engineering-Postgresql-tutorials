SELECT 
    p.first_name || ' ' || p.last_name AS full_name,
    c.city_name,
    s.name AS state_name,
    co.name AS country_name
FROM people p
JOIN cities c ON p.city_id = c.id
JOIN states s ON c.state_id = s.id
JOIN countries co ON s.country_id = co.id
WHERE co.id = (
    SELECT id FROM countries WHERE name = 'Brazil'
);

-- Example SQL Subquery:
-- Recupere o nome completo, nome da cidade, nome do estado e nome do país de todas as pessoas que vivem no Brasil.

-- Explicação:
--     O Main Query recupera os nomes completos das pessoas e sua cidade e detalhes do estado.
--     A subconsulta encontra o país de identificação do Brasil da tabela dos países.
--     A condição garante que apenas aqueles que residem em cidades pertencentes a estados brasileiros são selecionados.