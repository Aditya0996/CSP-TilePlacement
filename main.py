import ReadFile
import arcconsistency
from output import getoutput


def getResult(file):
    landscape = ReadFile.getlandscape(file)
    givenTiles = ReadFile.gettiles(file)
    target = ReadFile.getTargets(file)
    tiles = ReadFile.tiles(landscape)
    result = arcconsistency.filterdomains(givenTiles, tiles, target)
    if not result:
        print("No Solution")
        return False
    else:
        getoutput(result, len(landscape[0]), len(tiles))
        return True


def main():
    print("Reading File")
    testFile = "test/test1.txt"
    print("Starting ArcConsistency")
    getResult(testFile)


if __name__ == '__main__':
    main()
