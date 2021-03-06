import json
import random


def mutate_probabilistic_fasting(plan):
    for day_idx, day in enumerate(plan):
        for meal, choice in day.items():
            if random.uniform(0, 1) < 0.05:
                plan[day_idx][meal] = ('❌ fasting', [])

    return plan


def generate_prune_plan(mode):
    plans = [generate_plan(mode) for e in range(1)]
    prop_set = []

    for plan in plans:
        all_ingredients = []

        for day in plan:
            all_ingredients += [e[1] for e in day.values()]

        all_ingredients = [
            elem for sublist in all_ingredients for elem in sublist]
        prop_set += [len(set(all_ingredients)) / len(all_ingredients)]

    return plans[prop_set.index(min(prop_set))]


def generate_plan(mode):
    day_plans = []

    if mode == '3x2+1':
        day_plans = [generate_day_plan(), generate_day_plan(),
                     generate_day_plan()]
        day_plans.insert(1, day_plans[0].copy())
        day_plans.insert(3, day_plans[2].copy())
        day_plans.insert(5, day_plans[4].copy())
    elif mode == '2x3+1':
        day_plans = [generate_day_plan(), generate_day_plan()]
        day_plans.insert(1, day_plans[0].copy())
        day_plans.insert(2, day_plans[0].copy())
        day_plans.insert(4, day_plans[3].copy())
        day_plans.insert(5, day_plans[3].copy())
    elif mode == '1x1':
        day_plans = [generate_day_plan()]

    return day_plans


def generate_day_plan():
    day_plan = {}

    kb = json.load(open('data/winter.json'))
    for meal in kb.keys():
        meal_choice = random.choice(list(kb[meal].keys()))
        meal_ingredients = []

        for ingredient in kb[meal][meal_choice]:
            if isinstance(ingredient, str):
                meal_ingredients += [ingredient]
            else:
                choice = random.choice(ingredient)
                if choice != '':
                    meal_ingredients += [choice]

        day_plan[meal] = (meal_choice, meal_ingredients)

    return day_plan
