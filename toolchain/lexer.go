package toolchain

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

	// makes the string that holds the tokens
	var charString string

	// for loop to append the characters of the file to the list of tokens
	for i := 0; i <= len(data)-1; i++ {

		// temporarily stores the character into this value and converts it into a string
		tempChar := string(data[i])

		// checks if tempvar is a separator
		// if it isn't append the character to the string
		if strings.ContainsAny(tempChar, " ()[]{}~!@#$%^&*-=_+|\\?/><,.:;\n") != true {
			if strings.ContainsAny(charString, "~!@#$%^&*-=_+|\\?/><,.:;\n") {
				tokenList = append(tokenList, charString)
				charString = ""
				charString = charString + tempChar
			} else if strings.ContainsAny(charString, "~!@#$%^&*-=_+|\\?/><,.:;\n") != true {
				charString = charString + tempChar
			}
			// if it is a space, don't and set charString to blank value
		} else if tempChar == " " {
			if charString != "" {
				tokenList = append(tokenList, charString)
				charString = ""
			}
			// if it is a separater, append the string, then separator, then make charString = ""
		} else if strings.ContainsAny(tempChar, "()[]{}") {
			if charString != "" {
				tokenList = append(tokenList, charString)
				tokenList = append(tokenList, tempChar)
				charString = ""
			} else {
				tokenList = append(tokenList, tempChar)
			}
		} else if strings.ContainsAny(tempChar, "~!@#$%^&*-=_+|\\?/><,.:;\n") {
			if strings.ContainsAny(charString, "~!@#$%^&*-=_+|\\?/><,.:;") {
				charString = charString + tempChar
			} else if strings.ContainsAny(charString, "~!@#$%^&*-=_+|\\?/><,.:;\n") != true {
				if charString != "" {
					tokenList = append(tokenList, charString)
					charString = ""
					charString = charString + tempChar
				} else {
					charString = charString + tempChar
				}

			}
		}
		// makes sure that if the end of the file is reached, it appends charString
		if i == len(data)-1 {
			if charString != "" {
				tokenList = append(tokenList, charString)
			}
		}

		// while appending, converts the datatype to string instead of byte
	}

	return tokenList
}
