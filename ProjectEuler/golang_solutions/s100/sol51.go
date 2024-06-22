package s100

import (
	"fmt"
	"golang_solutions/s50"
	"time"
)

func Sol51() int {
	start := time.Now()
	primes := s50.ListPrimes(10000000)
	end := time.Now()
	fmt.Println(end.Sub(start))
	return primes[len(primes)-1]
}
