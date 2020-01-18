@outputSchema( 'a:double' )

def calc_hr_percent(g, hr):
	# check that each value is not None
	if not hr:
		hr = 0.0
	if not g:
		return 0.0

	return 1.0*hr/g

if __name__=='__main__':
	print(calc_hr_percent(3,4))
