n = int(input())
arr = map(int, input().split())
arr = list(arr)

# We start by assigning same score arr[0] to both winner and runnerup

winner = arr[0]
runnerup = arr[0]

for i in range(n):
    # As runnerup value should always be lesser than winner value, there is no if condition with runnerup > winner

    if winner == runnerup:
        # If both winner and runner code are equal, as they are in the beginning of the program, check if the current score is greater than existing winner score, if yes, replace the existing winner score with current score
        if arr[i] > winner:
            winner = arr[i]

        # As both winner and runnerup score are equal initially, so this elif condition can be written with respect to any of them, if the current score is lesser than the winner score, then replace existing runner up score with the current score
        elif arr[i] < winner:
            runnerup = arr[i]

        # In all other cases for winner == runnerup , that is as only one case remains, where current score is equal to both runnerup and winner score, we can simply continue the loop with continue or pass statement
        else:
            continue
    if winner > runnerup:
        # If the current score is both greater than winner and runnerup, assign previous winner code to runner code and assign current score to new winner code
        if arr[i] > winner:
            runnerup = winner
            winner = arr[i]
        # If the current score lies between runner score and winner score, only assign current score as new runner score as current score is greater than previous runner code
        elif arr[i] > runnerup and arr[i] < winner:
            runnerup = arr[i]

        # In all other cases, that is when arr[i] is equal to either winner score or runnerup score, we continue without changing the values of any of them, while if arr[i] is smaller than both winner and runnerup, we also let the loop continue
        else:
            continue

# At the end, we print the runnerup value
print(runnerup)
