<template>
  <p v-if="error">Something went wrong... {{ error.toString() }} </p>
  <p v-if="loading">Loading...</p>
  <div class="movie" v-if="result">
      <h2>{{ result.movieBySlug.title }} - {{ releaseDate(result.movieBySlug.releaseDate) }}</h2>
      <div class="movie__date" v-if="result.movieBySlug.watched">Watched {{ watchDate(result.movieBySlug.watchedDate) }}</div>
      <p class="movie__description">{{ result.movieBySlug.movieSynopsis }}</p>
      <ul>
        <li class="movie__reviews" v-for="review in result.movieBySlug.reviewSet" :key="review.title">
          <span v-if="review.published">
            <router-link :to="`/reviews/${review.slug}`">Read the review: {{ review.title }}</router-link>
          </span>
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
    movieBySlug(slug: $slug) {
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
            slug
            published
        }
    }
  }`

export default {
  name: 'ReviewItem',
  data () {
    return {
      movie: null,
    }
  },
  methods: {
    releaseDate (date) {
      return new Intl.DateTimeFormat(
        'en-US',
        { year: 'numeric' },
      ).format(new Date(date))
    },
    watchDate (date) {
        return new Intl.DateTimeFormat(
            'en-US',
            { dateStyle: 'full' },
        ).format(new Date(date))
    },
  },
  setup() {
    const movieSlug = useRoute().params.slug.toString();
    const { result, loading, error } = useQuery(REVIEW_QUERY, () => ({
      slug: movieSlug,
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
.movie__reviews {
  list-style: none;
  font-weight: bold;
}
</style>