package sudoku

import (
	"math/rand"
	"time"
)

var nums = [9]int{1, 2, 3, 4, 5, 6, 7, 8, 9}

// Generate creates a sudoku puzzle using random values
func Generate(board *[9][9]int) bool {
	if !hasEmptyCell(board) {
		return true
	}
	for i := 0; i < 9; i++ {
		for j := 0; j < 9; j++ {
			if board[i][j] == 0 {
				rand.Seed(time.Now().Unix())
				rand.Shuffle(len(nums), func(i, j int) { nums[i], nums[j] = nums[j], nums[i] })
				for _, candidate := range nums {
					board[i][j] = candidate
					if isBoardValid(board) {
						if Backtrack(board) {
							return true
						}
						board[i][j] = 0
					} else {
						board[i][j] = 0
					}
				}
				return false
			}
		}
	}
	return false
}

// RemoveNumbers erases between 50% and 80% of the numbers to create
// the unsolved grid with a random difficulty.
func RemoveNumbers(b *[9][9]int) {
	r1 := randInt(0, 100) // 0-99
	r2 := randInt(50, 80) // 50-79
	for i := 0; i < 9; i++ {
		for j := 0; j < 9; j++ {
			if r1 < r2 {
				b[i][j] = 0
			}
			r1 = randInt(0, 100)
		}
	}
}

func randInt(min int, max int) int {
	return min + rand.Intn(max-min)
}

func numInSlice(a int, list [9]int) bool {
	for _, b := range list {
		if b == a {
			return true
		}
	}
	return false
}
