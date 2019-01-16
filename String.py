'''
Simulates python string built-in functions

STRING CONSTANTS

string.ascii_letters
The concatenation of the ascii_lowercase and ascii_uppercase constants described below. This value is not locale-dependent.

string.ascii_lowercase
The lowercase letters 'abcdefghijklmnopqrstuvwxyz'. This value is not locale-dependent and will not change.

string.ascii_uppercase
The uppercase letters 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'. This value is not locale-dependent and will not change.

string.digits
The string '0123456789'.

string.hexdigits
The string '0123456789abcdefABCDEF'.

string.letters
The concatenation of the strings lowercase and uppercase described below. The specific value is locale-dependent, and will be updated when locale.setlocale() is called.

string.lowercase
A string containing all the characters that are considered lowercase letters. On most systems this is the string 'abcdefghijklmnopqrstuvwxyz'. The specific value is locale-dependent, and will be updated when locale.setlocale() is called.

string.octdigits
The string '01234567'.

string.punctuation
String of ASCII characters which are considered punctuation characters in the C locale.

string.printable
String of characters which are considered printable. This is a combination of digits, letters, punctuation, and whitespace.

string.uppercase
A string containing all the characters that are considered uppercase letters. On most systems this is the string 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'. The specific value is locale-dependent, and will be updated when locale.setlocale() is called.

string.whitespace
A string containing all characters that are considered whitespace. On most systems this includes the characters space, tab, linefeed, return, formfeed, and vertical tab.


STRING FUNCTIONS

string.capitalize(word)
Return a copy of word with only its first character capitalized.

string.expandtabs(s[, tabsize])
Expand tabs in a string replacing them by one or more spaces, depending on the current column and the given tab size. The column number is reset to zero after each newline occurring in the string. This doesn’t understand other non-printing characters or escape sequences. The tab size defaults to 8.

string.find(s, sub[, start[, end]])
Return the lowest index in s where the substring sub is found such that sub is wholly contained in s[start:end]. Return -1 on failure. Defaults for start and end and interpretation of negative values is the same as for slices.

string.rfind(s, sub[, start[, end]])
Like find() but find the highest index.

string.index(s, sub[, start[, end]])
Like find() but raise ValueError when the substring is not found.

string.rindex(s, sub[, start[, end]])
Like rfind() but raise ValueError when the substring is not found.

string.count(s, sub[, start[, end]])
Return the number of (non-overlapping) occurrences of substring sub in string s[start:end]. Defaults for start and end and interpretation of negative values are the same as for slices.

string.lower(s)
Return a copy of s, but with upper case letters converted to lower case.

string.split(s[, sep[, maxsplit]])
Return a list of the words of the string s. If the optional second argument sep is absent or None, the words are separated by arbitrary strings of whitespace characters (space, tab, newline, return, formfeed). If the second argument sep is present and not None, it specifies a string to be used as the word separator. The returned list will then have one more item than the number of non-overlapping occurrences of the separator in the string. If maxsplit is given, at most maxsplit number of splits occur, and the remainder of the string is returned as the final element of the list (thus, the list will have at most maxsplit+1 elements). If maxsplit is not specified or -1, then there is no limit on the number of splits (all possible splits are made).

The behavior of split on an empty string depends on the value of sep. If sep is not specified, or specified as None, the result will be an empty list. If sep is specified as any string, the result will be a list containing one element which is an empty string.

string.rsplit(s[, sep[, maxsplit]])
Return a list of the words of the string s, scanning s from the end. To all intents and purposes, the resulting list of words is the same as returned by split(), except when the optional third argument maxsplit is explicitly specified and nonzero. If maxsplit is given, at most maxsplit number of splits – the rightmost ones – occur, and the remainder of the string is returned as the first element of the list (thus, the list will have at most maxsplit+1 elements).

New in version 2.4.

string.splitfields(s[, sep[, maxsplit]])
This function behaves identically to split(). (In the past, split() was only used with one argument, while splitfields() was only used with two arguments.)

string.join(words[, sep])
Concatenate a list or tuple of words with intervening occurrences of sep. The default value for sep is a single space character. It is always true that string.join(string.split(s, sep), sep) equals s.

string.joinfields(words[, sep])
This function behaves identically to join(). (In the past, join() was only used with one argument, while joinfields() was only used with two arguments.) Note that there is no joinfields() method on string objects; use the join() method instead.

string.lstrip(s[, chars])
Return a copy of the string with leading characters removed. If chars is omitted or None, whitespace characters are removed. If given and not None, chars must be a string; the characters in the string will be stripped from the beginning of the string this method is called on.

Changed in version 2.2.3: The chars parameter was added. The chars parameter cannot be passed in earlier 2.2 versions.

string.rstrip(s[, chars])
Return a copy of the string with trailing characters removed. If chars is omitted or None, whitespace characters are removed. If given and not None, chars must be a string; the characters in the string will be stripped from the end of the string this method is called on.

Changed in version 2.2.3: The chars parameter was added. The chars parameter cannot be passed in earlier 2.2 versions.

string.strip(s[, chars])
Return a copy of the string with leading and trailing characters removed. If chars is omitted or None, whitespace characters are removed. If given and not None, chars must be a string; the characters in the string will be stripped from the both ends of the string this method is called on.

Changed in version 2.2.3: The chars parameter was added. The chars parameter cannot be passed in earlier 2.2 versions.

string.swapcase(s)
Return a copy of s, but with lower case letters converted to upper case and vice versa.

string.translate(s, table[, deletechars])
Delete all characters from s that are in deletechars (if present), and then translate the characters using table, which must be a 256-character string giving the translation for each character value, indexed by its ordinal. If table is None, then only the character deletion step is performed.

string.upper(s)
Return a copy of s, but with lower case letters converted to upper case.

string.ljust(s, width[, fillchar])
string.rjust(s, width[, fillchar])
string.center(s, width[, fillchar])
These functions respectively left-justify, right-justify and center a string in a field of given width. They return a string that is at least width characters wide, created by padding the string s with the character fillchar (default is a space) until the given width on the right, left or both sides. The string is never truncated.

string.zfill(s, width)
Pad a numeric string s on the left with zero digits until the given width is reached. Strings starting with a sign are handled correctly.

string.replace(s, old, new[, maxreplace])
Return a copy of string s with all occurrences of substring old replaced by new. If the optional argument maxreplace is given, the first maxreplace occurrences are replaced.

'''
