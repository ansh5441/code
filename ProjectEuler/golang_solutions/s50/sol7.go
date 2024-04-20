package s50

func Sol7() int {
	// what is the 10001st prime number?
	var primes []int
	primes = append(primes, 2)
	var i int = 3
	for len(primes) < 10001 {
		var isPrime bool = true
		for _, prime := range primes {
			if i%prime == 0 {
				isPrime = false
				break
			}
		}
		if isPrime {
			primes = append(primes, i)
		}
		i++
	}
	return primes[len(primes)-1]
}
