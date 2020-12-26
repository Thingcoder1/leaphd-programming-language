package toolchain

import "fmt"

// ContextState is the state of the context
type ContextState int

const (
	START ContextState = iota
	KEYWORD
)

// Lexer this is the structure of our lexer
type Lexer struct {
	In      chan string
	curChar string
	curCtx  ContextState
}

// NewLexer makes a new Lexer structure
func NewLexer(in chan string) *Lexer {
	return &Lexer{
		In: in,
	}
}

// Run returns the Lexer output
func (lexer *Lexer) Run() {
	for {
		loc := <-lexer.In
		err := lexer.process(loc)
		if err != nil {
			panic(err)
		}
	}
}

func (lexer *Lexer) process(loc string) error {
	for _, r := range loc {
		lexer.curChar = string(r)
	}
	switch lexer.curCtx {
	case START:
	}
	return nil
}
