import Vue from 'vue'
import VueRouter from 'vue-router'
import MovieList from '@/views/movies/MovieList'


Vue.use(VueRouter)

const routes = [
  // {  나중에 쓸거
  //   path: '/',
  //   name: 'Home',
  //   component: Home
  // },
  {
    path: '/movies',
    name: 'MovieList',
    component: MovieList
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
