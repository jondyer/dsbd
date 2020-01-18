-- load our function from python
REGISTER 'a8_udf.py' USING jython AS py;

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

-- Want to calculate the homerun percentage field and then sort players accordingly

-- Apply the function to each player to get homerun percentage
Homers = FOREACH Batting GENERATE playerID, py.calc_hr_percent(G, HR) as hrp;
--dump Homers;

-- Now sorting and limit to top 10
Final = LIMIT (ORDER Homers BY hrp DESC) 10;
dump Final;
