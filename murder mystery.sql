-- QUERY TO FIND WITNESS 1

SELECT name, address_street_name, address_number, person_id, transcript
FROM person
JOIN interview
	ON person.id = interview.person_id
WHERE address_street_name = 'Northwestern Dr'
ORDER BY 4 DESC
LIMIT 1;


-- Should be Morty Schapiro

------------------------------------------------------------------------------------------
-- QUERY TO FIND WITNESS 2

SELECT name, address_street_name, address_number, person_id, transcript
FROM person
JOIN interview
	ON person.id = interview.person_id
WHERE name LIKE 'Annabel %';



-- Should be Annabel Miller

-------------------------------------------------------------------------------------------
-- ATTEMPT AT JOINING THE PREVIOUS QUERIES

SELECT name, address_street_name, MAX(address_number) AS address_num, person_id, transcript
FROM person
JOIN interview
	ON person.id = interview.person_id
WHERE address_street_name = 'Northwestern Dr'

UNION
SELECT name, address_street_name, address_number, person_id, transcript
FROM person
JOIN interview
	ON person.id = interview.person_id
WHERE name LIKE 'Annabel %';


-------------------------------------------------------------------------------------------
-- QUERY TO IDENTIFY THE MURDERER

WITH Suspect AS 
	(SELECT person.id AS id_of_person,
		get_fit_now_member.name AS name,
       		get_fit_now_member.id AS member_id,
       		get_fit_now_check_in.check_in_date AS check_in_date,
       		get_fit_now_member.membership_status AS member_status,
       		drivers_license.plate_number AS plate_number
		FROM person
		JOIN get_fit_now_member
			ON person.id = get_fit_now_member.person_id
		JOIN get_fit_now_check_in
			ON get_fit_now_check_in.membership_id = get_fit_now_member.id
		JOIN drivers_license
			ON person.license_id = drivers_license.id
		WHERE check_in_date LIKE '%0109'
			AND membership_id LIKE '48Z%'
				AND membership_status = 'gold') 

Select *
FROM Suspect
JOIN interview
	ON Suspect.id_of_person = interview.person_id

--------------------------------------------------------------------------------------------
-- QUERY TO IDENTIFY THE TRUE MASTERMIND

WITH mastermind_suspects AS
	(SELECT person_id,
		name, 
		license_id
		FROM facebook_event_checkin
		JOIN person
			ON facebook_event_checkin.person_id = person.id
		WHERE event_name = 'SQL Symphony Concert'
			AND date LIKE "201712%"
		GROUP BY person_id
		HAVING COUNT(person_id) >= 3)

SELECT *
FROM mastermind_suspects
JOIN drivers_license
	ON mastermind_suspects. license_id = drivers_license.id;