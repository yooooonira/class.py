import math #ceil()필요

user_n=int(input()) #참가자 수 
s,m,l,xl,xxl,xxxl=map(int,input().split()) #사이즈별 신청자 수 
T,P=map(int,input().split()) # 묶음 당 t장으로 구성, 묶음 당 p개로 구성

s_set=math.ceil(s/T)  #부족x 남는건o -> 올림
m_set=math.ceil(m/T)
l_set=math.ceil(l/T)
xl_set=math.ceil(xl/T)
xxl_set=math.ceil(xxl/T)
xxxl_set=math.ceil(xxxl/T)

t_set = s_set+m_set+l_set+xl_set+xxl_set+xxxl_set
print(t_set) #티셔츠 몇 묶음인지. 

p_set=user_n//P
p_one=user_n-(P*p_set) #부족한 걸 충당

print(p_set,p_one)  #펜 몇 묶음인지  #펜 개당은 몇개 필요한지 
