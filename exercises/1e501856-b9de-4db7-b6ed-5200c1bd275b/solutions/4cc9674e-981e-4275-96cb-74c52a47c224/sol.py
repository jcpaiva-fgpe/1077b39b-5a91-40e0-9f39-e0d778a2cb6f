mies = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
print('Date (DD.MM.YYYY)?')
print(mies[int(input().split('.')[1])-1])
