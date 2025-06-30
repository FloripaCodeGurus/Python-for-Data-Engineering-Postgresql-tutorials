CREATE OR REPLACE FUNCTION get_people_by_country_and_agegroup(
    country_name TEXT,
    input_age_group TEXT
)
RETURNS TABLE (
    full_name TEXT,
    age INTEGER,
    city_name TEXT,
    state_name TEXT,
    country TEXT,
    age_group TEXT
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT
        p.first_name || ' ' || p.last_name AS full_name,
        p.age,
        c.city_name,
        s.name AS state_name,
        co.name AS country,
        CASE
            WHEN p.age < 30 THEN 'Young'
            WHEN p.age BETWEEN 30 AND 60 THEN 'Adult'
            ELSE 'Senior'
        END AS age_group
    FROM people p
    JOIN cities c ON p.city_id = c.id
    JOIN states s ON c.state_id = s.id
    JOIN countries co ON s.country_id = co.id
    WHERE co.name = country_name
      AND (
          (input_age_group = 'Young' AND p.age < 30) OR
          (input_age_group = 'Adult' AND p.age BETWEEN 30 AND 60) OR
          (input_age_group = 'Senior' AND p.age > 60)
      );
END;
$$;

Example: Stored Procedure to Retrieve People by Country and Age Group
This stored procedure retrieves all people belonging to a specific country and within a given age group (Young, Adult, Senior).

-- Exemplo: Stored Procedure para Recuperar Pessoas por País e Faixa Etária
-- Este procedimento armazenado recupera todas as pessoas pertencentes a um país específico e dentro de uma 
-- determinada faixa etária (Jovem, Adulto, Idoso).

SELECT * FROM get_people_by_country_and_agegroup('Brazil', 'Adult');
SELECT * FROM get_people_by_country_and_agegroup('USA', 'Senior');
SELECT * FROM get_people_by_country_and_agegroup('Canada', 'Young');

-- Explicação:
-- Parâmetros: country_name (ex.: "Brasil") e age_group ("Jovem", "Adulto" ou "Idoso").
-- Lógica de Procedimento Armazenado: Filtra pessoas com base no país especificado e as categoriza por faixa etária.
-- Retorna: Conjunto de resultados estruturado com nomes completos, idades, locais e suas respectivas faixas etárias.
-- Este procedimento demonstra encapsulamento eficaz, reutilização e clareza no tratamento de consultas complexas.