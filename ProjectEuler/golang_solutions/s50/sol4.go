package s50

import (
	"fmt"
	"sort"
)

func Sol4() int {
	var firstNum int
	var secondNum int
	palindromes := []int{} // Initialize palindromes as an empty slice of integers
	for firstNum = 999; firstNum > 0; firstNum-- {
		for secondNum = 999; secondNum > 0; secondNum-- {
			if IsPalindrome(firstNum * secondNum) {
				palindromes = append(palindromes, firstNum*secondNum)
			}
		}

	}
	sort.Ints(palindromes) // Sort the palindromes slice
	return palindromes[len(palindromes)-1]

}

func IsPalindrome(n int) bool {
	numString := fmt.Sprint(n)
	lenNumString := len(numString)
	leftIndex := 0
	rightIndex := lenNumString - 1
	for leftIndex <= rightIndex {
		if numString[leftIndex] != numString[rightIndex] {
			return false
		}
		leftIndex += 1
		rightIndex -= 1
	}
	return true

}
