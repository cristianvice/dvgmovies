<template>
  <p v-if="error">Something went wrong... </p>
  <p v-if="loading">Loading...</p>
  <div class="movie" v-if="result">
      <h2>{{ result.movieBySlug.title }} - {{ releaseDate(result.movieBySlug.releaseDate) }}</h2>
      <div class="movie__info" v-if="result.movieBySlug.watched">Watched {{ watchDate(result.movieBySlug.watchedDate) }}</div>
      <div  class="movie__info">
        <p class="movie__description">{{ result.movieBySlug.movieSynopsis }}</p>
      </div>
      <div class="movie__info">
        <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24"><path d="M4 11c-2.21 0-4-1.791-4-4s1.791-4 4-4 4 1.791 4 4-1.791 4-4 4zm10 2c.702 0 1.373-.127 2-.35v6.35c0 1.104-.896 2-2 2h-10c-1.104 0-2-.896-2-2v-6.35c.627.223 1.298.35 2 .35 2.084 0 3.924-1.068 5-2.687 1.076 1.619 2.916 2.687 5 2.687zm4 1v4l6 3v-10l-6 3zm-4-11c-2.209 0-4 1.791-4 4s1.791 4 4 4 4-1.791 4-4-1.791-4-4-4z"/></svg>
        Directed by 
        <ul>
          <li class="movie__producer">
            <router-link :to="`/directors/${result.movieBySlug.director.name}`">
              {{ result.movieBySlug.director.name }} 
            </router-link>
          </li>
        </ul>      </div>
      <div class="movie__info">
        <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24"><path d="M10 20v-6l5 3-5 3zm14-15.625l-.008-.042-1.008-4.333-21.169 4.196c-1.054.209-1.815 1.134-1.815 2.207v14.597c0 1.657 1.343 3 3 3h18c1.656 0 3-1.343 3-3v-14h-12.734l12.734-2.625zm-3.89-2.618l2.396 1.604-2.994.595-2.398-1.605 2.996-.594zm-5.897 1.169l2.399 1.606-2.993.595-2.402-1.607 2.996-.594zm-5.905 1.171l2.403 1.608-2.993.595-2.406-1.61 2.996-.593zm2.538 3.903l-2.039 2h-3.054l2.039-2h3.054zm8.978 0h3.054l-2.038 2h-3.055l2.039-2zm-6.012 0h3.053l-2.039 2h-3.053l2.039-2zm8.188 4v8.75c0 .69-.56 1.25-1.25 1.25h-17.5c-.69 0-1.25-.56-1.25-1.25v-8.75h20z"/></svg>
        Produced by 
        <ul>
          <li class="movie__producer" v-for="producer in result.movieBySlug.productionHouse" :key="producer.name">
            <router-link :to="`/producers/${producer.name}`">
              {{ producer.name }} 
            </router-link>
          </li>
        </ul>
      </div>
      <div class="movie__info">
        <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24"><path d="M12 .288l2.833 8.718h9.167l-7.417 5.389 2.833 8.718-7.416-5.388-7.417 5.388 2.833-8.718-7.416-5.389h9.167z"/></svg>
        Starring 
        <ul>
          <li class="movie__producer" v-for="actor in result.movieBySlug.cast" :key="actor.name">
            <router-link :to="`/cast/${actor.name}`">
              {{ actor.name }} 
            </router-link>
          </li>
        </ul>
      </div>
      <div class="movie__info">
        <svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 24 24"><path d="M15.812 4.819c-.33-.341-.312-.877.028-1.207l3.469-3.365c.17-.164.387-.247.603-.247.219 0 .438.085.604.257l-4.704 4.562zm-5.705 8.572c-.07.069-.107.162-.107.255 0 .194.158.354.354.354.089 0 .178-.033.247-.1l.583-.567-.493-.509-.584.567zm4.924-6.552l-1.994 1.933c-1.072 1.039-1.619 2.046-2.124 3.451l.881.909c1.419-.461 2.442-.976 3.514-2.016l1.994-1.934-2.271-2.343zm5.816-5.958l-5.137 4.982 2.586 2.671 5.138-4.98c.377-.366.566-.851.566-1.337 0-1.624-1.968-2.486-3.153-1.336zm-11.847 12.119h-4v1h4v-1zm9-1.35v1.893c0 4.107-6 2.457-6 2.457s1.518 6-2.638 6h-7.362v-20h12.629l2.062-2h-16.691v24h10.189c3.163 0 9.811-7.223 9.811-9.614v-4.687l-2 1.951z"/></svg>
        Read the review: 
        <ul>
          <li class="movie__reviews" v-for="review in result.movieBySlug.reviewSet" :key="review.title">
            <span v-if="review.published">
              <router-link :to="`/reviews/${review.slug}`"> {{ review.title }} </router-link>
            </span>
          </li>
        </ul>
      </div>
      <ul>
        <li class="movie__genre" v-for="genre in result.movieBySlug.genre" :key="genre.name">
          <router-link :to="`/genre/${genre.name}`">
            | {{ genre.name }} | 
          </router-link>
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
.movie__genre {
  list-style: none;
  font-weight: bold;
  font-size: 0.8125rem;
  display: inline;
}
.movie__producer {
  list-style: none;
  font-weight: bold;
}
</style>