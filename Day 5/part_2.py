with open("input.txt") as input:
    lines = input.readlines()
    seeds = [int(x) for x in lines[0].split(":")[1].strip().split(" ")]
    seed_ranges = [[seeds[i-1], seeds[i]] for i in range(len(seeds)) if i % 2 != 0]
    changed = {}
    for j in range(len(seed_ranges)):
        changed[j] = False

    for i in range(2, len(lines)):
        if not lines[i][0].isdigit():
            for j in range(len(seed_ranges)):
                changed[j] = False
        if lines[i][0].isdigit():
            nums = [int(x) for x in lines[i].strip().split(" ")]
            min_map_range = nums[1]
            max_map_range = nums[1] + nums[2]
            delta = nums[0] - nums[1]

            for index, r in enumerate(seed_ranges):
                seed = r[0]
                val = r[1]

                # Right Overlap
                if min_map_range < seed < max_map_range < seed + val and not changed[index]:
                    start = seed + delta
                    values = max_map_range - seed
                    new_s = nums[1] + nums[2]
                    new_v = val - values
                    seed = start
                    val = values
                    seed_ranges.append([new_s, new_v])
                    changed[index] = True
                    changed[len(seed_ranges) - 1] = False

                # Left overlap
                elif seed < min_map_range < seed + val < max_map_range and not changed[index]:
                    start = nums[1] + delta
                    values = seed + val - nums[1]
                    new_s = seed
                    new_v = val - values
                    seed = start
                    val = values
                    seed_ranges.append([new_s, new_v])
                    changed[index] = True
                    changed[len(seed_ranges) - 1] = False

                # Full overlap
                elif min_map_range <= seed < seed + val <= max_map_range and not changed[index]:
                    seed = seed + delta
                    changed[index] = True

                # Overflow overlap
                elif seed < min_map_range and seed + val > max_map_range and not changed[index]:
                    s1 = seed
                    v1 = nums[1] - seed
                    s2 = nums[1] + nums[2]
                    v2 = seed + val - nums[1] + nums[2]
                    seed_ranges.append([s1, v1])
                    changed[len(seed_ranges) - 1] = False
                    seed_ranges.append([s2, v2])
                    changed[len(seed_ranges) - 1] = False
                    seed = seed + delta
                    val = val - v1 - v2
                    changed[index] = True

                r[0] = seed
                r[1] = val
locations = []
[locations.append(x[0]) for x in seed_ranges]
print(min(locations))
