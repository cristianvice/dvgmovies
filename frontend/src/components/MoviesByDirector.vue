<template>
  <div>
    <h2>Movies by {{ director }}</h2>
    <p v-if="error">Something went wrong...</p>
    <p v-if="loading">Loading...</p>
    <MovieList v-if="result" :movies="result.moviesByDirector" />
  </div>
</template>

<script>
import gql from 'graphql-tag'
import { useQuery } from '@vue/apollo-composable'
import MovieList from '@/components/MovieList.vue'

const  MOVIES_BY_DIRECTOR_QUERY = gql`
  query ($director: String!) {
    moviesByDirector {
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
    name: "MoviesByDirector",
    props: {
        director: {
            type: String,
            required: true,
        }
    },
    components: {
      MovieList,
    },
    data() {
        return {
            movies: null,
        };
    },
    setup() {
        const director = this.director;
        const { result, loading, error } = useQuery(MOVIES_BY_DIRECTOR_QUERY, () => ({
            director: director,
        }));
        return {
            result,
            loading,
            error
        };
    },
}
</script>