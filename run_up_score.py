if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    unique_scores = set(arr)
    if len(unique_scores) <= 1:
        print("There is no runner-up score.")
    else:
        max_score = max(unique_scores)
        unique_scores.remove(max_score)
        runner_up_score = max(unique_scores)
        print(runner_up_score)
