# Palindrom

Palindrom (z řec. palindromos, běžící pozpátku) je slovo, věta, číslo nebo melodie (obecně jakákoliv sekvence symbolů, např. sekvence DNA), která má tu vlastnost, že ji lze číst v libovolném směru zleva nebo zprava.
Jedná se například o slova: _radar_, _kajak_, _Anna_, _tahat_.

## Zadání
Vytvořte funkci s názvem `isPalindrome`, která bude brát jeden argument `String slovo` a bude mít návratový typ `bool`.

Vrátí `true` pokud slovo předané v argumentu bude palindrom, pokud nebude, očekávaná návratová hodnota je `false`.

## Příklad funkcionality
```java
public static void main() {
	System.out.println(isPalindrome("radar")) // vrací true
	System.out.println(isPalindrome("david")) // vrací false

	// pro rozšíření
	// easy
	System.out.println(isPalindrome("Anna")) // vrací true

	// medium
	System.out.println(isPalindrome("Kobyla ma maly bok")) // vrací true
}
```
## Rozšíření
1) Co, když funkci předáte jméno __Anna__? Asi si řekne, že se o palindrom nejedná. Zkuste funkci vylepšit tak, aby nezáleželo na velikosti písmen.
2) Co, když funkci předáme větu __Kobyla ma maly bok__ (tečku za větou nepišme)? Palindrom může být i věta, pokud se neberou v potaz mezery mezi slovy. Vylepšíte funkci tak, aby správně rozpoznávala palindromy z vět?

## Nápověda
- použijte cyklus __for__
- v podmínce cyklu se bude hodit metoda `slovo.length()`
- nebojte se googlit :)
