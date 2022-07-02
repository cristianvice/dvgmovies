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
    <ul>
      <li class="review__genre" v-for="genre in review.genre" :key="genre.name">
        <router-link :to="`/genre/${genre.name}`">#{{ genre.name }}</router-link>
      </li>
    </ul>
  </div>
</template>

<script>
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
}
</script>