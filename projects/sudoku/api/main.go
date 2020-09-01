package main

import (
	"encoding/json"
	"fmt"
	"io"
	"log"
	"net/http"

	"github.com/gorilla/mux"
	"github.com/kswarthout/sudoku/api/sudoku"
)

type puzzle struct {
	Sln   string `json:"sln"`
	Start string `json:"start"`
}

// SendJSON marshals v to a json struct and send the appropriate headers to w
func sendJSON(w http.ResponseWriter, r *http.Request, v interface{}, code int) {
	w.Header().Add("Content-Type", "application/json")

	b, err := json.Marshal(v)

	if err != nil {
		log.Print(fmt.Sprintf("Error while encoding JSON: %v", err))
		w.WriteHeader(http.StatusInternalServerError)
		io.WriteString(w, `{"error"}: "Internal server error"`)
	} else {
		w.WriteHeader(code)
		io.WriteString(w, string(b))
	}
}

func getPuzzle(w http.ResponseWriter, r *http.Request) {

	p := puzzle{}

	// generate solution
	board := [9][9]int{}
	sudoku.Generate(&board)
	p.Sln = sudoku.ParseGrid(board)

	// genrate puzzle from solution
	sudoku.RemoveNumbers(&board)
	p.Start = sudoku.ParseGrid(board)

	// p := puzzle{sln, start}
	sendJSON(w, r, p, http.StatusOK)
}

// Routes configures all API routes
func Routes() *mux.Router {

	// Register Routes
	router := mux.NewRouter().StrictSlash(true)
	router.HandleFunc("/puzzle", getPuzzle).Methods("GET")
	log.Fatal(http.ListenAndServe(":8080", router))

	return router
}

func main() {

	router := Routes()

	log.Println("Serving application at Port : 8080")
	log.Fatal(http.ListenAndServe(":8080", router))
}
