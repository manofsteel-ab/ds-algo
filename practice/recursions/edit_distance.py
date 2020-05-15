"""
You have given two string source and target. You need to convert soruce string
into target string.

You can acheive this by inserting a char or by deleting a char or by
replacing a char.

Return minimum operation you required to acheive the result.


"""

def editDistance(source, target, m,n): # m soruce string size, n target size
    if m == 0: # need to insert all the char
        return n
    if n == 0: # need to delete all the char
        return m

    if source[m-1] == target[n-1]:
        return editDistance(source, target, m-1, n-1)
    else:
        return 1 + min(
            editDistance(source, target, m-1, n-1), # replace
            editDistance(source, target, m-1, n), # delete
            editDistance(source, target, m, n-1), # insert
        )
str1 = "sunday"
str2 = "saturday"
print editDistance(str1, str2, len(str1), len(str2))

#  Time complexity of above algorithm is O(3^m)
