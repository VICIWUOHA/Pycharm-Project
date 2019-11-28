
import pandas as pd

excel = pd.ExcelFile('Food_Security.xlsx')
Food_Security_data = excel.parse('CoffeeConsumption')
Food_Security_data_1 = excel.parse('FoodSecurity1')
Food_Security_data_2 = excel.parse('FoodSecurity2')
Food_Security_data_3 = excel.parse('Food Security 3')
Food_Security_data_4 = excel.parse('Food Security 4')
Food_Security_data_5 = excel.parse('Food Security 5')
Food_Security_data_6 = excel.parse('Food Security 6')
Food_Security_data_7 = excel.parse('Food Security 7')
Food_Security_data_8 = excel.parse('Food Security 8')
Food_Security_data_9 = excel.parse('Food Security 9')

print(Food_Security_data)
print(Food_Security_data_1)
print(Food_Security_data_2)
print(Food_Security_data_3)
print(Food_Security_data_4)
print(Food_Security_data_5)
print(Food_Security_data_6)
print(Food_Security_data_7)
print(Food_Security_data_8)
print(Food_Security_data_9)


Food_Security_data.to_csv('Food_Security_data.csv', sep=',')
Food_Security_data_1.to_csv('Food_Security_data_1.csv', sep=',')
Food_Security_data_2.to_csv('Food_Security_data_2.csv', sep=',')
Food_Security_data_3.to_csv('Food_Security_data_3.csv', sep=',')
Food_Security_data_4.to_csv('Food_Security_data_4.csv', sep=',')
Food_Security_data_5.to_csv('Food_Security_data_5.csv', sep=',')
Food_Security_data_6.to_csv('Food_Security_data_6.csv', sep=',')
Food_Security_data_7.to_csv('Food_Security_data_7.csv', sep=',')
Food_Security_data_8.to_csv('Food_Security_data_8.csv', sep=',')
Food_Security_data_9.to_csv('Food_Security_data_9.csv', sep=',')








