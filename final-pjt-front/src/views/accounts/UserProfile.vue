<template>
  <div>
    <div class="m-4 p-3 d-flex justify-content-center">
      <div class="card-profile p-4">
        <div class=" image d-flex flex-column justify-content-center align-items-center"> 
          <button class="btn-profile btn-secondary"> <img src="https://i.imgur.com/wvxPV9S.png" height="100" width="100" /></button> <span class="name mt-3">Eleanor Pena</span> <span class="idd">@eleanorpena</span>
          <div class="d-flex flex-row justify-content-center align-items-center gap-2"> 
            <span class="idd1">Oxc4c16a645_b21a</span> <span><i class="fa fa-copy"></i></span> 
          </div>
          <div class="d-flex flex-row justify-content-center align-items-center mt-3"> 
            <span class="number">1069 <span class="follow">Followers</span></span> 
          </div>
          <div class="d-flex flex-row justify-content-center align-items-center mt-3"> 
            <span class="number">1069 <span class="follow">Followers</span></span> 
          </div>
          <div class=" d-flex mt-2"> 
            <button class="btn-profile1 btn-dark">Edit Profile</button> 
          </div>
          <div class="gap-3 mt-3 icons d-flex flex-row justify-content-center align-items-center"> 
            <span><i class="fa fa-twitter"></i></span> <span><i class="fa fa-facebook-f"></i></span> <span><i class="fa fa-instagram"></i></span> <span><i class="fa fa-linkedin"></i></span>
          </div>
        </div>
      </div>
    </div>
    <!-- <div class="contain">
      <div class="card">
        <img src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxEHBhAIBw8OFRUODw8QEBMSEBAPEA4SFhMWFhYSFx8YHTQgGRoxHRMTITEhJSkuLi4uFx8zODMsNyktLisBCgoKDg0OGhAQGjYlHyU1Ky0tKy0wKy0tLi0tLS0rLS0tLS0tLS0tKy03NystLSsrNS0tLS03Kzc3LS0rLS0tN//AABEIAOEA4QMBIgACEQEDEQH/xAAaAAEAAgMBAAAAAAAAAAAAAAAABAUCAwYB/8QAMxABAAECAwUFBwQDAQAAAAAAAAECAwQRcQUhMTJBEhNRYXI0gZGhsdHhIkKSwSMzghT/xAAZAQEBAQEBAQAAAAAAAAAAAAAAAwIBBAX/xAAcEQEBAQEBAQEBAQAAAAAAAAAAAQIRAzESQSH/2gAMAwEAAhEDEQA/AOsAe980AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHvHgscLs/d27/8fu5bx2S1At2qrk5W4mdISKdn3J6RGs/ZbUxFMZUxlo9Y/ak84qJ2fcjhETpLRcs1Wv8AZTMfRfExnGUn7L5xzotMVs+Ko7VjdPh0nTwVkx2Zyno3L1O5seAOuAAAAAAAAAAAAAAAAAAANlm33t2KI6yCds3DZR39f/Pl5rAiMoyjoJW9Xk5ABx0AAQto4bt0d7Rxjj5wmhLws7HOjdirXc36qI8d2ktKzzgAAAAAAAAAAAAAAAAACZsunPE5+FMz/X9oabsqcsRMeNM/WHNfHc/VqAkuAAAAAAq9rU5XqavGnL4T+UFYbWn/ACUx5T9fwr1c/ENfQB1wAAAAAAAAAAAAAAAAbsJc7rEU1T45TpO5pAjohFwGI7612auNO6fOPFKRv+PRL0AAAABoxl/uLOccZ3U/cLeK3H3O8xU5dP0/D85oz14tHnt6AAAAAAAAAAAAAAAAAAAAztXJtVxXRxhcYXFU4iMuE9Y+ykexOW+HLOu51x0IqLW0K7cZVZVa8fik07Tp/dTV7piWPzVZuJwgztOn9tNXvyhHu7Qrr3UZU6b5c/NLuLDEYmmxT+rj0jrKnvXZvXO3X+IjwYTPanOp4pM8T1roA6yAAAAAAAAAAAAAAAAAAAAAADKmmauWJnSM2cWK54UV/wAZBqG2cPXHGiv+MsJomnmiY1jIOMQAAAAAAAAAAAAAAAAAAABnatTdq7NuM/6WVjZ0U772+fDp+XLZHZm1W0W5uTlREzpCVb2dVVvrmI+crSmmKYypiI03PWLtSec/qJb2dRTzZz78o+TfRYoo5aafhvbBztakkAHHQAGFVmmvmppn3Q0V7Poq4RMaT90oOlkqsubNmN9uqJ13SiXbNVqcrkTH0XxMZxlLU1WLiOdFtf2fTXvt/pn5K69Yqs1ZXI0npLcsqdzY1AOuAAAAAAAAAADdhcPOIudmOEcZ8GleYSz3NiKevGdXNXjWc9rOzaizR2bcfedWYJLAAAAAAAAAAAADyuiK6ezXGcS9AU2Mwv8A56s6eWeHl5Iy/vW4u2poq6/LzUMx2ZynpuUzeo7zyvAGmQAAAAAAAHtPNGroXPU80aw6FjanmAMKAAAAAAAAAAAAAACixW7E1+qfqvVHi/aq/VLeGPT40gNpAAAAAAAAMqeaNYdA5+nmjWHQMbU8wBhQAAAAAAAAAAAAAAUeL9qr9UrxR4v2qv1S3hj0+NIDaQAAAAAAADKnmjWHQOfo541h0DG1PMAYUAAAAAAAAAAAAAAFHi/aq/VK8UeL9qr9Ut4Y9PjSA2kAAAAAAAAyo541h0AMbU8wBhQAAAAAAAAAAAAAAUeL9qr9Ug3hj0+NIDaQAAAD/9k=" class="rounded mx-auto d-block" alt="...">
        <h1>{{ userProfile.nickname }} PROFILE</h1>
      </div>
    </div> -->
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
      <p>팔로잉: {{ followersCounting }}, {{ followers }}</p>
      <p>팔로워: {{ followingsCounting }}, {{ followings }}</p>
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

<style scoped>
* {
  margin: 0;
  padding: 0
}

body {
  background-color: #000
}

.card-profile {
  width: 350px;
  background-color: #efefef;
  border: none;
  cursor: pointer;
  transition: all 0.5s
}

.image img {
  transition: all 0.5s
}

.card-profile:hover .image img {
  transform: scale(1.5)
}

.btn-profile {
  height: 140px;
  width: 140px;
  border-radius: 50%
}

.name {
  font-size: 22px;
  font-weight: bold
}

.idd {
  font-size: 14px;
  font-weight: 600
}

.idd1 {
  font-size: 12px
}

.number {
  font-size: 22px;
  font-weight: bold
}

.follow {
  font-size: 12px;
  font-weight: 500;
  color: #444444
}

.btn-profile1 {
  height: 40px;
  width: 150px;
  border: none;
  background-color: #000;
  color: #aeaeae;
  font-size: 15px
}

.text span {
  font-size: 13px;
  color: #545454;
  font-weight: 500
}

.icons i {
  font-size: 19px
}

hr .new1 {
  border: 1px solid
}

.join {
  font-size: 14px;
  color: #a0a0a0;
  font-weight: bold
}

.date {
  background-color: #ccc
}

</style>