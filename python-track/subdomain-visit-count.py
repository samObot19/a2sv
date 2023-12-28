class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domains = defaultdict(lambda: 0)
        for i in cpdomains:
            count_pair = i.split()
            domains[count_pair[1]] += int(count_pair[0])
            sub_domains = count_pair[1].split('.')
            #slicing the sub domain
            for i in range(1, len(sub_domains)):
                val = ".".join(sub_domains[i:])
                domains[val] += int(count_pair[0])
                
                
        out_put = []
        for keys, values in domains.items():
            out_put.append(str(values) + " " + str(keys))
            
        return out_put
            
            
        