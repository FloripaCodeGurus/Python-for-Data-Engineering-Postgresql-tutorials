SELECT
    p.first_name || ' ' || p.last_name AS full_name,
    p.age,
    c.city_name,
    CASE
        WHEN p.age < 30 THEN 'Young'
        WHEN p.age BETWEEN 30 AND 60 THEN 'Adult'
        ELSE 'Senior'
    END AS age_group
FROM people p
JOIN cities c ON p.city_id = c.id
ORDER BY age_group, p.age;


-- Example SQL CASE WHEN statement:
-- Classificar as pessoas em grupos etários (jovem, adultos, idosos) com base na idade.

-- Explicação:
--     A instrução CASE WHEN avalia a idade de cada pessoa e atribui um grupo etário correspondente.
--     Os resultados são ordenados primeiro pelo grupo etário e depois pela idade para facilitar a visualização.
--     A consulta retorna o nome completo, idade, nome da cidade e o grupo etário de cada pessoa.
--     Isso permite uma análise rápida da distribuição etária entre as pessoas em diferentes cidades.
--     A consulta pode ser útil para entender a demografia de uma população em termos de idade e localização.