package s50

import "math"

func Sol10() int {
	// sum of all primes below 2 million
	primes := ListPrimes(2000000)
	sm := 0
	for _, num := range primes {
		sm += num
	}
	return sm
}

func ListPrimes(limit int) []int {
	primes := []int{}
	numPrimes := 0
	for n := 2; n < limit; n++ {
		isPrime := true
		lim := int(1 + math.Sqrt(float64(n)))

		for i := 0; i < numPrimes && primes[i] < lim; i++ {
			if n%primes[i] == 0 {
				isPrime = false
				break
			}
		}
		if isPrime {
			primes = append(primes, n)
			numPrimes += 1
		}
	}
	return primes
}
