from constants import constant

power_number = float(input("Nhập vào số điện nhà bạn sử dụng: "))
result = -1
if power_number < constant.INT_ZERO:
    result = "Số bạn nhập không đúng"
elif constant.INT_ZERO <= power_number < constant.INT_ONE_HUNDRED:
    result = power_number * constant.ELECTRICITY_PRICE_UNDER_100
elif constant.INT_ONE_HUNDRED <= power_number <= constant.INT_THREE_HUNDRED:
    result = constant.INT_ONE_HUNDRED * constant.ELECTRICITY_PRICE_UNDER_100 + (power_number - constant.INT_ONE_HUNDRED) * constant.ELECTRICITY_PRICE_UNDER_300
else:
    result = constant.INT_ONE_HUNDRED * constant.ELECTRICITY_PRICE_UNDER_100 + (constant.INT_THREE_HUNDRED - constant.INT_ONE_HUNDRED) * constant.ELECTRICITY_PRICE_UNDER_300 + (power_number - constant.INT_THREE_HUNDRED) * constant.ELECTRICITY_PRICE_MORE_THAN_300
print(result) if result < constant.INT_ZERO else print(f"Số tiền bạn phải trả là: {result}")