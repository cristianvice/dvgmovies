<template>
  <div>
    <h2>Movies by {{ $route.params.director }}</h2>
    <p v-if="error">Something went wrong...</p>
    <p v-if="loading">Loading...</p>
    <MovieList v-if="result" :movies="result.moviesByDirector" />
  </div>
</template>

<script>
import gql from 'graphql-tag'
import { useQuery } from '@vue/apollo-composable'
import { useRoute } from 'vue-router'
import MovieList from '@/components/MovieList.vue'

const  MOVIES_BY_DIRECTOR_QUERY = gql`
  query ($director: String!) {
    moviesByDirector(director: $director) {
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
            tags {
                name
            }
        }
    }
  }`

export default {
    name: "MoviesByDirector",
    components: {
      MovieList,
    },
    data() {
        return {
            movies: null,
        };
    },
    setup() {
        const director = useRoute().params.director.toString();
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