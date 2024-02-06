#!/usr/bin/env python3

import random


def main(difficulty: int = 1):
    health = 49
    potion_health = int(random.randint(24, 50) / difficulty)
    health += potion_health
    return health


if __name__ == "__main__":
    print(main())
