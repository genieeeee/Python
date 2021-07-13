#!/usr/bin/env python
# coding: utf-8

# # 코딩테스트 문제1번

# In[3]:


import math

def solution(w):
    '''        
        @test question : 토너먼트에서 4강 안에 들어갈 원소의 index 찾기
        @test point : 4강 안에 들어온 원소 최조 배열의 index 알아내기!
        @param w: w[] 토너먼트 list
        return : answer[] 4강 안에 들어온 원소의 idex가 담긴 배열
    '''    
    
    # 변수 초기화 및 선언
    answer = [];     
    error_msg='';
    w_len = len(w)
    
    # w배열 길이의 제약조건
    if ( (w_len >=4 and w_len <= 1024) and (w_len & (w_len-1) == 0) ):
   
        copy_w = [];
        isContinue = True;
        
        # w배열의 index와 value값 [index,value]로 담아서 copy_w 2차배열 만들기
        for w_idx, w_val in enumerate(w):
            
            # 원소값 제약조건
            if w_val <1 or w_val >1000000: 
                isContinue = False;
                break;
            copy_w.append([w_idx,w_val]);
        
        if(isContinue):
            while True:
                for idx, val in enumerate(copy_w):
                    
                    # 토너먼트 경기
                    remove_idx = idx if (copy_w[idx][1] < copy_w[(idx+1)][1]) else idx+1;
                    del copy_w[remove_idx];
                
                # 4강일 때 토너먼트 break
                if len(copy_w)<=4: break; 
            
            # 4강 안에 들어온 원소의 idex, answer 배열에 담아 정렬
            answer = sorted([copy_w[idx][0] for idx, val in enumerate(copy_w)])
            
        else:
            error_msg += '1 ≤ w의 원소 ≤ 1,000,000\n';
                    
    else:
        error_msg += 'w의 길이는 ' + str(w_len) + '입니다.\n'
        error_msg += '4 ≤ w의 길이 ≤ 1,024\n';
        error_msg += 'w의 길이는 2의 거듭제곱입니다. 즉, 4, 8, 16, 32, 64, …, 1024 중 하나입니다.\n';
    
    print(error_msg);
        
    return answer

print('w = [3, 2, 4, 5, 6, 2, 4, 5] / result =  ', solution([3, 2, 4, 5, 6, 2, 4, 5]))
print('w = [3, 2, 4, 5, 6, 2, 4, 5] / result =  ', solution([3, 2, 4, 5, 6, 2, 4, 5, 1, 2, 3, 4, 5, 6, 7, 8]))


# In[ ]:


# 2의 거듭제곱 구하는 방법 : math.log(len(w), 2).is_integer() #math.log(n,2) -> n이 음수일 때 ValueError 발생


# In[ ]:


# test case
# print(solution([9,10,4,8,1,9,15,20,25,30,45,70,80,2,1, 2, 3, 4, 5, 6]))
# print(solution([9,10,4]))
# print(solution([3, 2, 10000000, 5, 6, 2, 4, 5]))
# print(solution([9,10,4,8,1,9,15,20,25,30,45,70,80,2,1, 2, 3, 4, 5, 6, 7, 8,10,22,33,44,55,66,25,67,82,1]))

