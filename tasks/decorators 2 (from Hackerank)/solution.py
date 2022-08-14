from utils import yield_test_data


def person_lister(f):
    def inner(people) -> list:
        people = sorted(people, key=lambda x: int(x[2]))
        results = []
        for p in people:
            results.append(f"{'Mr.' if p[3]=='M' else 'Ms.'} {p[0]} {p[1]}")
        return results
    return inner


@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]


# Tests
def test_result(test_data, correct_result, test_number):
    test_data = yield_test_data(test_data)

    people_list = [next(test_data).split() for _ in range(int(next(test_data)))]
    result = name_format(people_list)

    assert result == correct_result
    print(f'Test #{test_number} passed successfully.')


if __name__ == '__main__':
    # Test 1
    test_data_list = ['3',
                      'Mike Thomson 20 M',
                      'Robert Bustle 32 M',
                      'Andria Bustle 30 F']
    correct_answer = ['Mr. Mike Thomson',
                      'Ms. Andria Bustle',
                      'Mr. Robert Bustle']
    test_result(test_data_list, correct_answer, 1)

    # Test2
    test_data_list = ['5',
                      'Laura Moser 50 F',
                      'Ted Moser 50 M',
                      'Yena Dixit 50 F',
                      'Diya Mirza 50 F',
                      'Rex Dsouza 51 M']
    correct_answer = ['Ms. Laura Moser',
                      'Mr. Ted Moser',
                      'Ms. Yena Dixit',
                      'Ms. Diya Mirza',
                      'Mr. Rex Dsouza']
    test_result(test_data_list, correct_answer, 2)

    # Test3
    test_data_list = ['10',
                      'Jake Jake 42 M',
                      'Jake Kevin 57 M',
                      'Jake Michael 91 M',
                      'Kevin Jake 2 M',
                      'Kevin Kevin 44 M',
                      'Kevin Michael 100 M',
                      'Michael Jake 4 M',
                      'Michael Kevin 36 M',
                      'Michael Michael 15 M',
                      'Micheal Micheal 6 M']
    correct_answer = ['Mr. Kevin Jake',
                      'Mr. Michael Jake',
                      'Mr. Micheal Micheal',
                      'Mr. Michael Michael',
                      'Mr. Michael Kevin',
                      'Mr. Jake Jake',
                      'Mr. Kevin Kevin',
                      'Mr. Jake Kevin',
                      'Mr. Jake Michael',
                      'Mr. Kevin Michael']
    test_result(test_data_list, correct_answer, 3)
