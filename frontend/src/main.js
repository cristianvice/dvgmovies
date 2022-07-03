import { createApp, provide, h } from 'vue'
import { DefaultApolloClient } from '@vue/apollo-composable'
import { ApolloClient, InMemoryCache } from '@apollo/client/core'
import App from './App.vue'
import router from "./router";

const cache = new InMemoryCache({
  addTypename: false
});

const apolloClient = new ApolloClient({
  cache,
  uri: 'http://localhost:8000/graphql',
  maskTypename: true,
});

const app = createApp({
  setup () {
    provide(DefaultApolloClient, apolloClient)
  },

  render: () => h(App),
})

app.use(router);

app.mount('#app');
