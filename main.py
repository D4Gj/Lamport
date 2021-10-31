"""Illustrating Lamport's Logical Clock
 in function of finding the maximum timestamp between 2 events"""


def max1(a, b):
    # Simple max between 2 values
    if a > b:
        return a
    else:
        return b


# Display timestamp
def display(e1, e2, p1, p2):
    print()
    print("The time stamps of events in P1:")
    for i in range(0, e1):
        print(p1[i], end=" ")

    print()
    print("The time stamps of events in P2:")

    # Print the array p2[]
    for i in range(0, e2):
        print(p2[i], end=" ")


# Find timestamp
def lamportLogicalClock(e1, e2, m):
    p1 = [0] * e1
    p2 = [0] * e2

    # Initialize p1[] and p2[]
    for i in range(0, e1):
        p1[i] = i + 1

    for i in range(0, e2):
        p2[i] = i + 1

    for i in range(0, e2):
        print(end='\t')
        print("e2", end="")
        print(i + 1, end="")

    for i in range(0, e1):
        print()
        print("e1", end="")
        print(i + 1, end="\t")

        for j in range(0, e2):
            print(m[i][j], end="\t")

    for i in range(0, e1):

        for j in range(0, e2):

            # Change the timestamp if the
            # message is sent
            if (m[i][j] == 1):
                p2[j] = max1(p2[j], p1[i] + 1)
                for i in range(j + 1, e2):
                    p2[k] = p2[k - 1] + 1

            # Change the timestamp if the
            # message is received
            if (m[i][j] == -1):
                p1[i] = max1(p1[i], p2[j] + 1)
                for k in range(i + 1, e1):
                    p1[k] = p1[k - 1] + 1

    display(e1, e2, p1, p2)


if __name__ == "__main__":
    e1 = 5
    e2 = 3
    m = [[0] * 3 for i in range(0, 5)]

    # dep[i][j] = 1, if message is sent
    # from ei to ej
    # dep[i][j] = -1, if message is received
    # by ei from ej
    # dep[i][j] = 0, otherwise

    m[0][0] = 0
    m[0][1] = 0
    m[0][2] = 0
    m[1][0] = 0
    m[1][1] = 0
    m[1][2] = 1
    m[2][0] = 0
    m[2][1] = 0
    m[2][2] = 0
    m[3][0] = 0
    m[3][1] = 0
    m[3][2] = 0
    m[4][0] = 0
    m[4][1] = -1
    m[4][2] = 0

    lamportLogicalClock(e1, e2, m)
