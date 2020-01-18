Data = LOAD 'tallest-buildings.txt' using PigStorage('!') as
               (category:chararray,
                structure, country, city,
		meter:chararray, -- float, 
                feet, year, coord);
--dump Data;

Height = FOREACH Data GENERATE meter;
--dump Height;

Digits = FOREACH Height GENERATE TRIM(meter) as t;
--dump Digits;

Lead = FOREACH Digits GENERATE SUBSTRING(t, 0, 1) as first;
--dump Lead;

Grp = GROUP Lead BY first;
--dump Grp;

Cnt = FOREACH Grp GENERATE group, COUNT(Lead) as c;
--dump Cnt;

Srt = ORDER Cnt BY c DESC;
dump Srt;
