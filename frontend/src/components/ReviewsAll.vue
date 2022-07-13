<template>
  <div>
    <h1 class="review__head">Recent reviews</h1>
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
        slug
      }
      publishDate
      published
      metaDescription
      slug
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

<style>
.review__head {
  padding: 1rem 0;
}
</style>