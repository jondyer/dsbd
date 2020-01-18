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

-- Want to find the ML1 team, player with the most runs in 1960

-- Filter by year
Year = FILTER Batting BY yearID==1960;
--dump Year;

-- Filter by team
Team = FILTER Year BY (teamID == 'ML1');
--dump Team;

-- Order by most runs
Top = FOREACH (ORDER Team BY R DESC) GENERATE playerID, R;
--dump Top;

-- Restrict to top player
Final = Limit Top 1;
dump Final;
