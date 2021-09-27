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
    component: () => import(/* webpackChunkName: "about" */ '../views/Words.vue'),
    props : route => ({ page : parseInt(route.query.page) || 1})
  },
  {
    path: '/sign-up',
    name: 'SignUp',
    component: () => import('../views/SignUp')
  },
  {
    path : "/login",
    name : "Login",
    component: () => import("../views/LoginUser")
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
