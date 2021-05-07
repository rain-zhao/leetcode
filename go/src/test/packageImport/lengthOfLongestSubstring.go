package packageImport

func LengthOfLongestSubstring(s string) int {
	if len(s) == 0 {
		return 0
	}
	appear := make(map[rune]int)
	left := -1
	res := 0
	for right, c := range s {
		if p, ok := appear[c]; ok {
			if left < p {
				left = p
			}
		}
		appear[c] = right
		if l := right - left; l > res {
			res = l
		}
	}
	return res
}
