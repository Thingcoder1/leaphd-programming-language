package lexer

import (
	"io/ioutil"
	"strings"
)

// Lex lexes the file into tokes for the parser
func Lex(pathToFile string) []string {
	// reads the file
	data, err := ioutil.ReadFile(pathToFile)
	// if there is an error, REPORT!
	if err != nil {
		panic(err)
	}
	// makes the list
	tokenList := make([]string, 0, len(data))

	// makes the string
	var charString string

	// for loop to append the characters of the file to the list
	for i := 0; i <= len(data)-1; i++ {

		// temporarily stores the character into this value and converts it into a string
		tempChar := string(data[i])

		// checks if tempvar is a separater
		// if it isn't append the character to the string
		if strings.ContainsAny(tempChar, " ()[]{}") != true {
			charString = charString + tempChar
			// if it is, don't and set charString to blank value
		} else if tempChar == " " {
			tokenList = append(tokenList, charString)
			charString = ""
		} else if strings.ContainsAny(tempChar, "()[]{}") {
			if charString != "" {
				tokenList = append(tokenList, charString)
				tokenList = append(tokenList, tempChar)
				charString = ""
			} else {
				tokenList = append(tokenList, tempChar)
			}
		}
		// makes sure that if the end of the file is reached, it appends charString
		if i == len(data)-1 {
			tokenList = append(tokenList, charString)
		}

		// while appending, converts the datatype to string instead of byte
		// charList = append(charList, string(data[i]))
	}

	return tokenList
}
