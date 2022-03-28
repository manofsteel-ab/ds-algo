class InterSectionOfList:

    def using_hash(self, A, B):
        hashMap = {}

        temp = A
        while temp:
            hashMap[temp] = 1
            temp = temp.next
        temp = B
        while temp:
            if temp in hashMap:
                return temp
            temp = temp.next
        return None

    def _list_len(self, head):
        cnt = 0
        temp = head
        while temp:
            cnt +=1
            temp = temp.next
        return cnt

    def without_hash(self, a, b):
        l1 = self._list_len(a)
        l2 = self._list_len(b)

        if l1 == 0 or l2 == 0:
            return None

        if l1-l2 >= 0:
            diff = l1-l2
            while diff > 0:
                a = a.next
                diff -= 1
        else:
            diff = l2 - l1
            while diff > 0:
                b = b.next
                diff -= 1

        while a and b and a != b:
            a = a.next
            b = b.next
        if a == b:
            return a
        return None