package task278

/**
 * Forward declaration of isBadVersion API.
 * @param   version   your guess about first bad version
 * @return 	 	      true if current version is bad
 *			          false if current version is good
 * func isBadVersion(version int) bool;
 */

func firstBadVersionClosure(n, v int) int {
	isBadVersion := func(version int) bool {
		return version >= v
	}

	//binary search
	firstBadVersion := func(n int) int {
		left, right := 0, n
		for left <= right {
			// mid := (left + right) >> 1
			mid := left + (right-left)>>1
			if isBadVersion(mid) {
				right = mid - 1
			} else {
				left = mid + 1
			}
		}
		return left
	}

	return firstBadVersion(n)
}
