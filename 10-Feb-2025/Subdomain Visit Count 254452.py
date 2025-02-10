# Problem: Subdomain Visit Count - https://leetcode.com/problems/subdomain-visit-count

class Solution(object):
    def subdomainVisits(self, cpdomains):
        count_dict = {}
        
        for entry in cpdomains:
            count, domain = entry.split()
            count = int(count)
            subdomains = domain.split('.')

            for i in range(len(subdomains)):
                subdomain = '.'.join(subdomains[i:])
                if subdomain in count_dict:
                    count_dict[subdomain] += count
                else:
                    count_dict[subdomain] = count
        result = []
        for domain, count in count_dict.items():
            result.append(str(count) + " " + domain)

        return result
        