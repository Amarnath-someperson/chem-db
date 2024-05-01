import { createMemoryHistory, createRouter } from 'vue-router'

import Home from '../views/Home.vue'
import Reactions from '../views/Reactions.vue'
import ReactionElement from '../views/ReactionElement.vue'

const routes = [
  { path: '/', component: Home },
  { path: '/reactions/', component: Reactions },
  { path: '/reactions/:id', component: ReactionElement}
]


const router = createRouter({
  history: createMemoryHistory(),
  routes,
})


export default router