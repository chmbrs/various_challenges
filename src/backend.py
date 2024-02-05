import asyncio
from datetime import datetime
import time


def find_duplicated_items(items):
    d = {}
    for item in items:
        d[item] = None

    for item in items:
        if d.get(item):
            d[item] = True

    return [k for k, v in d.items() if v]


async def progressive_delay_item_writer(items):
    async def print_async(item, sleep_time, start):
        await asyncio.sleep(sleep_time)
        return item, (datetime.now() - start).seconds

    start = datetime.now()
    items_iterator = iter(items)
    tasks = []

    item = next(items_iterator, None)
    aux_counter = 0
    while item is not None:
        i = 2 ** aux_counter
        task = asyncio.create_task(print_async(item, i, start))
        tasks.append(task)
        item = next(items_iterator, None)
        aux_counter += 1

    return await asyncio.gather(*tasks)


def closed_brackets_checker(brackets_input):
    brackets_pairs = {
        '{': '}',
        '(': ')',
        '[': ']'
    }

    pilha = []
    skipping_time = False
    for item in brackets_input:

        if item == '\'' and not skipping_time:
            skipping_time = True
            continue

        if item == '\'' and skipping_time:
            skipping_time = False
            continue

        if skipping_time:
            continue

        if item in brackets_pairs.keys():
            pilha.append(item)
        if item in brackets_pairs.values():
            ultimo_da_pilha = pilha.pop()
            if item == brackets_pairs[ultimo_da_pilha]:
                continue
            break
    return len(pilha) == 0


def achilles_and_turtle_print():
    # speed in m/s
    turtle_speed = 3
    achilles_speed = 6

    # position in meters
    turtle_pos = 6
    achilles_pos = 0

    print(f'TURTLE SPEED: {turtle_speed} m/s')
    print(f'ACHILLES SPEED: {achilles_speed} m/s')

    print('--------------------------------')
    print('--------------------------------')

    prev_timestamp = 0

    for timestamp in [0, 1, 1.5, 1.6, 1.7, 1.8, 1.9, 1.99]:
        turtle_pos += turtle_speed * (timestamp - prev_timestamp)
        achilles_pos += achilles_speed * (timestamp - prev_timestamp)

        print(f'Time: {timestamp} second(s)')
        print(f'Turtle position: {round(turtle_pos, 2)} m.')
        print(f'Achilles position: {round(achilles_pos, 2)} m.')
        print('--------------------------------')

        time.sleep(0.5)
        prev_timestamp = timestamp
