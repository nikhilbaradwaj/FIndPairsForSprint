from app.pairs import pair_is_recent, already_picked_for_the_week

def test_pair_is_recent():

    # Case where a pair has already been created in the previous week
    arr = ['a', 'b', 'c']
    pair = ('b', 'c')
    weeks = [[('a'), ('b', 'c')]]
    week_num = 1
    assert pair_is_recent(pair, weeks, week_num, arr) == True

    # Case where a pair has not been created in the previous week
    arr = ['a', 'b', 'c']
    pair = ('a', 'b')
    weeks = [[('a'), ('b', 'c')]]
    week_num = 1
    assert pair_is_recent(pair, weeks, week_num, arr) == False

    # Case where a pair has not been created yet and this is the first week
    arr = ['a', 'b', 'c']
    pair = ('a', 'b')
    weeks = []
    week_num = 0
    assert pair_is_recent(pair, weeks, week_num, arr) == False


    # arr = ['a', 'b', 'c', 'd', 'e']
    # pair = ('b', 'c')
    # weeks = [[('a'), ('b', 'c')('d', 'e')], [('b'), ('a', 'c'), ()]]
    # week_num = 1
    # assert pair_is_recent(pair, weeks, week_num, arr) == True


def test_already_picked_for_the_week():
    person = 'b'
    week_pairings = [('a'), ('b', 'c')]
    assert already_picked_for_the_week(person, week_pairings) == True

    person = 'd'
    week_pairings = [('a'), ('b', 'c')]
    assert already_picked_for_the_week(person, week_pairings) == False

    person = 'a'
    week_pairings = [('a'), ('b', 'c')]
    assert already_picked_for_the_week(person, week_pairings) == True
