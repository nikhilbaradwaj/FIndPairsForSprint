import argparse
from app.utilities import read_json_file, write_to_file, print_output

def get_all_distinct_pairings(arr):
    if len(arr) == 1:
        return [(arr[0],)]
    if len(arr) == 2:
        return [[(arr[0],arr[1])]]
    if len(arr) % 2 == 1:
        all_pairings = []
        for i in range(len(arr)):
            all_pairings = all_pairings + [[(arr[i],)] + pairing for pairing in get_all_distinct_pairings(arr[:i] + arr[i+1:])]
        return all_pairings
    else:
        all_pairings = []
        for i in range(1, len(arr)):
            all_pairings = all_pairings + [[(arr[0], arr[i])] + pairing for pairing in get_all_distinct_pairings(arr[1:i] + arr[i+1:])]
        return all_pairings

# def pick_optimal_pairings(arr, num_weeks):
#     all_distinct_weeks = get_all_distinct_pairings(arr)
#     optimal_weeks = []
#     all_distinct_weeks_copy = all_distinct_weeks[:]
#     index = 0
#     while optimal_weeks < num_weeks:
#         for i in range(len(all_distinct_weeks)):
#             for pair in all_distinct_weeks_copy[i]:
#                 if pair_is_recent(pair, optimal_weeks, 3):
#                     continue
#         continue
#     return optimal_weeks


def pick_from_pairs(arr, num_weeks):
    weeks = []
    for i in range(num_weeks):
        week = []
        arr = arr[-1:] + arr[:len(arr) - 1] # rotate right by 1
        week.append((arr[0],)) # pick a solo
        for person in arr:  # pick the remaining pairs for the week
            if already_picked_for_the_week(person, week):
                continue
            for partner in arr:
                if partner == person:
                    continue
                if already_picked_for_the_week(partner, week):
                    continue
                if pair_is_recent((person, partner), weeks, i, arr):
                    continue
                week.append((person, partner))
                break
        weeks.append(week)
    return weeks

def pair_is_recent(pair, weeks, week_num, arr):
    # Check tp see is a given pair ('a', 'b') has been selected in the recent weeks.
    i = week_num - 1
    possible_pairs_per_person = len(arr) - 1 # number of possible pairs with a person 'a'
    # while ((i >= 0)  and (i > week_num - possible_pairs_per_person - 1)):
    while ((i >= 0)  and (i > week_num - 2)):
        if already_picked_in_recent_weeks(pair, weeks, i):
            return True
        i = i - 1
    return False

def already_picked_in_recent_weeks(pair, weeks, week_num):
    for p in weeks[week_num]:
        if len(p) != 1:
            if (p[0] == pair[0] and p[1] == pair[1]) or (p[1] == pair[0] and p[0] == pair[1]):
                return True
    return False

def already_picked_for_the_week(person, week_pairings):
    for pair in week_pairings:
        if len(pair) == 1: # solo
            if person == pair[0]:
                return True
        else:  # pair
            if (person == pair[0]) or (person == pair[1]):
                return True
    return False

def main(args):
    employee_data = read_json_file(args.employees_info)
    weeks = pick_from_pairs(employee_data, args.num_weeks)
    print_output(weeks)
    write_to_file(weeks)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Employee Pair Programming Scheduler')
    parser.add_argument('employees_info', type=str, help='Employee information in JSON format')
    parser.add_argument('num_weeks', type=int, help='Number of weeks to schedule for')
    args = parser.parse_args()
    main(args)
