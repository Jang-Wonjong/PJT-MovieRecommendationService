<template>
  <div>
    {{ youId }}
    <br>
    {{ userProfile }}

    <hr>

    <div v-if="isSelf">
      <input 
        type="text"
        v-model.trim="nicknameUpdate"
        @keyup.enter="updateProfile(userProfile)"
      >
      <button @click="updateProfile(userProfile)">수정</button>
      <br>
      <button @click="deleteProfile">회원탈퇴</button>
      <button @click="logout">로그아웃</button>
    </div>
    <div v-else>
      <button @click="follow">팔로우</button>
      <p>팔로워: {{ followersCounting }}, {{ followers }}</p>
      <p>팔로잉: {{ followingsCounting }}, {{ followings }}</p>
    </div>

    <hr>

    <div>
        <span>{{ userMovies }}</span>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { mapGetters, mapActions } from 'vuex'


export default {
  name: 'UserProfile',
  data: function () {
    return {
      isSelf: false,
      youId: null,
      userProfile: null,
      userMovies: null,

      nicknameUpdate: null,

      followers: null,
      followersCounting: null,
      followings: null,
      followingsCounting: null,
    }
  },
  methods: {
    ...mapActions([
      'logout',
    ]),
    getProfile: function () {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/accounts/${this.youId}/profile/`,
        headers: this.config
      })
        .then(res => {
          console.log(res)
          this.userProfile = res.data
          this.getUserMovies() // 유저가 저장한 영화 불러오기
        })
        .catch(err => {
          console.log(err)
        })
    },
    deleteProfile: function () {
      axios({
        method: 'delete',
        url: `http://127.0.0.1:8000/accounts/${this.youId}/profile/`,
        headers: this.config
      })
        .then(res => {
          console.log(res)
          this.$store.dispatch('logout')
        })
        .catch(err => {
          console.log(err)
        })
    },
    updateProfile: function (userProfile) {
      // console.log(userProfile)
      const profileItem = {
        ...userProfile,
        nickname: this.nicknameUpdate,
      }
      // console.log(profileItem)
      axios({
        method: 'put',
        url: `http://127.0.0.1:8000/accounts/${this.youId}/profile/`,
        data: profileItem,
        headers: this.config
      })
        .then(res => {
          console.log(res)
          this.$store.dispatch('profileUpdate', profileItem)
          this.getProfile()
        })
        .catch(err => {
          console.log(err)
        })
      this.nicknameUpdate = null
    },
    getUserMovies: function () {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/movie/user-movies/${this.youId}/`,
        headers: this.config
      })
        .then(res => {
          // console.log(res)
          this.userMovies = res.data
          // this.getProfile()
        })
        .catch(err => {
          console.log(err)
        })
    },
    follow: function () {
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/accounts/follow/${this.youId}/`,
        headers: this.config
      })
        .then(res => {
          console.log(res)
          // this.userMovies = res.data
          // this.getProfile()
        })
        .catch(err => {
          console.log(err)
        })
    },
    getFollowers: function () {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/accounts/followers/${this.$store.state.id}/`,
        headers: this.config
      })
        .then(res => {
          console.log(res)
          this.followers = res.data
          this.followersCounting = res.data.length
          // this.getProfile()
        })
        .catch(err => {
          console.log(err)
        })
    },
    getFollowings: function () {
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/accounts/followings/${this.$store.state.id}/`,
        headers: this.config
      })
        .then(res => {
          console.log(res)
          this.followings = res.data
          this.followingsCounting = res.data.length
          // this.getProfile()
        })
        .catch(err => {
          console.log(err)
        })
    },
  },
  computed: {
    ...mapGetters([
      'config',
    ])
  },
  created: function () {
    if (localStorage.getItem('jwt')) {
      // console.log(this.$route.query.userId)
      this.youId = this.$route.query.userId
      this.getProfile()
      this.getFollowers()
      this.getFollowings()
      if (this.$store.state.id === this.youId) {
        this.isSelf = true
      }
    } else {
      this.$router.push({ name: 'Login' })
    }
  },
}
</script>

<style>

</style>