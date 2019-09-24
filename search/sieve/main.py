# 20190905 potados

# Get list of prime number from range 2(the smallist prime)
# to the end(inclusive).
#
# Performance not considered :)
# That is only to shorten the code.
# Do not do this in production.
#
# @param end the end of prime number range. Inclusive.
#
# @return the prime list.
def sieve(end):
    if end < 2:
        return None

    # The minimum prime number is 2.
    raw = list(range(2, end + 1))

    # We need to kill 2*n, 3*n, 5*n, ... , (end**0.5)*n.
    # There are redundent numbers in this list because thery are not prime.
    # e.g. 4 is redundent because 2 kill all 4*n.
    # They will be filtered by checking if the first multiple(M*1) is killed.
    to_kill = list(range(2, int(end**0.5) + 1))

    # Get set of all multiplied numbers in range from 2 to end,
    # excluding the first object, which is multiplied by 1, the prime number.
    non_prime_set = set([x for inner_range in [range(x, end + 1, x)[1:] for x in to_kill] for x in inner_range])

    # Filter only the prime number
    prime_list = [x for x in raw if x not in non_prime_set]

    return prime_list

N = 50
print(sieve(N))
