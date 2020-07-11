import re
x='abhinavshukla@gmail.com'
m =  re.match(r'(?P<User>\w+)@(?P<Website>\w+).(?P<Extension>\w+)',x)
print(m.groupdict())
