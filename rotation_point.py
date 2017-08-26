"""Find the rotation point of a sorted list"""

def rotation_point(values):
    if values[0] < values[-1]:
        return 0
    left = 0
    right = len(values) - 1
    mid = right / 2
    while right - left > 1:
        print(left, mid, right)
        if values[mid] < values[left]:
            right = mid
        else:
            left = mid
        mid = (left + right) / 2

    if values[right] < values[left]:
        return right
    else:
        return left

print(rotation_point(['ptolemaic',
    'retrograde',
    'supplant',
    'undulate',
    'xenoepist',
    'asymptote', # <-- rotates here!
    'babka',
    'banoffee',
    'engender',
    'karpatka',
    'othellolagkage',]))
print(rotation_point(['asymptote', # <-- rotates here!
    'babka',
    'banoffee',
    'engender',
    'karpatka',
    'othellolagkage',
    'ptolemaic',
    'retrograde',
    'supplant',
    'undulate',
    'xenoepist']))
print(rotation_point([
    'babka',
    'banoffee',
    'engender',
    'karpatka',
    'othellolagkage',
    'ptolemaic',
    'retrograde',
    'supplant',
    'undulate',
    'xenoepist',
    'asymptote']))
print(rotation_point(['undulate',
    'xenoepist',
    'asymptote', # <-- rotates here!
    'babka',
    'banoffee',
    'engender',
    'karpatka',
    'othellolagkage',
    'ptolemaic',
    'retrograde',
    'supplant',]))