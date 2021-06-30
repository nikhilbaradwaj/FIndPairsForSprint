import argparse
from utilities import read_json_file, write_to_file, print_output

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
    employee_data = read_json_file("app/employees.json")
    weeks = pick_from_pairs(employee_data, args.num_weeks)
    print_output(weeks)
    write_to_file(weeks)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Employee Scheduler')
    parser.add_argument('num_weeks', type=int, help='Number of weeks to schedule for')
    args = parser.parse_args()
    main(args)
