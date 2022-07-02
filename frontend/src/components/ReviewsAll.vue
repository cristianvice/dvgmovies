<template>
  <div>
    <h2>Recent posts</h2>
    <ReviewList v-if="allReviews" :reviews="allReviews" />
  </div>
</template>

<script>
import ReviewList from '@/components/ReviewList.vue'

export default {
  name: 'ReviewsAll',
  components: {
    ReviewList,
  },
  data () {
    return {
        allReviews: null,
    }
  },
}
</script>