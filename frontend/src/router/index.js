import { createRouter, createWebHistory } from "vue-router";
import HomeView from "@/views/HomeView.vue";
import AboutView from "@/views/AboutView.vue"
import ReviewItem from "@/components/ReviewItem.vue";
import ReviewsByTag from "@/components/ReviewsByTag.vue";
import ReviewsAll from "@/components/ReviewsAll.vue";


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
      path: "/tag/:tag", 
      name: "tags",
      component: ReviewsByTag,
    },
  ],
});

export default router;
