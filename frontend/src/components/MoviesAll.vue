<template>
  <div>
    <h2>All movies</h2>
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