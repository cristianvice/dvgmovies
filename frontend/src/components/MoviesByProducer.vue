<template>
  <div>
    <h2>Movies by {{ $route.params.productionHouse }}</h2>
    <p v-if="error">Something went wrong...</p>
    <p v-if="loading">Loading...</p>
    <MovieList v-if="result" :movies="result.moviesByProductionHouse" />
  </div>
</template>

<script>
import gql from 'graphql-tag'
import { useQuery } from '@vue/apollo-composable'
import { useRoute } from 'vue-router'
import MovieList from '@/components/MovieList.vue'

const  MOVIES_BY_PRODUCER_QUERY = gql`
  query ($productionHouse: String!) {
    moviesByProductionHouse(productionHouse: $productionHouse) {
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
    name: "MoviesByProducer",
    components: {
      MovieList,
    },
    data() {
        return {
            movies: null,
        };
    },
    setup() {
        const productionHouse = useRoute().params.productionHouse.toString();
        const { result, loading, error } = useQuery(MOVIES_BY_PRODUCER_QUERY, () => ({
            productionHouse: productionHouse,
        }));
        return {
            result,
            loading,
            error
        };
    },
}
</script>