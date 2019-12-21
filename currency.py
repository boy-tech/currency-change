USD_vs_RMB = 6.77
currency_str_value = input('请输入带单位的货币人民币（CNY）美元（USD）（请输入Q退出）：')
count = 0
while currency_str_value != 'Q':
	count += 1
	print('第{}转换'.format(count))
	uint = currency_str_value[-3:] 
	if uint == 'CNY':
		rmb_str_value = currency_str_value[:-3]
		rmb_value = eval(rmb_str_value)
		usd_value = rmb_value / USD_vs_RMB
		print('对应的美元金额为:',usd_value)
	elif uint == 'USD':
		usd_str_value = currency_str_value[:-3]
		usd_value = eval(usd_str_value)
		rmb_value = usd_value * USD_vs_RMB
		print('对应的人民币金额为:',rmb_value)
	else:
		print("暂不支持此数据类型")
	
	print('*******************************************************************************')

	currency_str_value = input('请输入带单位的货币人民币（CNY）美元（USD）（请输入Q退出）：')

print('程序已退出')
