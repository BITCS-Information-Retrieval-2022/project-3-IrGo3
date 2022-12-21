import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import FirstView from '../views/FirstPage.vue'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/home',
    name: 'home',
    component: HomeView
  },
  {
    path: '/searchResult',
    name: 'searchResult',
    component: ()=> import('../views/SecondPage.vue')
  },
  {
    path:'/searchDetails',
    name:'searchDetails',
    component:()=>import('../views/ThirdPage.vue')
  },
  {
    path:'/',
    name:'firstPage',
    component:FirstView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
