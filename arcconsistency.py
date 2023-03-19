import itertools
from csp_check import getCspCheck, setCspCheck


def filterdomains(givenTiles, tiles, targets):
    targets = [targets['1'], targets['2'], targets['3'], targets['4']]
    locationCount = len(tiles)

    elCombinationsCount = getCombinationsCount(locationCount, givenTiles, 'EL_SHAPE')
    outerCombinationsCounts = getCombinationsCount(locationCount, givenTiles, 'OUTER_BOUNDARY')

    combos = {'EL_SHAPE': itertools.combinations(range(locationCount), givenTiles['EL_SHAPE']),
              'OUTER_BOUNDARY': itertools.combinations(range(locationCount), givenTiles['OUTER_BOUNDARY'])}
    mrv = getMrv(elCombinationsCount, outerCombinationsCounts)
    validMrv = startForwardCheck(combos[mrv[0]], tiles, [], targets, mrv[0], False)
    orderLcv(validMrv)
    return enforceConsistency(combos, targets, validMrv, mrv, tiles)


def enforceConsistency(combos, targets, validMrv, mrv, tiles):
    mrv2Combinations = list(combos[mrv[1]])
    for validLcvCombinations in validMrv:
        updatedTarget = [targets[0] - validLcvCombinations[1][0], targets[1] - validLcvCombinations[1][1],
                         targets[2] - validLcvCombinations[1][2], targets[3] - validLcvCombinations[1][3]]
        valid_full_combos = startForwardCheck(mrv2Combinations, tiles, validLcvCombinations[0], updatedTarget,
                                              mrv[1], True)
        if getCspCheck():
            print("Solution:")

            # Order Matters for Print function
            if mrv[0] == 'EL_SHAPE':
                return [valid_full_combos, validLcvCombinations[0]]
            else:
                return [validLcvCombinations[0], valid_full_combos]
    return False


def getCombinationsCount(locationCount, givenTiles, type):
    combinations = itertools.combinations(range(locationCount), givenTiles[type])
    combo_counts = sum(1 for ignore in combinations)
    return combo_counts


def getMrv(elCombinationCounts, outerCombinationCounts):
    mrv = None
    if elCombinationCounts > outerCombinationCounts:
        mrv = ['OUTER_BOUNDARY', 'EL_SHAPE']
    else:
        mrv = ['EL_SHAPE', 'OUTER_BOUNDARY']

    return mrv


def startForwardCheck(combos, tiles, reservedTiles, targets, type, last_var):
    valid_combos = []
    for combinations in combos:
        overlap = False
        for element in combinations:
            if element in reservedTiles:
                overlap = True
                break

        if not overlap:
            current = forwardCheck(combinations, tiles, targets, type, last_var)
            if getCspCheck():
                return combinations
            elif current != -1:
                minConstraints = min([targets[0] - current[0], targets[1] - current[1], targets[2] - current[2],
                                      targets[3] - current[3]])
                valid_combos.append([combinations, current, minConstraints])

    return valid_combos


def forwardCheck(combo, tiles, targets, type, last_var):
    current = [0, 0, 0, 0]
    for location in combo:
        if type == 'EL_SHAPE':
            current[0] += tiles[location].el['ones']
            current[1] += tiles[location].el['twos']
            current[2] += tiles[location].el['threes']
            current[3] += tiles[location].el['fours']
        else:
            current[0] += tiles[location].outer['ones']
            current[1] += tiles[location].outer['twos']
            current[2] += tiles[location].outer['threes']
            current[3] += tiles[location].outer['fours']

    if last_var and constraintSatisfied(current, targets):
        setCspCheck(True)
        return current
    elif constraintNotViolated(current, targets):
        return current
    else:
        return -1


def constraintSatisfied(current, targets):
    if current[0] == targets[0] and current[1] == targets[1] and current[2] == targets[2] and current[3] == targets[3]:
        return True
    else:
        return False


def constraintNotViolated(current, targets):
    if current[0] <= targets[0] and current[1] <= targets[1] and current[2] <= targets[2] and current[3] <= targets[3]:
        return True
    else:
        return False


def orderLcv(combinations):
    combinations.sort(key=lambda k: k[2], reverse=True)
