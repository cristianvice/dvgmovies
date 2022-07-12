<template>
  <div>
    <h2>Reviews in #{{ $route.params.tag }}</h2>
    <p v-if="error">Something went wrong... </p>
    <p v-if="loading">Loading...</p>
    <ReviewList v-if="result" :reviews="result.reviewsByTag" />
  </div>
</template>

<script>
import gql from 'graphql-tag'
import { useQuery } from '@vue/apollo-composable'
import { useRoute } from 'vue-router'
import ReviewList from '@/components/ReviewList.vue'

const REVIEWS_BY_TAG_QUERY = gql`
  query ($tag: String!) {
    reviewsByTag(tag: $tag) {
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
  name: 'ReviewsByTag',
  components: {
    ReviewList,
  },
  data () {
    return {
      reviews: null,
    }
  },
  setup() {
    const tag = useRoute().params.tag.toString();
    const { result, loading, error } = useQuery(REVIEWS_BY_TAG_QUERY, () => ({
      tag: tag,
    }));
    return {
      result,
      loading,
      error
    };
  },
}
</script>