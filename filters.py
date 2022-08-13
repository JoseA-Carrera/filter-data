from data import DATA


if __name__ == '__main__':
    # filter datas with comprehensions

    all_python_devs_platzi = [
        worker['name'] for worker in DATA if worker['language'] == 'python' and worker['organization'] == 'Platzi'
    ]
    old_people = [i['name'] for i in DATA if i['age'] >= 60]

    # ----------------------------------------------------------------------------------------

    # using higher order functions

    # all_python_devs_platzi = list(filter(lambda worker: worker['language'] == 'python' and worker['organization'] == 'Platzi', DATA))
    # all_python_devs_platzi = list(map(lambda worker: worker['name'], all_python_devs_platzi))

    # old_people = list(map(lambda worker: {**worker, **{"old": worker["age"] > 60}}, DATA))
    # old_people = list(filter(lambda worker: worker['old'] == True, old_people))
    # old_people = list(map(lambda worker: worker['name'], old_people))

    for worker in old_people:
        print(worker)

# sorry if it's wrong xd
