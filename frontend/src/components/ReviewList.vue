<template>
  <div>
    <ol class="review-list">
      <li class="review" v-for="review in publishedReviews" :key="review.title">
          <span class="review__title">
            <router-link
              :to="`/review/${review.slug}`"
            >{{ review.title }}: {{ review.movie }}</router-link>
          </span>
          <span v-if="showAuthor">
            by <AuthorLink :author="review.author" />
          </span>
          <div class="review__date">{{ displayableDate(review.publishDate) }}</div>
        <p class="review__description">{{ review.metaDescription }}</p>
        <ul>
          <li class="review__tags" v-for="tag in review.tags" :key="tag.name">
            <router-link :to="`/tag/${tag.name}`">#{{ tag.name }}</router-link>
          </li>
        </ul>
       <ul>
          <li class="review__genres" v-for="genre in review.genre" :key="genre.name">
            <router-link :to="`/genre/${genre.name}`">#{{ genre.name }}</router-link>
          </li>
        </ul>
      </li>
    </ol>
  </div>
</template>

<script>
import AuthorLink from '@/components/AuthorLink.vue'

export default {
  name: 'ReviewList',
  components: {
    AuthorLink,
  },
  props: {
    reviews: {
      type: Array,
      required: true,
    },
    showAuthor: {
      type: Boolean,
      required: false,
      default: true,
    },
  },
  computed: {
    publishedReviews () {
      return this.reviews.filter(review => review.published)
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
}
</script>

<style>
.review-list {
  list-style: none;
}

.review {
  border-bottom: 1px solid #ccc;
  padding-bottom: 1rem;
}

.review__title {
  font-size: 1.25rem;
}

.review__description {
  color: #777;
  font-style: italic;
}

.review__tags {
  list-style: none;
  font-weight: bold;
  font-size: 0.8125rem;
}
</style>