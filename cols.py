#!/usr/bin/env python3

# Unfortunately, Google Sheet queries aren't quite powerful enough to do this
# type of query without some code generation. This script will generate a query
# to paste into the All Members sheet.

# Put keys for program elements / tracks here
elements = [
    "TRACK1",
    "TRACK2",
    "CHAIR",
]

print("Elements:")
for elt in elements:
    print(elt)

def add(letter, n):
    return chr(ord(letter) + n)

ncols = 13
first = 'A'
last = add(first, ncols - 1)


def elt_range(elt):
    r = elt + "!$%s$21:$%s" % (first, last)
    indirect = 'indirect("%s")' % r
    cols = ",".join("ABCDEFGHIJKLM")
    q = """query(%s, "select %s,'%s' label '%s' ''")""" % (
        indirect, cols, elt, elt
    )
    return q

print()
print("Query:")
query = 'query({%s},\n"select %s where Col1 is not null", FALSE)' % (
    ";\n".join([elt_range(elt) for elt in elements]),
    ",".join(["Col%d" % (i+1) for i in range(14)]),
)

# paste this into B6 in the All Members sheet
query = "=sort(iferror((%s))" % query
print(query)
