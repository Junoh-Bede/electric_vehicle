

def calculate_ev(area, usage, factor):
    ev_capacity = 7
    parking_lot = {
        'CULTURAL': int(area / 100),
        'ETC': int(area / 200),
        'HOSPITAL': int(area / 100),
        'HOTEL': int(area / 134),
        'MULTI_RES': int(area / 60),
        'OFFICE': int(area / 100),
        'COMMERCIAL': int(area / 134),
        'SCHOOL': int(area / 200),
        'SOCIAL': int(area / 200),
        'GYM': int(area / 100),
        'INDUSTRIAL': int(area / 200),
        'SINGLE_RES': 0,
        'PARKING': int(area / 24 * 0.7),
        'AGRICULTURAL': 0,
        'COOLROOM': 0,
        'UNIVERSITY': int(area / 200),
        'COOL': 0,
        'COLD': 0,
        'GENERAL': 0,
        'RETAIL': int(area / 134),
    }
    if area > 50 and usage == 'SINGLE_RES':
        if area <= 150:
            parking_lot['SINGLE_RES'] = 1
        else:
            parking_lot['SINGLE_RES'] = int(1 + (area - 150) / 100)
    return factor * parking_lot[usage] * ev_capacity
