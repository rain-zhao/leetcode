package task1310

func xorQueries(arr []int, queries [][]int) []int {
	xors := make([]int, len(arr)+1)
	for i, num := range arr {
		xors[i+1] = xors[i] ^ num
	}
	res := make([]int, len(queries))
	for i, query := range queries {
		res[i] = xors[query[1]+1] ^ xors[query[0]]
	}
	return res
}
