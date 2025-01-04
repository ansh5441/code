package s50

import (
	"math"
)

func Sol12() int {
	var divisors []int
	var num int
	for numDivisors, i := 0, 12374; numDivisors <= 500; i++ {
		sm := (i * (i + 1)) / 2
		divisors = ListDivisors(sm)
		numDivisors = len(divisors)
		num = sm
	}

	return num
}

func ListDivisors(n int) []int {
	lim := int(math.Sqrt(float64(n)))
	divisors := []int{1}
	for i := 2; i < lim; i++ {
		if n%i == 0 {
			divisors = append(divisors, i)
		}
	}
	lenDivisors := len(divisors)
	if n%lim == 0 && lim > 1 {
		divisors = append(divisors, lim)
	}
	for i := lenDivisors - 1; i > -1; i-- {
		divisors = append(divisors, n/divisors[i])
	}
	return divisors
}
