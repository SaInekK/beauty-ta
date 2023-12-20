json = {
    'company_id': 111111,
    'resource': 'record',
    'resource_id': 406155061,
    'status': 'create',
    'data': {
        'id': 11111111,
        'company_id': 111111,
        'services': [
            {
                'id': 9035445,
                'title': 'Стрижка',
                'cost': 1500,
                'cost_per_unit': 1500,
                'first_cost': 1500,
                'amount': 1
            }
        ],
        'goods_transactions': [],
        'staff': {
            'id': 1819441,
            'name': 'Мастер'
        },
        'client': {
            'id': 130345867,
            'name': 'Клиент',
            'phone': '79111111111',
            'success_visits_count': 2,
            'fail_visits_count': 0
        },
        'clients_count': 1,
        'datetime': '2022-01-25T11:00:00+03:00',
        'create_date': '2022-01-22T00:54:00+03:00',
        'online': False,
        'attendance': 0,
        'confirmed': 1,
        'seance_length': 3600,
        'length': 3600,
        'master_request': 1,
        'visit_id': 346427049,
        'created_user_id': 10573443,
        'deleted': False,
        'paid_full': 0,
        'last_change_date': '2022-01-22T00:54:00+03:00',
        'record_labels': '',
        'date': '2022-01-22 10:00:00'
    }
}
json_old = {
    'company_id': 111111,
    'resource': 'record',
    'resource_id': 406155061,
    'status': 'create',
    'data': {
        'id': 11111111,
        'company_id': 111111,
        'services': [
            {
                'id': 9035445,
                'title': 'Стрижка',
                'cost': 1500,
                'cost_per_unit': 1500,
                'first_cost': 1500,
                'amount': 1
            }
        ],
        'goods_transactions': [],
        'staff': {
            'id': 1819441,
            'name': 'Мастер'
        },
        'client': {
            'id': 130345867,
            'name': 'Клиент',
            'phone': '79111111111',
            'success_visits_count': 2,
            'fail_visits_count': 0
        },
        'clients_count': 1,
        'datetime': '2022-01-25T11:00:00+03:00',
        'create_date': '2022-01-22T00:54:00+03:00',
        'online': False,
        'attendance': 0,
        'confirmed': 1,
        'seance_length': 3600,
        'length': 3600,
        'master_request': 1,
        'visit_id': 346427049,
        'created_user_id': 10573443,
        'deleted': False,
        'paid_full': 0,
        'last_change_date': '2022-01-22T00:54:00+03:00',
        'record_labels': '',
        'date': '2022-01-22 10:00:00'
    }
}
json_new = {
    'company_id': 111111,
    'resource': 'record',
    'resource_id': 406155061,
    'status': 'create',
    'data': {
        'id': 11111111,
        'company_id': 111111,
        'services': [
            {
                'id': 22222225,
                'title': 'Стрижка',
                'cost': 1500,
                'cost_per_unit': 1500,
                'first_cost': 1500,
                'amount': 1
            }
        ],
        'goods_transactions': [],
        'staff': {
            'id': 1819441,
            'name': 'Мастер'
        },
        'client': {
            'id': 130345867,
            'name': 'Клиент',
            'phone': '79111111111',
            'success_visits_count': 2,
            'fail_visits_count': 0
        },
        'clients_count': 1,
        'datetime': '2022-01-25T13:00:00+03:00',
        'create_date': '2022-01-22T00:54:00+03:00',
        'online': False,
        'attendance': 2,
        'confirmed': 1,
        'seance_length': 3600,
        'length': 3600,
        'master_request': 1,
        'visit_id': 346427049,
        'created_user_id': 10573443,
        'deleted': False,
        'paid_full': 1,
        'last_change_date': '2022-01-22T00:54:00+03:00',
        'record_labels': '',
        'date': '2022-01-22 10:00:00'
    }
}

diff_list = [
    'services',
    'staff',
    'datetime',
]


class Empty:
    pass

# e = Empty()
# print(isinstance(e, None))


def get_json_diff(diff_list, json_old, json_new):
    diff_dict = {}
    for param in diff_list:
        old_value = json_old.get(param, Empty)
        new_value = json_new.get(param, Empty)
        equal = compare_values(old_value, new_value)
        if not equal:
            diff_dict[param] = new_value
    return diff_dict


def compare_values(val_1, val_2):
    type_1 = type(val_1)
    type_2 = type(val_2)
    if type_1 != type_2:
        return False
    if isinstance(val_1, (str, int, bool, float)):
        return val_1 == val_2
    if isinstance(val_1, list):
        if len(val_1) != len(val_2):
            return False
        for i, e in enumerate(val_1):
            res = compare_values(e, val_2[i])
            if res is False:
                return False
        return True
    if isinstance(val_1, dict):
        if len(val_1) != len(val_2):
            return False
        for k, v in val_1.items():
            res = compare_values(v, val_2.get(k, Empty))
            if res is False:
                return False
        return True


if __name__ == '__main__':
    # res = get_json_diff(diff_list, json_old, json_new)
    res = get_json_diff(diff_list, json_old, json_new)
    print(res)
