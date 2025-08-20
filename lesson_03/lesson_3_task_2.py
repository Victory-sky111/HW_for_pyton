from smartphone import Sm_phone

library = [
    Sm_phone("Nokia", "3310", "+79209990099"),
    Sm_phone("Samsung", "C100", "+79219990099"),
    Sm_phone("Motorola", "V3", "+79229990099"),
    Sm_phone("Sony Ericsson", "K750i", "+79239990099"),
    Sm_phone("Siemens", "C35", "+79259990099")
]

for Smart_phone in library:
    print(f"{Smart_phone.brand} - {Smart_phone.model} - {Smart_phone.number}")
