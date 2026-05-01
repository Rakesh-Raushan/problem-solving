class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        #combined pos and speed array
        position_speed = [(position, speed) for position, speed in zip(position, speed)]
        #order by position in reverse so that we process cars from nearest to target to farthest 
        position_speed.sort(reverse = True)

        #fleet stack, cars taking more time than the one ahead of it stack[-1] get appended to represent a separate fleet
        #while cars taking less time than the one ahead of it stack[-1] would get merged and hence we can skip them from stack
        fleet_stack = []

        for cur_position, cur_speed in position_speed:
            cur_time_to_dest = (target - cur_position)/cur_speed, #float time
            if fleet_stack and cur_time_to_dest <= fleet_stack[-1]:
                #check car ahead of it, (note we just need to check the one ahead of it)
                #taking lesser time, will not add a new fleet so skip
                continue
            #else add it to mark a separate fleet
            fleet_stack.append(cur_time_to_dest)
        #fleet_stack will represent the count of unique fleet
        return len(fleet_stack)
        
        #NOTE it is a simple stack application and not monotonic stack case actually