from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        container = set()
        for mail in emails:
            acutal = []
            pos = mail.find('@')
            for i in mail[:pos]:
                if i == '.':
                    continue
                elif i == '+':
                    break
                else:
                    acutal.append(i)
            container.add(''.join(acutal)+mail[pos:])
        return len(container)

    def numUniqueEmails2(self, emails: List[str]) -> int:
        container = set()
        for mail in emails:
            addr, domain = mail.split('@')
            addr = addr[:addr.find('+')] if addr.find('+') != -1 else addr
            container.add(addr.replace('.', '')+domain)
        return len(container)


emails = ["test.email+alex@leetcode.com", "test.email@leetcode.com"]

so = Solution()
print(so.numUniqueEmails2(emails))
