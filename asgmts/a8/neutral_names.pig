-- First load the data from the input parameter file
Names = LOAD '$input' USING PigStorage(',') AS (
	state:		chararray,
	gender:		chararray,
	year:		int,
	fname:		chararray,
	number:		int);

-- Get all male names and their counts in groups
M_Filtered = FILTER Names BY gender=='M';
M_Groups = GROUP M_Filtered BY (fname, gender);
Male_Names = FOREACH M_Groups GENERATE group as m_key, SUM(M_Filtered.number) as mnumber;


-- Get all female names and their counts in groups
F_Filtered = FILTER Names BY gender=='F';
F_Groups = GROUP F_Filtered BY (fname, gender);
Female_Names = FOREACH F_Groups GENERATE group as f_key, SUM(F_Filtered.number) as fnumber;


-- Now join the two tables above (only keeping gender neutral names)
Joined_Names = JOIN Male_Names BY m_key.fname, Female_Names BY f_key.fname;


-- Let's add the extra field for total names and the male/female ratio
Totals = FOREACH Joined_Names GENERATE *, 
				(mnumber+fnumber) as total,
				((float)mnumber / (float)fnumber) as ratio;


-- Now we filter by those elements with ratio between 0.25 and 4
Filtered_Totals = FILTER (FILTER Totals BY ratio >= 0.25) BY ratio <= 4;


-- Finally sort by sum of names desc and limit to top 10 
Final = LIMIT (ORDER Filtered_Totals BY total DESC) 10;
		
dump Final;
