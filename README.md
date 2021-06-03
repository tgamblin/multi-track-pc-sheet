# Multi-track PC Google Sheet

This repo contains a single Python script for generating one of the more
complicated queries in the
[Multi-track PC spreadsheet](https://docs.google.com/spreadsheets/d/1HG_4q2hHHVSjJVI-gi5t-9Po29hiWCWIBqIp_7aGgT8/edit#gid=435749560).

You'll need to edit `cols.py` to add the names of your tracks, then run it like
this:

```console
> ./cols.py
Elements:
TRACK1
TRACK2
CHAIR

Query:
=sort(iferror((query({query(indirect("TRACK1!$A$21:$M"), "select A,B,C,D,E,F,G,H,I,J,K,L,M,'TRACK1' label 'TRACK1' ''");
query(indirect("TRACK2!$A$21:$M"), "select A,B,C,D,E,F,G,H,I,J,K,L,M,'TRACK2' label 'TRACK2' ''");
query(indirect("CHAIR!$A$21:$M"), "select A,B,C,D,E,F,G,H,I,J,K,L,M,'CHAIR' label 'CHAIR' ''")},
"select Col1,Col2,Col3,Col4,Col5,Col6,Col7,Col8,Col9,Col10,Col11,Col12,Col13,Col14 where Col1 is not null", FALSE)))
>
```

Copy the query and paste it into the AllMembers sheet, here:

![Image of spreadsheet](https://raw.githubusercontent.com/tgamblin/multi-track-pc-sheet/main/paste-instructions.png)
