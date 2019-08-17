### Glossary:
- `HT`: Hash Table
- `slot`: HT index
- `hash collision`: when two keys return the same value

### Random notes:
- `dict` is Python's implementation of a hash table.
- Goal of a Hash Table is to achieve constant time for operations (lookup, insert, delete).
  - This happens by having a key (uniqe, by definition) to a value in an array (the _table_ in Hash Table).
  - The idea is to give the Hash Table a key and it gives you back a value (again, think python `dict`)
  - The big idea with a Hash Table is that it takes the Key and converts it to a value that can be used to identify the position in the _table_ (array) of the Hash Table
    - pseudo code: `hash_key(key) >>> index in the array`
- an index in the  is often called a `slot`; the array will have slots numbered from `0` to `hash_table.length - 1`

### Collisions:
- it's important to know the problem domain. say you want a table with 1000 values.
  - it'd be normal to expect the key range to be huge.
    - if you wanted to use a single 2 byte unsigned int as the key, that means 2^16 possible values
      - if you wanted to be able to use 4 ascii chars (1 byte each) as the key, that's 2^32 possible keys
  - two options:
    1) create an equal number of slots for the key range
      - give each of the original 1000 values a slot, and fill the rest of the slots with null
    2) create only 1000 slots and use a hash function that maps multiple keys to the same slot: `hashf(key1) = slot5 = hashf(key25)`
      - this will allow us to use a much smaller table (less memory) but it's now possible to have multiple keys access the same value. that is called a collision.
- the birthday question is a great stats illustration[1]:
  > To illustrate, consider a classroom full of students. What is the probability that some pair of students shares the same birthday (i.e., the same day of the year, not necessarily the same year)? If there are 23 students, then the odds are about even that two will share a birthday. This is despite the fact that there are 365 days in which students can have birthdays (ignoring leap years). On most days, no student in the class has a birthday. With more students, the probability of a shared birthday increases. The mapping of students to days based on their birthday is similar to assigning records to slots in a table (of size 365) using the birthday as a hash function.






[1](https://research.cs.vt.edu/AVresearch/hashing/hashfunc.php)