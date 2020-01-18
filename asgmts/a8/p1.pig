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

-- Want to find the minimum salary for each team and check that it's > 100,000

-- Get minimum salary
Mins = FOREACH (GROUP Salaries BY teamID)
    GENERATE group, MIN(Salaries.salary) as small;
--dump Mins;

-- Keep only teams with min salary over 100,000
Rich = FILTER Mins BY small > 100000;
--dump Rich;

-- Create final list
Final = FOREACH Rich GENERATE group;
dump Final;
