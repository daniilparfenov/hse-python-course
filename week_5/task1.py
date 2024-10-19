"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/subdomain-visit-count/description
"""  # noqa: E501


class Solution:
    def subdomainVisits(self, cpdomains: list[str]) -> list[str]:
        domainsFreq = dict()
        for domainPair in cpdomains:
            domainPairSplitted = domainPair.split()
            freq = int(domainPairSplitted[0])
            domain = domainPairSplitted[1]
            domainSplitted = domain.split(".")[::-1]

            for i in range(1, len(domainSplitted) + 1):
                subDomain = []
                while len(subDomain) != i:
                    subDomain.append(domainSplitted[len(subDomain)])
                subDomain = ".".join(subDomain[::-1])
                if domainsFreq.get(subDomain):
                    domainsFreq[subDomain] += freq
                else:
                    domainsFreq[subDomain] = freq

        ans = []
        for key in domainsFreq:
            ans.append(" ".join((str(domainsFreq[key]), key)))
        return ans
