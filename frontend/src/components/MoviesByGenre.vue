<template>
  <div>
    <h1>Movies by genre</h1>
    <h2 v-if="loadingMovies || loading">Loading movies by {{ $route.params.genre }}</h2>
    <h2 v-if="result">Genre: {{ $route.params.genre }} </h2>
    <p v-if="error">Something went wrong... </p>
    <MovieList v-if="!loadingMovies && result" :movies="result.moviesByGenre" />
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
      movies: [],
      loadingMovies: false,
    }
  },
  apollo: {
    movies: {
      query: MOVIES_BY_GENRE_QUERY,
      variables() {
        return { genre: this.$route.params.genre };
      },
    },
  },
  created() {
    this.$watch(
      () => this.$route.params,
      (toParams, previousParams) => {
        if (toParams !== previousParams) {
          this.loadingMovies = true;
          //This is still very hacky
          setTimeout(location.reload(), 2000);
        }
      }
    )
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
  }
}
</script>