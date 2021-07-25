print('Number of children?')
ile = int(input())
print('Income per member?')
income_percapita = int(input())
plus = 200
if income_percapita <= 500:
    print(f'Total children benefit: {plus*(ile)}')
elif income_percapita > 800:
    print(f'Total children benefit: {plus*(ile-1)}')   
else:
    print('Handicapped?')
    incapacitation = input().lower()
    if incapacitation == 'yes' or income_percapita <= 800:
        print(f'Total children benefit: {plus*(ile)}')
 
