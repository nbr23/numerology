# Numerology tools

## About
This is a small set of fun tools designed to play with numbers.
Based on a given string of digits, it will create all the possible combinations
of numbers, arrange them in all the imaginable ways, and try to add, substract,
multiply or divide each element composing the number in order to land on the
"Magic" number of which you want to prove the omnipresence.

## Usage
Usage:  ./numtools.py -i input [-slgq] [-m match]

* -i input : input on which to work (numeric string)
* -m match : number to find/match
* -l : performs a lexical generation of permutations (implies -s to be called)
* -s : sorts the numbers before processing
* -g : generate groups
* -q : quick mode, exists on the first match found instead of finding them all

## Examples

### Finding a number
This tool can be used for example to prove the omnipresence of the number 23 in
important dates, by simply feeding it a date (formated DDMMYY for example):
```
./numtools.py -i 110615 -m 23 -slgq
```
Which will result in:
```
(0+(1+(1+(15+6))))
```
Which equals 23!

### Generating lists
If no match (-m) is selected, the output will simply be the generated list of
numbers.

```
./numtools.py -i 123 -slg
```

Will result in:

```
[1, 2, 3]
[1, 23]
[12, 3]
[123]
[1, 3, 2]
[1, 32]
[13, 2]
[132]
[2, 1, 3]
[2, 13]
[21, 3]
[213]
[2, 3, 1]
[2, 31]
[23, 1]
[231]
[3, 1, 2]
[3, 12]
[31, 2]
[312]
[3, 2, 1]
[3, 21]
[32, 1]
[321]
```
