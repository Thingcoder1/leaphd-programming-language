package toolchain

import (
	//"fmt"
	"strconv"
)

type operation struct {
	operand string
	val1    string
	val2    string
	outType string
}

type function struct {
	funcname   string
	inputs     []string
	outputs    []string
	operations [][]operation
}

// Parse parses the token list from lexer
func Parse(tokenList []string) {
	progLines := [][]string{}
	//variables := [][]string{}
	tempLine := []string{}
	//tempVar := []string{}
	strCount := 0
	parenCount := 0
	for i := range tokenList {
		tempToken := tokenList[i]
		if tempToken == "\n" {
			progLines = append(progLines, tempLine)
		} else if tempToken == "\"" {
			strCount = (strCount + 1) % 2
		} else if tempToken == "{}[]()" {
			parenCount = (parenCount + 1) % 2
		} else {
			_, err := strconv.Atoi(tempToken)
			if err != nil && strCount != 1 && parenCount != 1 {

			}
		}
	}
}
