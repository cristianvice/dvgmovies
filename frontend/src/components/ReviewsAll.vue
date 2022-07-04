<template>
  <div>
    <h2>Recent reviews</h2>
      <p v-if="error">Something went wrong...</p>
      <p v-if="loading">Loading...</p>
      <ReviewList v-if="result" :reviews="result.allReviews" />
  </div>
</template>

<script>
import gql from 'graphql-tag'
import { useQuery } from '@vue/apollo-composable'
import ReviewList from '@/components/ReviewList.vue'

const REVIEWS_QUERY = gql`
  query {
    allReviews {
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
  }`

export default {
    name: "ReviewsAll",
    components: {
      ReviewList,
    },
    data() {
        return {
            allReviews: null,
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