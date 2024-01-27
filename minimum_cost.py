import heapq

def minimum_cost(cables):
    # Convert cables to heap
    heapq.heapify(cables)
    
    total_cost = 0
   
    while len(cables) > 1:
        # Pop the two smallest cables
        cable_1 = heapq.heappop(cables)
        cable_2 = heapq.heappop(cables)
        
        combined_cabels = cable_1 + cable_2
        total_cost += combined_cabels
        
        # Push the combined cable back into the heap
        heapq.heappush(cables, combined_cabels)
    
    return total_cost

cables = [5, 9, 1, 2, 4, 3]
min_cost = minimum_cost(cables)
print(f"\nMinimum cost: {min_cost}\n")
