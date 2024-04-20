package s50

func Sol5() int {
	var n int = 1
	for i := 2; i <= 20; i++ {
		n = lcm(n, i)
	}
	return n
}

func lcm(a, b int) int {
	return a * b / gcd(a, b)
}

func gcd(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}
