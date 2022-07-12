<template>
  <div>
    <h2>Movies starring {{ $route.params.actor }}</h2>
    <p v-if="error">Something went wrong...</p>
    <p v-if="loading">Loading...</p>
    <MovieList v-if="result" :movies="result.moviesByCast" />
  </div>
</template>

<script>
import gql from 'graphql-tag'
import { useQuery } from '@vue/apollo-composable'
import { useRoute } from 'vue-router'
import MovieList from '@/components/MovieList.vue'

const  MOVIES_BY_CAST_QUERY = gql`
  query ($cast: String!) {
    moviesByCast(cast: $cast) {
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
    name: "MoviesByActor",
    components: {
      MovieList,
    },
    data() {
        return {
            movies: null,
        };
    },
    setup() {
        const cast = useRoute().params.actor.toString();
        const { result, loading, error } = useQuery(MOVIES_BY_CAST_QUERY, () => ({
            cast: cast,
        }));
        return {
            result,
            loading,
            error
        };
    },
}
</script>