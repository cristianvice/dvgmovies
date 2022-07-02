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
import ReviewList from '@/components/ReviewList.vue'

export default {
  name: 'Author',
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
}
</script>