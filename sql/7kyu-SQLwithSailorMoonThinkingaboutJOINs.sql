SELECT senshi_name AS sailor_senshi,
       real_name_jpn AS real_name, 
       name AS cat, 
       school
FROM sailorsenshi 
LEFT JOIN cats ON sailorsenshi.cat_id = cats.id
LEFT JOIN schools ON sailorsenshi.school_id = schools.id
