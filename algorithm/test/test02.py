#!/usr/bin/env python
# coding: utf-8

# # 코딩테스트 문제2번

# In[80]:


def solution(v1, v2, a, b):  
    '''        
        @test question : a와 b 친구 맺어줄 a,b 친구를 동시에 아는 지인 구하기! 
        @test point : a와 b를 동시에 아는 지인 구하기, 지인은 친구의 수가 가장 적다.
        @param v1: v1[] a의 친구들 list
        @param v2: v1[] b의 친구들 list
        @param a : b가 만나게 될 친구 0 ≤ a ≤ 1,000
        @param b : a가 만나고 싶은 친구 0 ≤ b ≤ 1,000
        return answer: answer 아는 지인 아이디, int형 
    '''    
        
    # 변수 초기화 및 선언
    answer = -2;
    friends = [];    
    a_friends=[];
    b_friends=[];
    sogaeting=[];
    v1_len = len(v1);
    v2_len = len(v2);
    
    # v1, v2 친구 맺기
    for i in range(len(v1)): 
        friends.append([v1[i], v2[i]]);
        
    # a와 b를 동시에 아는 지인 찾기
    for i in range(len(friends)):
        # a를 아는 b의 지인 구하기
        if friends[i][0] == a: a_friends.append(friends[i][1]);

        # b를 아는 a의 지인 구하기
        if friends[i][1] == b: b_friends.append(friends[i][0]);

    a_friends_len = len(a_friends);
    b_friends_len = len(b_friends);

    # 해당 지인이 동일한지 파악
    if a_friends_len > b_friends_len:
        for i in range(a_friends_len):
            for j in range(b_friends_len):
                if a_friends[i] == b_friends[j]: sogaeting.append(a_friends[i])
    else:
        for i in range(b_friends_len):
            for j in range(a_friends_len):
                if b_friends[i] == a_friends[j]: sogaeting.append(b_friends[i])        

    # 동일 친구가 있을 경우 ID값이 작은 친구를 뽑음
    if len(sogaeting) > 0:
        answer = sorted(a_friends)[0];
    else:
        answer = -1;
        
                
    return answer


# In[82]:


print(solution([0, 0, 1, 2, 2], [1, 2, 3, 3, 4], 0, 3));
print(solution([0, 0, 1, 2, 3], [1, 2, 3, 3, 4], 0, 4));
print(solution([998,1000], [1000,999], 998, 999));


# In[83]:


#test case
# print(solution([7,6,8,8,9,10],[10,10,6,9,7,7],8,10))


# In[ ]:




