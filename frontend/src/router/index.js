import { createRouter, createWebHistory } from "vue-router";
import HomeView from "@/views/HomeView.vue";
import AboutView from "@/views/AboutView.vue"
import ReviewItem from "@/components/ReviewItem.vue";
import ReviewsByTag from "@/components/ReviewsByTag.vue";
import ReviewsAll from "@/components/ReviewsAll.vue";
import MovieItem from "@/components/MovieItem.vue";
import MoviesAll from "@/components/MoviesAll.vue";
import MoviesByDirector from "@/components/MoviesByDirector.vue";
import MoviesByProducer from "@/components/MoviesByProducer.vue";
import MoviesByActor from "@/components/MoviesByActor.vue";
import MoviesByGenre from "@/components/MoviesByGenre.vue";


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/about",
      name: "about",
      component: AboutView,
    },    { 
      path: "/reviews/:slug", 
      name: "review",
      component: ReviewItem,
    },
    { 
      path: "/reviews", 
      name: "reviews",
      component: ReviewsAll, 
    },
    { 
      path: "/movies", 
      name: "movies",
      component: MoviesAll, 
    },
    { 
      path: "/movies/:slug", 
      name: "movie",
      component: MovieItem, 
    },
    { 
      path: "/directors/:director", 
      name: "director",
      component: MoviesByDirector, 
    },
    {
      path: "/producers/:productionHouse",
      name: "producer",
      component: MoviesByProducer,
    },
    {
      path: "/cast/:actor",
      name: "actor",
      component: MoviesByActor,
    },
    { 
      path: "/tag/:tag", 
      name: "tags",
      component: ReviewsByTag,
    },
    { 
      path: "/genre/:genre", 
      name: "genre",
      component: MoviesByGenre, 
    },
  ],
});

export default router;
