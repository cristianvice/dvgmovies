<template>
  <div>
    <h1 class="movie__head">My movie list</h1>
    <h2 class="filter__head">Filter movies</h2>
    <div>
        <p v-if="error">Something went wrong...</p>
        <p v-if="loading">Loading...</p>
            <div class="switch-field" v-if="result">
        		<input type="radio" id="radio-all" name="filter-switch" value="all" @change="filterMovies(result.allMovies)" v-model="movieFilter" checked/>
                <label for="radio-all">Show all</label>
                <input type="radio" id="radio-to-watch" name="filter-switch" value="toWatch" @change="filterMovies(result.allMovies)" v-model="movieFilter" />
                <label for="radio-to-watch">Watch List</label>
                <input type="radio" id="radio-watched" name="filter-switch" value="watched" @change="filterMovies(result.allMovies)" v-model="movieFilter" />
                <label for="radio-watched">Already Seen</label>
	        </div>
    </div>
    <MovieList v-if="allMovies" :movies="allMovies" />
    <MovieList v-if="result && !allMovies" :movies="result.allMovies" />
  </div>
</template>

<script>
import gql from 'graphql-tag'
import { useQuery } from '@vue/apollo-composable'
import MovieList from '@/components/MovieList.vue'

const  MOVIES_QUERY = gql`
  query {
    allMovies {
        title
        releaseDate
        slug
        movieSynopsis
        director {
            name
        }
        cast {
            name
        }
        productionHouse {
            name
        }
        genre {
            name
        }
        watched
        watchedDate
        reviewSet {
            title
            movie {
                title
            }
            publishDate
            published
            metaDescription
            slug
            author {
                user {
                    username
                    firstName
                    lastName
                }
            }
            tags {
                name
            }
        }
    }
  }`

export default {
    name: "MoviesAll",
    components: {
      MovieList,
    },
    data() {
        return {
            allMovies: null,
            movieFilter: "all",
        };
    },
    setup() {
        const { result, loading, error } = useQuery(MOVIES_QUERY);
        return {
            result,
            loading,
            error
        };
    },
    methods: {
        filterMovies (movies) {
            const vm = this;
            const movieFilter = vm.movieFilter;
            if (movieFilter === "all") {
                this.allMovies = movies;
            }
            if (movieFilter === "watched") {
                this.allMovies = movies.filter(movie => movie.watched);
            }
            if (movieFilter === "toWatch") {
                this.allMovies = movies.filter(movie => !movie.watched);
            }
        }
    }
}
</script>

<style>
.movie__head {
  padding: 1rem 0;
}

.filter__head {
    padding-bottom: .5rem;
}

.switch-field {
	display: flex;
	margin-bottom: 36px;
	overflow: hidden;
}

.switch-field input {
	position: absolute !important;
	clip: rect(0, 0, 0, 0);
	height: 1px;
	width: 1px;
	border: 0;
	overflow: hidden;
}

.switch-field label {
	background-color: #e4e4e4;
	color: rgba(0, 0, 0, 1);
	font-size: 14px;
	line-height: 1;
	text-align: center;
	padding: 8px 16px;
	margin-right: -1px;
	border: 1px solid rgba(0, 0, 0, 0.2);
	box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.3), 0 1px rgba(255, 255, 255, 0.1);
	transition: all 0.1s ease-in-out;
}

.switch-field label:hover {
	cursor: pointer;
}

.switch-field input:checked + label {
	background-color: hsla(160, 100%, 37%, .5);
	box-shadow: none;
}

.switch-field label:first-of-type {
	border-radius: 4px 0 0 4px;
}

.switch-field label:last-of-type {
	border-radius: 0 4px 4px 0;
}
</style>