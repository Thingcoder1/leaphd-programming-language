package toolchain

type lexer struct {
	input        string
	currentToken string
	lexemes      []string
}

func Lex(in string) {
	Lexer := lexer{
		input:        in,
		currentToken: "",
		lexemes:      []string{},
	}
	for charNum := range Lexer.input {
		char := string(Lexer.input[charNum])
		print(char, "\n")
	}
}
