# -*- coding: utf-8 -*-
"""PGMaster function catalog. Every entry is executed against PostgreSQL 16
at build time; the printed output in the site is the server's real answer."""

CATS = [
    ("Math", "1. Math & Numeric", "#38bdf8"),
    ("String", "2. String & Text", "#3fb950"),
    ("Binary", "3. Binary, Bit & Encoding", "#8b949e"),
    ("Format", "4. Data Type Formatting", "#f97316"),
    ("DateTime", "5. Date / Time", "#e3b341"),
    ("Conditional", "6. Conditional", "#da3633"),
    ("Array", "7. Array", "#a371f7"),
    ("Range", "8. Range & Multirange", "#db61a2"),
    ("JSON", "9. JSON & JSONB", "#00bcd4"),
    ("XML", "10. XML", "#bc8cff"),
    ("TextSearch", "11. Full Text Search", "#56d364"),
    ("Aggregate", "12. Aggregate", "#f778ba"),
    ("Window", "13. Window", "#79c0ff"),
    ("SetReturning", "14. Set Returning"  , "#ffa657"),
    ("Sequence", "15. Sequence", "#d29922"),
    ("Network", "16. Network Address", "#39c5cf"),
    ("Geometric", "17. Geometric", "#a5d6ff"),
    ("Types", "18. Enum, UUID & Type Info", "#ff7b72"),
    ("SystemInfo", "19. System Information", "#7ee787"),
    ("Admin", "20. System Administration", "#ffa198"),
    ("Trigger", "21. Trigger & Event", "#d2a8ff"),
]

FUNCS = []

def F(cat, name, sig, desc, code, setup=None, out=None, volatile=False):
    FUNCS.append(dict(cat=cat, name=name, sig=sig, desc=desc, code=code,
                      setup=setup, out=out, volatile=volatile))

# ------------------------------------------------------------------ 1. MATH
F("Math", "abs", "abs(numeric) -> numeric", "Absolute (unsigned) value of a number.", "SELECT abs(-17.4) AS abs_neg, abs(17.4) AS abs_pos;")
F("Math", "cbrt", "cbrt(double) -> double", "Cube root of the argument.", "SELECT cbrt(64.0) AS cube_root;")
F("Math", "ceil", "ceil(numeric) -> numeric", "Nearest integer greater than or equal to the argument.", "SELECT ceil(42.2) AS up, ceil(-42.8) AS up_neg;")
F("Math", "ceiling", "ceiling(numeric) -> numeric", "Standard SQL alias for ceil().", "SELECT ceiling(42.2) AS ceiling;")
F("Math", "degrees", "degrees(double) -> double", "Converts radians to degrees.", "SELECT degrees(pi()) AS deg, degrees(pi()/2) AS half;")
F("Math", "div", "div(y numeric, x numeric) -> numeric", "Integer quotient of y/x, truncating toward zero.", "SELECT div(9, 4) AS quotient, 9 / 4 AS int_division;")
F("Math", "exp", "exp(numeric) -> numeric", "Exponential of the argument (e raised to the power x).", "SELECT exp(1.0) AS e, exp(0) AS e_zero;")
F("Math", "factorial", "factorial(bigint) -> numeric", "Factorial of a non-negative integer.", "SELECT factorial(5) AS f5, factorial(10) AS f10;")
F("Math", "floor", "floor(numeric) -> numeric", "Nearest integer less than or equal to the argument.", "SELECT floor(42.8) AS down, floor(-42.2) AS down_neg;")
F("Math", "gcd", "gcd(a, b) -> numeric", "Greatest common divisor of the two arguments.", "SELECT gcd(1071, 462) AS gcd;")
F("Math", "lcm", "lcm(a, b) -> numeric", "Least common multiple of the two arguments.", "SELECT lcm(6, 10) AS lcm;")
F("Math", "ln", "ln(numeric) -> numeric", "Natural (base e) logarithm.", "SELECT ln(2.0) AS ln2, ln(exp(1)) AS ln_e;")
F("Math", "log", "log(numeric) / log(b, x) -> numeric", "Base 10 logarithm, or logarithm to the given base b.", "SELECT log(1000) AS base10, log(2.0, 64.0) AS base2;")
F("Math", "log10", "log10(numeric) -> numeric", "Base 10 logarithm (explicit spelling).", "SELECT log10(1000) AS log10;")
F("Math", "min_scale", "min_scale(numeric) -> integer", "Minimum scale (decimal digits) needed to represent the value exactly.", "SELECT min_scale(8.4100) AS min_scale, scale(8.4100) AS stored_scale;")
F("Math", "mod", "mod(y, x) -> numeric", "Remainder of y/x; sign follows y.", "SELECT mod(9, 4) AS r1, mod(-9, 4) AS r2;")
F("Math", "pi", "pi() -> double", "The constant PI.", "SELECT pi() AS pi;")
F("Math", "power", "power(a, b) -> numeric", "a raised to the power of b.", "SELECT power(2, 10) AS pow, 2 ^ 10 AS operator_form;")
F("Math", "radians", "radians(double) -> double", "Converts degrees to radians.", "SELECT radians(180) AS rad, radians(45) AS rad45;")
F("Math", "random", "random() -> double", "Random value in the range 0.0 <= x < 1.0.", "SELECT random() AS r1, random() AS r2;", volatile=True)
F("Math", "random_normal", "random_normal(mean, stddev) -> double", "Normally distributed random value (PostgreSQL 16+).", "SELECT round(random_normal(100, 15)::numeric, 3) AS iq_sample;", volatile=True)
F("Math", "round", "round(numeric [, s]) -> numeric", "Rounds to the nearest integer, or to s decimal places.", "SELECT round(42.4382) AS whole, round(42.4382, 2) AS two_dp, round(-0.5) AS half_away;")
F("Math", "scale", "scale(numeric) -> integer", "Scale of the argument (decimal digits in the fractional part).", "SELECT scale(8.4100) AS scale;")
F("Math", "setseed", "setseed(double) -> void", "Sets the seed for subsequent random() calls, making them reproducible.", "SELECT setseed(0.42) AS seeded, random() AS deterministic;")
F("Math", "sign", "sign(numeric) -> numeric", "Sign of the argument: -1, 0 or +1.", "SELECT sign(-8.4) AS neg, sign(0) AS zero, sign(8.4) AS pos;")
F("Math", "sqrt", "sqrt(numeric) -> numeric", "Square root of the argument.", "SELECT sqrt(2) AS root2, |/ 25.0 AS operator_form;")
F("Math", "trim_scale", "trim_scale(numeric) -> numeric", "Reduces the scale by dropping trailing fractional zeroes.", "SELECT trim_scale(8.4100) AS trimmed;")
F("Math", "trunc", "trunc(numeric [, s]) -> numeric", "Truncates toward zero, optionally to s decimal places.", "SELECT trunc(42.8) AS whole, trunc(42.4382, 2) AS two_dp, trunc(-42.8) AS neg;")
F("Math", "width_bucket", "width_bucket(operand, low, high, count) -> integer", "Bucket number in an equal-width histogram.", "SELECT width_bucket(5.35, 0, 10, 5) AS bucket, width_bucket(9.99, 0, 10, 5) AS top_bucket;")
F("Math", "acos", "acos(double) -> double", "Inverse cosine, result in radians.", "SELECT acos(1) AS zero_rad, acos(0) AS half_pi;")
F("Math", "acosd", "acosd(double) -> double", "Inverse cosine, result in degrees.", "SELECT acosd(0.5) AS degrees;")
F("Math", "asin", "asin(double) -> double", "Inverse sine, result in radians.", "SELECT asin(1) AS half_pi;")
F("Math", "asind", "asind(double) -> double", "Inverse sine, result in degrees.", "SELECT asind(0.5) AS degrees;")
F("Math", "atan", "atan(double) -> double", "Inverse tangent, result in radians.", "SELECT atan(1) AS quarter_pi;")
F("Math", "atand", "atand(double) -> double", "Inverse tangent, result in degrees.", "SELECT atand(1) AS degrees;")
F("Math", "atan2", "atan2(y, x) -> double", "Inverse tangent of y/x, result in radians (quadrant aware).", "SELECT atan2(1, 1) AS radians;")
F("Math", "atan2d", "atan2d(y, x) -> double", "Inverse tangent of y/x, result in degrees.", "SELECT atan2d(1, 1) AS degrees;")
F("Math", "cos", "cos(double) -> double", "Cosine, argument in radians.", "SELECT cos(0) AS one, round(cos(pi())::numeric, 10) AS minus_one;")
F("Math", "cosd", "cosd(double) -> double", "Cosine, argument in degrees.", "SELECT cosd(60) AS half;")
F("Math", "cot", "cot(double) -> double", "Cotangent, argument in radians.", "SELECT cot(0.5) AS cot;")
F("Math", "cotd", "cotd(double) -> double", "Cotangent, argument in degrees.", "SELECT cotd(45) AS one;")
F("Math", "sin", "sin(double) -> double", "Sine, argument in radians.", "SELECT sin(0) AS zero, sin(pi()/2) AS one;")
F("Math", "sind", "sind(double) -> double", "Sine, argument in degrees.", "SELECT sind(30) AS half;")
F("Math", "tan", "tan(double) -> double", "Tangent, argument in radians.", "SELECT tan(0) AS zero, round(tan(pi()/4)::numeric, 10) AS one;")
F("Math", "tand", "tand(double) -> double", "Tangent, argument in degrees.", "SELECT tand(45) AS one;")
F("Math", "sinh", "sinh(double) -> double", "Hyperbolic sine.", "SELECT sinh(1) AS sinh;")
F("Math", "cosh", "cosh(double) -> double", "Hyperbolic cosine.", "SELECT cosh(0) AS one, cosh(1) AS cosh1;")
F("Math", "tanh", "tanh(double) -> double", "Hyperbolic tangent.", "SELECT tanh(1) AS tanh;")
F("Math", "asinh", "asinh(double) -> double", "Inverse hyperbolic sine.", "SELECT asinh(1) AS asinh;")
F("Math", "acosh", "acosh(double) -> double", "Inverse hyperbolic cosine.", "SELECT acosh(1) AS zero, acosh(2) AS acosh2;")
F("Math", "atanh", "atanh(double) -> double", "Inverse hyperbolic tangent.", "SELECT atanh(0.5) AS atanh;")

# ---------------------------------------------------------------- 2. STRING
F("String", "ascii", "ascii(text) -> integer", "Unicode code point of the first character of the string.", "SELECT ascii('A') AS a, ascii('x') AS x;")
F("String", "bit_length", "bit_length(text) -> integer", "Number of bits in the string (8 times octet_length).", "SELECT bit_length('jose') AS bits;")
F("String", "btrim", "btrim(string [, characters]) -> text", "Removes the longest string of listed characters from both ends.", "SELECT btrim('  spaced  ') AS spaces, btrim('xxhelloxx', 'x') AS chars;")
F("String", "char_length", "char_length(text) -> integer", "Number of characters in the string.", "SELECT char_length('PostgreSQL') AS chars, character_length('cafe') AS alias;")
F("String", "chr", "chr(integer) -> text", "Character with the given Unicode code point.", "SELECT chr(65) AS letter, chr(9731) AS snowman;")
F("String", "concat", "concat(val1, val2, ...) -> text", "Concatenates all arguments; NULL arguments are ignored.", "SELECT concat('Post', 'gre', NULL, 'SQL') AS joined;")
F("String", "concat_ws", "concat_ws(sep, val1, val2, ...) -> text", "Concatenates with a separator, skipping NULL arguments.", "SELECT concat_ws('-', 2026, 01, 09) AS iso_date, concat_ws(', ', 'Alice', NULL, 'IT') AS skips_null;")
F("String", "format", "format(formatstr, args...) -> text", "Formats a string, C sprintf style: %s value, %I identifier, %L literal.", "SELECT format('Hello, %s! You are %s.', 'Alice', 'hired') AS greeting, format('SELECT * FROM %I WHERE name = %L', 'employees', 'O''Hara') AS safe_sql;")
F("String", "initcap", "initcap(text) -> text", "Capitalises the first letter of each word, lowercasing the rest.", "SELECT initcap('hello wide world') AS title_case;")
F("String", "left", "left(string, n) -> text", "First n characters; when n is negative, all but the last |n|.", "SELECT left('PostgreSQL', 4) AS first4, left('PostgreSQL', -3) AS drop_last3;")
F("String", "length", "length(text) -> integer", "Number of characters in the string.", "SELECT length('PostgreSQL') AS len, length('  padded  ') AS with_spaces;")
F("String", "lower", "lower(text) -> text", "Converts the string to lower case.", "SELECT lower('PostgreSQL ROCKS') AS lowered;")
F("String", "lpad", "lpad(string, length [, fill]) -> text", "Left-pads (or truncates) the string to the given length.", "SELECT lpad('7', 3, '0') AS zero_pad, lpad('PostgreSQL', 4) AS truncated;")
F("String", "ltrim", "ltrim(string [, characters]) -> text", "Removes listed characters from the start of the string.", "SELECT ltrim('   left') AS spaces, ltrim('000042', '0') AS strip_zeros;")
F("String", "md5", "md5(text) -> text", "MD5 hash of the argument, as a hexadecimal string.", "SELECT md5('postgres') AS hash;")
F("String", "normalize", "normalize(text [, form]) -> text", "Converts the string to the given Unicode normalization form.", "SELECT normalize(U&'\\0065\\0301', NFC) = U&'\\00E9' AS composed_equal;")
F("String", "octet_length", "octet_length(text) -> integer", "Number of bytes in the string.", "SELECT octet_length('jose') AS ascii_bytes, octet_length('josé') AS utf8_bytes;")
F("String", "overlay", "overlay(string PLACING newsub FROM start [FOR count]) -> text", "Replaces a substring with another, by position.", "SELECT overlay('Txxxxas' placing 'hom' from 2 for 4) AS replaced;")
F("String", "parse_ident", "parse_ident(qualified_identifier) -> text[]", "Splits a qualified identifier into an array of its parts.", "SELECT parse_ident('public.employees.name') AS parts;")
F("String", "position", "position(substring IN string) -> integer", "Location of the first occurrence of substring, 1-based; 0 when absent.", "SELECT position('gre' in 'PostgreSQL') AS found, position('zzz' in 'PostgreSQL') AS missing;")
F("String", "quote_ident", "quote_ident(text) -> text", "Quotes a string so it can be used as an SQL identifier.", "SELECT quote_ident('employees') AS plain, quote_ident('Mixed Case') AS needs_quotes;")
F("String", "quote_literal", "quote_literal(text) -> text", "Quotes a string as an SQL literal, doubling embedded quotes.", "SELECT quote_literal('O''Hara') AS safe;")
F("String", "quote_nullable", "quote_nullable(text) -> text", "Like quote_literal(), but returns the string NULL for a NULL input.", "SELECT quote_nullable('Alice') AS value, quote_nullable(NULL) AS null_in;")
F("String", "regexp_count", "regexp_count(string, pattern) -> integer", "Counts the matches of a POSIX regular expression.", "SELECT regexp_count('ABCABCAXYaxy', 'A.') AS matches;")
F("String", "regexp_instr", "regexp_instr(string, pattern [, start, N]) -> integer", "Position of the Nth match of a regular expression.", "SELECT regexp_instr('ABCDEF', 'c(.)(..)', 1, 1, 0, 'i') AS pos;")
F("String", "regexp_like", "regexp_like(string, pattern [, flags]) -> boolean", "True when the string matches the regular expression.", "SELECT regexp_like('Hello World', 'world$', 'i') AS ci_match, regexp_like('Hello', '^h') AS cs_match;")
F("String", "regexp_match", "regexp_match(string, pattern) -> text[]", "First match of the pattern; capture groups become array elements.", "SELECT regexp_match('alice@corp.io', '(.+)@(.+)') AS parts;")
F("String", "regexp_matches", "regexp_matches(string, pattern [, flags]) -> setof text[]", "Set of all matches; use the g flag to return every match as a row.", "SELECT regexp_matches('cat bat rat', '(.)at', 'g') AS m;")
F("String", "regexp_replace", "regexp_replace(string, pattern, replacement [, flags]) -> text", "Replaces matches of a regular expression; \\1 refers to a capture group.", "SELECT regexp_replace('Alice Smith', '(\\w+) (\\w+)', '\\2, \\1') AS swapped, regexp_replace('a1b2c3', '\\d', '#', 'g') AS all_digits;")
F("String", "regexp_split_to_array", "regexp_split_to_array(string, pattern) -> text[]", "Splits the string using a regular expression, returning an array.", "SELECT regexp_split_to_array('one1two22three', '\\d+') AS parts;")
F("String", "regexp_split_to_table", "regexp_split_to_table(string, pattern) -> setof text", "Splits the string using a regular expression, returning one row per piece.", "SELECT regexp_split_to_table('the quick brown fox', '\\s+') AS word;")
F("String", "regexp_substr", "regexp_substr(string, pattern [, start, N]) -> text", "Returns the Nth substring matching the regular expression.", "SELECT regexp_substr('order 4711 shipped', '\\d+') AS number;")
F("String", "repeat", "repeat(string, number) -> text", "Repeats the string the given number of times.", "SELECT repeat('=-', 5) AS rule;")
F("String", "replace", "replace(string, from, to) -> text", "Replaces every occurrence of a literal substring.", "SELECT replace('2026-01-09', '-', '/') AS slashes;")
F("String", "reverse", "reverse(text) -> text", "Reverses the order of the characters.", "SELECT reverse('PostgreSQL') AS backwards;")
F("String", "right", "right(string, n) -> text", "Last n characters; when n is negative, all but the first |n|.", "SELECT right('PostgreSQL', 3) AS last3, right('PostgreSQL', -4) AS drop_first4;")
F("String", "rpad", "rpad(string, length [, fill]) -> text", "Right-pads (or truncates) the string to the given length.", "SELECT rpad('Alice', 10, '.') AS padded;")
F("String", "rtrim", "rtrim(string [, characters]) -> text", "Removes listed characters from the end of the string.", "SELECT rtrim('right   ') || '|' AS spaces, rtrim('trailing///', '/') AS slashes;")
F("String", "split_part", "split_part(string, delimiter, n) -> text", "Nth field of the string, counting from a delimiter; negative counts from the end.", "SELECT split_part('a,b,c,d', ',', 2) AS second, split_part('a,b,c,d', ',', -1) AS last;")
F("String", "starts_with", "starts_with(string, prefix) -> boolean", "True when the string begins with the given prefix.", "SELECT starts_with('PostgreSQL', 'Post') AS yes, starts_with('PostgreSQL', 'My') AS no;")
F("String", "string_to_array", "string_to_array(string, delimiter [, null_string]) -> text[]", "Splits the string on a delimiter into an array.", "SELECT string_to_array('IT,Sales,HR', ',') AS depts;")
F("String", "string_to_table", "string_to_table(string, delimiter) -> setof text", "Splits the string on a delimiter into a set of rows.", "SELECT string_to_table('IT,Sales,HR', ',') AS dept;")
F("String", "strpos", "strpos(string, substring) -> integer", "Location of the substring, 1-based (same as position()).", "SELECT strpos('PostgreSQL', 'SQL') AS pos;")
F("String", "substr", "substr(string, start [, count]) -> text", "Extracts a substring by position and length.", "SELECT substr('PostgreSQL', 5, 3) AS mid, substr('PostgreSQL', 5) AS to_end;")
F("String", "substring", "substring(string FROM start FOR count) -> text", "SQL-standard substring; also supports a regular expression pattern.", "SELECT substring('PostgreSQL' from 1 for 4) AS by_pos, substring('order 4711' from '\\d+') AS by_regex;")
F("String", "to_hex", "to_hex(integer) -> text", "Hexadecimal representation of an integer.", "SELECT to_hex(255) AS ff, to_hex(2147483647) AS max_int;")
F("String", "translate", "translate(string, from, to) -> text", "Replaces characters one-for-one using two character sets.", "SELECT translate('12345', '143', 'ax') AS translated;")
F("String", "trim", "trim([LEADING|TRAILING|BOTH] chars FROM string) -> text", "SQL-standard trim of characters from either or both ends.", "SELECT trim(both 'x' from 'xxPostgresxx') AS both_ends, trim(leading '0' from '00042') AS leading;")
F("String", "unistr", "unistr(text) -> text", "Evaluates Unicode escapes in the string (PostgreSQL 16+).", "SELECT unistr('d\\0061t\\+000061') AS decoded;")
F("String", "upper", "upper(text) -> text", "Converts the string to upper case.", "SELECT upper('postgresql rocks') AS shouted;")
F("String", "|| (concatenation)", "text || text -> text", "Concatenation operator; a NULL operand yields NULL.", "SELECT 'Post' || 'greSQL' AS joined, 'Post' || NULL AS null_result;")
F("String", "LIKE", "string LIKE pattern -> boolean", "Pattern match with % (any sequence) and _ (any single character).", "SELECT name FROM employees WHERE name LIKE 'A%' OR name LIKE '_o%';")
F("String", "ILIKE", "string ILIKE pattern -> boolean", "Case-insensitive LIKE.", "SELECT name FROM employees WHERE name ILIKE 'a%';")
F("String", "SIMILAR TO", "string SIMILAR TO pattern -> boolean", "SQL-standard regular expression matching.", "SELECT 'abc' SIMILAR TO '%(b|d)%' AS matches, 'abc' SIMILAR TO 'a' AS whole_string;")
F("String", "~ (regex match)", "string ~ pattern -> boolean", "POSIX regular expression operators: ~, ~*, !~, !~*.", "SELECT 'PostgreSQL' ~ 'gre' AS match, 'PostgreSQL' ~* 'SQL$' AS ci_match, 'PostgreSQL' !~ 'MySQL' AS not_match;")

# ------------------------------------------- 3. BINARY, BIT & ENCODING
F("Binary", "encode", "encode(bytes bytea, format) -> text", "Encodes binary data into a text representation: base64, hex or escape.", "SELECT encode('PostgreSQL'::bytea, 'base64') AS b64, encode('Pg'::bytea, 'hex') AS hex;")
F("Binary", "decode", "decode(string text, format) -> bytea", "Decodes text back into binary data.", "SELECT decode('UG9zdGdyZVNRTA==', 'base64') AS bytes, convert_from(decode('5067', 'hex'), 'UTF8') AS text_again;")
F("Binary", "convert_to", "convert_to(string text, dest_encoding) -> bytea", "Converts a text value to the given encoding, as bytea.", "SELECT convert_to('café', 'LATIN1') AS latin1_bytes;")
F("Binary", "convert_from", "convert_from(bytes bytea, src_encoding) -> text", "Converts bytea in the given encoding to the database encoding.", "SELECT convert_from('\\x636166c3a9'::bytea, 'UTF8') AS decoded;")
F("Binary", "convert", "convert(bytes, src_encoding, dest_encoding) -> bytea", "Converts binary data from one encoding to another.", "SELECT encode(convert('café'::bytea, 'UTF8', 'LATIN1'), 'hex') AS latin1_hex;")
F("Binary", "length (bytea)", "length(bytea) -> integer", "Number of bytes in a binary string.", "SELECT length('\\x120034'::bytea) AS bytes, octet_length('café'::bytea) AS utf8_bytes;")
F("Binary", "substr (bytea)", "substr(bytes, start [, count]) -> bytea", "Extracts a run of bytes from a binary string.", "SELECT substr('\\x1234567890'::bytea, 2, 3) AS slice;")
F("Binary", "btrim (bytea)", "btrim(bytes, bytesremoved) -> bytea", "Trims the listed bytes from both ends of a binary string.", "SELECT btrim('\\x1234567890'::bytea, '\\x9012'::bytea) AS trimmed;")
F("Binary", "get_bit", "get_bit(bits, n) -> integer", "Extracts the nth bit from a binary or bit string.", "SELECT get_bit('\\x1234'::bytea, 7) AS byte_bit, get_bit(B'10101', 0) AS bit_str;")
F("Binary", "set_bit", "set_bit(bits, n, newvalue) -> bytea", "Sets the nth bit of a binary or bit string.", "SELECT set_bit('\\x1234'::bytea, 7, 1) AS flipped;")
F("Binary", "get_byte", "get_byte(bytes, n) -> integer", "Extracts the nth byte (0-based) of a binary string.", "SELECT get_byte('\\x1234567890'::bytea, 4) AS byte;")
F("Binary", "set_byte", "set_byte(bytes, n, newvalue) -> bytea", "Sets the nth byte of a binary string.", "SELECT set_byte('\\x1234567890'::bytea, 4, 64) AS updated;")
F("Binary", "bit_count", "bit_count(bytes) -> bigint", "Counts the set bits (population count) in a binary or bit string.", "SELECT bit_count('\\x1234567890'::bytea) AS ones, bit_count(B'10111') AS bit_ones;")
F("Binary", "md5 (bytea)", "md5(bytea) -> text", "MD5 hash of binary data as a hexadecimal string.", "SELECT md5('\\x1234567890'::bytea) AS hash;")
F("Binary", "sha224", "sha224(bytea) -> bytea", "SHA-224 hash of binary data.", "SELECT encode(sha224('postgres'::bytea), 'hex') AS digest;")
F("Binary", "sha256", "sha256(bytea) -> bytea", "SHA-256 hash of binary data.", "SELECT encode(sha256('postgres'::bytea), 'hex') AS digest;")
F("Binary", "sha384", "sha384(bytea) -> bytea", "SHA-384 hash of binary data.", "SELECT left(encode(sha384('postgres'::bytea), 'hex'), 48) || '...' AS digest_head;")
F("Binary", "sha512", "sha512(bytea) -> bytea", "SHA-512 hash of binary data.", "SELECT left(encode(sha512('postgres'::bytea), 'hex'), 48) || '...' AS digest_head;")
F("Binary", "overlay (bit)", "overlay(bits PLACING newbits FROM start) -> bit", "Replaces a run of bits inside a bit string.", "SELECT overlay(B'01010101010101010' placing B'11111' from 2) AS overlaid;")
F("Binary", "position (bit)", "position(substring IN bits) -> integer", "Location of the first occurrence of a bit substring.", "SELECT position(B'010' in B'000001101011') AS pos;")
F("Binary", "bit shift & logic", "bits << n, bits & bits, ~bits", "Bitwise operators on bit strings and integers: AND, OR, XOR, NOT, shifts.", "SELECT B'10001' & B'01101' AS and_op, B'10001' | B'01101' AS or_op, B'10001' # B'01101' AS xor_op, B'10001' << 3 AS shifted, 17 & 5 AS int_and;")
F("Binary", "cast to bit", "integer::bit(n), bit::integer", "Casting between integers and bit strings.", "SELECT 44::bit(10) AS as_bits, B'1010'::int AS as_int;")

# ------------------------------------------------ 4. DATA TYPE FORMATTING
F("Format", "to_char (number)", "to_char(numeric, format) -> text", "Formats a number as text using a picture template.", "SELECT to_char(1234567.891, '999G999G999D99') AS grouped, to_char(0.42, '990D99%') AS percent, to_char(-125, 'S9999') AS signed;")
F("Format", "to_char (timestamp)", "to_char(timestamp, format) -> text", "Formats a date or timestamp as text.", "SELECT to_char(timestamp '2026-01-09 15:04:05', 'FMDay, DD FMMonth YYYY') AS pretty, to_char(timestamp '2026-01-09 15:04:05', 'HH12:MI:SS AM') AS clock;")
F("Format", "to_char (interval)", "to_char(interval, format) -> text", "Formats an interval as text.", "SELECT to_char(interval '15h 2m 12s', 'HH24:MI:SS') AS duration;")
F("Format", "to_date", "to_date(text, format) -> date", "Parses text into a date using a picture template.", "SELECT to_date('09 Jan 2026', 'DD Mon YYYY') AS parsed;")
F("Format", "to_number", "to_number(text, format) -> numeric", "Parses text into a numeric value.", "SELECT to_number('12,454.8-', '99G999D9S') AS parsed;")
F("Format", "to_timestamp (text)", "to_timestamp(text, format) -> timestamptz", "Parses text into a timestamp with time zone.", "SELECT to_timestamp('2026-01-09 15:04:05', 'YYYY-MM-DD HH24:MI:SS') AS parsed;")
F("Format", "to_timestamp (epoch)", "to_timestamp(double) -> timestamptz", "Converts a Unix epoch (seconds since 1970-01-01 UTC) into a timestamp.", "SELECT to_timestamp(1767970800) AS from_epoch;")

# --------------------------------------------------------- 5. DATE / TIME
F("DateTime", "age", "age(timestamp [, timestamp]) -> interval", "Symbolic difference between two timestamps, in years/months/days.", "SELECT age(timestamp '2026-01-09', timestamp '2019-03-15') AS since_hire;")
F("DateTime", "clock_timestamp", "clock_timestamp() -> timestamptz", "Current wall-clock time; advances during a statement.", "SELECT clock_timestamp() AS reading;", volatile=True)
F("DateTime", "current_date", "current_date -> date", "Current date in the session time zone.", "SELECT current_date AS today;", volatile=True)
F("DateTime", "current_time", "current_time -> timetz", "Current time of day with time zone.", "SELECT current_time AS now_time;", volatile=True)
F("DateTime", "current_timestamp", "current_timestamp -> timestamptz", "Start time of the current transaction.", "SELECT current_timestamp AS txn_start;", volatile=True)
F("DateTime", "date_bin", "date_bin(stride, source, origin) -> timestamp", "Buckets a timestamp into fixed-width intervals from an origin.", "SELECT date_bin('15 minutes', timestamp '2026-01-09 15:44:17', timestamp '2026-01-09 00:00:00') AS bucket;")
F("DateTime", "date_part", "date_part(field, source) -> double", "Extracts a subfield, the function form of EXTRACT.", "SELECT date_part('year', date '2019-03-15') AS yr, date_part('dow', date '2019-03-15') AS day_of_week, date_part('quarter', date '2019-03-15') AS q;")
F("DateTime", "date_trunc", "date_trunc(field, source) -> timestamp", "Truncates a timestamp to the given precision.", "SELECT date_trunc('month', timestamp '2026-01-09 15:04:05') AS month_start, date_trunc('hour', timestamp '2026-01-09 15:04:05') AS hour_start;")
F("DateTime", "extract", "EXTRACT(field FROM source) -> numeric", "Extracts a subfield from a date, time or interval.", "SELECT extract(year from date '2019-03-15') AS yr, extract(doy from date '2019-03-15') AS day_of_year, extract(epoch from interval '5 days') AS seconds;")
F("DateTime", "isfinite", "isfinite(date | timestamp | interval) -> boolean", "False for the special values infinity and -infinity.", "SELECT isfinite(date '2026-01-09') AS finite, isfinite(timestamp 'infinity') AS infinite;")
F("DateTime", "justify_days", "justify_days(interval) -> interval", "Normalises 30-day periods into months.", "SELECT justify_days(interval '95 days') AS justified;")
F("DateTime", "justify_hours", "justify_hours(interval) -> interval", "Normalises 24-hour periods into days.", "SELECT justify_hours(interval '50 hours') AS justified;")
F("DateTime", "justify_interval", "justify_interval(interval) -> interval", "Applies both justify_days and justify_hours, with sign adjustment.", "SELECT justify_interval(interval '1 mon -1 hour') AS justified;")
F("DateTime", "localtime", "localtime -> time", "Current time of day, without time zone.", "SELECT localtime AS clock;", volatile=True)
F("DateTime", "localtimestamp", "localtimestamp -> timestamp", "Current transaction timestamp, without time zone.", "SELECT localtimestamp AS stamp;", volatile=True)
F("DateTime", "make_date", "make_date(year, month, day) -> date", "Builds a date from year, month and day fields.", "SELECT make_date(2026, 1, 9) AS built;")
F("DateTime", "make_interval", "make_interval([years, months, weeks, days, hours, mins, secs]) -> interval", "Builds an interval from named parts.", "SELECT make_interval(days => 10, hours => 6) AS built;")
F("DateTime", "make_time", "make_time(hour, min, sec) -> time", "Builds a time value from hour, minute and second.", "SELECT make_time(8, 15, 23.5) AS built;")
F("DateTime", "make_timestamp", "make_timestamp(y, m, d, h, min, sec) -> timestamp", "Builds a timestamp without time zone from its parts.", "SELECT make_timestamp(2026, 1, 9, 15, 4, 5.2) AS built;")
F("DateTime", "make_timestamptz", "make_timestamptz(y, m, d, h, min, sec [, tz]) -> timestamptz", "Builds a timestamp with time zone, optionally in a named zone.", "SELECT make_timestamptz(2026, 1, 9, 15, 4, 5, 'UTC') AS built;")
F("DateTime", "now", "now() -> timestamptz", "Start time of the current transaction (same as current_timestamp).", "SELECT now() AS txn_start;", volatile=True)
F("DateTime", "statement_timestamp", "statement_timestamp() -> timestamptz", "Start time of the current statement.", "SELECT statement_timestamp() AS stmt_start;", volatile=True)
F("DateTime", "timeofday", "timeofday() -> text", "Current wall-clock time as a formatted text string.", "SELECT timeofday() AS wall_clock;", volatile=True)
F("DateTime", "transaction_timestamp", "transaction_timestamp() -> timestamptz", "Start time of the current transaction, explicit spelling.", "SELECT transaction_timestamp() = now() AS same_as_now;", volatile=True)
F("DateTime", "AT TIME ZONE", "timestamp AT TIME ZONE zone", "Converts a timestamp between time zones.", "SELECT timestamp '2026-01-09 15:04:05' AT TIME ZONE 'UTC' AS to_tz, timestamptz '2026-01-09 15:04:05+00' AT TIME ZONE 'Asia/Kolkata' AS in_ist;")
F("DateTime", "OVERLAPS", "(s1, e1) OVERLAPS (s2, e2) -> boolean", "True when two time periods overlap.", "SELECT (date '2019-01-01', date '2019-12-31') OVERLAPS (date '2019-06-01', date '2020-06-01') AS overlaps;")
F("DateTime", "interval arithmetic", "date + interval -> timestamp", "Dates, times and intervals combine with + and - operators.", "SELECT date '2026-01-09' + interval '45 days' AS later, date '2026-01-09' - date '2019-03-15' AS days_between, hire_date + interval '1 year' AS anniversary FROM employees WHERE id = 1;")
F("DateTime", "pg_sleep family", "pg_sleep(seconds) / pg_sleep_for / pg_sleep_until", "Suspends the session for the given duration.", "SELECT pg_sleep(0.05) IS NULL AS returns_void;")
F("DateTime", "date_add", "date_add(timestamptz, interval [, zone]) -> timestamptz", "Adds an interval, honouring daylight-saving rules in the given zone.", "SELECT date_add(timestamptz '2021-10-31 00:00:00+02', interval '1 day', 'Europe/Warsaw') AS dst_aware;")
F("DateTime", "date_subtract", "date_subtract(timestamptz, interval [, zone]) -> timestamptz", "Subtracts an interval, honouring daylight-saving rules in the given zone.", "SELECT date_subtract(timestamptz '2021-10-31 00:00:00+02', interval '2 hours', 'Europe/Warsaw') AS dst_aware;")

# --------------------------------------------------------- 6. CONDITIONAL
F("Conditional", "COALESCE", "COALESCE(value [, ...]) -> value", "Returns the first non-NULL argument.", "SELECT name, COALESCE(email, 'no email on file') AS contact FROM employees;")
F("Conditional", "NULLIF", "NULLIF(value1, value2) -> value", "Returns NULL when the two arguments are equal, otherwise the first.", "SELECT NULLIF(0, 0) AS becomes_null, NULLIF(salary, 55000) AS masked FROM employees WHERE id IN (1,5) ORDER BY id;")
F("Conditional", "GREATEST", "GREATEST(value [, ...]) -> value", "Largest of the arguments; NULLs are skipped.", "SELECT GREATEST(70000, 85000, 60000) AS top, GREATEST('a', 'z', NULL) AS ignores_null;")
F("Conditional", "LEAST", "LEAST(value [, ...]) -> value", "Smallest of the arguments; NULLs are skipped.", "SELECT LEAST(70000, 85000, 60000) AS bottom;")
F("Conditional", "CASE", "CASE WHEN cond THEN result ... ELSE result END", "Conditional expression, the SQL equivalent of if/else.", "SELECT name, salary, CASE WHEN salary >= 85000 THEN 'Senior' WHEN salary >= 65000 THEN 'Mid' ELSE 'Junior' END AS band FROM employees ORDER BY salary DESC;")
F("Conditional", "num_nulls", "num_nulls(VARIADIC any) -> integer", "Counts the NULL arguments.", "SELECT num_nulls(1, NULL, 3, NULL) AS nulls;")
F("Conditional", "num_nonnulls", "num_nonnulls(VARIADIC any) -> integer", "Counts the non-NULL arguments.", "SELECT num_nonnulls(1, NULL, 3, NULL) AS non_nulls;")
F("Conditional", "IS DISTINCT FROM", "a IS DISTINCT FROM b -> boolean", "NULL-safe inequality: treats NULL as a comparable value.", "SELECT NULL = NULL AS plain_equals, NULL IS NOT DISTINCT FROM NULL AS null_safe, 1 IS DISTINCT FROM NULL AS distinct_from_null;")

# --------------------------------------------------------------- 7. ARRAY
F("Array", "array_append", "array_append(anyarray, anyelement) -> anyarray", "Appends an element to the end of an array.", "SELECT array_append(ARRAY[1,2], 3) AS appended, ARRAY[1,2] || 3 AS operator_form;")
F("Array", "array_prepend", "array_prepend(anyelement, anyarray) -> anyarray", "Adds an element to the beginning of an array.", "SELECT array_prepend(0, ARRAY[1,2]) AS prepended;")
F("Array", "array_cat", "array_cat(anyarray, anyarray) -> anyarray", "Concatenates two arrays.", "SELECT array_cat(ARRAY[1,2], ARRAY[3,4]) AS joined, ARRAY[1,2] || ARRAY[3,4] AS operator_form;")
F("Array", "array_dims", "array_dims(anyarray) -> text", "Text representation of an array's dimensions.", "SELECT array_dims(ARRAY[[1,2,3],[4,5,6]]) AS dims;")
F("Array", "array_fill", "array_fill(anyelement, int[] [, int[]]) -> anyarray", "Builds an array filled with copies of a value.", "SELECT array_fill(7, ARRAY[4]) AS filled, array_fill(0, ARRAY[2,2]) AS matrix;")
F("Array", "array_length", "array_length(anyarray, dim) -> integer", "Length of the requested array dimension.", "SELECT array_length(ARRAY[1,2,3,4], 1) AS len, array_length(ARRAY[[1,2],[3,4]], 2) AS dim2;")
F("Array", "array_lower", "array_lower(anyarray, dim) -> integer", "Lower bound (starting subscript) of a dimension.", "SELECT array_lower(ARRAY[1,2,3], 1) AS lo, array_lower('[3:5]={1,2,3}'::int[], 1) AS custom_lo;")
F("Array", "array_upper", "array_upper(anyarray, dim) -> integer", "Upper bound (last subscript) of a dimension.", "SELECT array_upper(ARRAY[1,2,3], 1) AS hi;")
F("Array", "array_ndims", "array_ndims(anyarray) -> integer", "Number of dimensions of an array.", "SELECT array_ndims(ARRAY[1,2,3]) AS flat, array_ndims(ARRAY[[1,2],[3,4]]) AS nested;")
F("Array", "array_position", "array_position(anyarray, anyelement [, start]) -> integer", "Subscript of the first occurrence of a value.", "SELECT array_position(ARRAY['IT','Sales','HR'], 'Sales') AS pos;")
F("Array", "array_positions", "array_positions(anyarray, anyelement) -> integer[]", "Subscripts of every occurrence of a value.", "SELECT array_positions(ARRAY['A','B','A','C','A'], 'A') AS positions;")
F("Array", "array_remove", "array_remove(anyarray, anyelement) -> anyarray", "Removes every element equal to the given value.", "SELECT array_remove(ARRAY[1,2,3,2], 2) AS cleaned;")
F("Array", "array_replace", "array_replace(anyarray, from, to) -> anyarray", "Replaces every element equal to a value with another value.", "SELECT array_replace(ARRAY[1,2,5,4], 5, 3) AS fixed;")
F("Array", "array_shuffle", "array_shuffle(anyarray) -> anyarray", "Randomly shuffles the elements of an array (PostgreSQL 16+).", "SELECT array_shuffle(ARRAY[1,2,3,4,5]) AS shuffled;", volatile=True)
F("Array", "array_sample", "array_sample(anyarray, n) -> anyarray", "Returns n randomly chosen elements of an array (PostgreSQL 16+).", "SELECT array_sample(ARRAY[1,2,3,4,5], 3) AS sampled;", volatile=True)
F("Array", "array_to_string", "array_to_string(anyarray, delimiter [, null_string]) -> text", "Joins the array elements into a delimited string.", "SELECT array_to_string(ARRAY['IT','Sales','HR'], ', ') AS csv, array_to_string(ARRAY[1,NULL,3], '-', '?') AS with_nulls;")
F("Array", "cardinality", "cardinality(anyarray) -> integer", "Total number of elements across all dimensions.", "SELECT cardinality(ARRAY[[1,2],[3,4]]) AS total, array_length(ARRAY[[1,2],[3,4]], 1) AS first_dim;")
F("Array", "trim_array", "trim_array(anyarray, n) -> anyarray", "Removes the last n elements of an array.", "SELECT trim_array(ARRAY[1,2,3,4,5], 2) AS trimmed;")
F("Array", "unnest", "unnest(anyarray) -> setof anyelement", "Expands an array into one row per element.", "SELECT unnest(ARRAY['IT','Sales','HR']) AS dept;")
F("Array", "array subscripting", "arr[n], arr[lo:hi]", "Arrays are 1-based and support slicing.", "SELECT (ARRAY['a','b','c','d'])[2] AS element, (ARRAY['a','b','c','d'])[2:3] AS slice;")
F("Array", "ANY / ALL", "value = ANY(array) -> boolean", "Compares a value against every element of an array.", "SELECT name FROM employees WHERE dept_id = ANY(ARRAY[101,103]) ORDER BY id;")
F("Array", "array containment", "@>, <@, &&", "Operators for contains, is contained by and overlaps.", "SELECT ARRAY[1,2,3] @> ARRAY[2] AS contains, ARRAY[2] <@ ARRAY[1,2,3] AS contained, ARRAY[1,2] && ARRAY[2,3] AS overlaps;")

# ------------------------------------------------ 8. RANGE & MULTIRANGE
F("Range", "range constructors", "int4range(lo, hi, bounds), tsrange, daterange", "Ranges are built from a lower bound, an upper bound and a bounds flag.", "SELECT int4range(1, 10) AS half_open, int4range(1, 10, '[]') AS inclusive, daterange('2026-01-01', '2026-02-01') AS dates;")
F("Range", "lower (range)", "lower(anyrange) -> anyelement", "Lower bound of a range; NULL when unbounded.", "SELECT lower(int4range(3, 7)) AS lo, lower(numrange(NULL, 7)) AS unbounded;")
F("Range", "upper (range)", "upper(anyrange) -> anyelement", "Upper bound of a range; NULL when unbounded.", "SELECT upper(int4range(3, 7)) AS hi;")
F("Range", "isempty", "isempty(anyrange) -> boolean", "True when the range is empty.", "SELECT isempty(numrange(1, 5)) AS not_empty, isempty(numrange(4, 4)) AS empty;")
F("Range", "lower_inc", "lower_inc(anyrange) -> boolean", "True when the lower bound is inclusive.", "SELECT lower_inc(numrange(1, 5)) AS default_inclusive, lower_inc(numrange(1, 5, '()')) AS exclusive;")
F("Range", "upper_inc", "upper_inc(anyrange) -> boolean", "True when the upper bound is inclusive.", "SELECT upper_inc(numrange(1, 5)) AS default_exclusive, upper_inc(numrange(1, 5, '[]')) AS inclusive;")
F("Range", "lower_inf", "lower_inf(anyrange) -> boolean", "True when the range has no lower bound.", "SELECT lower_inf('(,5)'::numrange) AS unbounded_below;")
F("Range", "upper_inf", "upper_inf(anyrange) -> boolean", "True when the range has no upper bound.", "SELECT upper_inf('(5,)'::numrange) AS unbounded_above;")
F("Range", "range_merge", "range_merge(anyrange, anyrange) -> anyrange", "Smallest range containing both inputs.", "SELECT range_merge(int4range(1, 5), int4range(10, 15)) AS merged;")
F("Range", "range operators", "@>, &&, <<, >>, -|-, *, +, -", "Containment, overlap, adjacency, intersection, union and difference.", "SELECT int4range(1,10) @> 5 AS contains, int4range(1,10) && int4range(5,20) AS overlaps, int4range(1,5) -|- int4range(5,10) AS adjacent, int4range(1,10) * int4range(5,20) AS intersection;")
F("Range", "multirange", "multirange(anyrange) / int4multirange(...)", "A multirange holds a set of non-overlapping ranges.", "SELECT int4multirange(int4range(1,5), int4range(10,15)) AS mr, multirange(int4range(1,5)) AS from_range;")
F("Range", "range_agg", "range_agg(anyrange) -> anymultirange", "Aggregates ranges into a multirange, merging where possible.", "SELECT range_agg(r) AS merged FROM (VALUES (int4range(1,5)), (int4range(4,9)), (int4range(20,25))) t(r);")
F("Range", "unnest (multirange)", "unnest(anymultirange) -> setof anyrange", "Expands a multirange into its component ranges.", "SELECT unnest('{[1,5),[10,15)}'::int4multirange) AS part;")

# --------------------------------------------------------- 9. JSON / JSONB
DOC = "'{\"name\":\"Alice\",\"dept\":\"IT\",\"skills\":[\"sql\",\"python\"],\"salary\":70000,\"manager\":null}'::jsonb"
F("JSON", "to_json", "to_json(anyelement) -> json", "Converts any SQL value to JSON.", "SELECT to_json('Fred said \"Hi.\"'::text) AS escaped, to_json(ARRAY[1,2,3]) AS arr;")
F("JSON", "to_jsonb", "to_jsonb(anyelement) -> jsonb", "Converts any SQL value to jsonb (parsed, deduplicated, key-sorted).", "SELECT to_jsonb(row(1, 'Alice', 70000)) AS row_doc;")
F("JSON", "array_to_json", "array_to_json(anyarray [, pretty]) -> json", "Converts an SQL array to a JSON array.", "SELECT array_to_json(ARRAY[[1,5],[99,100]]) AS nested;")
F("JSON", "row_to_json", "row_to_json(record) -> json", "Converts a row to a JSON object keyed by column name.", "SELECT row_to_json(e) AS doc FROM (SELECT id, name, salary FROM employees WHERE id = 1) e;")
F("JSON", "json_build_object", "json_build_object(VARIADIC any) -> json", "Builds a JSON object from alternating key/value arguments.", "SELECT json_build_object('name', name, 'salary', salary) AS doc FROM employees WHERE id = 2;")
F("JSON", "json_build_array", "json_build_array(VARIADIC any) -> json", "Builds a JSON array from a variadic argument list.", "SELECT json_build_array(1, 'two', true, NULL) AS mixed;")
F("JSON", "json_object", "json_object(text[]) -> json", "Builds a JSON object from a text array of keys and values.", "SELECT json_object('{dept, IT, head, Alice}') AS doc;")
F("JSON", "json_array_length", "json_array_length(json) -> integer", "Number of elements in a JSON array.", "SELECT jsonb_array_length('[1,2,3,4]'::jsonb) AS len;")
F("JSON", "json_each", "json_each(json) -> setof (key text, value json)", "Expands the top-level object into key/value rows.", "SELECT * FROM jsonb_each(" + DOC + ");")
F("JSON", "json_each_text", "json_each_text(json) -> setof (key text, value text)", "Like json_each(), but values come back as text.", "SELECT * FROM jsonb_each_text(" + DOC + ");")
F("JSON", "json_object_keys", "json_object_keys(json) -> setof text", "Lists the keys of the top-level JSON object.", "SELECT jsonb_object_keys(" + DOC + ") AS key;")
F("JSON", "json_array_elements", "json_array_elements(json) -> setof json", "Expands a JSON array into one row per element.", "SELECT jsonb_array_elements('[\"sql\",\"python\",\"go\"]'::jsonb) AS skill;")
F("JSON", "json_array_elements_text", "json_array_elements_text(json) -> setof text", "Expands a JSON array into text rows.", "SELECT jsonb_array_elements_text('[\"sql\",\"python\"]'::jsonb) AS skill;")
F("JSON", "json_extract_path", "json_extract_path(json, VARIADIC path) -> json", "Extracts the JSON value at the given path.", "SELECT jsonb_extract_path(" + DOC + ", 'skills', '0') AS first_skill;")
F("JSON", "json_extract_path_text", "json_extract_path_text(json, VARIADIC path) -> text", "Extracts the value at the given path as text.", "SELECT jsonb_extract_path_text(" + DOC + ", 'dept') AS dept;")
F("JSON", "json_typeof", "json_typeof(json) -> text", "Type of the outermost JSON value: object, array, string, number, boolean or null.", "SELECT jsonb_typeof(" + DOC + ") AS doc, jsonb_typeof('[1,2]'::jsonb) AS arr, jsonb_typeof('null'::jsonb) AS null_type;")
F("JSON", "json_strip_nulls", "json_strip_nulls(json) -> json", "Removes object fields whose value is JSON null.", "SELECT jsonb_strip_nulls(" + DOC + ") AS cleaned;")
F("JSON", "jsonb_set", "jsonb_set(target, path, new_value [, create_missing]) -> jsonb", "Replaces the value at a path inside a jsonb document.", "SELECT jsonb_set(" + DOC + ", '{salary}', '75000') AS raised;")
F("JSON", "jsonb_set_lax", "jsonb_set_lax(target, path, new_value, create_missing, null_handling) -> jsonb", "Like jsonb_set(), but with an explicit policy for a NULL new value.", "SELECT jsonb_set_lax(" + DOC + ", '{dept}', NULL, true, 'delete_key') AS dept_dropped;")
F("JSON", "jsonb_insert", "jsonb_insert(target, path, new_value [, insert_after]) -> jsonb", "Inserts a new value into an array or object without overwriting.", "SELECT jsonb_insert('[\"a\",\"c\"]'::jsonb, '{1}', '\"b\"') AS inserted;")
F("JSON", "jsonb_pretty", "jsonb_pretty(jsonb) -> text", "Renders jsonb as indented, human-readable text.", "SELECT jsonb_pretty('{\"b\":1,\"a\":{\"x\":[1,2]}}'::jsonb) AS pretty;")
F("JSON", "jsonb_path_query", "jsonb_path_query(target, jsonpath) -> setof jsonb", "Runs a SQL/JSON path expression, returning every match as a row.", "SELECT jsonb_path_query('{\"team\":[{\"pay\":70000},{\"pay\":92000}]}'::jsonb, '$.team[*].pay ? (@ > 80000)') AS high_pay;")
F("JSON", "jsonb_path_query_array", "jsonb_path_query_array(target, jsonpath) -> jsonb", "Runs a JSON path expression and wraps all matches in an array.", "SELECT jsonb_path_query_array('{\"team\":[{\"pay\":70000},{\"pay\":92000}]}'::jsonb, '$.team[*].pay') AS pays;")
F("JSON", "jsonb_path_query_first", "jsonb_path_query_first(target, jsonpath) -> jsonb", "Returns only the first match of a JSON path expression.", "SELECT jsonb_path_query_first('{\"team\":[{\"pay\":70000},{\"pay\":92000}]}'::jsonb, '$.team[*].pay') AS first_pay;")
F("JSON", "jsonb_path_exists", "jsonb_path_exists(target, jsonpath) -> boolean", "True when the JSON path returns at least one item.", "SELECT jsonb_path_exists(" + DOC + ", '$.skills[*] ? (@ == \"sql\")') AS knows_sql;")
F("JSON", "jsonb_path_match", "jsonb_path_match(target, jsonpath) -> boolean", "Evaluates a JSON path predicate to a single boolean.", "SELECT jsonb_path_match(" + DOC + ", '$.salary > 50000') AS well_paid;")
F("JSON", "json_populate_record", "json_populate_record(base, json) -> record", "Maps a JSON object onto a composite row type.", "SELECT * FROM json_populate_record(null::employees, '{\"id\":9,\"name\":\"Nina\",\"salary\":81000}');")
F("JSON", "json_to_record", "json_to_record(json) -> record", "Expands a JSON object into a row with an explicit column definition.", "SELECT * FROM json_to_record('{\"name\":\"Nina\",\"salary\":81000}') AS x(name text, salary numeric);")
F("JSON", "json_to_recordset", "json_to_recordset(json) -> setof record", "Expands a JSON array of objects into a table.", "SELECT * FROM json_to_recordset('[{\"n\":\"Alice\",\"s\":70000},{\"n\":\"Bob\",\"s\":85000}]') AS x(n text, s int);")
F("JSON", "jsonb operators", "->, ->>, #>, #>>, @>, ?, ||, -", "Field access, path access, containment, key existence, concatenation and delete.", "SELECT " + DOC + " -> 'skills' AS as_json, " + DOC + " ->> 'name' AS as_text, " + DOC + " #>> '{skills,1}' AS path_text, " + DOC + " ? 'dept' AS has_key, " + DOC + " - 'salary' AS key_removed;")
F("JSON", "jsonb @@ / @?", "jsonb @@ jsonpath, jsonb @? jsonpath", "Predicate-check and existence-check operators for JSON path expressions.", "SELECT " + DOC + " @@ '$.salary > 60000' AS predicate, " + DOC + " @? '$.skills[*] ? (@ == \"go\")' AS exists_go;")

# ---------------------------------------------------------------- 10. XML
F("XML", "xmlcomment", "xmlcomment(text) -> xml", "Creates an XML comment node.", "SELECT xmlcomment('generated by PGMaster') AS node;")
F("XML", "xmlconcat", "xmlconcat(xml [, ...]) -> xml", "Concatenates XML values into a fragment.", "SELECT xmlconcat('<a>1</a>'::xml, '<b>2</b>'::xml) AS fragment;")
F("XML", "xmlelement", "xmlelement(NAME n [, XMLATTRIBUTES(...)] [, content]) -> xml", "Builds an XML element with optional attributes and content.", "SELECT xmlelement(name employee, xmlattributes(id AS \"id\"), name) AS node FROM employees WHERE id = 1;")
F("XML", "xmlforest", "xmlforest(content AS name [, ...]) -> xml", "Builds a forest (sequence) of XML elements from columns.", "SELECT xmlforest(name, salary) AS forest FROM employees WHERE id = 2;")
F("XML", "xmlpi", "xmlpi(NAME target [, content]) -> xml", "Creates an XML processing instruction.", "SELECT xmlpi(name php, 'echo \"hi\";') AS pi;")
F("XML", "xmlroot", "xmlroot(xml, VERSION v [, STANDALONE s]) -> xml", "Adds or replaces the XML declaration of a document.", "SELECT xmlroot('<r>ok</r>'::xml, version '1.0', standalone yes) AS doc;")
F("XML", "xmlagg", "xmlagg(xml) -> xml", "Aggregate that concatenates XML values across rows.", "SELECT xmlagg(xmlelement(name emp, name)) AS doc FROM employees;")
F("XML", "xpath", "xpath(xpath, xml [, nsarray]) -> xml[]", "Evaluates an XPath expression, returning an array of nodes.", "SELECT xpath('/team/member/text()', '<team><member>Alice</member><member>Bob</member></team>'::xml) AS names;")
F("XML", "xpath_exists", "xpath_exists(xpath, xml) -> boolean", "True when the XPath expression selects at least one node.", "SELECT xpath_exists('/team/member', '<team><member>Alice</member></team>'::xml) AS found;")
F("XML", "xmlexists", "XMLEXISTS(xpath PASSING BY REF xml) -> boolean", "SQL-standard existence test for an XPath expression.", "SELECT xmlexists('//member' PASSING BY REF xml '<team><member>Alice</member></team>') AS found;")
F("XML", "xml_is_well_formed", "xml_is_well_formed(text) -> boolean", "Checks whether a text value parses as well-formed XML.", "SELECT xml_is_well_formed('<a>ok</a>') AS good, xml_is_well_formed('<a>broken') AS bad;")
F("XML", "xmltable", "XMLTABLE(rowexpr PASSING doc COLUMNS ...)", "Turns an XML document into a relational table.", "SELECT * FROM xmltable('/team/member' PASSING xml '<team><member id=\"1\">Alice</member><member id=\"2\">Bob</member></team>' COLUMNS id int PATH '@id', name text PATH '.');")
F("XML", "query_to_xml", "query_to_xml(query, nulls, tableforest, targetns) -> xml", "Runs a query and returns its result set as XML.", "SELECT query_to_xml('SELECT name FROM employees WHERE id <= 2', false, true, '') AS doc;")
F("XML", "table_to_xml", "table_to_xml(tbl, nulls, tableforest, targetns) -> xml", "Exports an entire table as an XML document.", "SELECT left(table_to_xml('departments', false, true, '')::text, 120) || '...' AS head;")
F("XML", "xmlserialize", "XMLSERIALIZE(DOCUMENT|CONTENT xml AS type) -> text", "Converts an XML value back to text or varchar.", "SELECT xmlserialize(content '<a>ok</a>'::xml AS text) AS serialized;")

# -------------------------------------------------- 11. FULL TEXT SEARCH
F("TextSearch", "to_tsvector", "to_tsvector([config,] document) -> tsvector", "Parses a document into normalised lexemes with positions.", "SELECT to_tsvector('english', 'The quick brown foxes jumped over lazy dogs') AS lexemes;")
F("TextSearch", "to_tsquery", "to_tsquery([config,] querytext) -> tsquery", "Parses a search query with explicit &, |, ! and <-> operators.", "SELECT to_tsquery('english', 'fox & !dog') AS query;")
F("TextSearch", "plainto_tsquery", "plainto_tsquery([config,] text) -> tsquery", "Converts plain text into a query, ANDing every word.", "SELECT plainto_tsquery('english', 'quick brown foxes') AS query;")
F("TextSearch", "phraseto_tsquery", "phraseto_tsquery([config,] text) -> tsquery", "Converts plain text into a phrase query using the distance operator.", "SELECT phraseto_tsquery('english', 'quick brown foxes') AS query;")
F("TextSearch", "websearch_to_tsquery", "websearch_to_tsquery([config,] text) -> tsquery", "Parses web-search syntax: quoted phrases, OR and leading minus.", "SELECT websearch_to_tsquery('english', '\"quick brown\" or fox -dog') AS query;")
F("TextSearch", "@@ (match)", "tsvector @@ tsquery -> boolean", "The text search match operator.", "SELECT to_tsvector('english', 'The quick brown fox') @@ to_tsquery('english', 'quick & fox') AS matches;")
F("TextSearch", "ts_rank", "ts_rank([weights,] tsvector, tsquery) -> real", "Ranks a document against a query by lexeme frequency.", "SELECT ts_rank(to_tsvector('english', 'a fox is a fox is a fox'), to_tsquery('english', 'fox')) AS rank;")
F("TextSearch", "ts_rank_cd", "ts_rank_cd([weights,] tsvector, tsquery) -> real", "Cover density ranking, which rewards close matches.", "SELECT ts_rank_cd(to_tsvector('english', 'the quick brown fox'), to_tsquery('english', 'quick <-> brown')) AS rank;")
F("TextSearch", "ts_headline", "ts_headline([config,] document, query [, options]) -> text", "Highlights the matching terms inside the original document.", "SELECT ts_headline('english', 'The quick brown fox jumps over the lazy dog', to_tsquery('english', 'fox & dog')) AS snippet;")
F("TextSearch", "setweight", "setweight(tsvector, label) -> tsvector", "Labels every lexeme with a weight A, B, C or D for ranking.", "SELECT setweight(to_tsvector('english', 'important title'), 'A') AS weighted;")
F("TextSearch", "strip", "strip(tsvector) -> tsvector", "Removes positions and weights from a tsvector.", "SELECT strip(to_tsvector('english', 'the quick brown fox')) AS stripped;")
F("TextSearch", "length (tsvector)", "length(tsvector) -> integer", "Number of distinct lexemes in a tsvector.", "SELECT length(to_tsvector('english', 'the quick brown fox jumps')) AS lexemes;")
F("TextSearch", "numnode", "numnode(tsquery) -> integer", "Number of lexemes plus operators in a tsquery.", "SELECT numnode(to_tsquery('english', 'fox & dog | cat')) AS nodes;")
F("TextSearch", "querytree", "querytree(tsquery) -> text", "The indexable portion of a tsquery.", "SELECT querytree(to_tsquery('english', 'fox & !dog')) AS indexable;")
F("TextSearch", "ts_delete", "ts_delete(tsvector, lexeme) -> tsvector", "Removes the given lexemes from a tsvector.", "SELECT ts_delete(to_tsvector('english', 'quick brown fox'), 'brown') AS trimmed;")
F("TextSearch", "ts_filter", "ts_filter(tsvector, weights) -> tsvector", "Keeps only the lexemes with the listed weights.", "SELECT ts_filter(setweight(to_tsvector('english', 'title body'), 'A'), '{a}') AS only_a;")
F("TextSearch", "tsvector_to_array", "tsvector_to_array(tsvector) -> text[]", "Converts a tsvector into an array of lexemes.", "SELECT tsvector_to_array(to_tsvector('english', 'quick brown fox')) AS lexemes;")
F("TextSearch", "array_to_tsvector", "array_to_tsvector(text[]) -> tsvector", "Builds a tsvector from an array of lexemes.", "SELECT array_to_tsvector(ARRAY['brown','fox','quick']) AS vec;")
F("TextSearch", "ts_lexize", "ts_lexize(dict, token) -> text[]", "Runs a single token through a text search dictionary.", "SELECT ts_lexize('english_stem', 'running') AS stemmed, ts_lexize('english_stem', 'the') AS stop_word;")
F("TextSearch", "ts_debug", "ts_debug([config,] document) -> setof record", "Shows how the parser and dictionaries treat each token.", "SELECT alias, token, lexemes FROM ts_debug('english', 'The foxes ran') WHERE token <> ' ';")
F("TextSearch", "ts_stat", "ts_stat(sqlquery) -> setof record", "Word statistics over a set of tsvector values.", "SELECT * FROM ts_stat('SELECT to_tsvector(''english'', name) FROM employees') ORDER BY word LIMIT 3;")
F("TextSearch", "get_current_ts_config", "get_current_ts_config() -> regconfig", "The text search configuration used when none is named.", "SELECT get_current_ts_config() AS default_config;")

# ----------------------------------------------------------- 12. AGGREGATE
F("Aggregate", "count", "count(*) / count(expr) -> bigint", "Counts rows, or non-NULL values of an expression.", "SELECT count(*) AS all_rows, count(dept_id) AS with_dept, count(DISTINCT dept_id) AS distinct_depts FROM employees;")
F("Aggregate", "sum", "sum(expr) -> numeric", "Sum of the non-NULL input values.", "SELECT sum(salary) AS payroll FROM employees;")
F("Aggregate", "avg", "avg(expr) -> numeric", "Arithmetic mean of the non-NULL input values.", "SELECT round(avg(salary), 2) AS mean_salary FROM employees;")
F("Aggregate", "max", "max(expr) -> same type", "Largest value across the input rows.", "SELECT max(salary) AS top_pay, max(name) AS last_alphabetically FROM employees;")
F("Aggregate", "min", "min(expr) -> same type", "Smallest value across the input rows.", "SELECT min(salary) AS lowest_pay, min(hire_date) AS first_hire FROM employees;")
F("Aggregate", "array_agg", "array_agg(expr [ORDER BY ...]) -> anyarray", "Collects the input values into an array.", "SELECT dept_id, array_agg(name ORDER BY name) AS team FROM employees WHERE dept_id IS NOT NULL GROUP BY dept_id ORDER BY dept_id;")
F("Aggregate", "string_agg", "string_agg(expr, delimiter [ORDER BY ...]) -> text", "Concatenates the input values with a delimiter.", "SELECT string_agg(name, ', ' ORDER BY salary DESC) AS by_pay FROM employees;")
F("Aggregate", "json_agg", "json_agg(expr) -> json", "Collects the input values into a JSON array.", "SELECT jsonb_agg(jsonb_build_object('name', name, 'pay', salary)) AS team FROM employees WHERE dept_id = 101;")
F("Aggregate", "json_object_agg", "json_object_agg(key, value) -> json", "Builds a JSON object from key/value pairs across rows.", "SELECT jsonb_object_agg(name, salary) AS pay_map FROM employees WHERE dept_id = 102;")
F("Aggregate", "bool_and", "bool_and(expr) -> boolean", "True when every input value is true.", "SELECT bool_and(salary > 50000) AS all_above_50k FROM employees;")
F("Aggregate", "bool_or", "bool_or(expr) -> boolean", "True when at least one input value is true.", "SELECT bool_or(salary > 90000) AS anyone_above_90k FROM employees;")
F("Aggregate", "every", "every(expr) -> boolean", "SQL-standard spelling of bool_and().", "SELECT every(hire_date < date '2026-01-01') AS all_hired FROM employees;")
F("Aggregate", "bit_and", "bit_and(expr) -> integer", "Bitwise AND across all input values.", "SELECT bit_and(dept_id) AS anded FROM employees;")
F("Aggregate", "bit_or", "bit_or(expr) -> integer", "Bitwise OR across all input values.", "SELECT bit_or(dept_id) AS ored FROM employees;")
F("Aggregate", "bit_xor", "bit_xor(expr) -> integer", "Bitwise XOR across all input values, useful as a checksum.", "SELECT bit_xor(id) AS checksum FROM employees;")
F("Aggregate", "stddev", "stddev(expr) -> numeric", "Sample standard deviation; alias for stddev_samp().", "SELECT round(stddev(salary), 2) AS sample_stddev FROM employees;")
F("Aggregate", "stddev_pop", "stddev_pop(expr) -> numeric", "Population standard deviation.", "SELECT round(stddev_pop(salary), 2) AS pop_stddev FROM employees;")
F("Aggregate", "stddev_samp", "stddev_samp(expr) -> numeric", "Sample standard deviation, explicit spelling.", "SELECT round(stddev_samp(salary), 2) AS sample_stddev FROM employees;")
F("Aggregate", "variance", "variance(expr) -> numeric", "Sample variance; alias for var_samp().", "SELECT round(variance(salary), 2) AS sample_variance FROM employees;")
F("Aggregate", "var_pop", "var_pop(expr) -> numeric", "Population variance.", "SELECT round(var_pop(salary), 2) AS pop_variance FROM employees;")
F("Aggregate", "var_samp", "var_samp(expr) -> numeric", "Sample variance, explicit spelling.", "SELECT round(var_samp(salary), 2) AS sample_variance FROM employees;")
F("Aggregate", "corr", "corr(Y, X) -> double", "Correlation coefficient between two columns.", "SELECT round(corr(salary, id)::numeric, 4) AS correlation FROM employees;")
F("Aggregate", "covar_pop", "covar_pop(Y, X) -> double", "Population covariance.", "SELECT round(covar_pop(salary, id)::numeric, 2) AS covariance FROM employees;")
F("Aggregate", "covar_samp", "covar_samp(Y, X) -> double", "Sample covariance.", "SELECT round(covar_samp(salary, id)::numeric, 2) AS covariance FROM employees;")
F("Aggregate", "regr_slope", "regr_slope(Y, X) -> double", "Slope of the least-squares fit line.", "SELECT round(regr_slope(salary, id)::numeric, 3) AS slope FROM employees;")
F("Aggregate", "regr_intercept", "regr_intercept(Y, X) -> double", "Y intercept of the least-squares fit line.", "SELECT round(regr_intercept(salary, id)::numeric, 2) AS intercept FROM employees;")
F("Aggregate", "regr_r2", "regr_r2(Y, X) -> double", "Square of the correlation coefficient.", "SELECT round(regr_r2(salary, id)::numeric, 4) AS r_squared FROM employees;")
F("Aggregate", "regr_count", "regr_count(Y, X) -> bigint", "Number of rows where both expressions are non-NULL.", "SELECT regr_count(salary, dept_id) AS pairs FROM employees;")
F("Aggregate", "regr_avgx / regr_avgy", "regr_avgx(Y, X), regr_avgy(Y, X) -> double", "Averages of the independent and dependent variables.", "SELECT regr_avgx(salary, id) AS avg_x, regr_avgy(salary, id) AS avg_y FROM employees;")
F("Aggregate", "regr_sxx / sxy / syy", "regr_sxx, regr_sxy, regr_syy -> double", "Sums of squares and products used by regression analysis.", "SELECT regr_sxx(salary, id) AS sxx, round(regr_sxy(salary, id)::numeric, 1) AS sxy, round(regr_syy(salary, id)::numeric, 1) AS syy FROM employees;")
F("Aggregate", "mode", "mode() WITHIN GROUP (ORDER BY expr)", "Ordered-set aggregate returning the most frequent input value.", "SELECT mode() WITHIN GROUP (ORDER BY dept_id) AS most_common_dept FROM employees;")
F("Aggregate", "percentile_cont", "percentile_cont(fraction) WITHIN GROUP (ORDER BY expr)", "Continuous percentile: interpolates between input values.", "SELECT percentile_cont(0.5) WITHIN GROUP (ORDER BY salary) AS median FROM employees;")
F("Aggregate", "percentile_disc", "percentile_disc(fraction) WITHIN GROUP (ORDER BY expr)", "Discrete percentile: returns an actual input value.", "SELECT percentile_disc(0.5) WITHIN GROUP (ORDER BY salary) AS median FROM employees;")
F("Aggregate", "rank (hypothetical)", "rank(args) WITHIN GROUP (ORDER BY ...)", "Rank a hypothetical row would have among the group.", "SELECT rank(80000) WITHIN GROUP (ORDER BY salary DESC) AS would_rank FROM employees;")
F("Aggregate", "dense_rank (hypothetical)", "dense_rank(args) WITHIN GROUP (ORDER BY ...)", "Dense rank of a hypothetical row within the group.", "SELECT dense_rank(80000) WITHIN GROUP (ORDER BY salary DESC) AS would_rank FROM employees;")
F("Aggregate", "percent_rank (hypothetical)", "percent_rank(args) WITHIN GROUP (ORDER BY ...)", "Relative rank of a hypothetical row, from 0 to 1.", "SELECT round(percent_rank(80000) WITHIN GROUP (ORDER BY salary DESC)::numeric, 4) AS pct FROM employees;")
F("Aggregate", "cume_dist (hypothetical)", "cume_dist(args) WITHIN GROUP (ORDER BY ...)", "Cumulative distribution of a hypothetical row.", "SELECT round(cume_dist(80000) WITHIN GROUP (ORDER BY salary DESC)::numeric, 4) AS cume FROM employees;")
F("Aggregate", "grouping", "GROUPING(expr) -> integer", "Marks which grouping columns a super-aggregate row summarises.", "SELECT dept_id, grouping(dept_id) AS is_total, sum(salary) AS pay FROM employees GROUP BY ROLLUP(dept_id) ORDER BY is_total, dept_id;")
F("Aggregate", "FILTER clause", "agg(expr) FILTER (WHERE cond)", "Restricts the rows fed to a single aggregate.", "SELECT count(*) AS everyone, count(*) FILTER (WHERE salary > 70000) AS well_paid FROM employees;")
F("Aggregate", "GROUPING SETS", "GROUP BY GROUPING SETS / ROLLUP / CUBE", "Computes several grouping levels in one pass.", "SELECT dept_id, count(*) AS headcount FROM employees GROUP BY GROUPING SETS ((dept_id), ()) ORDER BY dept_id NULLS LAST;")

# -------------------------------------------------------------- 13. WINDOW
F("Window", "row_number", "row_number() OVER (...) -> bigint", "Sequential number of the row within its window partition.", "SELECT name, salary, row_number() OVER (ORDER BY salary DESC) AS rn FROM employees;")
F("Window", "rank", "rank() OVER (...) -> bigint", "Rank with gaps after ties.", "SELECT name, dept_id, rank() OVER (PARTITION BY dept_id ORDER BY salary DESC) AS rnk FROM employees ORDER BY dept_id NULLS LAST, rnk;")
F("Window", "dense_rank", "dense_rank() OVER (...) -> bigint", "Rank without gaps after ties.", "SELECT name, salary, dense_rank() OVER (ORDER BY salary DESC) AS drnk FROM employees;")
F("Window", "percent_rank", "percent_rank() OVER (...) -> double", "Relative rank of the row, from 0 to 1.", "SELECT name, round(percent_rank() OVER (ORDER BY salary)::numeric, 3) AS pct FROM employees;")
F("Window", "cume_dist", "cume_dist() OVER (...) -> double", "Cumulative distribution: fraction of rows at or below this one.", "SELECT name, round(cume_dist() OVER (ORDER BY salary)::numeric, 3) AS cume FROM employees;")
F("Window", "ntile", "ntile(buckets) OVER (...) -> integer", "Splits the partition into the requested number of buckets.", "SELECT name, salary, ntile(2) OVER (ORDER BY salary DESC) AS half FROM employees;")
F("Window", "lag", "lag(value [, offset [, default]]) OVER (...)", "Value from a previous row in the partition.", "SELECT name, salary, lag(salary) OVER (ORDER BY salary) AS previous, salary - lag(salary, 1, 0::numeric) OVER (ORDER BY salary) AS gap FROM employees;")
F("Window", "lead", "lead(value [, offset [, default]]) OVER (...)", "Value from a following row in the partition.", "SELECT name, salary, lead(salary) OVER (ORDER BY salary) AS next_up FROM employees;")
F("Window", "first_value", "first_value(value) OVER (...)", "First value in the window frame.", "SELECT name, dept_id, first_value(name) OVER (PARTITION BY dept_id ORDER BY salary DESC) AS top_earner FROM employees ORDER BY dept_id NULLS LAST;")
F("Window", "last_value", "last_value(value) OVER (...)", "Last value in the frame; usually needs an explicit frame clause.", "SELECT name, last_value(name) OVER (ORDER BY salary ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS highest_paid FROM employees;")
F("Window", "nth_value", "nth_value(value, n) OVER (...)", "Nth value in the window frame.", "SELECT name, nth_value(name, 2) OVER (ORDER BY salary DESC ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS runner_up FROM employees;")
F("Window", "aggregates OVER ()", "sum(expr) OVER (PARTITION BY ... ORDER BY ...)", "Any aggregate becomes a window function with an OVER clause.", "SELECT name, dept_id, salary, sum(salary) OVER (PARTITION BY dept_id) AS dept_total, round(avg(salary) OVER (), 2) AS company_avg FROM employees ORDER BY dept_id NULLS LAST;")
F("Window", "frame clause", "ROWS / RANGE / GROUPS BETWEEN ...", "Defines which rows around the current row the window covers.", "SELECT name, salary, sum(salary) OVER (ORDER BY salary ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS running_total FROM employees;")
F("Window", "WINDOW clause", "WINDOW w AS (PARTITION BY ... ORDER BY ...)", "Names a window definition so several functions can share it.", "SELECT name, rank() OVER w AS rnk, salary - min(salary) OVER w AS above_min FROM employees WINDOW w AS (ORDER BY salary DESC) ORDER BY rnk;")

# ------------------------------------------------------- 14. SET RETURNING
F("SetReturning", "generate_series (numeric)", "generate_series(start, stop [, step]) -> setof", "Generates a series of numeric values.", "SELECT generate_series(1, 10, 3) AS n;")
F("SetReturning", "generate_series (timestamp)", "generate_series(start, stop, step interval) -> setof timestamp", "Generates a series of timestamps, ideal for gap-free calendars.", "SELECT generate_series(date '2026-01-01', date '2026-01-15', interval '5 days')::date AS day;")
F("SetReturning", "generate_subscripts", "generate_subscripts(anyarray, dim) -> setof integer", "Generates the valid subscripts of an array dimension.", "SELECT i, (ARRAY['IT','Sales','HR'])[i] AS dept FROM generate_subscripts(ARRAY['IT','Sales','HR'], 1) AS i;")
F("SetReturning", "WITH ORDINALITY", "func(...) WITH ORDINALITY", "Adds a row-number column to any set-returning function.", "SELECT * FROM unnest(ARRAY['IT','Sales','HR']) WITH ORDINALITY AS t(dept, pos);")
F("SetReturning", "ROWS FROM", "ROWS FROM (func1(...), func2(...))", "Runs several set-returning functions side by side.", "SELECT * FROM ROWS FROM (generate_series(1,3), unnest(ARRAY['a','b'])) AS t(n, letter);")
F("SetReturning", "LATERAL", "FROM tbl, LATERAL func(tbl.col)", "Lets a set-returning function reference columns of preceding FROM items.", "SELECT e.name, s.skill FROM (SELECT name, ARRAY['sql','python'] AS skills FROM employees WHERE id <= 2) e, LATERAL unnest(e.skills) AS s(skill);")
F("SetReturning", "VALUES list", "VALUES (...), (...)", "An inline set of rows usable anywhere a table is.", "SELECT * FROM (VALUES (101, 'IT'), (102, 'Sales')) AS d(dept_id, dept_name);")

# ------------------------------------------------------------ 15. SEQUENCE
F("Sequence", "nextval", "nextval(regclass) -> bigint", "Advances the sequence and returns its new value.", "SELECT nextval('emp_seq') AS first_call, nextval('emp_seq') AS second_call;")
F("Sequence", "currval", "currval(regclass) -> bigint", "Value most recently returned by nextval() in this session.", "SELECT nextval('emp_seq') AS advanced, currval('emp_seq') AS current;")
F("Sequence", "lastval", "lastval() -> bigint", "Value most recently returned by nextval() for any sequence in the session.", "SELECT nextval('emp_seq') AS advanced, lastval() AS last;")
F("Sequence", "setval", "setval(regclass, value [, is_called]) -> bigint", "Resets a sequence's counter.", "SELECT setval('emp_seq', 500) AS set_to, nextval('emp_seq') AS next_value;")
F("Sequence", "pg_get_serial_sequence", "pg_get_serial_sequence(table, column) -> text", "Name of the sequence backing an identity or serial column.", "SELECT pg_get_serial_sequence('audit_log', 'id') AS seq;", setup="CREATE TABLE audit_log (id serial PRIMARY KEY, msg text);")
F("Sequence", "GENERATED AS IDENTITY", "column int GENERATED ALWAYS AS IDENTITY", "The SQL-standard replacement for serial columns.", "INSERT INTO ticket (subject) VALUES ('printer jam'), ('vpn down') RETURNING id, subject;", setup="CREATE TABLE ticket (id int GENERATED ALWAYS AS IDENTITY, subject text);")

# ------------------------------------------------------ 16. NETWORK ADDRESS
F("Network", "abbrev", "abbrev(inet | cidr) -> text", "Abbreviated display form of a network address.", "SELECT abbrev(inet '10.1.0.0/16') AS inet_form, abbrev(cidr '10.1.0.0/16') AS cidr_form;")
F("Network", "broadcast", "broadcast(inet) -> inet", "Broadcast address of the network.", "SELECT broadcast(inet '192.168.1.5/24') AS broadcast;")
F("Network", "family", "family(inet) -> integer", "Address family: 4 for IPv4, 6 for IPv6.", "SELECT family(inet '192.168.1.5') AS v4, family(inet '::1') AS v6;")
F("Network", "host", "host(inet) -> text", "Host address as text, dropping the netmask.", "SELECT host(inet '192.168.1.5/24') AS host;")
F("Network", "hostmask", "hostmask(inet) -> inet", "Host mask for the network.", "SELECT hostmask(inet '192.168.23.20/30') AS hostmask;")
F("Network", "masklen", "masklen(inet) -> integer", "Netmask length in bits.", "SELECT masklen(inet '192.168.1.5/24') AS bits;")
F("Network", "netmask", "netmask(inet) -> inet", "Netmask for the network.", "SELECT netmask(inet '192.168.1.5/24') AS netmask;")
F("Network", "network", "network(inet) -> cidr", "Network part of the address.", "SELECT network(inet '192.168.1.5/24') AS network;")
F("Network", "set_masklen", "set_masklen(inet, int) -> inet", "Sets the netmask length of an address.", "SELECT set_masklen(inet '192.168.1.5/24', 16) AS widened;")
F("Network", "inet_merge", "inet_merge(inet, inet) -> cidr", "Smallest network containing both addresses.", "SELECT inet_merge(inet '192.168.1.5/24', inet '192.168.2.5/24') AS merged;")
F("Network", "inet_same_family", "inet_same_family(inet, inet) -> boolean", "True when both addresses are of the same family.", "SELECT inet_same_family(inet '192.168.1.5', inet '10.0.0.1') AS both_v4, inet_same_family(inet '192.168.1.5', inet '::1') AS mixed;")
F("Network", "macaddr8_set7bit", "macaddr8_set7bit(macaddr8) -> macaddr8", "Sets the 7th bit of a MAC address, forming a modified EUI-64.", "SELECT macaddr8_set7bit(macaddr8 '00:34:56:ab:cd:ef') AS eui64;")
F("Network", "trunc (macaddr)", "trunc(macaddr) -> macaddr", "Zeroes the last three bytes, leaving the manufacturer prefix.", "SELECT trunc(macaddr '12:34:56:78:90:ab') AS vendor_prefix;")
F("Network", "network operators", "<<, <<=, >>, >>=, &&, ~, &, |", "Containment, overlap and bitwise operators for inet values.", "SELECT inet '192.168.1.5' << inet '192.168.1.0/24' AS contained, inet '192.168.1.0/24' >>= inet '192.168.1.5' AS contains, inet '192.168.1.0/24' && inet '192.168.1.128/25' AS overlaps;")

# --------------------------------------------------------- 17. GEOMETRIC
F("Geometric", "point", "point(x, y) -> point", "Constructs a point from two coordinates.", "SELECT point(3, 4) AS p, point '(1,2)' AS literal;")
F("Geometric", "box", "box(point, point) -> box", "Constructs a rectangular box from two opposite corners.", "SELECT box(point '(0,0)', point '(2,3)') AS b;")
F("Geometric", "circle", "circle(point, radius) -> circle", "Constructs a circle from a centre and a radius.", "SELECT circle(point '(0,0)', 5) AS c;")
F("Geometric", "line / lseg", "line(p1, p2), lseg(p1, p2)", "Constructs an infinite line or a finite line segment.", "SELECT lseg(point '(0,0)', point '(3,4)') AS segment, line(point '(0,0)', point '(1,1)') AS infinite_line;")
F("Geometric", "path / polygon", "path(polygon), polygon(box)", "Converts between paths, polygons and boxes.", "SELECT polygon(box '((0,0),(2,2))') AS poly, path(polygon '((0,0),(1,1),(2,0))') AS closed_path;")
F("Geometric", "area", "area(box | circle | path) -> double", "Area of a geometric shape.", "SELECT area(box '((0,0),(2,3))') AS rect, round(area(circle '((0,0),2)')::numeric, 4) AS circ;")
F("Geometric", "center", "center(box | circle) -> point", "Centre point of a shape.", "SELECT center(box '((0,0),(2,4))') AS centre;")
F("Geometric", "diagonal / diameter", "diagonal(box), diameter(circle)", "Diagonal of a box as a segment, diameter of a circle.", "SELECT diagonal(box '((0,0),(3,4))') AS diag, diameter(circle '((0,0),5)') AS dia;")
F("Geometric", "height / width", "height(box), width(box)", "Vertical and horizontal size of a box.", "SELECT height(box '((0,0),(3,4))') AS h, width(box '((0,0),(3,4))') AS w;")
F("Geometric", "length", "length(lseg | path) -> double", "Total length of a segment or path.", "SELECT length(lseg '((0,0),(3,4))') AS seg_len;")
F("Geometric", "npoints", "npoints(path | polygon) -> integer", "Number of points in a path or polygon.", "SELECT npoints(path '((0,0),(1,1),(2,0))') AS pts;")
F("Geometric", "isclosed / isopen", "isclosed(path), isopen(path)", "Whether a path is closed or open.", "SELECT isclosed(path '((0,0),(1,1),(2,0))') AS closed, isopen(path '[(0,0),(1,1),(2,0)]') AS open;")
F("Geometric", "pclose / popen", "pclose(path), popen(path)", "Converts a path to closed or open form.", "SELECT pclose(path '[(0,0),(1,1)]') AS closed, popen(path '((0,0),(1,1))') AS opened;")
F("Geometric", "radius", "radius(circle) -> double", "Radius of a circle.", "SELECT radius(circle '((0,0),5)') AS r;")
F("Geometric", "bound_box", "bound_box(box, box) -> box", "Smallest box containing both inputs.", "SELECT bound_box(box '((0,0),(1,1))', box '((3,3),(4,4))') AS bounding;")
F("Geometric", "geometric operators", "<->, @>, &&, #, ?-|, ?||", "Distance, containment, overlap, intersection and orientation tests.", "SELECT point '(0,0)' <-> point '(3,4)' AS distance, box '((0,0),(3,3))' @> point '(1,1)' AS contains, lseg '((0,0),(0,3))' ?|| lseg '((1,0),(1,3))' AS parallel;")

# --------------------------------------------- 18. ENUM, UUID & TYPE INFO
F("Types", "gen_random_uuid", "gen_random_uuid() -> uuid", "Generates a version 4 (random) UUID.", "SELECT gen_random_uuid() AS id;", volatile=True)
F("Types", "enum_first", "enum_first(anyenum) -> anyenum", "First value of an enum type.", "SELECT enum_first(null::mood) AS first_label;")
F("Types", "enum_last", "enum_last(anyenum) -> anyenum", "Last value of an enum type.", "SELECT enum_last(null::mood) AS last_label;")
F("Types", "enum_range", "enum_range(anyenum [, anyenum]) -> anyarray", "All values of an enum type, optionally within a range.", "SELECT enum_range(null::mood) AS all_labels, enum_range('ok'::mood, 'happy'::mood) AS subset;")
F("Types", "pg_typeof", "pg_typeof(any) -> regtype", "Data type of any expression.", "SELECT pg_typeof(1) AS int_lit, pg_typeof(1.0) AS num_lit, pg_typeof(now()) AS ts, pg_typeof(salary) AS column_type FROM employees LIMIT 1;")
F("Types", "format_type", "format_type(type_oid, typemod) -> text", "SQL name of a type, given its OID and modifier.", "SELECT format_type(atttypid, atttypmod) AS declared_type, attname AS column FROM pg_attribute WHERE attrelid = 'employees'::regclass AND attnum > 0 ORDER BY attnum;")
F("Types", "CAST", "CAST(expr AS type) / expr::type", "Explicit type conversion, in SQL-standard and PostgreSQL syntax.", "SELECT CAST('42' AS integer) AS standard, '2026-01-09'::date AS shorthand, 42::text || '!' AS to_text;")
F("Types", "to_regclass", "to_regclass(text) -> regclass", "Looks up a relation by name, returning NULL instead of erroring.", "SELECT to_regclass('employees') AS found, to_regclass('no_such_table') AS missing;")
F("Types", "OID reference types", "regclass, regtype, regproc, regnamespace", "Object identifier types that display as readable names.", "SELECT 'employees'::regclass::oid > 0 AS has_oid, 'int4'::regtype AS type_name, 'public'::regnamespace AS schema_name;")
F("Types", "composite & row", "ROW(...), (composite).field", "Row constructors and field access on composite values.", "SELECT (ROW(1, 'Alice'::text, 70000)).f2 AS second_field, (e).name AS from_table FROM employees e WHERE id = 1;")

# ------------------------------------------------- 19. SYSTEM INFORMATION
F("SystemInfo", "version", "version() -> text", "Full version string of the running server.", "SELECT version() AS server;")
F("SystemInfo", "current_database", "current_database() -> name", "Name of the database the session is connected to.", "SELECT current_database() AS db, current_catalog AS sql_standard_spelling;")
F("SystemInfo", "current_schema", "current_schema() -> name", "First schema of the search path, where new objects are created.", "SELECT current_schema() AS creation_schema, current_schemas(true) AS full_path;")
F("SystemInfo", "current_user", "current_user -> name", "Role used for permission checks in the current context.", "SELECT current_user AS effective, session_user AS logged_in_as, user AS alias;")
F("SystemInfo", "current_query", "current_query() -> text", "Text of the query currently being executed.", "SELECT current_query() AS running;")
F("SystemInfo", "pg_backend_pid", "pg_backend_pid() -> integer", "Process ID of the backend serving this session.", "SELECT pg_backend_pid() > 0 AS has_pid;")
F("SystemInfo", "pg_blocking_pids", "pg_blocking_pids(pid) -> integer[]", "Process IDs blocking the given backend on a lock.", "SELECT pg_blocking_pids(pg_backend_pid()) AS blockers;")
F("SystemInfo", "pg_postmaster_start_time", "pg_postmaster_start_time() -> timestamptz", "When the server was started.", "SELECT pg_postmaster_start_time() < now() AS started_before_now;")
F("SystemInfo", "pg_conf_load_time", "pg_conf_load_time() -> timestamptz", "When the configuration files were last loaded.", "SELECT pg_conf_load_time() <= now() AS loaded;")
F("SystemInfo", "pg_is_in_recovery", "pg_is_in_recovery() -> boolean", "True when the server is a standby replaying WAL.", "SELECT pg_is_in_recovery() AS standby;")
F("SystemInfo", "pg_jit_available", "pg_jit_available() -> boolean", "True when the JIT compiler provider is available.", "SELECT pg_jit_available() AS jit;")
F("SystemInfo", "pg_listening_channels", "pg_listening_channels() -> setof text", "Channels this session is listening to via LISTEN.", "SELECT count(*) AS channels FROM pg_listening_channels();")
F("SystemInfo", "pg_notification_queue_usage", "pg_notification_queue_usage() -> double", "Fraction of the asynchronous notification queue in use.", "SELECT pg_notification_queue_usage() AS queue_fraction;")
F("SystemInfo", "pg_trigger_depth", "pg_trigger_depth() -> integer", "Nesting level of the trigger currently executing.", "SELECT pg_trigger_depth() AS depth;")
F("SystemInfo", "inet_client_addr", "inet_client_addr() -> inet", "Address of the connected client; NULL over a Unix socket.", "SELECT inet_client_addr() AS client, inet_client_port() AS port;")
F("SystemInfo", "inet_server_addr", "inet_server_addr() -> inet", "Address the server accepted the connection on.", "SELECT inet_server_addr() AS server, inet_server_port() AS port;")
F("SystemInfo", "has_table_privilege", "has_table_privilege([user,] table, privilege) -> boolean", "Tests a role's privilege on a table.", "SELECT has_table_privilege('employees', 'SELECT') AS can_read, has_table_privilege('employees', 'TRUNCATE') AS can_truncate;")
F("SystemInfo", "has_column_privilege", "has_column_privilege(table, column, privilege) -> boolean", "Tests a role's privilege on a single column.", "SELECT has_column_privilege('employees', 'salary', 'SELECT') AS can_read_salary;")
F("SystemInfo", "has_schema_privilege", "has_schema_privilege(schema, privilege) -> boolean", "Tests a role's privilege on a schema.", "SELECT has_schema_privilege('public', 'USAGE') AS can_use, has_schema_privilege('public', 'CREATE') AS can_create;")
F("SystemInfo", "has_database_privilege", "has_database_privilege(db, privilege) -> boolean", "Tests a role's privilege on a database.", "SELECT has_database_privilege('pgmaster_demo', 'CONNECT') AS can_connect;")
F("SystemInfo", "pg_has_role", "pg_has_role([user,] role, privilege) -> boolean", "Tests role membership.", "SELECT pg_has_role('pgmaster', 'MEMBER') AS is_member;")
F("SystemInfo", "pg_table_is_visible", "pg_table_is_visible(oid) -> boolean", "True when the table is reachable through the search path unqualified.", "SELECT pg_table_is_visible('employees'::regclass) AS visible;")
F("SystemInfo", "pg_get_viewdef", "pg_get_viewdef(view [, pretty]) -> text", "Reconstructs the SELECT statement behind a view.", "SELECT pg_get_viewdef('high_earners'::regclass, true) AS definition;")
F("SystemInfo", "pg_get_indexdef", "pg_get_indexdef(index) -> text", "Reconstructs the CREATE INDEX statement for an index.", "SELECT pg_get_indexdef('idx_emp_name'::regclass) AS definition;")
F("SystemInfo", "pg_get_constraintdef", "pg_get_constraintdef(oid) -> text", "Reconstructs the definition of a constraint.", "SELECT conname AS constraint_name, pg_get_constraintdef(oid) AS definition FROM pg_constraint WHERE conrelid = 'employees'::regclass ORDER BY conname;")
F("SystemInfo", "pg_get_functiondef", "pg_get_functiondef(func) -> text", "Reconstructs the CREATE FUNCTION statement for a function.", "SELECT pg_get_functiondef('annual_bonus(numeric)'::regprocedure) AS definition;", setup="CREATE FUNCTION annual_bonus(pay numeric) RETURNS numeric AS $$ SELECT round(pay * 0.10, 2) $$ LANGUAGE sql IMMUTABLE;")
F("SystemInfo", "pg_get_expr", "pg_get_expr(expr, relation) -> text", "Decompiles an internal expression tree, such as a column default.", "SELECT attname AS column, pg_get_expr(adbin, adrelid) AS default_expr FROM pg_attrdef d JOIN pg_attribute a ON a.attrelid = d.adrelid AND a.attnum = d.adnum WHERE adrelid = 'note'::regclass;", setup="CREATE TABLE note (id int, created timestamptz DEFAULT now(), tag text DEFAULT 'general');")
F("SystemInfo", "pg_describe_object", "pg_describe_object(classid, objid, objsubid) -> text", "Human-readable description of a database object.", "SELECT pg_describe_object('pg_class'::regclass, 'employees'::regclass, 0) AS described;")
F("SystemInfo", "obj_description", "obj_description(object_oid [, catalog]) -> text", "Reads the COMMENT attached to a database object.", "SELECT obj_description('employees'::regclass, 'pg_class') AS table_comment;", setup="COMMENT ON TABLE employees IS 'Staff roster used by the PGMaster demos';")
F("SystemInfo", "col_description", "col_description(table_oid, column_number) -> text", "Reads the COMMENT attached to a column.", "SELECT col_description('employees'::regclass, 4) AS salary_comment;", setup="COMMENT ON COLUMN employees.salary IS 'Annual gross pay in USD';")
F("SystemInfo", "information_schema", "information_schema.columns / tables", "Portable, SQL-standard catalog views describing the database.", "SELECT column_name, data_type, is_nullable FROM information_schema.columns WHERE table_name = 'employees' ORDER BY ordinal_position;")
F("SystemInfo", "pg_catalog views", "pg_class, pg_attribute, pg_indexes, pg_stat_activity", "PostgreSQL's own system catalogs, richer than information_schema.", "SELECT indexname, indexdef FROM pg_indexes WHERE tablename = 'employees' ORDER BY indexname;")

# ------------------------------------------- 20. SYSTEM ADMINISTRATION
F("Admin", "current_setting", "current_setting(name [, missing_ok]) -> text", "Reads the value of a run-time configuration parameter.", "SELECT current_setting('server_version') AS version, current_setting('search_path') AS path, current_setting('nope.nope', true) AS missing_ok;")
F("Admin", "set_config", "set_config(name, value, is_local) -> text", "Sets a configuration parameter, optionally for the transaction only.", "SELECT set_config('my.tenant', 'acme', true) AS was_set, current_setting('my.tenant') AS read_back;")
F("Admin", "pg_size_pretty", "pg_size_pretty(bigint) -> text", "Formats a byte count in human-readable units.", "SELECT pg_size_pretty(1234567::bigint) AS pretty, pg_size_pretty(pg_total_relation_size('employees')) AS employees_table;")
F("Admin", "pg_column_size", "pg_column_size(any) -> integer", "Bytes used to store a value on disk, including compression.", "SELECT pg_column_size(42) AS int_bytes, pg_column_size('Alice'::text) AS text_bytes, pg_column_size(now()) AS ts_bytes;")
F("Admin", "pg_relation_size", "pg_relation_size(relation [, fork]) -> bigint", "Size of the main data fork of a table or index.", "SELECT pg_size_pretty(pg_relation_size('employees')) AS heap_size;")
F("Admin", "pg_table_size", "pg_table_size(relation) -> bigint", "Table size including TOAST and free space map, excluding indexes.", "SELECT pg_size_pretty(pg_table_size('employees')) AS table_size;")
F("Admin", "pg_indexes_size", "pg_indexes_size(relation) -> bigint", "Total size of all indexes attached to a table.", "SELECT pg_size_pretty(pg_indexes_size('employees')) AS index_size;")
F("Admin", "pg_total_relation_size", "pg_total_relation_size(relation) -> bigint", "Table plus indexes plus TOAST: the complete footprint.", "SELECT pg_size_pretty(pg_total_relation_size('employees')) AS total;")
F("Admin", "pg_database_size", "pg_database_size(name) -> bigint", "Total disk space used by a database.", "SELECT pg_size_pretty(pg_database_size('pgmaster_demo')) AS db_size;")
F("Admin", "pg_relation_filepath", "pg_relation_filepath(relation) -> text", "Path of a relation's file, relative to the data directory.", "SELECT pg_relation_filepath('employees') LIKE 'base/%' AS under_base;")
F("Admin", "pg_column_compression", "pg_column_compression(any) -> text", "Compression method used for a stored value, or NULL when uncompressed.", "SELECT pg_column_compression(name) AS short_value, pg_column_compression(repeat(name, 500)::text) AS long_value FROM employees WHERE id = 1;")
F("Admin", "pg_advisory_lock", "pg_advisory_lock(key) -> void", "Takes an application-defined lock held until released or session end.", "SELECT pg_advisory_lock(4711) IS NULL AS acquired, pg_advisory_unlock(4711) AS released;")
F("Admin", "pg_try_advisory_lock", "pg_try_advisory_lock(key) -> boolean", "Takes an advisory lock without waiting; returns false when unavailable.", "SELECT pg_try_advisory_lock(4712) AS got_it, pg_advisory_unlock(4712) AS released;")
F("Admin", "pg_advisory_xact_lock", "pg_advisory_xact_lock(key) -> void", "Advisory lock released automatically at the end of the transaction.", "SELECT pg_advisory_xact_lock(4713) IS NULL AS held_until_commit;")
F("Admin", "pg_current_xact_id", "pg_current_xact_id() -> xid8", "Transaction ID of the current transaction, assigning one if needed.", "SELECT pg_current_xact_id() > '0'::xid8 AS has_xid, pg_current_xact_id_if_assigned() IS NOT NULL AS assigned;")
F("Admin", "pg_export_snapshot", "pg_export_snapshot() -> text", "Exports the current snapshot for another session to import.", "SELECT length(pg_export_snapshot()) > 0 AS exported;")
F("Admin", "pg_current_wal_lsn", "pg_current_wal_lsn() -> pg_lsn", "Current write-ahead log write position.", "SELECT pg_current_wal_lsn() > '0/0'::pg_lsn AS advancing, pg_walfile_name(pg_current_wal_lsn()) IS NOT NULL AS has_segment;")
F("Admin", "pg_stat views", "pg_stat_activity, pg_stat_user_tables, pg_statio_*", "Cumulative statistics views for activity, I/O and table access.", "SELECT relname, seq_scan >= 0 AS has_counter FROM pg_stat_user_tables ORDER BY relname;")
F("Admin", "ANALYZE / VACUUM", "VACUUM [FULL|ANALYZE] table", "Reclaims dead tuples and refreshes planner statistics.", "SELECT relname, last_analyze IS NULL AS never_analyzed FROM pg_stat_user_tables WHERE relname = 'employees';")
F("Admin", "EXPLAIN", "EXPLAIN [ANALYZE] statement", "Shows the planner's execution plan for a statement.", "EXPLAIN SELECT name FROM employees WHERE salary > 70000;")
F("Admin", "pg_cancel_backend", "pg_cancel_backend(pid) -> boolean", "Politely cancels the query running in another backend.", "SELECT pg_cancel_backend(12345);",
  out="MSG:Query cancelled in backend 12345 (returns t). Not executed here — it interrupts another session.")
F("Admin", "pg_terminate_backend", "pg_terminate_backend(pid [, timeout]) -> boolean", "Terminates another backend, closing its connection.", "SELECT pg_terminate_backend(12345);",
  out="MSG:Backend 12345 terminated (returns t). Not executed here — it disconnects another session.")
F("Admin", "pg_reload_conf", "pg_reload_conf() -> boolean", "Signals the server to re-read its configuration files.", "SELECT pg_reload_conf();",
  out="MSG:Returns t after the postmaster re-reads postgresql.conf and pg_hba.conf. Not executed here — it changes live server state.")
F("Admin", "pg_switch_wal", "pg_switch_wal() -> pg_lsn", "Forces the server to switch to a new write-ahead log file.", "SELECT pg_switch_wal();",
  out="MSG:Returns the ending LSN of the WAL segment just closed, e.g. 0/1A4C8D0. Not executed here — it forces a WAL segment switch.")
F("Admin", "pg_ls_dir", "pg_ls_dir(dirname) -> setof text", "Lists the files in a directory inside the data directory (superuser only).", "SELECT pg_ls_dir('pg_wal') LIMIT 3;",
  out="MSG:Returns one row per file, e.g. 000000010000000000000001, archive_status. Not executed here — the output would expose local filesystem paths.")
F("Admin", "pg_read_file", "pg_read_file(filename [, offset, length]) -> text", "Reads a text file on the server (superuser or pg_read_server_files).", "SELECT pg_read_file('postgresql.conf', 0, 120);",
  out="MSG:Returns the first 120 characters of postgresql.conf. Not executed here — the output would expose local server configuration.")
F("Admin", "pg_stat_file", "pg_stat_file(filename) -> record", "Returns size and timestamps for a file on the server.", "SELECT size, modification FROM pg_stat_file('postgresql.conf');",
  out="MSG:Returns size, access, modification, change, creation and isdir. Not executed here — the output would expose local filesystem detail.")
F("Admin", "pg_backup_start / stop", "pg_backup_start(label), pg_backup_stop()", "Brackets a low-level base backup of the cluster.", "SELECT pg_backup_start('nightly'); SELECT * FROM pg_backup_stop();",
  out="MSG:pg_backup_start returns the starting LSN; pg_backup_stop returns lsn, labelfile and spcmapfile. Not executed here — it puts the cluster into backup mode.")
F("Admin", "pg_promote", "pg_promote([wait, wait_seconds]) -> boolean", "Promotes a standby server to become the primary.", "SELECT pg_promote();",
  out="MSG:Returns t once the standby is promoted. Not executed here — this server is a primary, and promotion is irreversible.")

# ------------------------------------------- 21. TRIGGERS & PROCEDURES
TRG_SETUP = """CREATE TABLE account (id int PRIMARY KEY, owner text, balance numeric, updated_at timestamptz);
CREATE TABLE account_audit (id int, old_balance numeric, new_balance numeric, changed_at timestamptz);
INSERT INTO account VALUES (1, 'Alice', 1000, '2026-01-01');"""
F("Trigger", "CREATE FUNCTION (SQL)", "CREATE FUNCTION name(args) RETURNS type AS $$ ... $$ LANGUAGE sql", "A stored function written in plain SQL.", "SELECT name, salary, annual_bonus(salary) AS bonus FROM employees ORDER BY id LIMIT 3;",
  setup="CREATE FUNCTION annual_bonus(pay numeric) RETURNS numeric AS $$ SELECT round(pay * 0.10, 2) $$ LANGUAGE sql IMMUTABLE;")
F("Trigger", "CREATE FUNCTION (PL/pgSQL)", "CREATE FUNCTION ... LANGUAGE plpgsql", "A stored function with procedural logic: variables, IF, loops.", "SELECT name, salary, pay_band(salary) AS band FROM employees ORDER BY salary DESC;",
  setup="""CREATE FUNCTION pay_band(pay numeric) RETURNS text AS $$
BEGIN
  IF pay >= 85000 THEN RETURN 'Senior';
  ELSIF pay >= 65000 THEN RETURN 'Mid';
  ELSE RETURN 'Junior';
  END IF;
END; $$ LANGUAGE plpgsql IMMUTABLE;""")
F("Trigger", "RETURNS TABLE", "CREATE FUNCTION ... RETURNS TABLE(...)", "A set-returning function that yields a whole result set.", "SELECT * FROM dept_roster(101);",
  setup="""CREATE FUNCTION dept_roster(d int) RETURNS TABLE(emp_name text, pay numeric) AS $$
  SELECT name, salary FROM employees WHERE dept_id = d ORDER BY salary DESC;
$$ LANGUAGE sql STABLE;""")
F("Trigger", "CREATE PROCEDURE / CALL", "CREATE PROCEDURE name(args) ... ; CALL name(args)", "Procedures run with CALL and may manage their own transactions.", "CALL give_raise(1, 5); SELECT name, salary FROM employees WHERE id = 1;",
  setup="""CREATE PROCEDURE give_raise(emp int, pct numeric) LANGUAGE plpgsql AS $$
BEGIN
  UPDATE employees SET salary = round(salary * (1 + pct/100), 2) WHERE id = emp;
END; $$;""")
F("Trigger", "CREATE TRIGGER (row)", "CREATE TRIGGER ... FOR EACH ROW EXECUTE FUNCTION f()", "A row-level trigger firing a function before or after each change.", "UPDATE account SET balance = 1500 WHERE id = 1; SELECT * FROM account_audit;",
  setup=TRG_SETUP + """
CREATE FUNCTION audit_balance() RETURNS trigger AS $$
BEGIN
  INSERT INTO account_audit VALUES (OLD.id, OLD.balance, NEW.balance, timestamptz '2026-01-09 10:00:00+00');
  RETURN NEW;
END; $$ LANGUAGE plpgsql;
CREATE TRIGGER trg_audit AFTER UPDATE ON account FOR EACH ROW EXECUTE FUNCTION audit_balance();""")
F("Trigger", "BEFORE trigger (NEW)", "BEFORE INSERT OR UPDATE ... RETURN NEW", "A BEFORE trigger can rewrite the row about to be stored.", "UPDATE account SET balance = 2000 WHERE id = 1; SELECT id, balance, updated_at FROM account;",
  setup=TRG_SETUP + """
CREATE FUNCTION stamp_row() RETURNS trigger AS $$
BEGIN
  NEW.updated_at := timestamptz '2026-01-09 10:00:00+00';
  RETURN NEW;
END; $$ LANGUAGE plpgsql;
CREATE TRIGGER trg_stamp BEFORE UPDATE ON account FOR EACH ROW EXECUTE FUNCTION stamp_row();""")
F("Trigger", "statement trigger", "FOR EACH STATEMENT EXECUTE FUNCTION f()", "Fires once per statement rather than once per row.", "UPDATE account SET balance = balance + 1; SELECT * FROM account_audit;",
  setup=TRG_SETUP + """
CREATE FUNCTION log_statement() RETURNS trigger AS $$
BEGIN
  INSERT INTO account_audit VALUES (0, NULL, NULL, timestamptz '2026-01-09 10:00:00+00');
  RETURN NULL;
END; $$ LANGUAGE plpgsql;
CREATE TRIGGER trg_stmt AFTER UPDATE ON account FOR EACH STATEMENT EXECUTE FUNCTION log_statement();""")
F("Trigger", "conditional trigger (WHEN)", "CREATE TRIGGER ... WHEN (condition)", "Restricts a trigger to rows that satisfy a condition.", "UPDATE account SET balance = 1001 WHERE id = 1; UPDATE account SET balance = 99999 WHERE id = 1; SELECT * FROM account_audit;",
  setup=TRG_SETUP + """
CREATE FUNCTION audit_big_move() RETURNS trigger AS $$
BEGIN
  INSERT INTO account_audit VALUES (OLD.id, OLD.balance, NEW.balance, timestamptz '2026-01-09 10:00:00+00');
  RETURN NEW;
END; $$ LANGUAGE plpgsql;
CREATE TRIGGER trg_big AFTER UPDATE ON account FOR EACH ROW WHEN (NEW.balance - OLD.balance > 1000) EXECUTE FUNCTION audit_big_move();""")
F("Trigger", "suppress_redundant_updates_trigger", "suppress_redundant_updates_trigger()", "Built-in trigger that skips UPDATEs which would not change the row.", "UPDATE account SET balance = balance WHERE id = 1; SELECT ctid = '(0,1)'::tid AS row_not_rewritten FROM account WHERE id = 1;",
  setup=TRG_SETUP + "\nCREATE TRIGGER trg_skip BEFORE UPDATE ON account FOR EACH ROW EXECUTE FUNCTION suppress_redundant_updates_trigger();")
F("Trigger", "tsvector_update_trigger", "tsvector_update_trigger(tsv_col, config, text_col...)", "Built-in trigger that keeps a tsvector column in sync with text columns.", "INSERT INTO doc (title, body) VALUES ('Quick Guide', 'the quick brown fox'); SELECT title, tsv FROM doc;",
  setup="""CREATE TABLE doc (id serial, title text, body text, tsv tsvector);
CREATE TRIGGER trg_tsv BEFORE INSERT OR UPDATE ON doc FOR EACH ROW EXECUTE FUNCTION tsvector_update_trigger(tsv, 'pg_catalog.english', title, body);""")
F("Trigger", "TG_OP / TG_TABLE_NAME", "TG_OP, TG_TABLE_NAME, TG_WHEN, TG_LEVEL", "Special variables telling a trigger function how it was invoked.", "INSERT INTO account VALUES (2, 'Bob', 500, now()); UPDATE account SET balance = 600 WHERE id = 2; SELECT * FROM trigger_log ORDER BY seq;",
  setup="""CREATE TABLE account (id int PRIMARY KEY, owner text, balance numeric, updated_at timestamptz);
CREATE TABLE trigger_log (seq serial, op text, tbl text, level text);
CREATE FUNCTION describe_event() RETURNS trigger AS $$
BEGIN
  INSERT INTO trigger_log (op, tbl, level) VALUES (TG_OP, TG_TABLE_NAME, TG_LEVEL);
  RETURN NEW;
END; $$ LANGUAGE plpgsql;
CREATE TRIGGER trg_desc AFTER INSERT OR UPDATE ON account FOR EACH ROW EXECUTE FUNCTION describe_event();""")
F("Trigger", "RAISE", "RAISE NOTICE | EXCEPTION 'msg', args", "Emits messages or aborts the transaction from PL/pgSQL.", "SELECT check_salary(-5);",
  setup="""CREATE FUNCTION check_salary(pay numeric) RETURNS text AS $$
BEGIN
  IF pay < 0 THEN
    RETURN 'rejected: ' || pay;
  END IF;
  RETURN 'accepted';
END; $$ LANGUAGE plpgsql;""")
F("Trigger", "event trigger", "CREATE EVENT TRIGGER ... ON ddl_command_end", "Fires on DDL rather than data changes; inspect it with pg_event_trigger_ddl_commands().", "CREATE TABLE demo_ddl (x int);",
  out="MSG:With an event trigger on ddl_command_end calling pg_event_trigger_ddl_commands(), the CREATE TABLE above raises: NOTICE: DDL: CREATE TABLE on public.demo_ddl. Not executed here — event triggers are database-wide and outlive the demo transaction.")
F("Trigger", "RETURNING", "INSERT/UPDATE/DELETE ... RETURNING expr", "Returns rows affected by a write statement, avoiding a second query.", "UPDATE employees SET salary = salary * 1.05 WHERE dept_id = 101 RETURNING id, name, salary;")
F("Trigger", "ON CONFLICT (upsert)", "INSERT ... ON CONFLICT (col) DO UPDATE SET ...", "Insert-or-update in a single atomic statement.", "INSERT INTO departments VALUES (101, 'Information Technology') ON CONFLICT (dept_id) DO UPDATE SET dept_name = EXCLUDED.dept_name RETURNING *;")
