
# ==================== map on list ============================
numbers_list = [36 , 67 , 74 , 56 , 40 ,68 , 87]

double_it = lambda x : 2*x
doubles_list = map(double_it,numbers_list)
print(list(doubles_list))

squred_num = map(lambda x : x*x , numbers_list)
print(list(squred_num))