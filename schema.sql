CREATE TABLE "magickarten" (
  "id"	INTEGER NOT NULL UNIQUE,
  "Name"	TEXT NOT NULL,
  "Farbe"	TEXT,
  "Kosten"	INTEGER,
  "Typ"		TEXT,
  "Staerke"	INTEGER,
  "Abwehr"	INTEGER,
  "Seltenheit"	TEXT,
  "Holo"	TEXT,
  "Serie"	TEXT,
  "Anzahl"	INTEGER,
  "Sprache"	TEXT,
  "Decks"	TEXT,
  PRIMARY KEY("id" AUTOINCREMENT)
)
