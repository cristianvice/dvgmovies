<template>
  <p v-if="error">Something went wrong...</p>
  <p v-if="loading">Loading...</p>
  <div class="review" v-if="result">
      <h2>{{ result.reviewBySlug.title }}</h2>
      <div class="review__movie">
          <router-link :to="`/movies/${result.reviewBySlug.movie.slug}`">{{ result.reviewBySlug.movie.title }}</router-link>
      </div>
      <div>{{ displayableDate(result.reviewBySlug.publishDate) }}</div>
    <p class="review__description">{{ result.reviewBySlug.metaDescription }}</p>
    <article>
      {{ result.reviewBySlug.body }}
    </article>
    <ul>
      <li class="review__tags" v-for="tag in result.reviewBySlug.tags" :key="tag.name">
        <router-link :to="`/tag/${tag.name}`">#{{ tag.name }}</router-link>
      </li>
    </ul>
  </div>
</template>

<script>
import gql from 'graphql-tag'
import { useQuery } from '@vue/apollo-composable'
import { useRoute } from 'vue-router'

const REVIEW_QUERY = gql`
  query ($slug: String!) {
    reviewBySlug(slug: $slug) {
      title
      movie {
        title
        slug
      }
      publishDate
      metaDescription
      slug
      body
      tags {
        name
      }
    }
  }`

export default {
  name: 'ReviewItem',
  data () {
    return {
      review: null,
    }
  },
  methods: {
    displayableDate (date) {
      return new Intl.DateTimeFormat(
        'en-US',
        { dateStyle: 'full' },
      ).format(new Date(date))
    },
  },
  setup() {
    const slug = useRoute().params.slug.toString();
    const { result, loading, error } = useQuery(REVIEW_QUERY, () => ({
      slug: slug,
    }));
    return {
      result,
      loading,
      error
    };
  },
}
</script>

<style>
.review__movie {
  font-weight: bold;
}
</style>