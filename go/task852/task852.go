package task852

// binary search
func peakIndexInMountainArray(arr []int) int {
	left, right := 1, len(arr)-2
	for left <= right {
		mid := left + (right-left)>>1
		if arr[mid] > arr[mid-1] && arr[mid] > arr[mid+1] {
			return mid
		} else if arr[mid] > arr[mid-1] {
			left = mid + 1
		} else {
			right = mid - 1
		}
	}
	return -1
}
