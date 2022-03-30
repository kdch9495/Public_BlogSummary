"""
220330
function join test
https://eastcold.tistory.com/18?category=855168에 정리함
"""

def test_join():
    print()

    temp_list = ['Dong', 'Chan', 'Na', 'Ra']
    print("temp_list :", temp_list, "\n")

    result1 = "".join(temp_list)
    print("result1 :", result1, "\n")

    result2 = '구분자'.join(temp_list)
    print("result2 :", result2, "\n")
    print("result2 원상태로 복구 : " , result2.split('구분자'), "\n")

    result3 = "'"+"','".join(temp_list)+"'"
    print("result3 :", result3, "\n")

test_join()

"""
temp_list : ['Dong', 'Chan', 'Na', 'Ra'] 

result1 : DongChanNaRa 

result2 : Dong구분자Chan구분자Na구분자Ra 

result2 원상태로 복구 :  ['Dong', 'Chan', 'Na', 'Ra'] 

result3 : 'Dong','Chan','Na','Ra' 
"""
