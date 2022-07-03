<template>
  <div>
    <h2>Reviews in #{{ $route.params.tag }}</h2>
    <ReviewList :reviews="reviews" v-if="reviews" />
  </div>
</template>

<script>
import gql from 'graphql-tag'
import ReviewList from '@/components/ReviewList.vue'

export default {
  name: 'ReviewsByTag',
  components: {
    ReviewList,
  },
  data () {
    return {
      posts: null,
    }
  },
  async created () {
    const reviews = await this.$apollo.query({
      query: gql`query ($tag: String!) {
        reviewsByTag(tag: $tag) {
          title
          movie
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
      }`,
      variables: {
        tag: this.$route.params.tag,
      },
    })
    this.reviews = reviews.data.reviewsByTag
  },
}
</script>