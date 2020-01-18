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

-- Want to find the average salary for each team in 1998, then list in proper order

-- Filter by year
Year = FILTER Salaries BY yearID==1998;
--dump Year

-- Get averages for each team
Avs = FOREACH (GROUP Year BY teamID)
    GENERATE group, AVG(Year.salary) as av;
--dump Avs;

-- Sort by desc avg salary then asc team name
Final = ORDER Avs BY av DESC, group ASC;
dump Final;
