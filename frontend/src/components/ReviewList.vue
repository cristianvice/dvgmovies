<template>
  <div>
    <ol class="review-list">
      <li class="review" v-for="review in publishedReviews" :key="review.title">
          <span class="review__title">
            <router-link
              :to="{ name: 'review', params: { slug: review.slug }}"
            >{{ review.title }}: {{ review.movie.title }}</router-link>
          </span>
          <span>
          </span>
          <div class="review__date">{{ displayableDate(review.publishDate) }}</div>
        <p class="review__description">{{ review.metaDescription }}</p>
        <ul>
          <li class="review__tags" v-for="tag in review.tags" :key="tag.name">
            <router-link :to="`/tag/${tag.name}`"> # {{ tag.name }} </router-link>
          </li>
        </ul>
      </li>
    </ol>
  </div>
</template>

<script>
export default {
  name: 'ReviewList',
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
  color: #120B21;
  font-style: italic;
}

.review__tags {
  list-style: none;
  font-weight: bold;
  font-size: 0.8125rem;
  display: inline;
}
</style>