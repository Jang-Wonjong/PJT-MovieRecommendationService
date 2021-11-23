import Vue from 'vue'
import VueRouter from 'vue-router'
import Sign from '@/views/accounts/Sign'
import UserProfile from '@/views/accounts/UserProfile'
import Main from '@/views/movies/Main'
import MovieList from '@/views/movies/MovieList'
import MovieDetail from '@/views/movies/MovieDetail'
import RecommendUser from '@/views/recommend/RecommendUser'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Main',
    component: Main
  },
  {
    path: '/sign',
    name: 'Sign',
    component: Sign
  },
  {
    path: '/user-profile',
    name: 'UserProfile',
    component: UserProfile
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
  {
    path: '/recommend-user',
    name: 'RecommendUser',
    component: RecommendUser
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router



// router.beforeEach((to, from, next) => {

//   // 1-1. 로그인이 필요한 컴포넌트
//   const authPages = [
//     'MovieList',
//     'Profile',
//     'Logout',
//   ]
//   // 1-2. 로그아웃이 필요한 컴포넌트
//   const publicPages = [
//     'Login',
//     'Signup',
//   ]

//   // 2. 
//   // 가려고 하는 곳(to)이 로그인이 필요한 곳인지 여부를 체크
//   const authRequired = authPages.includes(to.name)
//   // 가려고 하는 곳이 로그인이 필요하지 않은 곳이지 여부를 체크
//   const authNotRequired = publicPages.includes(to.name)
//   // 로그인이 되어있는지 여부를 체크
//   const isLoggedin = localStorage.getItem('jwt') ? true : false

//   //3 .
//   // 3-1. 만약 로그인이 필요한 컴포넌트인데 로그인이 안되어 있는 경우에 강제로 가려하면
//   if (authRequired && !isLoggedin) {
//     // 로그인 할 수 있도록 가드 -> Login 컴포넌트로 보내기(redirect 느낌)
//     next({ name: 'Login' })
//   } else if (authNotRequired && isLoggedin) {
//     next({ name: 'MovieList' })
//   } else {
//     next()
//   }  
// })