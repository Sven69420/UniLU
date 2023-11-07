#tp4 "Recursion"
def sum_series(n):
    """Function to calculate recursive sum"""
    if n == 1:
        return 1
    return sum_series(n - 1) + n
print(sum_series(1)) #should return 1
print(sum_series(5)) #should retrun 15


def is_magic_sequence(s):
    """Function to check if given sequence is a magic sequence"""
    if len(s) == 0:
        return True
    return abs(s[0]) == abs(s[-1]) and is_magic_sequence(s[-1:1])

print(is_magic_sequence([-1, -2, 0, 2, 1])) #should return True
print(is_magic_sequence([1, -2, 0, 2, 3])) #should return False
print(is_magic_sequence([-1, 1])) #should return True
print(is_magic_sequence([1])) #should return True
print(is_magic_sequence([])) #should return True