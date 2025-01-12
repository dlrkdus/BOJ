def solution(n, times):
    answer = 0
    left = min(times)
    right = max(times)*n 
    
    while left <= right:
        mid = (right + left) // 2 
        people = 0
        for time in times:
            people += (mid // time)
            if people >= n:
                break
        
        if people >=n :
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return answer 
            
        