<template>
  <div>
    <ol class="movie-list">
      <li class="movie" v-for="movie in movies" :key="movie.title">
          <span class="movie__title">
            <router-link
              :to="{ name: 'movie', params: { slug: movie.slug }}"
            >{{ movie.title }}</router-link>
          </span>
          <span>
          </span>
          <div class="movie__date">{{ displayableDate(movie.releaseDate) }}</div>
        <p class="movie__description">{{ movie.movieSynopsis }}</p>
        <ul>
          <li class="movie__genre" v-for="genre in movie.genre" :key="genre.name">
            <router-link :to="`/genre/${genre.name}`">#{{ genre.name }}</router-link>
          </li>
        </ul>
      </li>
    </ol>
  </div>
</template>

<script>
export default {
  name: 'MovieList',
  props: {
    movies: {
      type: Array,
      required: true,
    },
    showAuthor: {
      type: Boolean,
      required: false,
      default: true,
    },
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
.movie-list {
  list-style: none;
}

.movie {
  border-bottom: 1px solid #ccc;
  padding-bottom: 1rem;
}

.movie__title {
  font-size: 1.25rem;
}

.movie__description {
  color: #777;
  font-style: italic;
}

.movie__tags {
  list-style: none;
  font-weight: bold;
  font-size: 0.8125rem;
}
</style>