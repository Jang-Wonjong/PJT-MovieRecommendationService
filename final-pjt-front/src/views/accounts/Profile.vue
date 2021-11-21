<template>
  <div>
    <h1>{{ profile }}</h1>

    <div>
      <input 
        type="text"
        v-model.trim="nicknameUpdate"
        @keyup.enter="updateProfile(profile)"
      >
      <button @click="updateProfile(profile)">수정</button>
    </div>

    <button @click="deleteProfile">회원탈퇴</button>

    <div>
      <span>{{ myMovies }}</span>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Profile',
  data: function () {
    return {
      profile: null,
      nicknameUpdate: null,
      myMovies: null,
      // passwordUpdate: null,
    }
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    getProfile: function () {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/accounts/profile/',
        headers: this.setToken()
      })
        .then(res => {
          // console.log(res)
          this.profile = res.data
        })
        .catch(err => {
          console.log(err)
        })
    },
    deleteProfile: function () {
      axios({
        method: 'delete',
        url: 'http://127.0.0.1:8000/accounts/profile/',
        headers: this.setToken()
      })
        .then(res => {
          console.log(res)
          this.isLogin = false  // app에 있는것을 어떻게 바꿀 것인가? vuex
          localStorage.removeItem('jwt')
          this.$router.push({ name: 'Login' })
        })
        .catch(err => {
          console.log(err)
        })
    },
    updateProfile: function (profile) {
      const profileItem = {
        ...profile,
        nickname: this.nicknameUpdate,
      }
      axios({
        method: 'put',
        url: `http://127.0.0.1:8000/accounts/profile/`,
        data: profileItem,
        headers: this.setToken()
      })
        .then(() => {
          // console.log(res)
          this.getProfile()
        })
        .catch(err => {
          console.log(err)
        })
      this.nicknameUpdate = null
    },
    getMyMovie: function () {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movie/my-movies/`,
        headers: this.setToken()
      })
        .then(res => {
          // console.log(res)
          this.myMovies = res.data
        })
        .catch(err => {
          console.log(err)
        })
    },
  },
  created: function () {
    if (localStorage.getItem('jwt')) {
      this.getProfile()
      this.getMyMovie()
    } else {
      this.$router.push({ name: 'Login' })
    }
  }
}
</script>

<style>

</style>