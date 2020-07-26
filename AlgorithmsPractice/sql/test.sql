select ret1.ITEM_ID, ret1.ACH_COUNT  from
	(select a1.ITEM_ID ITEM_ID, sum(a1.ITEM_ID) ACH_COUNT
	from 
		(select r.ITEM_ID
		from 
			CRECORD r, (select * from CEMPLOYEE where HIRE_DATE = (select min(HIRE_DATE) MIN_DATE from CEMPLOYEE)) h1
		where
			r.EMP_ID = h1.EMP_ID and r.ITEM_ID = '01'
		) a1
	group by a1.ITEM_ID) union

	(select a2.ITEM_ID ITEM_ID, sum(a2.ITEM_ID) ACH_COUNT
	from 
		(select r.ITEM_ID
		from 
			CRECORD r, (select * from CEMPLOYEE where HIRE_DATE = (select max(HIRE_DATE) MAX_DATE from CEMPLOYEE)) h2
		where
			r.EMP_ID = h2.EMP_ID and r.ITEM_ID = '02'
		) a2
	group by a2.ITEM_ID)
