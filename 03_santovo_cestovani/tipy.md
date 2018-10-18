# Rady a tipy k řešení
1) Chápeme zadání? Zkusit si vše nakreslit! Papír totiž existuje i pro programátory. :D
  - Zkuste si nakreslit mapu a v ní se pohybovat pomocí instrukcí ze zadání.
  - Nejprve zkuste ty jednodušší a ověřte si, že víte, jak to funguje.
2) __instructions.txt__ - WTF? Pojďme to zparsovat!
  - Stáhneme, načteme soubor, převedeme ho do podoby, abychom měli pole nebo `ArrayList instructions`, kde `instructions[0]` bude `R1`. Hodit se bude `trim()` a `split()`
  - Směr, kterym se otočit, získáme pomocí `charAt()`. O kolik se posunout pak zjistíme pomocí `substring()`.
3) Jak na "kompas"?
  - čísla a modulo
  - enum
4) Manhattanská metrika a logika instrukcí
5) Aktuální pozice
  - Zamyslete se, jestli nebude hezčí vytvořit si třídu Point do které budete ukládat souřadnice __x__ a __y__.
