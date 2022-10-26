import random

random.seed(2)
items = ["A", "B", "C", "D", "E"]
next_item_prob = { items[i]:{ items[k]:random.random() for k in range(len(items)) if i != k } for i in range(len(items))}
num_transactions = 100
end_transaction_p = 0.25

def P(p):
    return True if random.random() < p else False

def gen_transaction():
    global items, next_item_prob, end_transaction_p
    # print(next_item_prob)
    # Pick a random item to start with.
    items_left = {item for item in items}
    initial_item = random.choice(items)
    items_chosen = [initial_item]
    items_left.remove(initial_item)
    while len(items_left) > 0:
        if P(end_transaction_p):
            break
        prev_choice = items_chosen[-1]
        next_choices = [item for item in items_left]
        weights = [next_item_prob[prev_choice][item] for item in next_choices]
        next_choice = random.choices(next_choices, weights)[0]
        items_chosen.append(next_choice)
        items_left.remove(next_choice)
    return items_chosen

def main():
    transactions = [gen_transaction() for _ in range(num_transactions)]
    lines = [",".join(transaction) for transaction in transactions]
    with open("transactions.dat", "w") as fp:
        fp.write("# Each line represents an individual transaction\n")
        fp.write("\n".join(lines))

if __name__ == "__main__":
    main()