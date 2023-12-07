
seeds = []
locations = []
with open("test.txt") as input:
    lines = input.readlines()
    seeds = [int(x) for x in lines[0].split(":")[1].strip().split(" ")]
    print("SEEDS " + str(seeds))
    for seed in seeds:
        not_changed = True
        print("NEW SEED: ", seed)
        for i in range(2, len(lines)):
            print(seed)
            print(lines[i].strip())
            if not lines[i][0].isdigit():
                not_changed = True
                continue

            if not_changed:
                nums = [int(x) for x in lines[i].strip().split(" ")]
                print(range(nums[1], nums[1] + nums[2]))
                if seed in range(nums[1], nums[1] + nums[2]):
                    seed2 = nums[0] + seed - nums[1]
                    print(seed, " -> ", seed2)
                    seed = seed2
                    not_changed = False

        locations.append(seed)
print(min(locations))
