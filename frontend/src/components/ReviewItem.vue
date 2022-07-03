<template>
  <div class="review" v-if="review">
      <h2>{{ review.title }}: {{ review.movie }}</h2>
      By <AuthorLink :author="post.author" />
      <div>{{ displayableDate(review.publishDate) }}</div>
    <p class="review__description">{{ review.metaDescription }}</p>
    <article>
      {{ review.body }}
    </article>
    <ul>
      <li class="review__tags" v-for="tag in review.tags" :key="tag.name">
        <router-link :to="`/tag/${tag.name}`">#{{ tag.name }}</router-link>
      </li>
    </ul>
  </div>
</template>

<script>
import gql from 'graphql-tag'
import AuthorLink from '@/components/AuthorLink.vue'

export default {
  name: 'ReviewItem',
  components: {
    AuthorLink,
  },
  data () {
    return {
      post: null,
    }
  },
  methods: {
    displayableDate (date) {
      return new Intl.DateTimeFormat(
        'en-US',
        { dateStyle: 'full' },
      ).format(new Date(date))
    }
  },
  async created () {
    const review = await this.$apollo.query({
      query: gql`query ($slug: String!) {
        reviewBySlug(slug: $slug) {
          title
          movie
          publishDate
          metaDescription
          slug
          body
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
        slug: this.$route.params.slug,
      },
    })
    this.review = review.data.reviewBySlug
  },
}
</script>