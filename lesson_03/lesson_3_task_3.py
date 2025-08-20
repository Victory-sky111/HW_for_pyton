from address import Address

from mail import Mailing

to_address = Address("101000", "Москва", "Маросейка", "15", "10")
from_address = Address("690000", "Владивосток", "Днепровская", "27", "1")
cost = int(5500)
track = str("654R654F")

offl_mail = Mailing(to_address, from_address, cost, track)

print(offl_mail)
