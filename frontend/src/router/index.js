import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'HomePage',
    component: () => import(/* webpackChunkName: "about" */ '../views/HomePage.vue')
  },

  {
    path: '/words',
    name: 'Words',
    component: () => import(/* webpackChunkName: "about" */ '../views/Words.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
