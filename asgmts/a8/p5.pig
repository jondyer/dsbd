-- The Lahman Baseball Database

Salaries = load 'Salaries.csv' USING PigStorage(',') AS (
        yearID:     int,
        teamID:     chararray,
        lgID:       chararray,
        playerID:   chararray,
        salary:     int
	);


Batting = load 'Batting.csv' USING PigStorage(',') AS (
	playerID:    chararray,
        yearID:      int,
        stint:       int,
        teamID:      chararray,
        lgID:        chararray,
        G:           int,
        G_batting:   int,
        AB:          int,
        R:           int,
        H:           int,
        B2:          int,
        B3:          int,
        HR:          int,
        RBI:         int,
        SB:          int,
        CS:          int,
        BB:          int,
        SO:          int,
        IBB:         int,
        HBP:         int,
        SH:          int,
        SF:          int,
        GIDP:        int
	);

-- Want to merge the two tables by playerID. First let's filter both by the conditions.

-- Filter salaries by year
YearS = FILTER Salaries BY yearID==2001;
--dump YearS;

-- Keep only high salaries
HighSal = FILTER YearS BY salary > 500000;
--dump HighSal;

-- Filter batting by year
YearB = FILTER Batting BY yearID==2001;
--dump YearB;

-- Keep only high homeruns
Homer = FILTER YearB BY HR > 50;
--dump Homer;

-- Get just the columns we want from each table.
SalColumns = FOREACH HighSal GENERATE playerID, salary;
--dump SalColumns;

BatColumns = FOREACH Homer GENERATE playerID, HR;
--dump BatColumns;

-- Finally join the tables and retrieve our desired information
Final = FOREACH (JOIN BatColumns BY playerID, SalColumns BY playerID) 
    GENERATE SalColumns::playerID, HR, salary;
dump Final;
