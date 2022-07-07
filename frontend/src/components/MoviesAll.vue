<template>
  <div>
    <h2>Filter movies</h2>
    <div class="switch-field">
		<input type="radio" id="radio-all" name="switch-two" value="all" v-model="filter" checked/>
		<label for="radio-all">Show all</label>
		<input type="radio" id="radio-to-watch" name="switch-two" value="toWatch" v-model="filter" />
		<label for="radio-to-watch">Watch List</label>
		<input type="radio" id="radio-watched" name="switch-two" value="watched" v-model="filter" />
		<label for="radio-watched">Already Seen</label>
	</div>
      <p v-if="error">Something went wrong...</p>
      <p v-if="loading">Loading...</p>
      <MovieList v-if="result" :movies="result.allMovies" />
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
}
</script>

<style>
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