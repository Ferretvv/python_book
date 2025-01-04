# Use slicing to write Python code to print a 6-character 
# substring of 'Launch School' that begins with the first c.
splice = "Launch School"
print(splice[4:10])

# Launch school suggests doing it programatically:
my_str = 'Launch School'
start = my_str.find('c')
print(my_str[start:start + 6])        # ch Sch