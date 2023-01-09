redShirtSpeeds = [5,5,3,9,2]
blueShirtSpeeds = [3,6,7,2,1]
fastest = False

#Fastest = False will be 25
#Fastest = True will be 32

def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    redShirtSpeeds.sort(reverse=True)
    speed = 0
    count = 0
    for idx, _ in enumerate(redShirtSpeeds):
        if fastest == False:
            blueShirtSpeeds.sort(reverse=True)
            count = max(redShirtSpeeds[idx],blueShirtSpeeds[idx])
            speed += count
        else:
            blueShirtSpeeds.sort(reverse=False)
            count = max(redShirtSpeeds[idx],blueShirtSpeeds[idx])
            speed += count
    return speed

print(tandemBicycle(redShirtSpeeds,blueShirtSpeeds,fastest))