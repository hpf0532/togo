# from django.test import TestCase
# from rest_framework.views import APIView
# from rest_framework.viewsets import GenericViewSet
# from rest_framework.serializers import Serializer
# # Create your tests here.
# from rest_framework.renderers import JSONRenderer
#
# class Test(APIView):
#     self.dispatch()
#
# # class Test(Serializer):
# #     def haha(self):
# #         pass
#
# if __name__ == '__main__':
#
#     import time
#
#     start_time = time.time()
#
#     # 注意是两重循环
#     for a in range(0, 1001):
#         for b in range(0, 1001 - a):
#             c = 1000 - a - b
#             if a ** 2 + b ** 2 == c ** 2:
#                 print("a, b, c: %d, %d, %d" % (a, b, c))
#
#     end_time = time.time()
#     print("elapsed: %f" % (end_time - start_time))
#     print("complete!")

# class SingleNode():
#     """单向链表节点"""
#     def __init__(self, elem, node=None):
#         self.elem = elem
#         self.next = node
#
#
# class SingleLinkList():
#     def __init__(self, node=None):
#         self.__head = node
#
#     def is_empty(self):
#         return self.__head is None
#
#     def length(self):
#         cur = self.__head
#         count = 0
#         while cur is not None:
#             count += 1
#             cur = cur.next
#
#         return count
#
#     def travel(self):
#         cur = self.__head
#         while cur is not None:
#             print(cur.elem, end=" ")
#             cur = cur.next
#         print("")
#
#
#     def add(self, item):
#         node = SingleNode(item)
#
#         node.next = self.__head
#         self.__head = node
#
#     def append(self, item):
#         node = SingleNode(item)
#         cur = self.__head
#         if self.is_empty():
#             self.__head = node
#             return
#         while cur.next is not None:
#             cur = cur.next
#
#         cur.next = node
#
#     def insert(self, pos, item):
#         node = SingleNode(item)
#
#         if pos <= 0:
#             self.add(item)
#         elif pos > self.length():
#             self.append(item)
#
#         else:
#             pre = None
#             next = self.__head
#             count = 0
#
#             while count != pos:
#                 pre = next
#                 next = next.next
#                 count += 1
#
#             # print(pre.elem, next.elem)
#             node.next = next
#             pre.next = node
#
#     def remove(self, item):
#         pre = None
#         cur = self.__head
#
#         while cur != None:
#             if cur.elem == item:
#                 if not pre:
#                     self.__head = cur.next
#                 else:
#                     pre.next = cur.next
#                 break
#
#             pre = cur
#             cur = cur.next
#
#     def search(self, item):
#         cur = self.__head
#
#         while cur is not None:
#             if cur.elem == item:
#                 return True
#             cur = cur.next
#
#         return False
#
#
#
#
#
#
# ll = SingleLinkList()
# print(ll.length())
# ll.append(1)
# ll.append(2)
# print(ll.length())
# ll.travel()
#
# ll.append(100)
# print(ll.is_empty())
# ll.travel()
#
# ll.add(26)
# ll.add(78)
# ll.travel()
# print(ll.length())
# print(ll.is_empty())
#
# ll.insert(6, 20)
# ll.insert(4, 111)
# ll.travel()
#
# ll.remove(100)
# ll.travel()
#
# print(ll.search(346457))

from django.conf.urls import handler404

from django_gravatar.helpers import get_gravatar_url, has_gravatar, get_gravatar_profile_url, calculate_gravatar_hash
from rest_framework import exceptions
from rest_framework.parsers import JSONParser
url = get_gravatar_url('alice@example.com', size=150)
gravatar_exists = has_gravatar('bob@example.com')
profile_url = get_gravatar_profile_url('alice@example.com')
email_hash = calculate_gravatar_hash('alice@example.com')