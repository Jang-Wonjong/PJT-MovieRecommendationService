import Vue from 'vue'
import VueRouter from 'vue-router'
import Signup from '@/views/accounts/Signup'
import Login from '@/views/accounts/Login'
import Profile from '@/views/accounts/Profile'
import MovieList from '@/views/movies/MovieList'
import MovieDetail from '@/views/movies/MovieDetail'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Signup',
    component: Signup
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/profile',
    name: 'Profile',
    component: Profile
  },
  {
    path: '/movies',
    name: 'MovieList',
    component: MovieList
  },
  {
    path: '/detail',
    name: 'MovieDetail',
    component: MovieDetail
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
