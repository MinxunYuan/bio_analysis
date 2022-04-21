import matplotlib.pyplot as plt


def test(**optoins):
    # optoins['city'] = 'changsha'

    for k in optoins.keys():
        print(k, optoins[k])
    if optoins.__contains__("name"):
        print(optoins["name"])
    print(optoins.get('city', 'changsha'))


if __name__ == '__main__':
    test(name="jerry", age=23);