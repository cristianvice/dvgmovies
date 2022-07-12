<template>
  <div>
    <h2>{{ $route.params.genre }} movies</h2>
    <p v-if="error">Something went wrong... </p>
    <p v-if="loading">Loading...</p>
    <MovieList v-if="result" :movies="result.moviesByGenre" />
  </div>
</template>

<script>
import gql from 'graphql-tag'
import { useQuery } from '@vue/apollo-composable'
import { useRoute } from 'vue-router'
import MovieList from '@/components/MovieList.vue'

const MOVIES_BY_GENRE_QUERY = gql`
  query ($genre: String!) {
    moviesByGenre(genre: $genre) {
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
  name: 'MoviesByGenre',
  components: {
    MovieList,
  },
  data () {
    return {
      movies: null,
    }
  },
  setup() {
    const genre = useRoute().params.genre.toString();
    const { result, loading, error } = useQuery(MOVIES_BY_GENRE_QUERY, () => ({
      genre: genre,
    }));
    return {
      result,
      loading,
      error
    };
  },
}
</script>