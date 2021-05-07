package test

import (
	"test/packageImport"
	"testing"
)

func TestPackageImport(t *testing.T) {
	t.Log(packageImport.LengthOfLongestSubstring("abcabcbb"))
}
