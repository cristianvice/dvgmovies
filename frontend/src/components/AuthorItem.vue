<template>
  <div v-if="author">
    <h2>{{ displayName }}</h2>
    <a
      :href="author.website"
      target="_blank"
      rel="noopener noreferrer"
    >Website</a>
    <p>{{ author.bio }}</p>

    <h3>Reviews by {{ displayName }}</h3>
    <ReviewList :reviews="author.reviewSet" :showAuthor="false" />
  </div>
</template>

<script>
import gql from 'graphql-tag'
import ReviewList from '../components/ReviewList.vue'

export default {
  name: 'AuthorItem',
  components: {
    ReviewList,
  },
  data () {
    return {
      author: null,
    }
  },
  computed: {
    displayName () {
      return (
        this.author.user.firstName &&
        this.author.user.lastName &&
        `${this.author.user.firstName} ${this.author.user.lastName}`
      ) || `${this.author.user.username}`
    },
  },
  async created () {
    const user = await this.$apollo.query({
      query: gql`query ($username: String!) {
        authorByUsername(username: $username) {
          website
          bio
          user {
            firstName
            lastName
            username
          }
          reviewSet {
            title
            movie
            publishDate
            published
            metaDescription
            slug
            tags {
              name
            }
          }
        }
      }`,
      variables: {
        username: this.$route.params.username,
      },
    })
    this.author = user.data.authorByUsername
  },
}
</script>