class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        #if we sort the tickets initially, out adj list will also be sorted (for the lexographical order thing)
        adj = {src:[] for src, dest in tickets}
        tickets.sort()
        for src, dest in tickets:
            adj[src].append(dest)
                
        flight_path = ["JFK"]
        #start at JFK
        def dfs(src):
            #if the len of result is 1 more than the tickets, it means we covered all cities
            #2 tickets would max lead to 3 cities if they are connected as a trip, 4 tickets 5 cities
            #so base positive case
            if len(flight_path) == len(tickets) + 1:
                return True
            #there is also a case where we will not have a valid path, the case where above true is not met
            #but we have no more path to go from, i.e this src will not be a key in adj list
            #so base negative case
            if src not in adj:
                return False

            #we not want to keep updating the adj as we traverse the destinations from src
            #so we must not loop on a list which we want to iterate over so, we create a temp to iterate on

            temp = list(adj[src]) #a copy created

            for i, v in enumerate(temp):
                #since already sorted, we just add them to result and pop them from adj
                flight_path.append(v)
                adj[src].pop(i)

                #then we further dfs on this v and also make sure that we handle its outcome
                if dfs(v):
                    return True
                #if not true means, we need to backtrack for any alt path
                #insert back in adj
                adj[src].insert(i,v)
                #update the result
                flight_path.pop()
            
            #if none of the dest from here give a valid path, we return False
            return False
        
        #we call this dfs from JFK
        dfs("JFK")
        return flight_path


        