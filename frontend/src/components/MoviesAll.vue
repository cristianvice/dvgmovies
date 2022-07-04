<template>
  <div>
    <h2>Recent movies</h2>
      <p v-if="error">Something went wrong...</p>
      <p v-if="loading">Loading...</p>
      <MovieList v-if="result" :movies="result.allMovies" />
  </div>
</template>

<script>
import gql from 'graphql-tag'
import { useQuery } from '@vue/apollo-composable'
import MovieList from '@/components/MovieList.vue'

const REVIEWS_QUERY = gql`
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
        const { result, loading, error } = useQuery(REVIEWS_QUERY);
        return {
            result,
            loading,
            error
        };
    },
}
</script>