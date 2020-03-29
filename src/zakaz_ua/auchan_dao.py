DAO = ['29 Mar 14:00 – 16:00', '28 Mar 14:00 – 16:00']


def get_slots():
    return DAO


def remove_slots(slots):
    for slot in slots:
        DAO.remove(slot)


def add_slots(slots):
    DAO.extend(slots)
