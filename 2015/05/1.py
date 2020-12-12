import re

with open('input.txt', 'r') as f:
    print(0)
    
    (?=([^ ]*[aeiou]){3,})\w*
    
    (?:([a-z])\1{1,})
    
    ((?![ab|cd|pq|xy]).)*
