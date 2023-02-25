#!/usr/bin/env python
# coding: utf-8

# In[53]:


# Median of Two Sorted Arrays

# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

 

# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.




class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        new_list=nums1+nums2
        new_list_sorted=sorted(new_list)
        n=len(new_list_sorted)
        if len(new_list_sorted)%2==0:
            median=(new_list_sorted[(n//2)-1]+new_list_sorted[n//2])/2
        else:
            median=new_list_sorted[(n//2)]
        return median


# In[50]:





# In[ ]:





# In[ ]:





# In[ ]:




