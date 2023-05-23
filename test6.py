import math

def constructRectangle(area):
        L = W = int(round(math.sqrt(area)))
        print(L,W)
        while L*W != area:
            if L*W < area:
                L += 1
            else:
                W -= 1
        return [L,W]
if __name__=="__main__":
    area=37
    print(constructRectangle(area))