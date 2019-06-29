def avg_list(list_numbers):
    total = 0
    for list in list_numbers:
        total += list
    avg = total/len(list_numbers)
    return avg

states = {
    'Imo' : 'Owerri',
    'Abia' : 'Umuahia',
    'Adamawa' : 'Yola',
    'Akwa Ibom' : 'Uyo',
}
