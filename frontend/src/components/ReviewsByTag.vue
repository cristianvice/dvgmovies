<template>
  <div>
    <h2>Reviews in #{{ $route.params.tag }}</h2>
    <ReviewList :reviews="reviews" v-if="reviews" />
  </div>
</template>

<script>
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
}
</script>