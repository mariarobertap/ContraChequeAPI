package main

import(
	"fmt"
	"log"
	"encoding/json"
	"net/http"

	"github.com/gorilla/mux"
)

type Movie struct {
	ID string  `json:"ID"`
	isbn string `json:"isbn"`
	Title string `json:"Title"`
	Director *Director `json:"Director"`
}

type Director struct {
	Firstname string `json:"firstname"`
	Lastname string `json:"lastname"`
}

var movies []Movie


func getMovies(w http.ResponseWriter, r *http.Request){


	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(movies)
}


func main(){

	r:=mux.NewRouter()
	
	myDirector := Director{
		Firstname:"John",
		Lastname: "Smith",
	}

	movie1 :=  Movie{
		ID: "1",
		isbn: "123",
		Title: "Movie one",
		Director: &myDirector,
	}
	movie2 :=  Movie{
		ID: "2",
		isbn: "123",
		Title: "Movie two",
		Director: &myDirector,
	}

	movies = append(movies, movie2)
	movies = append(movies, movie1)


	r.HandleFunc("/movies", getMovies).Methods("GET")
	/*
	r.HandleFunc("/movies/{id}", getMovie.Methods("GET"))
	r.HandleFunc("/movies", createMovie.Methods("POST"))
	r.HandleFunc("/movies/{id}", updateMovie.Methods("PUT"))
	r.HandleFunc("/movies/{id}", deleteMovie.Methods("DELETE"))
	*/

	fmt.Printf("Starting server at port 8080\n")
	log.Fatal(http.ListenAndServe(":8080", r))
	



}
