"""
220326
*args , **kwargs test
https://eastcold.tistory.com/17에 정리함
"""

def test(person, *enterprise, **countries):
    # 일반 변수
    print("type(person): ", type(person))
    print(person, end="\n\n")

    # args 변수
    print("type(enterprise): ", type(enterprise))
    for name in enterprise:
        print(name)
    print(end="\n")

    # kwargs
    print("type(countries) : ", type(countries))
    for country, continent in countries.items():
        print(f"{country} is in {continent}.")

Korea = 'Korea'
France = 'France'
Rwanda = 'Rwanda'

test('chan',
     'apple', 'samsung', 'lg',
     Korea='Asia', France='Europe', Rwanda='Africa'
     )


