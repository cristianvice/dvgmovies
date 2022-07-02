import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import AuthorLink from "../components/AuthorLink.vue";
import ReviewList from "../components/ReviewList.vue";
import ReviewItem from "../components/ReviewItem.vue";
import ReviewsByTag from "../components/ReviewsByTag.vue";
import ReviewsAll from "../components/ReviewsAll.vue";


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    { 
      path: '/author/:username', 
      name: "author",
      component: AuthorLink, 
    },
    { 
      path: '/reviews/:slug', 
      name: "review",
      component: ReviewItem,
    },
    { 
      path: '/tag/:tag', 
      name: "tags",
      component: ReviewsByTag,
    },
    { 
      path: '/reviews', 
      name: "reviews",
      component: ReviewsAll, 
    },
  ],
});

export default router;
