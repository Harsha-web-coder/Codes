print("Date Time Module")
print("Directive"+"\t"+"Example")

import datetime
import pendulum
import pytz

x = datetime.datetime.now()

l=["%a","%A","%w","%d","%b","%B","%m","%y","%Y","%H","%I","%p","%M",
   "%S","%f","%z","%Z","%j","%U","%W","%c","%C","%x","%X","%%","%G","%u","%V"]

for i in range(len(l)):
    print(l[i]+"\t\t"+x.strftime(l[i]))
print("offset-local:\t"+pendulum.now().strftime('%z'))
local = pendulum.local(2023,2,11)
print("TimeZone:\t"+local.timezone.name)